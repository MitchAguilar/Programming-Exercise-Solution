a=""
line=""
b=(int)(input())
for c in range(b):
	line=input()
	if(len(line)==5):
		print("3")
		continue
	if (line[0] == 'o' and line[1] == 'n') or (line[1] == 'n' and line[2] == 'e') or  (line[2] == 'e' and line[0] == 'o'):
                print("1")
	else:
       	        print("2")
