import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

plt.style.use('fivethirtyeight')
# plt.subplots_adjust(left=0.25, bottom=0.25)


def chaos(n, r=1.0):
    x = 0.1
    for i in range(n):
        x = r * x * (1 - x)
    return x


r0 = 1
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

ax.set(xlabel='n', ylabel='Value', title='Chaos function')
ax.grid()

axcolor = 'lightgoldenrodyellow'

axr = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sr = Slider(axr, 'Freq', 0.1, 10.0, valinit=r0, valstep=0.05)


def update(val):
    n = np.arange(1, 100, 1)
    s = np.array([chaos(xi, val) for xi in n])
    # ax.clear()
    ax.set_title('Chaos function: r = ' + str(1 + sr.val / 50))
    plt.axis([0, 100, 0, 1.1])
    ax.plot(n, s)

# fig.savefig("test.png")
plt.show()
