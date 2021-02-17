 #aotudrew.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pensize(5)
t.pencolor("red")
 #数据读取
fd=open("data.txt")
datals=list()
for line in fd:
    line=line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
fd.close()
#图形绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

    
