input_file = open('A-small-practice.in')
output_file = open('output.txt', 'w')
lines = input_file.readlines()
test_cases = lines[0][:-1]
rows_positions = range(1, len(lines), 5)
row = 1
first_selected_row = 0
last_selected_row = 0
case = 1
row = 1
second_choose = False
header_color = '\033[94m'
end_color = '\033[0m'
for i in range(1,len(lines)):
	if i in rows_positions[::2]:
		first_selected_row = int(lines[i][:-1])
		row = 1
		second_choose = False
		print '_'*80
		print header_color, '\t\t\tCASE', case, end_color
		print header_color,'FIRST SELECTED ROW =',end_color, first_selected_row, header_color,'/ LINE =',end_color, i+1

	if i in rows_positions[1::2]:
		last_selected_row = int(lines[i][:-1])
		row = 1
		second_choose = True
		print header_color,'LAST SELECTED ROW =',end_color, last_selected_row, header_color,'/ LINE =',end_color, i+1

	if i not in rows_positions:
		if not second_choose and first_selected_row == row:
			first_selected_row_values = [int(x) for x in lines[i][:-1].split(' ')]
			print header_color,'FIRST SELECTED ROW VALUES =',end_color, first_selected_row_values, header_color,'/ LINE =',end_color, i+1
		elif second_choose and last_selected_row == row:
			last_selected_row_values = [int(x) for x in lines[i][:-1].split(' ')]
			print header_color,'LAST SELECTED ROW VALUES =',end_color, last_selected_row_values, header_color,'/ LINE =',end_color, i+1
		if second_choose and row == 4:
			repeated_times = 0
			value = ''
			for j in range(4):
				for k in range(4):
					if first_selected_row_values[j] == last_selected_row_values[k]:
						repeated_times += 1
						value = str(first_selected_row_values[j])
			result_string = value
			if repeated_times == 0:
				result_string = 'Volunteer cheated!'
			if repeated_times > 1:
				result_string = 'Bad magician!'
			open('output.txt', 'a+b').write('Case #%i: %s\n' %(case, result_string))
			case += 1
		row += 1
