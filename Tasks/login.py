from screenpy import Actor
from screenpy.pacing import beat

from screenpy_appium.actions import Tap, Enter

from Actions.wait import Wait

from Locators.HomeUI import *
from Locators.LoginUI import *

class Login:
    """
    Tarea para realizar el Login en la aplicación

        
    
    """

    @staticmethod
    def using(username: str, password:str) -> "Login":
        return Login(username, password)
    
    @beat('{} "{username} tries to login"')
    def perform_as(self, the_actor: Actor) ->None:
        the_actor.attempts_to(
            Tap.on_the(menu_locator),
            Wait.for_the(login_option_locator).to_appear(),
            Tap.on_the(login_option_locator),
            Wait.for_the(login_button_locator).to_appear(),
            Enter.the_text(self.username).into_the(username_input_locator),
            Enter.the_password(self.password).into_the(password_input_locator),
            Tap.on_the(login_button_locator),
            Wait.for_the(product_label_locator).to_appear()
        )
    
    def __init__(self, username: str, password:str) -> None:
        self.username = username
        self.password = password
