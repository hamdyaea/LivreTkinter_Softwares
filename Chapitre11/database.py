import sqlite3
import tkinter as tk

# Connexion à la base de données
conn = sqlite3.connect('users.db')

# Création de la table utilisateur
conn.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL,age INTEGER NOT NULL);''')

# Fonction pour enregistrer les données utilisateur dans la base de données
def save_user():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Saisie utilisateur")

# Création des champs de saisie pour les données utilisateur
name_label = tk.Label(root, text="Nom")
name_entry = tk.Entry(root)
email_label = tk.Label(root, text="Email")
email_entry = tk.Entry(root)
age_label = tk.Label(root, text="Âge")
age_entry = tk.Entry(root)

# Ajout des champs de saisie à la fenêtre principale
name_label.pack()
name_entry.pack()
email_label.pack()
email_entry.pack()
age_label.pack()
age_entry.pack()

# Bouton pour enregistrer les données utilisateur dans la base de données
save_button = tk.Button(root, text="Enregistrer", command=save_user)
save_button.pack()

# Boucle principale de la fenêtre
root.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
