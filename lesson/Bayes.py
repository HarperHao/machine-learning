import matplotlib.pyplot as plt
import numpy as np

def bayes(x):
    return 1-(1/(np.power(2.0,-x)+1))
def draw():
    x=np.arange(1,20,1)
    y=bayes(x)
    plt.plot(x,y)
    plt.show()

draw()
