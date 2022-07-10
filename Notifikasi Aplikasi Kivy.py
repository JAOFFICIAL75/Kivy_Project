from kivy.app import App
from kivy.uix.button import Button
import plyer

class myapp(App):
    def build(self):
        return Button(text="Notif", on_press=self.notif)

    def notif(self, obj):
        plyer.notification.notify("Juan Aditya", "Tes Notifikasi Android")

myapp().run()
