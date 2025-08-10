from appium import webdriver
from dotenv import load_dotenv
import os
from appium.options.android import UiAutomator2Options
import allure
import random
import json

def load_device_config(device_name):
    try:
        with open('config/device-config.json', 'r') as f:
            config = json.load(f)
            return config['devices'].get(device_name)
    except FileNotFoundError:
        raise FileNotFoundError("El archivo device-config.json no fue encontrado")
    except KeyError:
        raise KeyError(f"Dispositivo '{device_name}' no encontrado en la configuración")

def before_all(context):
    load_dotenv()
    if not os.getenv('APP_PASSWORD'):
        raise EnvironmentError("Variable APP_PASSWORD no está definida en .env")

def before_step(context, step):
    print("....................................................................................................................................................")
    print(f"Ejecutando step: {step.name}")
    print("....................................................................................................................................................")

def after_step(context, step):
    print("....................................................................................................................................................")
    print(f"Finalizo Ejecución de step: {step.name}")
    print("....................................................................................................................................................")

def before_scenario(context, scenario):
    # Definir los tags que deben activar el environment
    TAGS_REQUERIDOS = {'smoke_test', 'search_products', 'amazon_login'}

    # Verificar si el escenario tiene alguno de los tags requeridos
    if not any(tag in scenario.tags for tag in TAGS_REQUERIDOS):
        return  # Salir si no tiene los tags requeridos

    print("....................................................................................................................................................")
    print("En ejecucion: " + scenario.name)
    print(f"Tags del escenario: {scenario.tags}")
    print("....................................................................................................................................................")

    appium_server_url = 'http://127.0.0.1:4723/wd/hub'
    
    # Cargar capabilities desde el JSON
    device_capabilities = load_device_config('claudio_real_device_samsung')
    if not device_capabilities:
        raise ValueError("No se encontraron capabilities para el dispositivo especificado")
    
    capabilities_options = UiAutomator2Options().load_capabilities(device_capabilities)
    context.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

def after_scenario(context, scenario):
    # Verificar si el escenario tiene los tags requeridos
    TAGS_REQUERIDOS = {'smoke_test', 'search_products', 'amazon_login'}
    if not any(tag in scenario.tags for tag in TAGS_REQUERIDOS):
        return  # Salir si no tiene los tags requeridos

    random_number = random.randint(1, 10000)
    miscreenshotname = "screenshoot" + str(random_number)
    try:
        allure.attach(context.driver.get_screenshot_as_png(), name=miscreenshotname,
                      attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(e)

    # Solo cerrar el driver si fue inicializado
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()