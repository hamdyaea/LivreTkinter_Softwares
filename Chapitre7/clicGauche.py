import tkinter as tk

def on_left_click(event):
    print("Clic gauche détecté.")

root = tk.Tk()
root.bind("<Button-1>", on_left_click)
root.mainloop()
