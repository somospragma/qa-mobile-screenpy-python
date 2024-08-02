from screenpy import Actor, when, then
from screenpy.actions import See

from screenpy_appium.actions import Tap, Enter
from screenpy_appium.questions import Element
from screenpy_appium.resolutions import IsVisible

from Tasks.login import Login

from Locators.HomeUI import product_label_locator

from Utils.users import *


def test_login_successfully(Jorge: Actor)->None:
    
    when(Jorge).attempts_to(
        Login.using(username, password)
    )
    then(Jorge).should(
        See.the(
            Element(product_label_locator), IsVisible()
        )
    )
