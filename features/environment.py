from appium import webdriver
import os
from appium.options.android import UiAutomator2Options

import allure
import random



#'appPackage': "com.google.android.calculator",
#'appActivity': 'com.android.calculator2.Calculator',

#com.ebay.mobile/com.ebay.mobile.home.impl.main.MainActivity
#com.amazon.mShop.android.shopping/com.amazon.mShop.startup.StartupLocalizationSelectionActivity
claudio_real_device_samsung = {
                        #'platformVersion': '14.0',
                        'platformName': 'Android',
                        'deviceName': 'R5CW32TQB3F',
                        'automationName': 'UiAutomator2',
                         #'app': os.path.abspath(os.path.join(__file__, "../../src/binaries/app-debugQA4-274.apk")),
                        'autoAcceptAlerts': 'true',  # to accept all alerts
                        'autoGrantPermissions': 'true',
                        'appPackage': "com.amazon.mShop.android.shopping",
                        'appActivity': 'com.amazon.mShop.splashscreen.StartupActivity',  # Actividad de splash
                        'noReset': True,
                        'printPageSourceOnFindFailure': 'true',
                        #'fullReset': 'true'
                        'newCommandTimeout': 800,
                       # 'browserName': "Chrome"
                        }

AMBIENTE = "QA4"

def before_all(context):
    print("Beforo all")


def before_step(context, step):
    print("....................................................................................................................................................")
    print(f"Ejecutando step: {step.name}")
    print("....................................................................................................................................................")

def after_step(context, step):
    print(
        "....................................................................................................................................................")
    print(f"Finalizo Ejecución de step: {step.name}")
    print(
        "....................................................................................................................................................")

    # random_number = random.randint(1, 10000)
    # miscreenshotname = "screenshoot"+str(random_number)
    # try:
    #     allure.attach(context.driver.get_screenshot_as_png(), name=miscreenshotname, attachment_type=allure.attachment_type.PNG)
    # except Exception as e:
    #     print(e)

#def before_feature(context, feature):

def before_scenario(context, scenario):
    print("....................................................................................................................................................")
    print("En ejecucion: " + scenario.name)
    print("....................................................................................................................................................")
    desired_capabilities = {
        "browserName": "chrome",
        "autoGrantPermissions": "true"
    }
    # # #  Browserstack # #
    #context.driver = webdriver.Remote(desired_capabilities=desired_capabilities,
    #                                 command_executor="https://hub.browserstack.com/wd/hub")

    # # # #  LOCAL

    # context.driver = webdriver.Remote("http://127.0.0.1:9000/wd/hub",local_desired_capabilities)
    # context.app = Application(context.driver)
    # context.driver.start_activity(local_desired_capabilities["appium:appPackage"], local_desired_capabilities["appium:appActivity"])
    # context.driver.implicitly_wait(15)


    appium_server_url = 'http://127.0.0.1:4723/wd/hub'
    capabilities_options = UiAutomator2Options().load_capabilities(claudio_real_device_samsung)
    context.driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)
    #context.app = Application(context.driver)
    #context.driver.execute_script('mobile: startActivity',{'component': f'ar.com.bancor.bancon/ar.com.bancor.bancon.MainActivity',})
    context.driver.implicitly_wait(20)

    #context.app.ambiente = AMBIENTE
    #context.chromedriver_path = chromedriver_path



def after_scenario(context, scenario):
    # Si el caso paso le hace un print para mostrar la pantalla final

    random_number = random.randint(1, 10000)
    miscreenshotname = "screenshoot" + str(random_number)
    try:
        allure.attach(context.driver.get_screenshot_as_png(), name=miscreenshotname,
                      attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(e)
    #print("Finaliza: " + scenario.name)
    # Invoke driver.quit() after the test is done to indicate to BrowserStack
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    #context.driver.quit()