import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer un cadre
frame = tk.Frame(window, bd=2, relief="ridge")

# Créer deux étiquettes
label1 = tk.Label(frame, text="Label 1")
label2 = tk.Label(frame, text="Label 2")

# Placer les étiquettes dans le cadre
label1.pack()
label2.pack()

# Placer le cadre dans la fenêtre
frame.pack()

# Afficher la fenêtre
window.mainloop()
