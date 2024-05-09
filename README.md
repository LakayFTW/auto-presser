# auto-presser
A little thing i made because i couldn't find any keyboard auto presser/clicker.  

__Use this with caution!.__  
- Hotkeys are not an option.  
- Timer setting will eventually be added

## Setup
- Make sure Python is installed
- Make sure pip is installed
- Create a venv
  - `python -m venv venv`
- Activate your venv
  - `.\venv\Scripts\Activate.ps1` (powershell)
- Install requirements
  - `pip install -r requirements.txt`
- Run clicker.py
  - `python clicker.py`

## Building your own .exe
If you made changes to the code you can build your own .exe very easily.
1. Install pyinstaller
   - `pip install pyinstaller`
2. Use pyinstaller
   - `pyinstaller clicker.py --onefile -w`
   - --onefile: provides just a single .exe file
   - -w removes the cli
   - If you dont want a single cli and need all the other files, just remove it from the command.