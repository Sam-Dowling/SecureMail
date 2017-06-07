from GUI import *

class LoginImplementation(Login):
	def on_button_login_clicked(self, button):
		print("Login Clicked")

if __name__ == '__main__':
	gui = LoginImplementation("res/Login.glade", "SecureMail_Login")
