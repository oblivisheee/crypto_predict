
# terminal_gui.py

# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox
from config import GUI_CONFIG
from decision_maker import make_decision

class CryptoAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(GUI_CONFIG['title'])
        self.root.geometry(f"{GUI_CONFIG['width']}x{GUI_CONFIG['height']}")
        self.root.resizable(GUI_CONFIG['resizable'], GUI_CONFIG['resizable'])

        self.decision_button = tk.Button(self.root, text="Make Decision", command=self.make_decision)
        self.decision_button.pack()

        self.decision_label = tk.Label(self.root, text="")
        self.decision_label.pack()

    def make_decision(self):
        decisions = make_decision()
        decision_text = "\n".join([f"{crypto}: {decision}" for crypto, decision in decisions.items()])
        self.decision_label.config(text=decision_text)
        messagebox.showinfo("Decisions", decision_text)

def main():
    root = tk.Tk()
    gui = CryptoAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()