
import logic
import PySimpleGUI as sg

if __name__ == '__main__':
	mat = logic.start_game()
	sg.theme("DarkAmber")
	layout = [[sg.Table(values=mat, headings=["Col1", "Col2", "Col3", "Col4"], justification="center",
				num_rows=4, row_height=70, key="-TABLE-")],
			[sg.Button('W'), sg.Button('S'), sg.Button('A'), sg.Button('D')],
        	[sg.Button("New Game", size=14), sg.Button("Exit", size=14)]
	]
	window = sg.Window("2048", layout)

while(True):
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == "Exit":
		break
	elif event == "W":
		x = "W"
	elif event == "S":
		x = "S"
	elif event == "A":
		x = "A"
	elif event == "D":
		x = "D"

	# we have to move up
	if(x == 'W' or x == 'w'):

		# call the move_up function
		mat, flag = logic.move_up(mat)

		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)

		# if game not over then continue
		# and add a new two
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)

		# else break the loop 
		else:
			break

	# the above process will be followed
	# in case of each type of move
	# below

	# to move down
	elif(x == 'S' or x == 's'):
		mat, flag = logic.move_down(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move left
	elif(x == 'A' or x == 'a'):
		mat, flag = logic.move_left(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move right
	elif(x == 'D' or x == 'd'):
		mat, flag = logic.move_right(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break
	else:
		print("Invalid Key Pressed")

	# print the matrix after each
	# move.
	window["-TABLE-"].update(values=mat)
	for list in mat:
		print(list)
window.close()
