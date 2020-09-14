def str_input_to_mine_coords(input_string):
	mine_coord=[]
	x_len,y_len=0,0

	temp=input_string.split("\n")
	x_len,y_len=len(temp[0]),len(temp) 

	x_mine,y_mine=0,0

	for i in temp:
		x_mine=0
		for s in i:
			if(s=='x'):
				mine_coord.append((x_mine,y_mine))
			x_mine+=1
		y_mine+=1		

	return (x_len, y_len, mine_coord)	



	