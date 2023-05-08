# Computer Startup Automation

This Python script automates the process of starting up my computer by opening specific web pages and applications.

## Installation

This script uses some external modules, which can be installed by running:

```
pip install -r requirements.txt
```

## Usage

To use this script, simply run it from the command line:

```
VSC.py
```

The script will then start up the following:

* Google Chrome windows with specific URLs opened in them.
* Microsoft VS Code editor.
* Logitech G13 software.

## Configuration

The script uses some hard-coded values that you might want to change, such as the paths to the executables and the URLs to be opened. You can modify these values directly in the script.

Note that some of the Chrome windows are opened with a specific user profile, which is identified by its "profile directory". You might need to change these values if you have different Chrome profiles or if you want to use a different window size.

## Make a executable

First you need to activate the virtual environment:

```
source venv/bin/activate
```

then you can run the following command:

```bash
python -m py2exe_gui
```

## License

This code is licensed under the CC 3 license.