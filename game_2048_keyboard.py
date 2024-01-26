import PySimpleGUI as sg
import keyboard as kb
from logic_colored import start_game, move_up, move_down, move_left, move_right, get_current_state, add_new_2

# Define a mapping of values to colors
VALUE_COLOR_MAP = {
    2: "red",
    4: "orange",
    8: "yellow",
    16: "green",
    32: "blue",
    64: "purple",
    128: "pink",
    256: "brown",
    512: "cyan",
    1024: "magenta",
    2048: "white",
}

def main_window(user_theme):
    sg.theme(user_theme)
    buttons = [[sg.Button('', size=(5, 2), pad=(5, 5), key=(i, j), font="Any 15") for j in range(4)] for i in range(4)]

    layout = [
        [buttons[0][0], buttons[0][1], buttons[0][2], buttons[0][3]],
        [buttons[1][0], buttons[1][1], buttons[1][2], buttons[1][3]],
        [buttons[2][0], buttons[2][1], buttons[2][2], buttons[2][3]],
        [buttons[3][0], buttons[3][1], buttons[3][2], buttons[3][3]],
        [sg.Button('\u21C7 A', font="Arial 22", size=(3, 1), pad=((22, 5), (15, 0)), key="-LEFT-"),
         sg.Button('\u21C8 W', font="Arial 22", size=(3, 1), pad=((5, 5), (15, 0)), key="-UP-"),
         sg.Button('\u21CA S', font="Arial 22", size=(3, 1), pad=((5, 5), (15, 0)), key="-DOWN-"),
         sg.Button('\u21C9 D', font="Arial 22", size=(3, 1), pad=((5, 5), (15, 0)), key="-RIGHT-")],
        [sg.Button("New Game", size=18, pad=((10, 5), (35, 0))),
         sg.Button("Exit", size=18, pad=((5, 10), (35, 0)))],
        [sg.Text("", size=(20, 1), key="-GAMEOVER-", text_color="red", font="Any 15")],
    ]

    window = sg.Window("2048", layout)

    return window

def update_buttons(window, mat):
    for i in range(4):
        for j in range(4):
            button_key = (i, j)
            value = mat[i][j]
            button_color = VALUE_COLOR_MAP.get(value, "grey")
            window[button_key].update(value if value != 0 else '', button_color=button_color)

def display_game_over(window):
    window["-GAMEOVER-"].update("Game Over!")

def on_key(event):
    global key_press
    key_press = event.name.lower()

def out_key(event):
    pass


if __name__ == '__main__':
    mat = start_game()
    user_theme = "DarkAmber"
    window = main_window(user_theme)

    while True:
        key_press = ""
        event = 0
        while key_press == "" and event == 0:
            event, values = window.read(500)
            kb.on_press(on_key)
        if key_press != "":
            kb.on_release_key(key_press, out_key)

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-UP-" or key_press == "w":
            # if key_press == "w":
            #     current_color = window["-UP-"][2]
            #     window["-UP-"].update(button_color="black")
            if move_up(mat):
                add_new_2(mat)
        elif event == "-DOWN-" or key_press == "s":
            if move_down(mat):
                add_new_2(mat)
        elif event == "-LEFT-" or key_press == "a":
            if move_left(mat):
                add_new_2(mat)
        elif event == "-RIGHT-" or key_press == "d":
            if move_right(mat):
                add_new_2(mat)
        elif event == "New Game":
            mat = start_game()
            window["-GAMEOVER-"].update("")
        update_buttons(window, mat)

        if get_current_state(mat) == 'LOST':
            display_game_over(window)

    window.close()
