# Application base
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import (dp, sp)
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from db import DB

# Theme Manager
from kivymd.theming import ThemeManager

# UI/UX components
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager, MDScreenManager
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel

# Rtl
from bidi.algorithm import get_display
from arabic_reshaper import reshape


# Mobile Screen
class MobileView(MDScreen):
    pass


# Tablet Screen
class TabletView(MDScreen):
    pass


# Desktop Screen
class DesktopView(MDScreen):
    pass


# Class ResponsiveLayout
class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class App(MDApp):
    def build(self):

                # Register the custom font
        LabelBase.register(
            name="nasalization",
            fn_regular="assets/fonts/nasalization.otf",
        )

        self.theme_cls.font_styles["nasalization"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "nasalization",
            },
        }
        
        global sm
        sm = ScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Tomato"
        self.titlebar_widget = False
        Window.minimum_height = 667
        Window.minimum_width = 375
        self.title = "Auto Ai Comment"

        if DB().check_first_run():
            sm.add_widget(Builder.load_file('templates/login.kv'))
        else:
            sm.add_widget(Builder.load_file('templates/main.kv'))
        return sm
        
    # Load Screen function
    def load_screen(self, screen):
        sm.current = screen

    # Fix arabic chars
    def persian(self, txt):
        reshaped_text = reshape(txt)
        bidi_text = get_display(reshaped_text)
        return bidi_text

    # Switch theme dark/light
    def switch_theme(self):
        custom_sheet = None

        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        self.theme_cls.primary_palette = (
                    "Tomato" if self.theme_cls.primary_palette == "Chocolate" else "Chocolate"
                )


if __name__ == "__main__":
    App().run()