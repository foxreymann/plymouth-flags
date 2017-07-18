import tkinter as tk
root = tk.Tk()

def showFlag(event):
    countryName = input.get()
    flagImgPath = "./flags/%s.png" %(countryName) 
    print(flagImgPath)
    #flagImg = tk.PhotoImage(file="./flags/{}.png")
    #flag.pack()

tk.Label(root, text = "enter county name to see it's flag").pack()

input = tk.Entry(root)
input.pack()
input.focus_set()
input.bind("<Return>", showFlag)

root.mainloop()
