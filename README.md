# Amazon Mobile & API Test Automation Challenge

## Overview
This project is a technical challenge for PinApp, implementing automated tests for:
1. Mobile testing of the Amazon app (login functionality)
2. API integration testing

## 📌 Project Details
**Author**: Claudio Rodolfo Garcete  
**Contact**: garcete.claudio@gmail.com  
**Technologies**: Appium, Python, Behave, Allure  

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Appium server
- Android SDK (for mobile tests)
- Allure commandline tools

### Installation
1. Clone the repository
2. Set up virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
3. Install dependencies:
pip install -r requirements.txt

## 🏗 Project Structure
![Captura de pantalla 2025-04-28 a la(s) 4.11.15 a. m..png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fz1%2Fjydw8bnj62l6tdxv522_z1_w0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_n9IESt%2FCaptura%20de%20pantalla%202025-04-28%20a%20la%28s%29%204.11.15%E2%80%AFa.%C2%A0m..png)


## 🏃 Running Tests
#### Run all tests
behave

#### Run specific feature
behave features/login.feature

## 📊 Generating Reports
### Generate Allure report
allure generate reports -o allure_report_output --clean

### Serve report (view in browser)
allure serve reports

## ⚙ Configuration

##### Mobile capabilities: Set in environment.py
##### API endpoints: Configured in test steps
##### Report settings: See behave.ini

## 📧 Contact
#### For questions or issues, please contact:
📩 garcete.claudio@gmail.com