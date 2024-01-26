
import logic
import gui_2048
import PySimpleGUI as sg

def main_window(user_theme, mat):
		
	sg.theme(user_theme)
	layout = [
    [sg.Table(values=mat, headings=["Col1", "Col2", "Col3", "Col4"], justification="center",
              num_rows=4, row_height=60, hide_vertical_scroll=True, border_width=10,
              pad=((40,40), (20,0)), key="-TABLE-")],
    [sg.Button('\u21C7', font="Arial 22", pad=((40,5), (0,0)), key="-LEFT-"),
     sg.Button('\u21C8', font="Arial 22", key="-UP-"), 
     sg.Button('\u21CA', font="Arial 22", key="-DOWN-"), 
     sg.Button('\u21C9', font="Arial 22", key="-RIGHT-")],
    [sg.Button("New Game", size=11, pad=((40,10), (0,0))), sg.Button("Exit", size=11)],
    [sg.Button("Change Theme", size=20, pad=((55,10), (30,0)))],
    [sg.Button("The game creator's", size=20, pad=((55,10), (10,0)))]
]

	
	window = sg.Window("2048", layout)
	return window


if __name__ == '__main__':
	mat = logic.start_game()
	user_theme = "DarkAmber"
	window = main_window(user_theme, mat)

while(True):
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == "Exit":
		break
	elif event == "-UP-":
		# call the move_up function
		mat, flag = logic.move_up(mat)
		# get the current state
		status = logic.get_current_state(mat)
		# if game not over then continue
		# and add a new two
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Up  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		# else break the loop 
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "-DOWN-":
		# to move down
		mat, flag = logic.move_down(mat)
		status = logic.get_current_state(mat)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Down  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "-LEFT-":
		# to move left
		mat, flag = logic.move_left(mat)
		status = logic.get_current_state(mat)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Left  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "-RIGHT-":
		# to move right
		mat, flag = logic.move_right(mat)
		status = logic.get_current_state(mat)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Right  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "New Game":
		mat = logic.start_game()
		window["-TABLE-"].update(values=mat)
		continue
	elif event == "The game creator's":
		gui_2048.titles(user_theme)
	elif event == "Change Theme":
		user_theme = gui_2048.theme_select(user_theme)
		window.close()
		sg.theme(user_theme)
		window = main_window(user_theme, mat)
		continue

	window["-TABLE-"].update(values=mat)

window.close()
