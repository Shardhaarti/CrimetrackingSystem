import tkinter as tk
from tkinter import font
from gui.report_crime import report_crime_screen
from gui.view_crimes import view_crime_records

def show_home_screen():
    window = tk.Tk()
    window.title("Crime Tracking System")
    window.geometry("500x300")
    window.configure(bg="#f2f2f2")

    heading = tk.Label(window, text="Crime Tracking System", font=("Arial", 20, "bold"), bg="#f2f2f2", fg="#333")
    heading.pack(pady=20)

    btn_style = {"font": ("Arial", 14), "bg": "#4CAF50", "fg": "white", "width": 20, "height": 2}

    report_btn = tk.Button(window, text="Report New Crime", command=report_crime_screen, **btn_style)
    report_btn.pack(pady=10)

    view_btn = tk.Button(window, text="View Past Reports", command=view_crime_records, **btn_style)
    view_btn.pack(pady=10)

    window.mainloop()
