# Python Virtual Environment

## Overview

A virtual environment is an isolated Python setup created for a specific project.

It helps keep each project independent by storing its own Python packages and dependencies separately from the main system Python.

## Why Virtual Environments Are Needed

Virtual environments are used to:

* Avoid dependency conflicts between projects
* Keep the operating system clean
* Install different package versions for different projects
* Make projects easier to share and run on other systems
* Ensure the same setup works on Windows, macOS, or Linux

## Problem Without Virtual Environment

If all Python packages are installed globally, every project uses the same package version.

Example:

* Project A needs an older version of a package
* Project B needs the latest version
* Updating the package globally may break Project A

This is why installing all dependencies in one global location is not a good practice.

## Solution: Virtual Environment

A virtual environment creates a separate Python environment for each project.

Each project gets:

* Its own Python environment
* Its own installed packages
* Its own dependency versions

This keeps projects isolated and stable.

## Create a Virtual Environment

Create a project folder first.

Example:

```bash
mkdir 01_virtual
cd 01_virtual
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Here, `.venv` is the folder where the virtual environment is created.

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

After activation, the terminal shows something like:

```bash
(.venv)
```

This means the virtual environment is active.

## Install Packages

Once the virtual environment is active, install packages using `pip`.

Example:

```bash
pip install flask
```

```bash
pip install requests
```

These packages are installed only inside the virtual environment.

## requirements.txt

A `requirements.txt` file stores all project dependencies.

Example:

```text
requests
flask
```

You can also mention specific versions:

```text
requests==2.31.0
flask==3.0.0
```

Install all dependencies from the file:

```bash
pip install -r requirements.txt
```

## Deactivate Virtual Environment

To exit the virtual environment, run:

```bash
deactivate
```

## Sharing Python Projects

Usually, we do not share the `.venv` folder.

Instead, we share:

* Python source code
* `requirements.txt`

The other person can create a fresh virtual environment and install the dependencies using:

```bash
pip install -r requirements.txt
```

## Git Ignore

The `.venv` folder should usually be added to `.gitignore`.

Example:

```text
.venv/
```

This avoids uploading the virtual environment to GitHub.

## Traditional Way vs Modern Way

The traditional way of creating virtual environments is using:

```bash
python -m venv .venv
```

A modern tool called `uv` can also be used for faster and smoother Python environment management.

## Key Takeaways

* Always use a virtual environment for Python projects.
* It keeps dependencies isolated.
* It avoids breaking other projects.
* It makes projects easier to share.
* Use `requirements.txt` to list project dependencies.
* Do not upload `.venv` to GitHub.
* Virtual environments are a best practice in Python development.

## Command Summary

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
source .venv/bin/activate
```

```bash
pip install flask
```

```bash
pip install -r requirements.txt
```

```bash
deactivate
```
