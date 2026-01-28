# Imports the classes from kivy used to make the menu screen
from kivy.app import App
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.config import Config
Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from kivy.uix.button import Butto

class HoverBehavior(object):
    hovered = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside


class HoverButton(HoverBehavior, Button):
    pass


KV = """
<HoverButton>:
    background_normal: ""
    background_color: 0.2, 0.2, 0.2, 1
    on_hovered:
        self.background_color = (1, 0, 0, 1) if self.hovered else (0.2, 0.2, 0.2, 0.2)
        
<SideMenu@BoxLayout>:
    orientation: "vertical"
    size_hint_x: None
    width: 200
    x: -self.width

    HoverButton:
        text: "Home Page"
        font_name: "Formula1-Bold_web_0.ttf"
        on_release: app.root.ids.sm.current = "homepage"
    HoverButton:
        text: "Graph Generation"
        font_name: "Formula1-Bold_web_0.ttf"
        on_release: app.root.ids.sm.current = "graph"
    HoverButton:
        text: "Insight"
        font_name: "Formula1-Bold_web_0.ttf"
        on_release: app.root.ids.sm.current = "insight"
    HoverButton:
        text: "Driver Compare"
        font_name: "Formula1-Bold_web_0.ttf"
        on_release: app.root.ids.sm.current = "compare" 
    HoverButton:
        text: "Settings"
        font_name: "Formula1-Bold_web_0.ttf"
        on_release: app.root.ids.sm.current = "settings"
    HoverButton:
        text: "Help & Feedback"
        font_name: "Formula1-Bold_web_0.ttf"
        on_release: app.root.ids.sm.current = "help"

<HomePageScreen@Screen>:
    BoxLayout:
        Label:
            text: "Home Page"
<GraphGeneratorScreen@Screen>:
    BoxLayout:
        Label:
            text: "Graph Generator Screen"
<InsightScreen@Screen>:
    BoxLayout:
        Label:
            text: "Insight Screen"
<ComparisonScreen@Screen>:
    BoxLayout:
        Label:
            text: "Driver Comparison Screen"
<SettingsScreen@Screen>:
    BoxLayout:
        Label:
            text: "Settings Screen"
<HelpAndFeedbackScreen@Screen>:
    BoxLayout:
        Label:
            text: "Help & Feedback Screen"


BoxLayout:
    orientation: "horizontal"

    SideMenu:
        id: menu

    ScreenManager:
        id: sm
        
        HomePageScreen:
            name: "homepage"
        GraphGeneratorScreen:
            name: "graph"
        InsightScreen:
            name: "insight"
        ComparisonScreen:
            name: "compare"
        SettingsScreen:
            name: "settings"
        HelpAndFeedbackScreen:
            name: "help"

    FloatLayout:
        Button:
            size_hint: None, None
            size: 50, 50
            pos_hint: {"right": 1, "top": 1}
            background_normal: "icon.png"
            background_down: "icon.png"
            border: 0, 0, 0, 0
            on_release: app.toggle_menu()
"""

class MenuApp(App):
    def build(self):
        return Builder.load_string(KV)

    def toggle_menu(self):
        menu = self.root.ids.menu
        if menu.x < 0:
            Animation(x=0, d=0.2).start(menu)
        else:
            Animation(x=-menu.width, d=0.2).start(menu)

MenuApp().run()
