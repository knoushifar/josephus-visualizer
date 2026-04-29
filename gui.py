import math
import tkinter as tk
from tkinter import messagebox

from josephus import josephus_order


class JosephusVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Josephus Problem Visualizer")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        self.canvas_width = 650
        self.canvas_height = 520
        self.center_x = self.canvas_width // 2
        self.center_y = self.canvas_height // 2
        self.radius = 200

        self.soldier_items = {}
        self.elimination_order = []
        self.survivor = None
        self.current_step = 0

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Josephus Problem Visualizer",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Number of soldiers:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.n_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
        self.n_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Step size:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
        self.k_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
        self.k_entry.grid(row=0, column=3, padx=5)

        self.start_button = tk.Button(
            input_frame,
            text="Start",
            command=self.start_visualization,
            font=("Arial", 12),
            width=10
        )
        self.start_button.grid(row=0, column=4, padx=10)

        self.reset_button = tk.Button(
            input_frame,
            text="Reset",
            command=self.reset,
            font=("Arial", 12),
            width=10
        )
        self.reset_button.grid(row=0, column=5, padx=5)

        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="white",
            highlightthickness=1,
            highlightbackground="gray"
        )
        self.canvas.pack(pady=10)

        self.info_label = tk.Label(
            self.root,
            text="Enter values and click Start.",
            font=("Arial", 13)
        )
        self.info_label.pack(pady=5)

        self.order_label = tk.Label(
            self.root,
            text="Elimination order: -",
            font=("Arial", 11),
            wraplength=800,
            justify="center"
        )
        self.order_label.pack(pady=5)

    def validate_inputs(self):
        try:
            n = int(self.n_entry.get())
            k = int(self.k_entry.get())

            if n <= 1:
                raise ValueError("Number of soldiers must be greater than 1.")

            if k <= 0:
                raise ValueError("Step size must be greater than 0.")

            if n > 100:
                raise ValueError("Please enter 100 or fewer soldiers for better visualization.")

            return n, k

        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
            return None, None

    def draw_soldiers(self, n):
        self.canvas.delete("all")
        self.soldier_items = {}

        for i in range(n):
            angle = 2 * math.pi * i / n
            x = self.center_x + self.radius * math.sin(angle)
            y = self.center_y - self.radius * math.cos(angle)

            soldier_number = i + 1

            circle = self.canvas.create_oval(
                x - 18,
                y - 18,
                x + 18,
                y + 18,
                fill="lightgray",
                outline="black",
                width=2
            )

            text = self.canvas.create_text(
                x,
                y,
                text=str(soldier_number),
                font=("Arial", 10, "bold")
            )

            self.soldier_items[soldier_number] = (circle, text)

    def start_visualization(self):
        n, k = self.validate_inputs()

        if n is None or k is None:
            return

        self.reset()
        self.draw_soldiers(n)

        self.elimination_order, self.survivor = josephus_order(n, k)
        self.current_step = 0

        self.info_label.config(text="Visualization started...")
        self.order_label.config(text="Elimination order: ")

        self.start_button.config(state="disabled")
        self.animate_elimination()

    def animate_elimination(self):
        if self.current_step < len(self.elimination_order):
            eliminated = self.elimination_order[self.current_step]
            circle, text = self.soldier_items[eliminated]

            self.canvas.itemconfig(circle, fill="tomato")
            self.canvas.itemconfig(text, fill="white")

            shown_order = self.elimination_order[:self.current_step + 1]
            self.order_label.config(
                text="Elimination order: " + ", ".join(map(str, shown_order))
            )

            self.info_label.config(text=f"Soldier {eliminated} eliminated.")

            self.current_step += 1
            self.root.after(700, self.animate_elimination)

        else:
            circle, text = self.soldier_items[self.survivor]
            self.canvas.itemconfig(circle, fill="lightgreen")
            self.canvas.itemconfig(text, fill="black")

            self.info_label.config(text=f"Survivor: Soldier {self.survivor}")
            self.start_button.config(state="normal")

    def reset(self):
        self.canvas.delete("all")
        self.soldier_items = {}
        self.elimination_order = []
        self.survivor = None
        self.current_step = 0
        self.info_label.config(text="Enter values and click Start.")
        self.order_label.config(text="Elimination order: -")
        self.start_button.config(state="normal")