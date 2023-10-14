import matplotlib.pyplot as plt
from random import choice

def rand_walk(step_num):
    walk = []
    step_choice = choice([1,-1])
    walk.append(step_choice)
    for step in range(1,step_num):
        next_step = walk[step-1]+ choice([1,-1])
        walk.append(next_step)
    return walk

def rand_show(walk):
    plt.title("Random walk Output")
    plt.xlabel(" Step Number")
    plt.ylabel(" Distance from Origin")
    plt.plot(walk)
    plt.show()

def plot_walks(num,walk_steps):
    lab_list = list(range(1, num+1))
    for i in range(0,num):
        x = range(1, walk_steps+1)

        plt.plot(x, rand_walk(walk_steps), label= "Walk" + ' '+ str(lab_list[i]))
        plt.xlabel("Number of steps")
        plt.ylabel(" Distance from Origin ")
        plt.title("Random walks")
        plt.legend(loc="lower left")
    plt.show()

plot_walks(5,100)


