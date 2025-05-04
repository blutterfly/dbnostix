Here is a summarized step-by-step guide from the article **"How to build MCP server with Authentication in Python using FastAPI"** by Miki Makhlevich, including key code blocks:

---

### ✅ Step 0: Install Required Dependencies

```bash
pip install uvicorn fastapi fastapi-mcp
```

---

### ✅ Step 1: Create a Basic FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "MCP is super cool"}
```

Run the server:

```bash
uvicorn main:app --reload
```

---

### ✅ Step 2: Mount the MCP Server

```python
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()
mcp = FastApiMCP(app)
mcp.mount()
```

MCP will now be accessible at: `http://127.0.0.1:8000/mcp`

---

### ✅ Step 3: Add Authentication

#### 🔐 Option 1: Bearer Token in Authorization Header

Example CLI call with token:

```json
{
  "mcpServers": {
    "remote-example": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:8000/mcp",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ]
    },
    "env": {
      "AUTH_HEADER": "Bearer <your-token>"
    }
  }
}
```

Protecting with FastAPI-MCP:

```python
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from fastapi_mcp import FastApiMCP, AuthConfig

token_auth_scheme = HTTPBearer()
app = FastAPI()

mcp = FastApiMCP(
    app,
    name="Protected MCP",
    auth_config=AuthConfig(
        dependencies=[Depends(token_auth_scheme)],
    ),
)
mcp.mount()
```

---

#### 🔐 Option 2: Full OAuth with Auth0 (Recommended)

**Step 1**: Create `.env`

```env
AUTH0_DOMAIN=your-tenant.auth0.com
AUTH0_AUDIENCE=https://your-tenant.auth0.com/api/v2/
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
```

**Step 2**: Load settings

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    auth0_domain: str
    auth0_audience: str
    auth0_client_id: str
    auth0_client_secret: str

    class Config:
        env_file = ".env"

settings = Settings()
```

**Step 3**: Get and convert JWK public key

```python
import jwt
import requests
from cryptography.hazmat.primitives import serialization

def _get_public_key(url: str):
    response = requests.get(url)
    jwks = response.json()
    return jwks["keys"][0]

def _convert_key_to_pem(jwk_key) -> str:
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(jwk_key)
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return pem.decode("utf-8")

jwks_key = _get_public_key(f"https://{settings.auth0_domain}/.well-known/jwks.json")
pem_key = _convert_key_to_pem(jwks_key)
```

**Step 4**: Create token verifier

```python
async def verify_auth(request: Request) -> dict[str, Any]:
    return jwt.decode(
        token,
        pem_key,
        algorithms=["RS256", "HS256"],
        audience=settings.auth0_audience,
        issuer=f"https://{settings.auth0_domain}/",
        options={"verify_signature": True},
    )
```

**Step 5**: Secure MCP with OAuth2

```python
from fastapi import Depends
from fastapi_mcp import FastApiMCP, AuthConfig

mcp = FastApiMCP(
    app,
    name="MCP With Auth0",
    auth_config=AuthConfig(
        issuer=f"https://{settings.auth0_domain}/",
        authorize_url=f"https://{settings.auth0_domain}/authorize",
        oauth_metadata_url=f"https://{settings.auth0_domain}/.well-known/openid-configuration",
        audience=settings.auth0_audience,
        client_id=settings.auth0_client_id,
        client_secret=settings.auth0_client_secret,
        dependencies=[Depends(verify_auth)],
        setup_proxies=True,
    ),
)
mcp.mount()
```

---

Let me know if you'd like a downloadable starter template or OAuth testing script.
