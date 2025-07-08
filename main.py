from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon

class CounterApp(MDApp):
    def build(self):
        self.count = 0
        self.theme_cls.primary_palette = "Green"
        self.screen = MDScreen(md_bg_color=self.theme_cls.backgroundColor)

        self.label = MDLabel(
            text="Count: 0",
            halign="center",
            pos_hint={"center_y": 0.75}
        )

        self.increase_button = MDButton(
            MDButtonText(text="Increase"),
            MDButtonIcon(icon="plus"),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.increase
        )

        self.decrease_button = MDButton(
            MDButtonText(text="Decrease"),
            MDButtonIcon(icon="minus"),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.decrease
        )

        self.reset_button = MDButton(
            MDButtonText(text="Reset"),
            MDButtonIcon(icon="refresh"),
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.reset
        )

        self.screen.add_widget(self.label)
        self.screen.add_widget(self.increase_button)
        self.screen.add_widget(self.decrease_button)
        self.screen.add_widget(self.reset_button)

        return self.screen

    def increase(self, *args):
        self.count += 1
        self.label.text = f"Count: {self.count}"

    def decrease(self, *args):
        self.count -= 1
        self.label.text = f"Count: {self.count}"

    def reset(self, *args):
        self.count = 0
        self.label.text = f"Count: {self.count}"

CounterApp().run()
