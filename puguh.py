from tkinter import *

import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

click = True

def checker(buttons):
	global click
	if buttons["text"] == " " and click == True:
		buttons["text"] = "X"
		click = False
	elif buttons["text"] == " " and click == False:
		buttons["text"] = "O"
		click = True
		
	elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
		button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
		button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
		button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
		button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
		button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
		button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
		button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
		tkinter.messagebox.showinfo("Winner X", "Selamat anda menang, Terima Kasih")
		exit()