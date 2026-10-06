import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

class FluxForgeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('FluxForge Analytics Studio')
        self.geometry('1200x800')

        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_panel = ctk.CTkFrame(self, width=200)
        self.left_panel.grid(row=0, column=0, sticky='ns', padx=10, pady=10)

        self.add_button = ctk.CTkButton(self.left_panel, text='Add Node', command=self.add_node)
        self.add_button.pack(pady=10)

        self.canvas = tk.Canvas(self, bg='#2b2b2b', highlightthickness=0)
        self.canvas.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        self.right_panel = ctk.CTkFrame(self, width=300)
        self.right_panel.grid(row=0, column=2, sticky='ns', padx=10, pady=10)

        self.node_listbox = tk.Listbox(self.right_panel, bg='#333333', fg='white', selectbackground='#444444')
        self.node_listbox.pack(fill=tk.BOTH, expand=True, pady=10)

    def add_node(self):
        node_id = len(self.node_listbox.get(0, tk.END)) + 1
        self.node_listbox.insert(tk.END, f'Node {node_id}')
        self.canvas.create_rectangle(50, 50, 150, 150, fill='#3a7ebf', outline='#2b2b2b')
        self.canvas.create_text(100, 100, text=f'Node {node_id}', fill='white')

if __name__ == '__main__':
    app = FluxForgeApp()
    app.mainloop()