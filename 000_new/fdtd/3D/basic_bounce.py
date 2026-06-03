import numpy as np
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation

y = 100
x = 0
cor = 0.7
vx = 0.01
vy = 0.0
tmax = 100
g = .5

xx = []
yy = []

# plt.xkcd()

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = fig.add_subplot(111, xlim=(0, 1.25), ylim=(-10, 100))
point, = ax.plot([], [], lw=5)


# initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    return point,


# animation function.  This is called sequentially
def animate(i):
    global xx, yy, y, x, cor, vx, vy, tmax, g
    if (y > 0):
        vy -= g
    else:
        vy = -vy * cor
    y += vy
    x += vx
    if (y < 0):
        y = 0
    xx.append(x)
    yy.append(y)
    print
    "(", x, ", ", y, ")"
    point.set_data(xx, yy)
    return point,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=125, interval=20, blit=True)

# this is how you save your animation to file:
# anim.save('animation.gif', writer='imagemagick_file', fps=30)
anim.save('animation.gif', writer='imagemagick', fps=30)

plt.show()