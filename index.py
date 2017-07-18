import tkinter as tk

root = tk.Tk()

def showFlag(event):
    countryName = input.get()
    flagImgPath = "./flags/%s.png" %(countryName) 
    photo2 = tk.PhotoImage(file='./flags/poland.png')
    lbl.configure(image=photo2)

tk.Label(root, text = "enter county name to see it's flag").pack()

input = tk.Entry(root)
input.pack()
input.focus_set()
input.bind("<Return>", showFlag)

photo = tk.PhotoImage(file='./flags/pt.png')
lbl = tk.Label(root, image=photo)
lbl.pack()

root.mainloop()
