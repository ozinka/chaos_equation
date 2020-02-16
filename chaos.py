import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

plt.style.use('fivethirtyeight')


def chaos(n, r=1.0):
    x = 0.4
    for i in range(n):
        x = r * x * (1 - x)
        print(f'n: {i}, x: {x}')
    return x


r0 = 1
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

ax.set(xlabel='n', ylabel='Value', title='Chaos function')
ax.grid()

axcolor = 'lightgoldenrodyellow'

axr = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)


sr = Slider(axr, 'Freq', 0.1, 10.0, valinit=r0, valstep=0.05)


def update(val):
    n = np.arange(1, 100, 1)
    s = np.array([chaos(xi, val) for xi in n])
    ax.clear()
    # plt.ylim(-2, 2)
    # plt.xlim(0, 100)
    ax.plot(n, s)
    fig.canvas.draw_idle()


sr.on_changed(update)
update(1)
plt.show()

# fig.savefig("test.png")