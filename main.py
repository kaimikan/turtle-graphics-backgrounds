import os
from tkinter import *
from turtle import RawTurtle

import convertapi
# this package is called python-dotenv in pip
from dotenv import load_dotenv

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
delete_ps_choice = None
deleted_ps_file_path = ""

# INIT UI
window = Tk()
terminal_text = StringVar()
entry_text = StringVar()
drawing_name_text = StringVar()
window.title("Turtle Draws")
window.config(padx=25, pady=50, bg="Gray")

# Drawing Title
drawing_title_label = Label(textvariable=drawing_name_text, fg="White", bg="Black")
drawing_title_label.grid(column=0, row=0, columnspan=8, sticky="EW")

# Turtle Drawing Canvas
canvas = Canvas(master=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.grid(column=0, row=1, columnspan=8)
artist = RawTurtle(canvas)

# Terminal Yes Button
yes_button = Button(text="Y")

# Terminal No Button
no_button = Button(text="N")

# Terminal Label
terminal_label = Label(textvariable=terminal_text, fg="White", bg="Black")
terminal_label.grid(column=0, row=2, columnspan=8, sticky="EW")

# Entry Field
entry_field = Entry(textvariable=entry_text)
entry_field.grid(column=0, row=3, columnspan=6, sticky="EW")

# Entry Confirmation Button
confirmation_button = Button(text="Enter")
confirmation_button.grid(column=6, row=3, sticky="EW")

# Entry Reset Button
reset_button = Button(text="Reset")
reset_button.grid(column=7, row=3, sticky="EW")

# Draw Button
draw_button = Button(text="Draw")
draw_button.grid(column=0, row=4, columnspan=4, sticky="EW")

# Export Button
export_button = Button(text="Export")
# export_button.grid(column=5, row=4, columnspan=4, sticky="EW")
export_button["state"] = DISABLED


def update_terminal(text):
    terminal_text.set(text)


def toggle_answer_layout(is_choice_layout_hidden):
    if not is_choice_layout_hidden:
        no_button.grid(column=7, row=2, sticky="EW")
        yes_button.grid(column=6, row=2, sticky="EW")
        terminal_label.grid_forget()
        terminal_label.grid(column=0, row=2, columnspan=6, sticky="EW")
    else:
        terminal_label.grid_forget()
        terminal_label.grid(column=0, row=2, columnspan=8, sticky="EW")
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
        export_button.grid(column=5, row=4, columnspan=4, sticky="EW")
        return True


def draw():
    update_terminal("drawing...")
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
            delete_converted_ps_file(folder_path, file_name)
    else:
        update_terminal("the program is in testing mode so no conversion is being made now "
                        "(doing this to preserve free API requests).")
        print("the program is in testing mode so no conversion is being made now "
              "(doing this to preserve free API requests).")


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


update_terminal("...")
drawing_name_text.set("No name for the drawing yet...")
reset_button.config(command=clear_entry)
confirmation_button.config(command=validate_entry)
yes_button.config(command=lambda answer=True: give_answer(answer))
no_button.config(command=lambda answer=False: give_answer(answer))
draw_button.config(command=draw)
export_button.config(command=export_drawing)

window.mainloop()
