import tkinter as tk
from tkinter import ttk

# Création d'une fenêtre
window = tk.Tk()
window.title("Tableau avec tkinter")

# Création du tableau
tree = ttk.Treeview(window, columns=("Nom", "Âge", "Pays"))

# Configuration des colonnes
tree.heading("#0", text="ID")
tree.heading("Nom", text="Nom")
tree.heading("Âge", text="Âge")
tree.heading("Pays", text="Pays")

tree.column("#0", width=50, anchor="w")
tree.column("Nom", width=100, anchor="center")
tree.column("Âge", width=50, anchor="center")
tree.column("Pays", width=100, anchor="center")

# Ajout des données
data = [
    {"id": 1, "nom": "Alice", "age": 25, "pays": "France"},
    {"id": 2, "nom": "Bob", "age": 30, "pays": "USA"},
    {"id": 3, "nom": "Charlie", "age": 20, "pays": "Canada"}
]

for item in data:
    tree.insert("", tk.END, text=item["id"], values=(item["nom"], item["age"], item["pays"]))

# Affichage du tableau
tree.pack()

# Exécution de la boucle principale
window.mainloop()
