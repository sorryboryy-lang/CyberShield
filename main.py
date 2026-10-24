from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
import string

class CyberShieldApp(App):
    def build(self):
        self.title = "CyberShield"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(
            text="CyberShield Generator", 
            font_size='20sp',
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.label)

        self.pass_display = TextInput(
            text='', 
            readonly=True, 
            halign='center',
            font_size='18sp',
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.pass_display)

        btn = Button(
            text="توليد كلمة سر قوية", 
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)
        )
        btn.bind(on_press=self.generate_password)
        layout.add_widget(btn)

        return layout

    def generate_password(self, instance):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for _ in range(12))
        self.pass_display.text = password

if __name__ == '__main__':
    CyberShieldApp().run()
