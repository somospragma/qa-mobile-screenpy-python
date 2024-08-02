from screenpy_appium import Target

from appium.webdriver.common.appiumby import AppiumBy


menu_locator = Target.the('Botón menu').located_by(
    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="open menu"]')
)

login_option_locator = Target.the('Opcion login en menu').located_by(
    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="menu item log in"]')
)

product_label_locator = Target.the('Titulo productos en el home').located_by(
    (AppiumBy.XPATH, '//android.widget.TextView[@text="Products"]')
)

