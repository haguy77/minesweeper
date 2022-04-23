from tkinter import Button, Label, Event
import utils
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    mines_count = settings.MINES_COUNT
    mines_count_label_object = None
    moves_count = 0
    moves_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        """
        Builder of Cell object
        :param x: x location on cells' grid
        :param y: y location on cells' grid
        :param is_mine: is the cell a mine (Boolean)
        """
        self.is_mine = is_mine
        self.is_opened = False
        self.is_marked_mine = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        """
        Initialize the Button Object of the cell
        :param location: tkinter.Frame for cell's Button
        """
        btn = Button(
            location,
            width=utils.cell_width(),
            height=utils.cell_height(),
            # text=f"{self.x}, {self.y}"
        )
        btn.bind("<Button-1>", self.left_click_actions)  # Left Click
        btn.bind("<Button-3>", self.right_click_actions)  # Right Click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        """
        Initialize the Cell Count Label Object of the game
        :param location: tkinter.Frame for Label's location
        :return: Label object of cell count
        """
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left: {Cell.cell_count}",
            font=("", utils.cell_count_label_font_size())
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_mines_count_label(location):
        """
        Initialize the Cell Count Label Object of the game
        :param location: tkinter.Frame for Label's location
        :return: Label object of cell count
        """
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Mines Left: {Cell.mines_count}",
            font=("", utils.cell_count_label_font_size())
        )
        Cell.mines_count_label_object = lbl

    @staticmethod
    def create_moves_count_label(location):
        """
        Initialize the Cell Count Label Object of the game
        :param location: tkinter.Frame for Label's location
        :return: Label object of cell count
        """
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Moves made: {Cell.moves_count}",
            font=("", utils.cell_count_label_font_size())
        )
        Cell.moves_count_label_object = lbl

    def left_click_actions(self, event: Event):
        print(event)
        if self.is_mine:
            self.show_mine()
        else:
            # Changing moves count label to newer count
            Cell.moves_count = Cell.moves_count + 1
            if Cell.moves_count_label_object:
                Cell.moves_count_label_object.configure(
                    text=f"Moves made: {Cell.moves_count}"
                )
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If Mine count is equal to cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "Congratulations !\nYou won the game !", "Game Over", 0)
                sys.exit()

        # Cancel Left and Right click events if cell is already opened:
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    @staticmethod
    def get_cell_by_axis(x: int, y: int):
        """
        Return a cell object of the value of x, y
        :param x: x place in grid
        :param y: y place in grid
        :return: cell object of the value of x, y
        """
        if 0 > x > settings.GRID_SIZE or 0 > y > settings.GRID_SIZE:
            return None
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter = counter + 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count = Cell.cell_count - 1
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length,
                bg="SystemButtonFace"
            )
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
            # Changing mines count label if showing cell of marked mine
            if self.is_marked_mine:
                Cell.mines_count = Cell.mines_count + 1
                if Cell.mines_count_label_object:
                    Cell.mines_count_label_object.configure(
                        text=f"Mines Left: {Cell.mines_count}"
                    )
            # Mark the cell as opened as the last line of this method
            self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine :(", "Game Over", 0)
        sys.exit()

    def right_click_actions(self, event: Event):
        print(event)
        if not self.is_opened:
            # Changing moves count label to newer count
            Cell.moves_count = Cell.moves_count + 1
            if Cell.moves_count_label_object:
                Cell.moves_count_label_object.configure(
                    text=f"Moves made: {Cell.moves_count}"
                )
            if not self.is_mine_candidate:
                self.cell_btn_object.configure(
                    bg="orange"
                )
                self.is_mine_candidate = True
            elif self.is_mine_candidate and not self.is_marked_mine:
                Cell.mines_count = Cell.mines_count - 1
                self.cell_btn_object.configure(
                    bg="green"
                )
                # Replace the text of mines count label with the newer count
                if Cell.mines_count_label_object:
                    Cell.mines_count_label_object.configure(
                        text=f"Mines Left: {Cell.mines_count}"
                    )
                self.is_marked_mine = True
            else:
                Cell.mines_count = Cell.mines_count + 1
                self.cell_btn_object.configure(
                    bg="SystemButtonFace"
                )
                # Replace the text of mines count label with the newer count
                if Cell.mines_count_label_object:
                    Cell.mines_count_label_object.configure(
                        text=f"Mines Left: {Cell.mines_count}"
                    )
                self.is_mine_candidate = False
                self.is_marked_mine = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
