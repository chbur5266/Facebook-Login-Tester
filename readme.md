# Facebook-Login-Tester

## Description
Facebook-Login-Tester is a Selenium-based Python script designed for educational purposes to demonstrate automated web interactions, specifically for testing login mechanisms and CAPTCHA handling on Facebook. This tool is intended to help developers understand web automation techniques and enhance security testing skills.

## Disclaimer
This tool is provided for educational purposes only. Any misuse of this software to engage in malicious or illegal activities is strictly prohibited. The authors or contributors do not condone unauthorized access to accounts, and users must comply with all applicable laws and regulations.

## Prerequisites
- Python 3.x
- Selenium
- WebDriver-Manager

### Installation
To use the Facebook-Login-Tester, you will need Python installed on your machine along with the required Python packages:

```bash
pip install selenium webdriver-manager
```

Ensure you have Google Chrome or any Chromium-based browser installed on your system as the script uses ChromeDriver to interact with web pages.

### Setup
Clone this repository or download the source code.
Navigate to the cloned/downloaded directory.

```bash
git clone https://github.com/yourusername/Facebook-Login-Tester.git
cd Facebook-Login-Tester
```
Install the necessary Python packages if not already installed:

```bash
pip install -r requirements.txt
```
### Configuration
Before running the script, ensure you have created the credentials.txt file with the credentials you have permission to test. The format should be:

email1:password1
email2:password2

### Usage
To run the script, use the following command:

```bash
python login.py
```
The script will attempt to log in using the provided credentials and check for the presence of CAPTCHAs or login failures.

### Features
Automated login attempts using Selenium WebDriver.
Detection of login success or failure.
CAPTCHA detection mechanism with user interaction required.
Headless browser support for background operation without UI interference.
Contributing
Contributions to the Facebook-Login-Tester are welcome, particularly those that improve functionality or extend features. Please fork the repository, make your changes, and submit a pull request.

