from GUI import *

class LoginImplementation(Login):
	def connect_button(self, button):
		print("Login")
		

if __name__ == '__main__':
	gui = LoginImplementation("res/Login.glade", "SecureMail_Login"
			)
