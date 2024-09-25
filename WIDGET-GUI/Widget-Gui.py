import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, bg="red", width=500, height=500)
canvas.pack()

label = tk.Label(root, text="Hello World")
label.pack()

root.mainloop()
