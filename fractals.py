import math
from tkinter import *
root = Tk()
canvas = Canvas()
 
root.geometry("500x500")


canvas.create_line(100, 0, 100, 100, width=1)



parent_queue = [[100,100]]
child_node = []
iterations = 0


while(iterations < 4):
    node_count = 0
    for i in range(len(parent_queue)):
        
    
        
        child_node.append([parent_queue[i][0] + parent_queue[i][0] * 0.25 * math.cos(math.pi/3) , (parent_queue[i][1] + parent_queue[i][1]* 0.25 * math.sin(math.pi/3))])
        child_node.append([parent_queue[i][0] - parent_queue[i][0] * 0.25 * math.cos(math.pi/3) , (parent_queue[i][1] + parent_queue[i][1]* 0.25 * math.sin(math.pi/3))])
        canvas.create_line(parent_queue[i][0], parent_queue[i][1], child_node[node_count][0], child_node[node_count][1])
        canvas.create_line(parent_queue[i][0], parent_queue[i][1], child_node[node_count+1][0], child_node[node_count+1][1])
        node_count = node_count + 2

    parent_queue = child_node
    child_node = []
    iterations +=1
canvas.pack()
root.mainloop()








