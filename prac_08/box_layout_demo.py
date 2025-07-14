from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a demo for boxlayout"""
    def build(self):
        """build a kivy app from the kivy file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def output_label(self):
        """create greeting string to label"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_greet(self):
        """handle greet(could be a button or other call), output greet to label"""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """handle clear(could be a button or other call), clear text in input box and output label"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


BoxLayoutDemo().run()
