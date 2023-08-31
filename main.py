from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.theming import ThemeManager

from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.datatables import MDDataTable


class MainApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        return

MainApp().run()
