import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from sys import exit
from os import path
from argparse import ArgumentParser

def startup(app):
    win = Gtk.ApplicationWindow(application=app)
    btn = Gtk.Button(label="Welcome to Kairos!")
    btn.connect('clicked', lambda x: win.close())
    win.set_child(btn)
    win.present()

app = Gtk.Application(application_id='org.gtk.Kairos')
app.connect('activate', startup)
app.run(None)
