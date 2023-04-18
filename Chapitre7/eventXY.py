import tkinter as tk

def on_left_click(event):
    print("Clic gauche détecté à la position X =", event.x, "et Y =", event.y)

root = tk.Tk()
root.bind("<Button-1>", on_left_click)
root.mainloop()
