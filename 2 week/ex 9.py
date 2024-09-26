c=0
with open('text.txt', 'r') as file:
    while True:
        line=file.readline()
        line=file[0:len(line)-1]
        if line=='':
            break
        if line[-1]=='\n':
             line=line[0:len(line)-1]
        for i in range(len(line)):
            if line[i]=='.' or line[i]=='!' or line[i]=='?' or line[i]=='...':
                c+=1
 print(c)               