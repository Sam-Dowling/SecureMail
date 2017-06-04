#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

def verify_login(username, password):
	if username == "Test":
		if password == "password":
			print("Correct details")
			return True
		else:
			print("incorrect password")
	else:
		print("incorrect username")

	return False

def start_main():
	main_gui = Main("res/Main.glade", "SecureMail_Main")

class Login:

	def __init__(self, gladefile, window_name):
		self.connect_to_gladefile(gladefile)
		self.set_components()
		self.connect_buttons()
		self.start_window(window_name)


	def connect_to_gladefile(self, gladefile):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladefile)

	def set_components(self):
		self.__entry_username = self.builder.get_object("login_entry_username")
		self.__entry_password = self.builder.get_object("login_entry_password")

	def connect_buttons(self):
		self.button = self.builder.get_object("login_button_login")
		self.button.connect("clicked", self.on_button_login_clicked)

		self.button = self.builder.get_object("login_button_close")
		self.button.connect("clicked", Gtk.main_quit)

	def start_window(self, window_name):
		self.window = self.builder.get_object(window_name)
		self.window.connect("delete-event", Gtk.main_quit)
		self.window.show_all()
		Gtk.main()

	def on_button_login_clicked(self, button):
		if verify_login(self.__entry_username.get_text(), self.__entry_password.get_text()):
			start_main()
		else:
			print("Error: with login details")


class Main:

	def __init__(self, gladefile, window_name):
		self.connect_to_gladefile(gladefile)
		self.set_components()
		self.connect_buttons()
		self.start_window(window_name)

	def connect_to_gladefile(self, gladefile):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladefile)

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

	def start_window(self, window_name):
		self.window = self.builder.get_object(window_name)
		self.window.connect("delete-event", Gtk.main_quit)
		self.window.show_all()
		Gtk.main()

	def on_button_create_clicked(self, button):
		print("Create")

	def on_button_delete_clicked(self, button):
		print("Delete")

	def on_button_mar_clicked(self, button):
		print("Mark As Read")

          	  
