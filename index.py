import tkinter as tk
root = tk.Tk()

def showFlag(event):
    countryName = input.get()
    print(countryName)

tk.Label(root, text = "enter county name to see it's flag").pack()

input = tk.Entry(root)
input.pack()
input.focus_set()
input.bind("<Return>", showFlag)

root.mainloop()
