from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


Builder.load_file("simple_encrypter.kv") # Принудительный запуск kv

class SimpleEncrypterLayout(BoxLayout):
    pass


class SimpleEncrypterApp(App):
    def on_lang_change(self, lang):
        pass

    def on_mode_change(self, mode):
        pass

    def build(self):
        Window.size = (600, 500)
        return SimpleEncrypterLayout()

if __name__ == '__main__':
    SimpleEncrypterApp().run()