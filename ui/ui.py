from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self,master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel = Label(self, text = 'Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text = 'Quit', command = self.quit)
		self.quitButton.pack()
		
def main():
	app = Application()
	app.master.title('hello')
	app.mainloop()

main()