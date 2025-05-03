import tkinter as tk
from tkinter import ttk
from utils.db import get_db_connection

def show_records(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Past Crime Reports ________   24BSCYS047")
    root.geometry("750x450")
    root.configure(bg="#ffe6f0")  # Baby pink background

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="#e0f7fa",  # Light sky blue
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#e0f7fa",
                    font=('Arial', 11))

    style.map("Treeview", background=[('selected', '#ff66a3')])  # Highlighted row: dark pink

    style.configure("Treeview.Heading",
                    font=('Arial', 12, 'bold'),
                    background="#ff66a3",  # Dark pink
                    foreground="white")

    back_button = tk.Button(root, text="Back to Report", command=lambda: go_back(root),
                            bg="#f44336", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
    back_button.pack(pady=(15, 5))

    cols = ('ID', 'Title', 'Date', 'Location')
    tree = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, date, location FROM crime_reports")
    records = cursor.fetchall()
    conn.close()

    for record in records:
        tree.insert("", tk.END, values=record)

    tree.pack(expand=True, fill='both', padx=20, pady=(5, 20))

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

def go_back(root):
    from gui.report_crime import report_crime_screen
    report_crime_screen(root)

