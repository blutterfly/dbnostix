# Build LLM and MCP

**“Ollama + MCP Servers from Scratch”**, including key code blocks:

---

## ✅ **Step-by-step Implementation**

### 🧱 1. **Install Dependencies**

```bash
uv add fastmcp ollama
```

---

### 📁 2. **Project Structure**

```
your-folder/
├── server.py      # defines the MCP server & tool
└── client.py      # launches server & connects Ollama
```

---

### 🛠 3. **Create MCP Server**

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("TestServer")

@mcp.tool()
def magicoutput(obj1: str, obj2: str) -> int:
    return "WomboWombat"

if __name__ == "__main__":
    mcp.run()
```

---

### 🔌 4. **Start & Connect Client**

```python
# client.py
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio, threading
from pathlib import Path

class OllamaMCP:
    def __init__(self, server_params):
        self.server_params = server_params
        self.tools = []
        self.initialized = threading.Event()

    def _run_background(self):
        asyncio.run(self._async_run())

    async def _async_run(self):
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools_result = await session.list_tools()
                self.tools = tools_result.tools
                self.initialized.set()

if __name__ == "__main__":
    server_params = StdioServerParameters(
        command="uv", args=["run", "python", "server.py"], cwd=str(Path.cwd())
    )
    client = OllamaMCP(server_params)
    client._run_background()
```

---

### 📦 5. **Convert Tools to Pydantic Models**

```python
from pydantic import BaseModel, create_model, Field

def convert_json_type(json_type):
    return {
        "string": (str, ...),
        "integer": (int, ...),
        "number": (float, ...),
        "boolean": (bool, ...)
    }.get(json_type, (str, ...))

def create_response_model(tools):
    dynamic_models = {}
    for tool in tools:
        fields = {
            name: convert_json_type(info.get("type", "string"))
            for name, info in tool.inputSchema["properties"].items()
        }
        dynamic_models[tool.name.capitalize()] = create_model(tool.name.capitalize(), **fields)

    # Combine all tool models into one
    AllTools = Union[tuple(dynamic_models.values())]
    return create_model("Response", response=(str, ...), tool=(Optional[AllTools], Field(None)))

# Usage
client.response_model = create_response_model(client.tools)
```

---

### 🧵 6. **Background Thread + Queues for Calling Tools**

```python
import queue

class OllamaMCP:
    ...
    def __init__(...):
        ...
        self.request_queue = queue.Queue()
        self.response_queue = queue.Queue()
        self.thread = threading.Thread(target=self._run_background)
        self.thread.start()

    def call_tool(self, name, args):
        self.request_queue.put((name, args))
        return self.response_queue.get()

    async def _async_run(...):
        ...
        while True:
            name, args = self.request_queue.get()
            if name is None: break
            result = await session.call_tool(name, args)
            self.response_queue.put(result)
```

---

### 🤖 7. **Send Messages to Ollama and Trigger Tool Execution**

```python
from ollama import chat

async def ollama_chat(self, messages):
    format_schema = self.response_model.model_json_schema()
    response = chat(model="gemma3:latest", messages=messages, format=format_schema)
    
    obj = self.response_model.model_validate_json(response.message.content)
    if obj.tool:
        func_name = obj.tool.__class__.__name__.lower()
        func_args = obj.tool.model_dump()
        return await asyncio.to_thread(self.call_tool, func_name, func_args)
    return obj.response
```

---

### 🏁 8. **Main Runner**

```python
async def main():
    ...
    session = OllamaMCP(params)
    session.create_response_model()
    messages = [
        {"role": "system", "content": "Use the available tools to respond."},
        {"role": "user", "content": "Get the magic output for Wombat and Dog."}
    ]
    result = await session.ollama_chat(messages)
    print("Result:", result)
    session.shutdown()
```

---

Would you like this scaffold bundled into a downloadable repo or ZIP?
