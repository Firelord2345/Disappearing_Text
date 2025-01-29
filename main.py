import tkinter as tk
from tkinter import messagebox
import threading
import time

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")
        self.root.geometry("600x400")
        self.last_written_time = time.time()

        # Add Home Page
        self.home_page()

    def home_page(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.root, text="Welcome to Dangerous Writing App!", font=("Arial", 20))
        title_label.pack(pady=20)

        start_button = tk.Button(self.root, text="Start Writing", command=self.start_writing)
        start_button.pack(pady=10)

    def start_writing(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        self.text_area = tk.Text(self.root, wrap=tk.WORD, width=70, height=20)
        self.text_area.pack(pady=10)
        self.text_area.bind("<KeyRelease>", self.on_key_press)

        # Start timer thread
        self.start_timer()

    def on_key_press(self, event):
        """This method is called every time a key is pressed."""
        self.last_written_time = time.time()

    def start_timer(self):
        """Start a timer in a separate thread to check for inactivity."""
        threading.Thread(target=self.check_inactivity, daemon=True).start()

    def check_inactivity(self):
        while True:
            time.sleep(1)
            if time.time() - self.last_written_time > 5:
                self.delete_progress()
                break

    def delete_progress(self):
        """Delete all written progress and show an end message."""
        self.text_area.delete(1.0, tk.END)
        messagebox.showinfo("Oops!", "You stopped writing. Your progress has been lost.")
        self.home_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
