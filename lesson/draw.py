import numpy as np
import warnings

# 心形线：x^2 = 1 - (y - x^(2/3))^2;
def draw_love():
    #warnings.filterwarnings('ignore')
    for y in np.arange(1.6,-1,-0.15):
        for x in np.arange(-1, 1, 0.025):
            if 1 - pow(y - pow(pow(x, 2), 1 / 3.0), 2) >x * x:
                #print('\033[0;31;40m',end='')
                print('\033[5;31;2m*',end='')
            else:
                print(' ',end='')
        print()


draw_love()
