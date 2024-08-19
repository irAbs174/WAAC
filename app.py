# Application base
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# Theme Manager
from kivymd.theming import ThemeManager

# UI/UX components
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel

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
        global sm
        sm = ScreenManager()
        self.theme_cls.primary_palette = "Red"
        self.titlebar_widget = False
        Window.minimum_height = 667
        Window.minimum_width = 375
        self.title = "Auto Ai Comment"

        sm.add_widget(Builder.load_file('templates/main.kv'))
        sm.add_widget(Builder.load_file('templates/login.kv'))
        return sm

    def load_screen(self, screen):
        sm.current = screen
        
        
if __name__ == "__main__":
    App().run()