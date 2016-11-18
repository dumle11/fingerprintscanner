#!/usr/bin/env python

import kivy

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("fingerprintscanner.kv")

# Declare screens
class MenuScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class CompatibilityScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(CompatibilityScreen(name='compatibility'))


class FingerprintScannerApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    FingerprintScannerApp().run()