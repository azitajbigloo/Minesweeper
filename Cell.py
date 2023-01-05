from tkinter import Button, Label, messagebox
import settings
import random
import sys

class Cell:
    all = []
    cell_count = settings.CELLS_COUNT
    cell_count_label_object = None
    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.is_open = False
        self.x = x
        self.y = y

        #append the object to Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 12,
            height = 4,
            bg='red'
            #text = f'{self.x, self.y}'
        )
        #assign events to the btn
        btn.bind('<Button-1>', self.left_click_actions)  
        btn.bind('<Button-2>', self.right_click_actions)  
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text = f"Cells Left: {Cell.cell_count}",
            width= 12,
            height = 4,
            bg = settings.BG_COLOR,
            font = ("", 36)

        )
        Cell.cell_count_label_object = lbl

    # return a cell object based on x, y
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        
    @property
    def neighbor_cells(self):    
        cells = [ 
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x,self.y+1),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x+1,self.y-1)
        ]    
        cells = [cell for cell in cells if cell is not None] 
        return cells
    
    @property
    def neighbor_mine_cells_count(self):
        count = 0
        for cell in self.neighbor_cells:
            if cell.is_mine:
                count += 1
        return count

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -=1
            self.cell_btn_object.configure(
                text = self.neighbor_mine_cells_count
                )
            # change count in label
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells Left: {Cell.cell_count}" )
            #if this cell was marked as mine candidate remove the color to normal
            self.cell_btn_object.configure( 
                highlightbackground='black',
                bg = 'SystemButtonFace')

        # mark the cell as open at the end of the show_cell method
        self.is_open = True

    # @staticmethod
    #def message_box_action():
    #    res = messagebox.askretrycancel("askretrycancel", "OOPS Game Over!")
    #    if res == 'Retry':
    #        Game.root.destroy()
    #        Game.root.mainloop()
    #    else: 
    #        sys.exit()

    def show_mine(self):
        self.cell_btn_object.configure( 
             highlightbackground='red',
             bg = 'red',
             text = '*BOMB*')
        #messagebox.showinfo("Game Over", "Game Over")
        res = messagebox.askretrycancel("askretrycancel", "OOPS Game Over!")
        #messagebox.askretrycancel("askretrycancel", "OOPS Game Over!")
        #message_box_action()
        
        #    sys.exit()

    @staticmethod
    def randomize_mines():
        mines = random.sample(Cell.all, settings.NUM_MINES)
        #print(mines)
        for mine in mines:
            mine.is_mine = True
            #print(mine.is_mine)
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else: 
            if self.neighbor_mine_cells_count == 0:
                for cell_obj in self.neighbor_cells:
                    cell_obj.show_cell()
            self.show_cell()
            #if mines count = left cells count then player won
            if Cell.cell_count == settings.NUM_MINES:
                messagebox.showinfo("YOU WON", "YEAYYY YOU WON!")

        #cancel left and right click if the cell is open
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-2>')

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure( 
                highlightbackground='yellow',
                bg = 'yellow')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure( 
                highlightbackground='black',
                bg = 'SystemButtonFace')
            self.is_mine_candidate = False
       
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
