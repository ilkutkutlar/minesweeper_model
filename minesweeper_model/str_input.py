field=[]
mine_coord=[]
x_len,y_len=0,0
x_mine=0
column=''

while(True):
	colum=str(input())
	
	if(colum=="done"):
		break
	else:
		field.append(colum)
		for i in colum:
			if(i=='x'):
				mine_coord.append((x_mine,y_len))
			x_mine+=1	
		y_len+=1
		x_mine=0



x_len=len(colum)

print(field,x_len,y_len)	
print(mine_coord)	
			

