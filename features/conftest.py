import pytest

from typing import Generator

from appium.webdriver import Remote
from appium.options.android.uiautomator2.base import UiAutomator2Options

from screenpy import Actor, the_narrator

from screenpy_adapter_allure import AllureAdapter

from screenpy_appium.abilities import UseAnAndroidDevice


@pytest.fixture(scope="function", name="Jorge")
def fixture_actions() -> Generator:
    capabilities = {
        "platformName": "android",
        "appium:deviceName": "emulator-5554",
        "appium:platformVersion": "12",
        "appium:appPackage": "com.saucelabs.mydemoapp.rn",
        "appium:appActivity": ".MainActivity",
        "appium:automationName": "uiautomator2"  
    }
    driver = Remote(
        command_executor="http://127.0.0.1:4723",
        options=UiAutomator2Options().load_capabilities(capabilities)
    )
    the_actor = Actor.named("Jorge").who_can(UseAnAndroidDevice.using(driver))
    yield the_actor
    the_actor.exit()

the_narrator.adapters.append(AllureAdapter())