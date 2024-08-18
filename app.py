from kivymd.uix.appbar import MDActionBottomAppBarButton
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemeManager
from kivymd.uix.card import MDCardSwipe
from bidi.algorithm import get_display
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from arabic_reshaper import reshape
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import sp


Window.titlebar_widget = False

Window.minimum_height = 667
Window.minimum_width = 375

class UniqueApp(MDApp):
    title = 'Unique App'

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gold"

        # Register the custom font
        LabelBase.register(
            name="nasalization",
            fn_regular="assets/fonts/nasalization.otf",
        )

        self.theme_cls.font_styles["nasalization"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "nasalization",
                "font-size": sp(57),
            },
        }

        # Initialize and return the root widget
        self.screen = ResponsiveView()
        return Builder.load_file('templates/base.kv')

    def persian(self, txt):
        reshaped_text = reshape(txt)
        bidi_text = get_display(reshaped_text)
        return bidi_text

    def load_screen(self, screen_cls):
        return screen_cls()


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class DrawerLabel(MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()


class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
    trailing_text = StringProperty()
    trailing_text_color = ColorProperty()

    _trailing_text_obj = None

    def on_trailing_text(self, instance, value):
        self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
            text=value,
            theme_text_color="Custom",
            text_color=self.trailing_text_color,
        )
        self.add_widget(self._trailing_text_obj)

    def on_trailing_text_color(self, instance, value):
        self._trailing_text_obj.text_color = value


class MainCard(MDCard):
    pass


class LoginScreen(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()


# Ensure the app runs as expected
if __name__ == "__main__":
    UniqueApp().run()