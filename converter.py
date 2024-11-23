import csv
import tkinter as tk
from tkinter import filedialog

def m3u8_to_csv(m3u8_file, csv_file):
    with open(m3u8_file, 'r', encoding='utf-8') as m3u8, open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        ID = 0
        lines = m3u8.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('#EXTINF:'):
                ID = ID + 1
                info = lines[i].split(',', 1)[1].strip()
                playtime = str(int(int(lines[i].split(':', 1)[1].split(',', 1)[0].strip())/60)) +" min" + " " + str(int(lines[i].split(':', 1)[1].split(',', 1)[0].strip())%60) + " sec"
                artist, title = info.split(' - ', 1)
                path = lines[i + 1].strip()
                csv_writer.writerow([ID, artist, title])

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("M3U8 files", "*.m3u8")])
    if file_path:
        m3u8_entry.delete(0, tk.END)
        m3u8_entry.insert(0, file_path)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        csv_entry.delete(0, tk.END)
        csv_entry.insert(0, file_path)

def start_conversion():
    m3u8_file = m3u8_entry.get()
    csv_file = csv_entry.get()
    if m3u8_file and csv_file:
        m3u8_to_csv(m3u8_file, csv_file)
        tk.messagebox.showinfo("Success", "Conversion completed successfully!")

root = tk.Tk()
root.title("M3U8 to CSV Converter")

tk.Label(root, text="Select M3U8 file:").grid(row=0, column=0, padx=10, pady=10)
m3u8_entry = tk.Entry(root, width=50)
m3u8_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Save CSV file as:").grid(row=1, column=0, padx=10, pady=10)
csv_entry = tk.Entry(root, width=50)
csv_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=save_file).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Start Conversion", command=start_conversion).grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()