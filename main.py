import tkinter as tk

from gui import JosephusVisualizer


def main():
    root = tk.Tk()
    app = JosephusVisualizer(root)
    root.mainloop()


if __name__ == "__main__":
    main()