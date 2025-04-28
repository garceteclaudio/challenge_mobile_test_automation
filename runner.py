from behave.__main__ import main as behave_main

value = "@amazon_login"

#behave_main("-f allure_behave.formatter:AllureFormatter -o reports/ "+value)
behave_main("--tags="+value+" -f allure_behave.formatter:AllureFormatter -o reports/")


