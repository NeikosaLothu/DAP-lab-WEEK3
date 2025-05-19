import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x400")  # Corrected geometry format
        self.root.configure(bg="#1e1e2f")  # Black background
        
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        self.create_ui()
    
    def create_ui(self):
        input_frame = tk.Frame(self.root, bg="#1e1e2f")
        input_frame.pack(fill="both", expand=True)
        
        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), bd=5, relief=tk.RIDGE, justify='right', bg="#1e1e2f", fg="cyan")
        input_field.pack(padx=10, pady=10, fill="both")
        
        button_frame = tk.Frame(self.root, bg="#1e1e2f")
        button_frame.pack(fill="both", expand=True)
        
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]
        
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                tk.Button(button_frame, text=button, font=('Arial', 14), width=5, height=2, bg="#00008b", fg="white", command=lambda b=button: self.on_button_click(b)).grid(row=i, column=j, padx=5, pady=5)
    
    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set("")
        elif button == "=":
            try:
                result = eval(self.expression)
                self.input_text.set(result)
                self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += button
            self.input_text.set(self.expression)
    
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
