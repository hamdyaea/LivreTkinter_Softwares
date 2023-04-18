from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk

fig, ax = plt.subplots()
x_values = [1, 2, 3, 4, 5]
y_values = [10, 8, 6, 4, 2]
ax.bar(x_values, y_values)

root = tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

tk.mainloop()
