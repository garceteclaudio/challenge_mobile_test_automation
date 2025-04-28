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
4. Create a `.env` file in the project root with:
   ```ini
   APP_PASSWORD=your_amazon_password_here
   
## ⚙ Configuration

##### Mobile capabilities: 
- Set in environment.py
##### API endpoints: 
- Configured in test steps
##### Report settings: 
- See behave.ini
##### Login credentials:
- Email: Set in feature file login.feature

- Password: Set in .env file

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

### Gerate Allure HTML report
allure generate --single-file reports -o allure_report_output --report-name "Mi Reporte de Pruebas" --lang es --clean

## 📧 Contact
#### For questions or issues, please contact:
📩 garcete.claudio@gmail.com