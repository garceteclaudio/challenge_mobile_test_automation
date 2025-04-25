from behave.__main__ import main as behave_main

value = "@test12345"

#behave_main("-f allure_behave.formatter:AllureFormatter -o reports/ "+value)
behave_main("--tags="+value+" -f allure_behave.formatter:AllureFormatter -o reports/")


