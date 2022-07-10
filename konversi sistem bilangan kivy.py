from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class myapp(App):
    def build(self):
        layout_utama = GridLayout(cols=1, row_force_default=True,
                                  spacing=10, row_default_height=100,
                                  padding=(50,150,50,0))
        layout_utama.add_widget(Label(text="Konversi Sistem Bilangan\n\n\n", font_size=60))

        self.label1 = Label(text="Biner = 0\nOktal = 0\nDesimal = 0\nHeksa = 0\n\n",
                       font_size=40)
        self.input = TextInput(hint_text="Masukkan angka", font_size=30)
        label2 = Label(text="Pilih tombol sesuai\njenis bilangan pada input", font_size=40)
        layout_utama.add_widget(self.label1)
        layout_utama.add_widget(self.input)
        layout_utama.add_widget(label2)

        layout_tombol = GridLayout(cols=4, row_force_default=True,
                                   spacing=10, row_default_height=100)
        layout_utama.add_widget(layout_tombol)

        b1 = Button(text="Biner", font_size=30, on_press=lambda  x: self.rumus(2))
        b2 = Button(text="Oktal", font_size=30, on_press=lambda  x: self.rumus(8))
        b3 = Button(text="Desimal", font_size=30, on_press=lambda  x: self.rumus(10))
        b4 = Button(text="Heksa", font_size=30, on_press=lambda  x: self.rumus(16))
        layout_tombol.add_widget(b1)
        layout_tombol.add_widget(b2)
        layout_tombol.add_widget(b3)
        layout_tombol.add_widget(b4)

        return layout_utama


    def rumus(self, data_konversi):
        try:
            data = int(self.input.text, data_konversi)
            biner = bin(data).replace("0b", "")
            hexa = hex(data).replace("0x", "")
            octal = oct(data).replace("0o", "")
            self.label1.text = f"Biner = {biner}\nOktal = {octal}\nDesimal = {data}\nHeksa = {hexa}\n\n"
        except:
            pass


myapp().run()
