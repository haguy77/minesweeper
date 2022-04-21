from tkinter import Button
import utils
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        """
        Builder of Cell object
        :param x: x location on cells' grid
        :param y: y location on cells' grid
        :param is_mine: is the cell a mine (Boolean)
        """
        self.is_mine = is_mine
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
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_click_actions)  # Left Click
        btn.bind('<Button-3>', self.right_click_actions)  # Right Click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
