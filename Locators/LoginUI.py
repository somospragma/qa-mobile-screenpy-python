from screenpy_appium import Target

from appium.webdriver.common.appiumby import AppiumBy


username_input_locator = Target.the('Campo de texto para ingresar nombre de usuario').located_by(
    (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="Username input field"]')
)

password_input_locator = Target.the('Campo de texto para ingresar contraseña').located_by(
    (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="Password input field"]')
)

login_button_locator = Target.the('Boton login').located_by(
    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Login button"]')
)




