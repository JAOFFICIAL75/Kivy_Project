from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import random


class myapp(App):
    benar = 0
    salah = 0
    angka1 = random.randint(1, 100)
    angka2 = random.randint(1, 100)
    total = angka1 + angka2

    def build(self):
        layout_utama = GridLayout(cols=1,
                                  row_force_default=True,
                                  row_default_height=80,
                                  spacing=50)
        label1 = Label(text="Aplikasi Pertambahan", font_size=50)
        self.label2 = Label(text=f"{self.angka1} + {self.angka2} =",
                       font_size=40)
        layout_utama.add_widget(label1)
        layout_utama.add_widget(self.label2)

        layout_isi = GridLayout(cols=2,
                                row_force_default=True,
                                padding=40, spacing=20,
                                row_default_height=80)
        self.entry = TextInput(hint_text="Jawaban", font_size=40)
        button = Button(text="Cek", font_size=40, size_hint=(0.3, 1),
                        on_press=self.periksa)
        layout_utama.add_widget(layout_isi)
        layout_isi.add_widget(self.entry)
        layout_isi.add_widget(button)

        layout_nilai = GridLayout(cols=1,
                                  row_force_default=True,
                                  row_default_height=200)
        self.label3 = Label(text=f"Benar = {self.benar}\nSalah = {self.salah}",
                       font_size=40)
        layout_utama.add_widget(layout_nilai)
        layout_nilai.add_widget(self.label3)
        return layout_utama


    # bagian pengecekan pada button
    def periksa(self, obj):
        data = self.entry.text
        if data.isdigit():
            if int(data) == self.total:
                self.benar += 1
            else:
                self.salah += 1
            self.entry.text = ""
            self.angka1 = random.randint(1, 100)
            self.angka2 = random.randint(1, 100)
            self.total = self.angka1 + self.angka2
            self.label2.text = f"{self.angka1} + {self.angka2} ="
            self.label3.text = f"Benar = {self.benar}\nSalah = {self.salah}"
        else:
            self.entry.text = ""

myapp().run()
