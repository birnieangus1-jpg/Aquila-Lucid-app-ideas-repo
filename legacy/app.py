# Language: Python
# python -m pip install kivy or py -3.10 -m pip insstall kivy
# Import necessary modules
import asyncio
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Optional: set window size
Window.size = (400, 600)


# Define the main messaging layout
class MessagingAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Create a scrollable area for messages
        self.scrollview = ScrollView()
        self.message_grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.message_grid.bind(minimum_height=self.message_grid.setter("height"))
        self.scrollview.add_widget(self.message_grid)
        self.add_widget(self.scrollview)

        # Text input and send button
        input_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        self.message_input = TextInput(hint_text="Type a message", multiline=False)
        self.send_button = Button(text="Send")
        self.send_button.bind(on_press=self.send_message)
        input_layout.add_widget(self.message_input)
        input_layout.add_widget(self.send_button)

        self.add_widget(input_layout)

    def send_message(self, instance):
        message_text = self.message_input.text.strip()
        if message_text:
            # Add message to the scrollable grid
            new_message = Label(
                text=message_text,
                size_hint_y=None,
                height=30,
                halign="left",
                valign="middle",
            )
            new_message.bind(size=new_message.setter("text_size"))
            self.message_grid.add_widget(new_message)
            self.message_input.text = ""
            # Auto scroll to the bottom
            self.scrollview.scroll_y = 0


# Main App Class
class MessagingApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return MessagingAppLayout()


# Usage example: run the app
if __name__ == "__main__":
    mapp = MessagingApp()
    asyncio.run(mapp.async_run(), debug=True)
