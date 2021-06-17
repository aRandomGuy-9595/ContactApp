import sys

import tkinter as tk
from tkinter import messagebox as msg

from settings import Settings
from appPage import AppPage
from loginPage import LoginPage

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_container()
		self.create_menus()

		self.pages = {}
		self.create_appPage()
		self.create_loginPage()

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self)
		self.menuBar.delete("File")

	def addnew_pressed(self):
		self.AppPage.clicked_add_new_btn()

	def auth_login(self):
		username = self.pages['loginPage'].var_username.get()
		password = self.pages['loginPage'].var_password.get()


		granted = self.settings.login(username, password)
		if granted:
			self.change_page('appPage')
			self.create_menus()
		elif len(username) == 0:
			msg.showerror("Error!", "Please enter a valid username.")
		elif len(password) == 0:
			msg.showerror("Error!", "Please enter your password.")
		else:
			msg.showerror("Error!", "ID and password not found/mismatch.")

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def create_menus(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
		#self.fileMenu.add_command(label="New Item", command=self.addnew_pressed)
		self.fileMenu.add_command(label="Log Out", command=self.create_loginPage)
		self.fileMenu.add_command(label="Exit", command=self.exit_program)

		self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
		self.helpMenu.add_command(label="About", command=self.show_about_info)

		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)


	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)


	def create_appPage(self):
		self.pages['appPage'] = AppPage(self.container, self.app)


	def show_about_info(self):
		msg.showinfo("About this app", "Created by Fioreno Malvin and Nicholas Dharmawan, with some teamwork w/ kelompok sblh: olip saori :hehe:")

	def exit_program(self):
		respond = msg.askyesnocancel("Exit Program", "Are you sure and really sure to close the program ?")
		if respond:
			sys.exit()
		


class GudangInfo:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myGudangInfo = GudangInfo()
	myGudangInfo.run()