# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
import tkinter as tk
import unittest
from Chapitre14.application import TaskList


class TaskTests(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.addCleanup(self.root.destroy)
        self.app = TaskList(self.root)

    def test_delete_before_selection(self):
        self.app.delete_task()
        self.assertEqual(self.app.tasks, [])

    def test_blank_task_ignored(self):
        self.app.task_entry.insert(0, "   ")
        self.app.add_task()
        self.assertEqual(self.app.tasks, [])

    def test_add_and_delete_selected_task(self):
        for value in ("one", "two"):
            self.app.task_entry.insert(0, value)
            self.app.add_task()
        self.app.task_list.selection_set(1)
        self.app.delete_task()
        self.assertEqual(self.app.tasks, ["one"])
        self.assertEqual(self.app.task_list.get(0, tk.END), ("one",))


if __name__ == "__main__":
    unittest.main()
