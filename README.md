# Program List Backup

This Python script captures a screenshot of the program list on a Windows operating system using the `pyautogui` library. It opens the Control Panel's "Programs and Features" window, takes a screenshot, saves it as `ProgramList.png`, and then closes the window.

## Prerequisites

- Python 3.x
- `pyautogui` library

## Installation

1. Install Python from the official website: [Python Downloads](https://www.python.org/downloads/).
2. Install the required `pyautogui` library by running the following command:

```bash
pip install pyautogui
```

## Usage

1. Import the necessary libraries in your Python script:

```python
import pyautogui
import os
from time import sleep
```

2. Add the following code snippet to your script:

```python
os.system('control.exe appwiz.cpl')
sleep(2)
im1 = pyautogui.screenshot()
im1.save('ProgramList.png')
pyautogui.hotkey('alt', 'f4')
```

3. Run the script, and it will open the "Programs and Features" window, capture a screenshot of the program list, save it as `ProgramList.png`, and then close the window.
