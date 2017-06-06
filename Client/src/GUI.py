#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class GUI:
	def __init__(self, gladefile, window_name):
		self.connect_gladefile(gladefile)
		self.set_components()
		self.connect_buttons()

	def connect_gladefile(self, gladefile):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladefile)

	def set_components(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def connect_button(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def start_window(self, window_name):
		self.window = self.builder.get_object(window_name)
		self.window.connect("delete-event", Gtk.main_quit)
		self.window.show_all()
		Gtk.main()


class Login(GUI):
	def set_components(self):
		self.__entry_username = self.builder.get_object("login_entry_username")
		self.__entry_password = self.builder.get_object("login_entry_password")

	def connect_buttons(self):
		self.button = self.builder.get_object("login_button_login")
		self.button.connect("clicked", self.on_button_login_clicked)

		self.button = self.builder.get_object("login_button_close")
		self.button.connect("clicked", Gtk.main_quit)

	def on_button_login_clicked(self, button):
		raise NotImplementedError("Subclass must implement abstract method")

class Main(GUI):
	def set_components(self):
		self.__treeview_account = self.builder.get_object("main_treeview_account")
		self.__treeview_mail = self.builder.get_object("main_treeview_mail")
		self.__treeview_email = self.builder.get_object("main_treeview_email")

	def connect_buttons(self):
		self.button = self.builder.get_object("main_button_create")
		self.button.connect("clicked", self.on_button_create_clicked)

		self.button = self.builder.get_object("main_button_delete")
		self.button.connect("clicked", self.on_button_delete_clicked)

		self.button = self.builder.get_object("main_button_mar")
		self.button.connect("clicked", self.on_button_mar_clicked)

	def on_button_create_clicked(self, button):
		raise NotImplementedError("Subclass must implement abstract method")

	def on_button_delete_clicked(self, button):
		raise NotImplementedError("Subclass must implement abstract method")

	def on_button_mar_clicked(self, button):
		raise NotImplementedError("Subclass must implement abstract method")

          	  
