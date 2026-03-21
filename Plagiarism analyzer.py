import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
from difflib import SequenceMatcher
class PlagiarismChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Plagiarism Analyzer")
        self.width = 600
        self.height = 500
        self.bg_color = "#90E0EF"
        self.root.configure(bg=self.bg_color)
        self.center_window()
        self.file1_content = ""
        self.file2_content = ""
        self.show_main_screen()
    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height // 2) - (self.height // 2)
        self.root.geometry(f'{self.width}x{self.height}+{x}+{y}')
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.configure(bg=self.bg_color)
    def show_main_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Plagiarism Analyzer",
                 font=("Helvetica", 26, "bold"),
                 bg=self.bg_color).pack(pady=60)
        start_btn = tk.Button(self.root, text="START",
                              command=lambda: [start_btn.config(bg="green"), self.upload_file1()],
                              width=20, height=2,
                              bg="white", fg="black",
                              font=("Helvetica", 12, "bold"))
        start_btn.pack()
    def read_file_with_pandas(self, filepath):
        try:
            df = pd.read_csv(filepath, sep='|', header=None,
                             engine='python', na_filter=False)
            return "\n".join(df[0].astype(str).tolist())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file:\n{e}")
            return None
    def upload_file1(self):
        self.clear_screen()
        tk.Label(self.root, text="Select First File",
                 font=("Helvetica", 14),
                 bg=self.bg_color).pack(pady=20)
        btn1 = tk.Button(self.root, text="Choose File 1",
                         command=lambda: [btn1.config(bg="green"), self.process_file1()],
                         bg="white", fg="black",
                         width=20)
        btn1.pack(pady=10)
    def process_file1(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text/CSV Files", "*.txt *.csv")])
        if file_path:
            content = self.read_file_with_pandas(file_path)
            if content:
                self.file1_content = content
                self.view_file(content, "File 1 Preview", self.upload_file2)
    def upload_file2(self):
        self.clear_screen()
        tk.Label(self.root, text="Select Second File",
                 font=("Helvetica", 14),
                 bg=self.bg_color).pack(pady=20)
        btn2 = tk.Button(self.root, text="Choose File 2",
                         command=lambda: [btn2.config(bg="green"), self.process_file2()],
                         bg="white", fg="black",
                         width=20)
        btn2.pack(pady=10)
    def process_file2(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text/CSV Files", "*.txt *.csv")])
        if file_path:
            content = self.read_file_with_pandas(file_path)
            if content:
                self.file2_content = content
                self.view_file(content, "File 2 Preview", self.ask_permission)
    def view_file(self, content, title, next_step):
        self.clear_screen()
        tk.Label(self.root, text=title,
                 font=("Helvetica", 12, "bold"),
                 bg=self.bg_color).pack(pady=10)
        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(expand=True, fill='both', padx=20)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text = tk.Text(frame, wrap='word',
                       yscrollcommand=scrollbar.set)
        text.insert(tk.END, content)
        text.config(state=tk.DISABLED)
        text.pack(side=tk.LEFT, expand=True, fill='both')
        scrollbar.config(command=text.yview)
        next_btn = tk.Button(self.root, text="Next",
                             command=lambda: [next_btn.config(bg="green"), next_step()],
                             bg="white", fg="black",
                             width=15)
        next_btn.pack(pady=15)
    def ask_permission(self):
        if messagebox.askyesno("Confirm", "Compare files now?"):
            self.calculate_plagiarism()
        else:
            self.show_main_screen()
    def calculate_plagiarism(self):
        matcher = SequenceMatcher(None,
                                  self.file1_content,
                                  self.file2_content,
                                  autojunk=False)
        percentage = matcher.ratio() * 100
        self.clear_screen()
        tk.Label(self.root, text="Result",
                 font=("Helvetica", 18, "bold"),
                 bg=self.bg_color).pack(pady=20)
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TProgressbar", thickness=25)
        progress = ttk.Progressbar(self.root,
                                   orient="horizontal",
                                   length=400,
                                   mode="determinate")
        progress.pack(pady=20)
        progress['value'] = percentage
        color = "red" if percentage > 30 else "green"
        tk.Label(self.root,
                 text=f"{percentage:.2f}%",
                 font=("Helvetica", 32, "bold"),
                 fg=color,
                 bg=self.bg_color).pack()
        tk.Label(self.root,
                 text="Percentage of Plagiarism",
                 font=("Helvetica", 14),
                 bg=self.bg_color).pack()
        restart_btn = tk.Button(self.root, text="Restart",
                                command=lambda: [restart_btn.config(bg="green"), self.show_main_screen()],
                                bg="white", fg="black",
                                width=15)
        restart_btn.pack(pady=30)
if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismChecker(root)
    root.mainloop()