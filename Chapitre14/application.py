import tkinter as tk

class TaskList:
    def __init__(self, master):
        self.master = master
        self.master.title("Liste de tâches")
        self.tasks = []
        self.create_widgets()
    
    def create_widgets(self):
        # Cadre pour les entrées de tâches
        self.task_frame = tk.Frame(self.master)
        self.task_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Entrée de texte pour la nouvelle tâche
        self.task_entry = tk.Entry(self.task_frame)
        self.task_entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.task_entry.bind("<Return>", self.add_task)
        
        # Bouton pour ajouter une nouvelle tâche
        self.add_button = tk.Button(self.task_frame, text="Ajouter", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Cadre pour la liste des tâches
        self.list_frame = tk.Frame(self.master)
        self.list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Zone de défilement pour la liste des tâches
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Liste des tâches
        self.task_list = tk.Listbox(self.list_frame, yscrollcommand=self.scrollbar.set)
        self.task_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.task_list.bind("<<ListboxSelect>>", self.select_task)
        
        # Bouton pour supprimer la tâche sélectionnée
        self.delete_button = tk.Button(self.master, text="Supprimer", command=self.delete_task)
        self.delete_button.pack(side=tk.BOTTOM, pady=5)
        
        # Configuration de la zone de défilement pour la liste des tâches
        self.scrollbar.config(command=self.task_list.yview)
    
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
    
    def select_task(self, event=None):
        task_index = self.task_list.curselection()
        if len(task_index) > 0:
            self.selected_task = task_index[0]
        else:
            self.selected_task = None
    
    def delete_task(self):
        if self.selected_task is not None:
            self.task_list.delete(self.selected_task)
            del self.tasks[self.selected_task]
            self.selected_task = None
    
if __name__ == "__main__":
    root = tk.Tk()
    task_list = TaskList(root)
    root.mainloop()
