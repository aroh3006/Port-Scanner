import tkinter as tk
import os
from tkinter import filedialog, messagebox
from datetime import datetime


current_scan_type = ""


def run_scan(scan_type):

    global current_scan_type

    target = entry.get()

    if target == "":
        messagebox.showerror("Error", "Please enter target IP")
        return

    if scan_type == 1:
        cmd = "nmap " + target
        current_scan_type = "Quick Scan"

    elif scan_type == 2:
        cmd = "nmap -p- " + target
        current_scan_type = "Full Port Scan"

    elif scan_type == 3:
        cmd = "nmap -sV " + target
        current_scan_type = "Service Version Scan"

    output.delete(1.0, tk.END)

    result = os.popen(cmd).read()

    output.insert(tk.END, result)



def save_report():

    data = output.get(1.0, tk.END)

    if data.strip() == "":
        messagebox.showerror("Error", "No scan result to save")
        return

    target = entry.get()

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    header = f"""
==========PORT SCANNER==========

Target   : {target}
Scan Type: {current_scan_type}
Date     : {date}
Time     : {time}

=================================

"""

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")]
    )

    if file == "":
        return

    with open(file, "w") as f:
        f.write(header)
        f.write(data)

    messagebox.showinfo("Success", "Report Saved Successfully!")



window = tk.Tk()
window.title("Port Scanner")
window.geometry("750x550")


tk.Label(window, text="Enter Target IP / Domain:").pack(pady=5)

entry = tk.Entry(window, width=45)
entry.pack(pady=5)


frame = tk.Frame(window)
frame.pack(pady=5)


tk.Button(frame, text="Quick Scan",
          command=lambda: run_scan(1), width=15).grid(row=0, column=0, padx=5)

tk.Button(frame, text="Full Scan",
          command=lambda: run_scan(2), width=15).grid(row=0, column=1, padx=5)

tk.Button(frame, text="Service Scan",
          command=lambda: run_scan(3), width=15).grid(row=0, column=2, padx=5)


tk.Button(window, text="Save Report",
          command=save_report, width=20).pack(pady=8)


output = tk.Text(window, height=22, width=90)
output.pack(pady=10)


window.mainloop()

