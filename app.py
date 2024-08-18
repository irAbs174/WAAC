from kivy.lang import Builder
from kivymd.uix.button import MDButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.theming import ThemeManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


Window.titlebar_widget = False

Window.minimum_height = 667
Window.minimum_width = 375

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<ResponsiveButton@MDButton>:
    md_bg_color: app.theme_cls.surfaceColor
    style: "elevated"
    pos_hint: {"center_x": .5, "center_y": .5}

    MDButtonIcon:
        icon: "plus"

    MDButtonText:
        text: "Elevated"

<MobileView>
    ResponsiveButton:
        font_size: "20sp"

<TabletView>
    ResponsiveButton:
        font_size: "30sp"

<DesktopView>
    ResponsiveButton:
        font_size: "40sp"

ResponsiveView:
    name: "responsive_view"
'''


class MobileView(MDScreen):
    pass

class TabletView(MDScreen):
    pass

class DesktopView(MDScreen):
    pass

class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()

class App(MDApp):
    def build(self):
        # Ensure that the theme is properly set, you can also choose 'Dark' theme here
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

App().run()
