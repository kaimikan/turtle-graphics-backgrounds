from turtle import Turtle, Screen
import os
import convertapi
# this package is called python-dotenv in pip
from dotenv import load_dotenv

artist = Turtle()
canvas = Screen()
artist.shape("square")
artist.color("Gray")

canvas.bgcolor("White")
canvas.colormode(255)
artist.circle(radius=50)


def name_drawing():
    name = input("drawing name: ")
    check_name = name.replace("-", "").replace("_", "")
    # is alphanumerical
    while not check_name.isalnum():
        name = input("not valid, try again: ")
        check_name = name.replace("-", "").replace("_", "")

    return name


def export_drawing():
    drawing = artist.getscreen()
    drawing_name = name_drawing()
    drawings_count = 0
    drawings_folder = "./drawings"
    # count total files to give each one a unique name
    for path in os.listdir(drawings_folder):
        if os.path.isfile(os.path.join(drawings_folder, path)):
            drawings_count += 1
    print(f"Total drawings: {drawings_count}")

    image_path = f"{drawings_folder}/drawing_{drawings_count}_{drawing_name}"

    drawing.getcanvas().postscript(file=f"{image_path}.ps")

    convert_ps_to_png(f"{drawings_folder}/", f"drawing_{drawings_count}_{drawing_name}")


def convert_ps_to_png(folder_path, file_name):
    testing_other_code = False
    if not testing_other_code:
        print("converting...")
        load_dotenv('.env')
        convertapi.api_secret = os.getenv("api_secret")
        try:
            convertapi.convert('png', {
                'File': folder_path + file_name + ".ps"
            }, from_format="ps").save_files(folder_path)
        except (convertapi.ApiError, convertapi.BaseError):
            print("some error occurred with the api")
        else:
            print("the file has been converted!")
            delete_converted_ps_file(folder_path, file_name)
    else:
        print("the program is in testing mode so no conversion is being made now "
              "(doing this to preserve free API requests).")


def delete_converted_ps_file(folder_path, file_name):
    choice = input("delete the converted .ps file ('y'/'n'): ").lower()
    while not choice == 'n' and not choice == 'y':
        choice = input("delete the converted .ps file ('y'/'n'): ").lower()

    if choice == 'y':
        os.remove(f"{folder_path}{file_name}.ps")
        print("deleted the ps file")
    else:
        print("kept the ps file")


export_drawing()

canvas.exitonclick()
