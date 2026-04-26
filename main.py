from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from cipher import encrypt, decrypt
from kivy.core.clipboard import Clipboard


Builder.load_file("simple_encrypter.kv") # Принудительный запуск kv

class SimpleEncrypterLayout(BoxLayout):
    pass


class SimpleEncrypterApp(App):
    # По умолчанию
    current_lang = "eng"
    current_mode = "enc"

    # Перевод
    texts = {
        "rus": {
            "lang_label": "ВЫБОР ЯЗЫКА:",
            "mode_label": "ВЫБОР РЕЖИМА:",
            "rus_btn": "РУС",
            "eng_btn": "АНГЛ",
            "enc_btn": "ЗАШИФРОВАТЬ",
            "dec_btn": "РАСШИФРОВАТЬ",
            "input_label": "ВВЕДИТЕ ТЕКСТ:",
            "output_label": "РЕЗУЛЬТАТ:",
            "copy_btn": "КОПИРОВАТЬ"
        },
        "eng": {
            "lang_label": "SELECT LANGUAGE:",
            "mode_label": "SELECT MODE:",
            "rus_btn": "RUS",
            "eng_btn": "ENG",
            "enc_btn": "ENCRYPT",
            "dec_btn": "DECRYPT",
            "input_label": "ENTER TEXT:",
            "output_label": "TEXT OUTPUT:",
            "copy_btn": "COPY"
        }
    }


    def update_interface_texts(self):
        """Функция обновляет весь интерфейс при смене языка"""
        text_update = self.texts[self.current_lang]

        # Надписи
        self.root.ids.lang_label.text = text_update["lang_label"]
        self.root.ids.mode_label.text = text_update["mode_label"]
        self.root.ids.input_label.text = text_update["input_label"]
        self.root.ids.output_label.text = text_update["output_label"]

        # Кнопки переключателей
        self.root.ids.rus_btn.text = text_update["rus_btn"]
        self.root.ids.eng_btn.text = text_update["eng_btn"]
        self.root.ids.enc_btn.text = text_update["enc_btn"]
        self.root.ids.dec_btn.text = text_update["dec_btn"]

        # Кнопка копирования
        self.root.ids.copy_btn.text = text_update["copy_btn"]

        self.update_action_button_text()

    def update_action_button_text(self):
        """Функция смены языка на кнопке шифрования"""
        if self.current_mode == "enc":
            text = "ЗАШИФРОВАТЬ" if self.current_lang == "rus" else "ENCRYPT"
        else:
            text = "РАСШИФРОВАТЬ" if self.current_lang == "rus" else "DECRYPT"

        self.root.ids.action_btn.text = text

    # Функции смены режима и языка
    def on_lang_change(self, lang):
        self.current_lang = lang
        self.update_interface_texts()

    def on_mode_change(self, mode):
        self.current_mode = mode
        self.update_action_button_text()

    def on_action_press(self):
        """Функция действия  шифровки и дешифровки"""
        input_text = self.root.ids.input_text.text

        if not input_text.strip():
            self.root.ids.output_text.text = "TEXT ERROR"
            return

        if self.current_mode == "enc":
            result = encrypt(input_text, self.current_lang)
        else:
            result = decrypt(input_text, self.current_lang)

        self.root.ids.output_text.text = result

    def on_copy_press(self):
        """Функция для кнопки копирования"""
        output = self.root.ids.output_text.text
        if output:
            Clipboard.copy(output)

    def build(self):
        Window.size = (600, 500)
        return SimpleEncrypterLayout()

if __name__ == '__main__':
    SimpleEncrypterApp().run()