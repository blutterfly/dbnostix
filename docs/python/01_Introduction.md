
# 📗 Introduction

## Overview

Welcome to this comprehensive Python guide, specifically tailored for data scientists, machine learning experts, and predictive modeling specialists. This resource aims to equip you with best practices, detailed examples, and practical use cases to streamline your data science projects and enhance your productivity. Whether you are a seasoned professional or a beginner looking to deepen your expertise, you'll find structured, actionable information to elevate your skills in Python programming, data analysis, and predictive modeling.

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

## Operating System

Python is a highly portable language that runs on a wide variety of operating systems and platforms, including:

### Operating Systems

- Windows – Supports Windows 10, 11, and older versions (7, 8, Server editions).
- macOS – Available on Intel and Apple Silicon (M1, M2, M3 chips).
- Linux – Supports major distributions:
  - Ubuntu
  - Debian
  - Fedora
  - CentOS
  - Red Hat Enterprise Linux (RHEL)
  - Arch Linux
  - openSUSE
  - Manjaro, etc.
- Unix-based OS:
  - FreeBSD
  - OpenBSD
  - NetBSD
  - Solaris
  - AIX (IBM Unix)
  - Android – Python can run via Termux or custom builds.
  - iOS/iPadOS – Python can be used via apps like Pythonista or Pyto.

### Platforms

- x86 (32-bit and 64-bit) – Common on Windows, Linux, and older macOS systems.
- ARM (32-bit and 64-bit) – Used in Raspberry Pi, Android devices, and Apple Silicon (via native builds).
- RISC-V – Growing support for open-source hardware.
- Web (Browser-based execution via Pyodide or Brython).
- Embedded Systems (Microcontrollers like Raspberry Pi Pico, ESP32 using MicroPython or CircuitPython).
- Mainframes (IBM z/OS supports Python for enterprise applications).
- Cloud Platforms – Runs on AWS, Azure, Google Cloud, and other cloud environments.
- Docker & Containers – Python is widely used in containerized environments.
- Virtual Machines – Can run inside VMs like VirtualBox, VMware, and Hyper-V.

Python’s versatility ensures it can run on almost any modern computing environment.

## Summary

There are several options presented on how to implement various topics.  Each Developer have adopted their own method and style.

### My Implementation

For me, this is my chosen path:
