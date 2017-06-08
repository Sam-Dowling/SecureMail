from GUI import *

def verify_username(username):
	if username == "Luke":
		return True
	else:
		return False

def verify_password(password):
	if password == "password":
		return True
	else:
		return False

def start_main_gui():
	main_gui = MainImplementation("res/Main.glade", "SecureMail_Main")
	main_gui.start_window()

class LoginImplementation(Login):
	def on_button_login_clicked(self, button):
		print("Login Clicked")
		if(verify_username(self.entry_username.get_text())):
			print("Correct Username")
			if(verify_password(self.entry_password.get_text())):
				print("Correct Password")
				start_main_gui()
			else:
				print("Incorrect password")
		else:
			print("Incorrect username")
		

class MainImplementation(Main):
	def on_button_create_clicked(self, button):
		print("create")

	def on_button_delete_clicked(self, button):
		print("delete")

	def on_button_mar_clicked(self, button):
		print("mark as read")


if __name__ == '__main__':
	gui = LoginImplementation("res/Login.glade", "SecureMail_Login")
	gui.start_window()
