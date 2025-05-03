import tkinter as tk
from utils.db import create_tables
from gui.report_crime import report_crime_screen

if __name__ == "__main__":
    create_tables()

    root = tk.Tk()
    report_crime_screen(root)
    root.mainloop()
