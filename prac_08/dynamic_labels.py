from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (1,0,1,1)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
