# main.py

# Importing necessary libraries
import tkinter as tk
from terminal_gui import CryptoAnalyzerGUI

def main():
    # Create a new Tk root
    root = tk.Tk()

    # Create the GUI
    gui = CryptoAnalyzerGUI(root)

    # Start the Tk main loop
    root.mainloop()

if __name__ == "__main__":
    main()
