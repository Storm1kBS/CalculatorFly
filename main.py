from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalcLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10

        self.display = TextInput(text='0', readonly=True, font_size=32, size_hint=(1, 0.25))
        self.add_widget(self.display)

        buttons = [
            ['C', '←', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        for row in buttons:
            hbox = BoxLayout(spacing=10)
            for txt in row:
                btn = Button(text=txt, font_size=24)
                btn.bind(on_press=self.press)
                hbox.add_widget(btn)
            self.add_widget(hbox)

    def press(self, btn):
        current = self.display.text
        t = btn.text

        if t == 'C':
            self.display.text = '0'
        elif t == '←':
            self.display.text = current[:-1] if len(current) > 1 else '0'
        elif t == '=':
            try:
                self.display.text = str(eval(current))
            except:
                self.display.text = 'Ошибка'
        else:
            if current == '0' and t not in '/*-+.%':
                self.display.text = t
            else:
                self.display.text += t

class FloatingCalc(MDApp):
    def build(self):
        Window.size = (340, 580)
        self.theme_cls.theme_style = "Dark"
        layout = CalcLayout()

        # Перетаскивание
        def drag_start(touch):
            if touch.is_double_tap:
                self.stop()
            self._touch = touch.pos

        def drag_move(touch):
            if hasattr(self, '_touch'):
                Window.left += int(touch.x - self._touch[0])
                Window.top += int(touch.y - self._touch[1])
                self._touch = touch.pos

        Window.bind(on_touch_down=drag_start)
        Window.bind(on_touch_move=drag_move)
        return layout

if __name__ == '__main__':
    FloatingCalc().run()
