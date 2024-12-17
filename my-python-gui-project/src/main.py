from tkinter import Tk, Frame, simpledialog
from utils import paint_cells

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Mi Aplicación GUI")
        self.ask_grid_size()
        self.setup_ui()

    def ask_grid_size(self):
        self.rows = simpledialog.askinteger("Input", "Número de filas:", minvalue=1, maxvalue=100)
        self.columns = simpledialog.askinteger("Input", "Número de columnas:", minvalue=1, maxvalue=100)

    def setup_ui(self):
        self.grid_frame = Frame(self.master)
        self.grid_frame.pack(fill="both", expand=True)

        self.create_grid(self.rows, self.columns)

    def create_grid(self, rows, columns):
        for row in range(rows):
            for column in range(columns):
                cell = Frame(self.grid_frame, borderwidth=1, relief="solid")
                cell.grid(row=row, column=column, sticky="nsew")

        for row in range(rows):
            self.grid_frame.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            self.grid_frame.grid_columnconfigure(column, weight=1)

        paint_cells(self.grid_frame, rows, columns)

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()