import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from numba import njit, prange
from time import perf_counter


@njit
def chaos(n, r=1.0, pr_start=40):
    x = pr_start / 100
    for i in range(n):
        i = i
        x = r * x * (1 - x)
    return x * 100


fig, ax = plt.subplots()

plt.subplots_adjust(bottom=0.25)
plt.ylim(0, 100)
plt.title("Equation: Xn+1 = R*Xn(1-Xn)")

t_max = 100
t = np.arange(0, t_max, 1)
pr_start0 = 50
r0 = 3
delta_f = 0.01
s = np.array([chaos(xi, r0, pr_start0) for xi in t])

l, = plt.plot(t, s, '-', color='red')

k, = plt.plot(t, s, '.')

ax.margins(x=0)

ax_r = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_pr_start = plt.axes([0.25, 0.15, 0.65, 0.03])

s_r = Slider(ax_r, 'R', 0.05, 5.0, valinit=r0, valstep=delta_f)
s_pr_start = Slider(ax_pr_start, '% Start', 0, 100, valinit=pr_start0)


# decorator to check FPS (1 / execution time)
def check_fps(f):
    def timed(*args, **kw):
        start = perf_counter()
        result = f(*args, **kw)
        end = perf_counter()
        fps.set_text(f"FPS: {1 / (end - start):>10,.2f}")
        return result

    return timed


@check_fps
def update(val):
    pr_start = float(s_pr_start.val)
    r = s_r.val
    data = [chaos(xi, r, pr_start) for xi in t]
    l.set_ydata(np.array(data))
    k.set_ydata(np.array(data))

    fig.canvas.draw_idle()


s_r.on_changed(update)
s_pr_start.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

fps = ax.annotate('FPS:    0.00',
                  xy=(1, 0),
                  xycoords='axes fraction',
                  fontsize=10,
                  horizontalalignment='right',
                  verticalalignment='bottom')


def reset(event):
    s_r.reset()
    s_pr_start.reset()


button.on_clicked(reset)

plt.show()
