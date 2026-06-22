# Installing and Running Python on Windows

## Overview

This lecture explains how to install Python on Windows, set up VS Code, and run the first Python program from a file.

Python can be used in two ways:

1. Directly in the Python shell
2. By writing code in a `.py` file

For real projects, writing code in a `.py` file is better because it can be saved, reused, and uploaded to GitHub.

## Tools Required

* Python
* VS Code
* Terminal or Command Prompt
* Optional: Warp terminal

## Step 1: Download Python

Go to the official Python website:

```text
https://www.python.org
```

Download the latest Windows installer.

During installation:

* Select **Add Python to PATH**
* Select **Use admin privileges**
* Click **Install Now**

Adding Python to PATH allows Python commands to run from any terminal.

## Step 2: Verify Python Installation

Open a terminal and run:

```bash
python --version
```

Example output:

```bash
Python 3.13.2
```

If the version appears, Python is installed correctly.

## Step 3: Install VS Code

Download VS Code from:

```text
https://code.visualstudio.com
```

Install it using the default setup.

VS Code is used as the code editor for writing Python programs.

## Step 4: Create a Project Folder

Create a folder on the desktop, for example:

```text
TestWin
```

Open this folder in VS Code.

Inside it, create another folder:

```text
01basics
```

Inside `01basics`, create a Python file:

```text
python_test.py
```

The `.py` extension is important because it tells the system that this is a Python file.

## Step 5: Install Python Extension in VS Code

VS Code may ask to install the Python extension.

Install the official Python extension by Microsoft.

This helps with:

* Code suggestions
* Syntax highlighting
* Faster development
* Better Python support

## Step 6: Write First Python Program

Add the following code in `python_test.py`:

```python
import sys

print(sys.version)
```

Explanation:

* `import sys` imports Python’s system module
* `sys.version` gives the installed Python version
* `print()` displays the output

## Step 7: Run the Python File

Open the terminal inside VS Code and run:

```bash
python 01basics/python_test.py
```

Expected output:

```bash
3.13.2
```

The exact output may vary depending on the installed Python version.

## Important Notes

* Python works similarly on Windows, macOS, and Linux.
* The main difference is usually file paths.
* Windows often uses backslashes:

```text
folder\file.py
```

* macOS and Linux use forward slashes:

```text
folder/file.py
```

* VS Code makes Python development easier.
* Writing code in files is better than using only the shell.

## Key Takeaways

* Python can be installed easily from `python.org`.
* Always add Python to PATH during installation.
* VS Code is a good editor for Python development.
* Python files must use the `.py` extension.
* The first program checked the installed Python version.
* Once Python runs successfully, the system is ready for learning Python basics.

## Final Command Summary

```bash
python --version
```

```bash
python 01basics/python_test.py
```

