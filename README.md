# Email-Bomber-Lookout

![Screenshot of the program](screenshot(1).png)
## Disclaimer

This project is provided for educational purposes only. I am not responsible for any misuse or illegal activities that may arise from the use of this project. 

## Features

- Send multiple emails to a specified target email address.
- Customize the content and subject of the emails.
- Easy to use and understand.

## Installation (Linux)

   ```bash
   sudo apt update
   sudo apt upgrade
   ```
   ```
   sudo apt install git
   ```
   ```
   sudo apt install python3-pip
   ```
   ```
   git clone https://github.com/lachsverdauer/Email-Bomb-lookout.git
   ```
   ```
   cd Email-Bomb-lookout
   ```
   ```
   pip install -r requirements.txt
   ```
   ### Run the program:
   ```
   python3 main.py
   ```

## Installation (macOS)
### Prerequisites:   homebrew & Xcode & git & python

   If you dont have it:
   ```
   xcode-select --install
   ```
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   ```
   brew install git
   ```
   ```
   brew install python
   ```
   ```
   git clone https://github.com/lachsverdauer/Email-Bomb-lookout.git
   ```
   ```
   cd Email-Bomb-lookout
   ```
   ```
   pip3 install -r requirements.txt
   ```
   ### Run the program
   ```
   python3 main.py
   ```
## Installation (Windows)
### Prerequisites: Git & Python

-Python: Download it from: https://www.python.org/downloads/
During installation, make sure to check the option "Add Python 3.x to PATH" to ensure Python and pip are available from the command line.

-Git: Download it from: https://git-scm.com/download/win

1. Open Command Prompt or PowerShell as an administrator.

2. Update pip, the Python package installer, to its latest version:
```
python -m pip install --upgrade pip
```
```
git clone https://github.com/lachsverdauer/Email-Bomb-lookout.git

```
```
cd Email-Bomb-lookout
```
```
pip install -r requirements.txt
```
Start the program:
```
python3 main.py
```

## Usage

### BEFORE YOU USE IT -> CONFIGURE THE EMAILS AND PASSWORDS IN THE config.py FILE
### 300 mails per 24h for 1 outlook account, 500 mails per 24h for 1 gmail account

You NEED to put yout email and App Password into the config.py file. The email MUST have 2FA to work.

The password WILL NOT work with your regular password. You will need to add an App password after your 2 Factor Authentication(2FA).

It works on Gmail and in Outlook.

# Run the program:

```
python3 main.py
```

