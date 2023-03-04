import os
import tkinter.ttk
import random
from tkinter import *
from turtle import RawTurtle, TurtleScreen
from PIL import Image, ImageTk

import convertapi
# this package is called python-dotenv in pip
from dotenv import load_dotenv

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = "#000000"
GREY = "#808080"
BROWN = "#964B00"
RED = "#FF0000"
ORANGE = "#FFA500"
YELLOW = "#FFFF00"
GREEN = "#00FF00"
BLUE = "#0000FF"
PURPLE = "#A020F0"
COLORS = [BLACK, GREY, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

COLOR_BUTTON_HEIGHT = 25
delete_ps_choice = None
deleted_ps_file_path = ""
load_image_selection = ""

# INIT UI
window = Tk()

terminal_text = StringVar()
random_color_state = StringVar()
is_color_random = False
random_color_state.set("Random Color (OFF)")
entry_text = StringVar()
drawing_name_text = StringVar()
window.title("Turtle Draws")
window.config(padx=25, pady=50)

# Pagination
notebook = tkinter.ttk.Notebook(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
notebook.grid(column=0, row=0)

drawing_exporting_frame = tkinter.ttk.Frame(notebook, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
drawing_exporting_frame.grid(column=0, row=0)

gallery_frame = tkinter.ttk.Frame(notebook, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
gallery_frame.grid(column=0, row=0)

notebook.add(drawing_exporting_frame, text="Draw")
notebook.add(gallery_frame, text="Gallery")

# Drawing Title
drawing_title_label = Label(master=drawing_exporting_frame, textvariable=drawing_name_text, fg="White", bg="Black")
drawing_title_label.grid(column=0, row=0, columnspan=9, sticky="EW")

# Turtle Drawing Canvas
canvas = Canvas(master=drawing_exporting_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT - 100 - COLOR_BUTTON_HEIGHT)
canvas.grid(column=0, row=1, columnspan=9)
drawing_screen = TurtleScreen(canvas)
artist = RawTurtle(drawing_screen)

# Terminal Yes Button
yes_button = Button(master=drawing_exporting_frame, text="Y")

# Terminal No Button
no_button = Button(master=drawing_exporting_frame, text="N")

# Terminal Label
terminal_label = Label(master=drawing_exporting_frame, textvariable=terminal_text, fg="White", bg="Black")
terminal_label.grid(column=0, row=2, columnspan=9, sticky="EW")

# Entry Field
entry_field = Entry(master=drawing_exporting_frame, textvariable=entry_text)
entry_field.grid(column=0, row=3, columnspan=7, sticky="EW")

# Entry Confirmation Button
confirmation_button = Button(master=drawing_exporting_frame, text="Enter")
confirmation_button.grid(column=7, row=3, sticky="EW")

# Entry Reset Button
reset_button = Button(master=drawing_exporting_frame, text="Reset")
reset_button.grid(column=8, row=3, sticky="EW")

# Draw Button
draw_button = Button(master=drawing_exporting_frame, text="Circle")
draw_button.grid(column=0, row=4, columnspan=1, sticky="EW")

# Penup Button
penup_button = Button(master=drawing_exporting_frame, text="Pen Up")
penup_button.grid(column=1, row=4, columnspan=1, sticky="EW")

# Pendown Button
pendown_button = Button(master=drawing_exporting_frame, text="Pen Down")
pendown_button.grid(column=2, row=4, columnspan=1, sticky="EW")
pendown_button["state"] = DISABLED

# Brush Size Buttons
increase_brush_size_button = Button(master=drawing_exporting_frame, text="+")
increase_brush_size_button.grid(column=3, row=4, columnspan=1, sticky="EW")

decrease_brush_size_button = Button(master=drawing_exporting_frame, text="-")
decrease_brush_size_button.grid(column=4, row=4, columnspan=1, sticky="EW")
decrease_brush_size_button["state"] = DISABLED

# Clear Canvas Button
clear_button = Button(master=drawing_exporting_frame, text="Clear", command=lambda: artist.clear())
clear_button.grid(column=5, row=4, columnspan=1, sticky="EW")

# Random Button
random_button = Button(master=drawing_exporting_frame, textvariable=random_color_state)
random_button.grid(column=6, row=4, columnspan=1, sticky="EW")

# Export Button
export_button = Button(master=drawing_exporting_frame, text="Export")
# export_button.grid(column=5, row=4, columnspan=4, sticky="EW")
export_button["state"] = DISABLED

# Color Selection Buttons
black_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(BLACK),
                      background=BLACK, highlightthickness=0, borderwidth=0)
black_button.grid(column=0, row=5, sticky="EW")

grey_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(GREY),
                     background=GREY, highlightthickness=0, borderwidth=0)
grey_button.grid(column=1, row=5, sticky="EW")

brown_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(BROWN),
                      background=BROWN, highlightthickness=0, borderwidth=0)
brown_button.grid(column=2, row=5, sticky="EW")

red_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(RED), background=RED,
                    highlightthickness=0, borderwidth=0)
red_button.grid(column=3, row=5, sticky="EW")

orange_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(ORANGE), background=ORANGE,
                       highlightthickness=0, borderwidth=0)
orange_button.grid(column=4, row=5, sticky="EW")

yellow_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(YELLOW), background=YELLOW,
                       highlightthickness=0, borderwidth=0)
yellow_button.grid(column=5, row=5, sticky="EW")

green_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(GREEN), background=GREEN,
                      highlightthickness=0, borderwidth=0)
green_button.grid(column=6, row=5, sticky="EW")

blue_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(BLUE), background=BLUE,
                     highlightthickness=0, borderwidth=0)
blue_button.grid(column=7, row=5, sticky="EW")

purple_button = Button(master=drawing_exporting_frame, command=lambda: artist.color(PURPLE), background=PURPLE,
                       highlightthickness=0, borderwidth=0)
purple_button.grid(column=8, row=5, sticky="EW")

# Gallery Frame Widgets

# List
scroll = Scrollbar(gallery_frame)
drawing_list = Listbox(gallery_frame, yscrollcommand=scroll.set)
scroll.config(command=drawing_list.yview)
drawing_list.grid(column=0, row=0)

# Load Image Canvas
# load_image_canvas = Canvas(master=gallery_frame, width=WINDOW_WIDTH - 100, height=WINDOW_HEIGHT - 200, background="red")
# load_image_canvas.grid(column=1, row=0)

# Load Image Label
image_label = Label(master=gallery_frame, text="what")
image_label.grid(row=0, column=1, rowspan=2)

# Load Image Button
load_image_button = Button(master=gallery_frame, text="Load")
load_image_button["state"] = DISABLED
load_image_button.grid(column=0, row=1, sticky="NEWS")


def update_terminal(text):
    terminal_text.set(text)


def toggle_answer_layout(is_choice_layout_hidden):
    if not is_choice_layout_hidden:
        no_button.grid(column=8, row=2, sticky="EW")
        yes_button.grid(column=7, row=2, sticky="EW")
        terminal_label.grid_forget()
        terminal_label.grid(column=0, row=2, columnspan=7, sticky="EW")
    else:
        terminal_label.grid_forget()
        terminal_label.grid(column=0, row=2, columnspan=9, sticky="EW")
        no_button.grid_forget()
        yes_button.grid_forget()


def give_answer(yes_no_answer):
    global delete_ps_choice, deleted_ps_file_path
    delete_ps_choice = yes_no_answer
    toggle_answer_layout(is_choice_layout_hidden=True)
    delete_converted_ps_file(deleted_ps_file_path, "")


def clear_entry():
    entry_text.set("")


def validate_entry():
    text = entry_text.get().replace("-", "").replace("_", "").replace(" ", "")
    entry_text.set(text)
    if not text.isalnum():
        update_terminal("not valid, try again: ")
        clear_entry()
        return False
    else:
        update_terminal(f"valid name entry ")
        drawing_name_text.set(text.title())
        export_button["state"] = NORMAL
        export_button.grid(column=7, row=4, columnspan=2, sticky="EW")
        return True


def draw():
    update_terminal("drawing...")
    if is_color_random:
        artist.color(random.choice(COLORS))
    artist.circle(radius=50)


def delete_converted_ps_file(folder_path, file_name):
    global deleted_ps_file_path
    if delete_ps_choice is None:
        update_terminal("delete the converted .ps file ('y'/'n'): ")
        toggle_answer_layout(is_choice_layout_hidden=False)
        deleted_ps_file_path = f"{folder_path}{file_name}.ps"
    elif delete_ps_choice is True:
        print(f"{deleted_ps_file_path}")
        os.remove(f"{deleted_ps_file_path}")
        update_terminal("deleted the ps file")
        print("deleted the ps file")
    elif delete_ps_choice is False:
        update_terminal("kept the ps file")
        print("kept the ps file")


def convert_ps_to_png(folder_path, file_name):
    testing_other_code = False
    if not testing_other_code:
        update_terminal("converting...")
        print("converting...")
        load_dotenv('.env')
        convertapi.api_secret = os.getenv("api_secret")
        try:
            convertapi.convert('png', {
                'File': folder_path + file_name + ".ps"
            }, from_format="ps").save_files(folder_path)
        except (convertapi.ApiError, convertapi.BaseError):
            update_terminal("some error occurred with the api")
            print("some error occurred with the api")
        else:
            update_terminal("the file has been converted!")
            print("the file has been converted!")
            load_gallery_images()
            delete_converted_ps_file(folder_path, file_name)
    else:
        update_terminal("the program is in testing mode so no conversion is being made now "
                        "(doing this to preserve free API requests).")
        print("the program is in testing mode so no conversion is being made now "
              "(doing this to preserve free API requests).")


def load_gallery_images():
    drawings_folder = "./drawings"
    drawing_list.delete(0, END)
    # count total files to give each one a unique name
    for path in os.listdir(drawings_folder):
        if path[-4:] == ".png":
            if os.path.isfile(os.path.join(drawings_folder, path)):
                drawing_list.insert(END, path)


def load_image():
    global load_image_selection
    image = Image.open(f"./drawings/{load_image_selection}")
    original_image_height = 2339
    original_image_width = 1653
    scale = 0.1
    image = image.resize((int(original_image_width * scale), int(original_image_height * scale)), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # not sure why but both lines are needed
    image_label.config(image=photo)
    image_label.image = photo


def export_drawing():
    drawing = artist.getscreen()
    update_terminal("drawing name: ")
    drawing_name = entry_text.get()
    drawings_count = 0
    drawings_folder = "./drawings"
    # count total files to give each one a unique name
    for path in os.listdir(drawings_folder):
        if os.path.isfile(os.path.join(drawings_folder, path)):
            drawings_count += 1

    update_terminal(f"Total drawings: {drawings_count}")
    print(f"Total drawings: {drawings_count}")

    image_path = f"{drawings_folder}/drawing_{drawings_count}_{drawing_name}"

    drawing.getcanvas().postscript(file=f"{image_path}.ps")

    convert_ps_to_png(f"{drawings_folder}/", f"drawing_{drawings_count}_{drawing_name}")


def callback(event):
    global load_image_selection
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        load_image_selection = data
        load_image_button["state"] = NORMAL
    else:
        load_image_selection = ""
        load_image_button["state"] = DISABLED


def move_artist(x, y):
    if is_color_random:
        artist.color(random.choice(COLORS))
    artist.setpos(x, y)


def pen_up():
    artist.penup()
    penup_button["state"] = DISABLED
    pendown_button["state"] = NORMAL
    pass


def pen_down():
    artist.pendown()
    penup_button["state"] = NORMAL
    pendown_button["state"] = DISABLED


def random_color():
    global is_color_random
    is_color_random = not is_color_random
    if is_color_random:
        random_color_state.set("Random Color (ON)")
    else:
        random_color_state.set("Random Color (OFF)")


def increase_brush_size():
    artist.pensize(artist.pen()['pensize'] + 1)
    decrease_brush_size_button["state"] = NORMAL
    pass


def decrease_brush_size():
    if artist.pen()['pensize'] - 1 <= 1:
        decrease_brush_size_button["state"] = DISABLED
    artist.pensize(abs(artist.pen()['pensize'] - 1))


increase_brush_size_button.config(command=increase_brush_size)
decrease_brush_size_button.config(command=decrease_brush_size)
random_button.config(command=random_color)
penup_button.config(command=pen_up)
pendown_button.config(command=pen_down)
drawing_screen.onclick(move_artist)
drawing_list.bind('<<ListboxSelect>>', callback)
load_image_button.config(command=load_image)
load_gallery_images()
update_terminal("...")
drawing_name_text.set("No name for the drawing yet...")
reset_button.config(command=clear_entry)
confirmation_button.config(command=validate_entry)
yes_button.config(command=lambda answer=True: give_answer(answer))
no_button.config(command=lambda answer=False: give_answer(answer))
draw_button.config(command=draw)
export_button.config(command=export_drawing)

window.mainloop()
