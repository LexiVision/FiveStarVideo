'''
Program: videostoreGUI.py (page: 251)
Author: Alexa Ingria 6/13/22

GUI-based version of the video store project from chapter 2
'''

from breezypythongui import EasyFrame
from tkinter.font import Font 
# other imports

class VideoStore(EasyFrame):
	#definition of the __init__() method whitch is our class constructor
	def __init__(self):
		#call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Five Store Video", background = "blue")
		titleFont = Font(family = "Arial Black", size = 40)
		self.addLabel(text = "Five Star Video", row = 0, columnspan = 2, sticky ="NSEW", background = "blue", foreground = "yellow", font = titleFont)
		self.addLabel(text = "New Rental $3.00, old Rentals $2.00", row = 1, column = 0 , columnspan = 2, sticky = "NSEW", background = "blue" , foreground = "white")
		self.addLabel(text = "No. of new rentals:", row = 2, colunm = 0,background = "blue", foreground = "white" )
		self.newRental = self.addIntegerField(value = 0, row = 3, column = 0, background = "blue", foreground = "white")
		self.addLabel(text = " No. of old rental:", row = 3, column = 0, background = "blue", foreground = "white")
		self.oldRentals = self.addIntegerField(value = 0, row = 3, colunm = 1)
		self.button = self.addbutton(text = "Calculate", row = 4, colunm = 0 , columnspan = 2)
		self.button["background"] = "yellow"
		self.button["width"] = 25
		self.addLable(text = "The total for this order is:", row = 5, colunm = 0, background = "Blue", foreground = "White")
		self.total = self.addFloatField(value = 0.0, row = 5, colunm = 1, precision = 2, state = "readonly")
	# the event handing method the button
	def calculate(self):
		new = self.newRentals.getNumber()
		old = self.oldRnetals.getNumber()
		result = (new * 3.00) + (old * 2.00)
		self.total.setNumber(result)
		self.titleLabel["foreground"] = "white"


		# definition of the main() method which will establish class odject
def main():
	#instantiate an object from the class into mainloop()
	VideoStore().mainloop()

#global call to the main() method
main()

