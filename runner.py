import shutil
import os
from behave.__main__ import main as behave_main

folders_to_remove = ["reports", "allure_report_output", "output"]

for folder in folders_to_remove:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"Se eliminó la carpeta: {folder}")

value = "@search_products"

# Ejecutar Behave con Allure
behave_main("--tags=" + value + " -f allure_behave.formatter:AllureFormatter -o reports/")
