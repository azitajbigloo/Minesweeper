from tkinter import *
from Cell import Cell
import settings
import utils
import ctypes

root = Tk()

## window settings
#window configs
root.configure(bg=settings.BG_COLOR)

#change the dimension of the table
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

#add title
root.title ("Minesweeper Game")

#window height and width is not resizable
root.resizable(False, False)

#create a frame in the window
top_frame = Frame(
    root,
    bg= settings.BG_COLOR,
    width=settings.WIDTH,
    height=utils.height_prct(25)
)

# where we want the frame to start (0,0)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = settings.BG_COLOR,
    width= utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg = settings.BG_COLOR,
    width= utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25), 
    y=utils.height_prct(25)
)

game_title = Label( 
    top_frame,
    bg = settings.BG_COLOR,
    fg = settings.TITLE_FONT_COLOR,
    text = "MINESWEEPER GAME",
    font = ("", 48)
)
game_title.place(
    x= utils.height_prct(75), 
    y = utils.width_prct(1))

for x  in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x, row = y
        )

#call the label from cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)

Cell.randomize_mines()


#for c in Cell.all:
#    print(c.is_mine)
## Run window
#creates a simple window
root.mainloop()

