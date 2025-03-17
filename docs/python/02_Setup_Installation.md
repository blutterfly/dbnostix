
# 02 🛠️ Setup and Installation



## Environment Setup

### Python Installation

Setting up Python correctly is essential. We recommend downloading the latest stable Python version from the [official Python website](https://www.python.org/downloads/). Ensure you select the appropriate version compatible with your operating system (Windows, macOS, Linux). Follow the installer instructions, selecting the option to add Python to your PATH environment variable.

Verify your installation by running:

```bash
python --version
```

### Virtual Environment

Using virtual environments helps isolate your project dependencies and avoids conflicts.

#### pip

`pip` is Python's package installer, allowing easy management of packages. It comes bundled with Python 3 by default. Verify pip installation by running:

```bash
pip --version
```

### Virtual Environment (venv)

Virtual environments isolate project dependencies. Set up a virtual environment with Python's built-in `venv`:

#### Creating and Activating a Virtual Environment

```bash
python -m venv myenv

# Activate the environment
# On Windows:
myenv\Scripts\activate

# On macOS/Linux
source myenv/bin/activate
```

!!! info  "VSCode"
    In VSCode the default library when Creating Environment is .venv instead of venv

## Installing Packages

Once activated, install packages using:

```bash
pip install numpy pandas matplotlib
```

## Integrated Development Environment

Choosing the right Integrated Development Environment (IDE) is crucial for efficiency.

### IDLE

IDLE comes bundled with Python and is suitable for basic scripting and quick experiments.

- Launch IDLE from your Python installation.
- Provides a straightforward interactive shell and simple editor.
- Ideal for beginners or small tasks.

### VSCode

- Highly recommended for professional development.
- Feature-rich editor with extensive Python support through extensions.
- Easy integration with Jupyter Notebooks, Git, and debugging tools.
- Installation: [VSCode](https://code.visualstudio.com/).

### PyCharm

A powerful, dedicated Python IDE ideal for larger, complex projects.

- Excellent code completion, debugging, and version control integration.
- Offers Community (free) and Professional (paid) editions.

### JupyterLab

Web-based IDE highly popular among data scientists.

- Combines notebooks, terminal, text editors, and visualization in one interface.
- Perfect for interactive data exploration, visualization, and documentation.
- Install via pip:

```bash
pip install jupyterlab
```

Launch by running:

```bash
jupyter lab
```

This setup ensures a solid foundation to maximize productivity in your Python-based projects.

!!! BUG
    Add topic
    Python CLI

