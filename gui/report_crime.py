import tkinter as tk
from tkinter import messagebox
from utils.db import get_db_connection
from gui.view_crimes import show_records

def report_crime_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Crime Reporting System__24BSCYS047")
    root.geometry("550x580")
    root.configure(bg="#ffe6f0")  # Baby pink background

    header = tk.Label(root, text="Crime Reporting Form", font=("Arial", 18, "bold"),
                      bg="#ff66a3", fg="white", pady=12)
    header.pack(fill=tk.X)

    def create_label_entry(label_text):
        outer_frame = tk.Frame(root, bg="#ff66a3", pady=2, padx=2)
        outer_frame.pack(pady=10, padx=25, fill=tk.X)

        inner_frame = tk.Frame(outer_frame, bg="#cce7ff", padx=10, pady=10)
        inner_frame.pack(fill=tk.BOTH)

        label = tk.Label(inner_frame, text=label_text, font=("Arial", 12), bg="#cce7ff", fg="#333")
        label.pack(anchor="w")

        entry = tk.Entry(inner_frame, width=45, font=("Arial", 11))
        entry.pack(pady=5)
        return entry

    title_entry = create_label_entry("Crime Title:")
    desc_entry = create_label_entry("Crime Description:")
    date_entry = create_label_entry("Date (YYYY-MM-DD):")
    location_entry = create_label_entry("Location:")

    def submit_report():
        title = title_entry.get()
        desc = desc_entry.get()
        date = date_entry.get()
        location = location_entry.get()

        if title and date and location:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO crime_reports (title, description, date, location) VALUES (?, ?, ?, ?)",
                (title, desc, date, location)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Crime Report Submitted Successfully!")
            for entry in [title_entry, desc_entry, date_entry, location_entry]:
                entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill all required fields!")

    def on_hover(e, btn, hover_color):
        btn['bg'] = hover_color

    def on_leave(e, btn, original_color):
        btn['bg'] = original_color

    submit_button = tk.Button(root, text="Submit Report", font=("Arial", 12),
                              bg="#28a745", fg="white", width=20, command=submit_report,
                              activebackground="#218838", bd=2, relief=tk.RAISED)
    submit_button.pack(pady=20)
    submit_button.bind("<Enter>", lambda e: on_hover(e, submit_button, "#218838"))
    submit_button.bind("<Leave>", lambda e: on_leave(e, submit_button, "#28a745"))

    view_button = tk.Button(root, text="View Past Records", font=("Arial", 12),
                            bg="#007bff", fg="white", width=20, command=lambda: show_records(root),
                            activebackground="#0056b3", bd=2, relief=tk.RAISED)
    view_button.pack(pady=10)
    view_button.bind("<Enter>", lambda e: on_hover(e, view_button, "#0056b3"))
    view_button.bind("<Leave>", lambda e: on_leave(e, view_button, "#007bff"))
