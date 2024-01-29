import PySimpleGUI as sg
import keyboard as kb
import time
import gui_2048
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
        [sg.Text("", size=(18, 1), key="-GAMEOVER-", pad=((100,0), (20,0)), text_color="red", font="Any 15")],
        [sg.Button("Change Theme", size=18, pad=((100,0), (20,0)))],
        [sg.Button("The game creator's", size=18, pad=((100,0), (10,20)))]
    ]

    window = sg.Window("2048", layout)

    return window

def update_buttons(window, mat):
    for i in range(4):
        for j in range(4):
            button_key = (i, j)
            value = mat[i][j]
            button_color = VALUE_COLOR_MAP.get(value, "grey")
            if value == 0:
                window[button_key].update("", button_color="grey")
            else:
                window[button_key].update(value, button_color=button_color)

def on_key(event):
    global key_press
    key_press = event.name.lower()

def flashing_button(window, window_button):
    current_button_color = window_button.ButtonColor
    window_button.update(button_color = (current_button_color[1], current_button_color[0]))
    window.refresh()
    time.sleep(0.1)
    window_button.update(button_color = (current_button_color[0], current_button_color[1]))
    return window


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

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-UP-" or key_press == "w" or key_press == "up":
            window = flashing_button(window, window["-UP-"])
            if move_up(mat):
                add_new_2(mat)
        elif event == "-DOWN-" or key_press == "s" or key_press == "down":
            window = flashing_button(window, window["-DOWN-"])
            if move_down(mat):
                add_new_2(mat)
        elif event == "-LEFT-" or key_press == "a" or key_press == "left":
            window = flashing_button(window, window["-LEFT-"])
            if move_left(mat):
                add_new_2(mat)
        elif event == "-RIGHT-" or key_press == "d" or key_press == "right":
            window = flashing_button(window, window["-RIGHT-"])
            if move_right(mat):
                add_new_2(mat)
        elif event == "New Game":
            mat = start_game()
            window["-GAMEOVER-"].update("")
        elif event == "The game creator's":
            gui_2048.titles(user_theme)
        elif event == "Change Theme":
            user_theme = gui_2048.theme_select(user_theme)
            window.close()
            sg.theme(user_theme)
            window = main_window(user_theme)
            continue
        
        update_buttons(window, mat)

        if get_current_state(mat) == 'LOST':
            window["-GAMEOVER-"].update("  Game Over!")
            window.refresh()

    window.close()
