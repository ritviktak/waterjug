#!/usr/bin/env python
# coding: utf-8

# In[1]:


jugs = [0,0]
queue = []


# In[3]:


over = []
counter = 1
queue.append(jugs)
J1 = int(input("J1: "))
J2 = int(input("J2: "))
remaining = int(input("Final in J1: " ))

def Solve(queue, counter):
    jugs = queue.pop(0)
    over.append(jugs)

    counter += 1
    if (jugs[0] == remaining and jugs[1] == 0):
        print ("Solution found!")
        print ("Approx count: ", counter)
        return
    ApplyRule(jugs, queue)
    Solve(queue, counter)
       
def Append(queue, temporary):
    if not (temporary in queue) and not (temporary in over):
        queue.append(temporary)
    
    
def ApplyRule(jugs, queue):

    x = jugs[0]
    y = jugs[1]

    if x < J1:
        print ("1")
        Append(queue, [J1,y])

    if y < J2:
        print ("2")
        Append(queue, [x,J2])

    if x > 0:
        print( "3")
        Append(queue, [0,y])

    if y > 0:
        print ("4")
        Append(queue, [x,0])

    if x + y >= J1 and y > 0:
        print ("5")
        Append(queue, [J1,y-J1+x])


    if x + y <= J1 and y > 0:
        print ("6")
        Append(queue, [x+y,0])


    if x == 0 and y == remaining:
        print ("7")
        Append(queue, [remaining,0])

Solve(queue,0)


# In[ ]:





# In[ ]:




