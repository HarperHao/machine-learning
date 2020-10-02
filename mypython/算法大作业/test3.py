import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import RadioButtons
mpl.use("Qt5Agg")

x = np.linspace(0.0, 2.0, 1000)
y1 = 1.5 * np.cos(2 * np.pi * x)
y2 = 1.0 * np.cos(2 * np.pi * x)
y3 = 0.8 * np.cos(2 * np.pi * x)

fig, ax = plt.subplots(1, 1)
line, = ax.plot(x, y1, color="red", lw=2)
plt.subplots_adjust(left=0.35)

facecolor = "cornflowerblue"

ax1 = plt.axes([0.1, 0.7, 0.15, 0.15], facecolor=facecolor)
radio1 = RadioButtons(ax1, ("1.5A", "1.0A", "0.8A"))


def amplitudefunc(label):
    hzdict = {"1.5A": y1, "1.0A": y2, "0.8A": y3}
    ydata = hzdict[label]
    line.set_ydata(ydata)
    plt.draw()


radio1.on_clicked(amplitudefunc)

ax2 = plt.axes([0.1, 0.4, 0.15, 0.15], facecolor=facecolor)
radio2 = RadioButtons(ax2, ("red", "green", "orange"))


def colorfunc(label):
    line.set_color(label)
    plt.draw()


radio2.on_clicked(colorfunc)

ax3 = plt.axes([0.1, 0.1, 0.15, 0.15], facecolor=facecolor)
radio3 = RadioButtons(ax3, ("-", "--", "-.", ":"))


def linestylefunc(label):
    line.set_linestyle(label)
    plt.draw()


radio3.on_clicked(linestylefunc)

plt.show()