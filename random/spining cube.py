import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#cube
x = [0,1,1,0,0,1,1,0]
y = [0,0,1,1,0,0,1,1]
z = [0,0,0,0,1,1,1,1]

#draw cube
ax.scatter(x, y, z)

#static points inside cube
points = [(0.25, 0.25, 0.25), (0.75, 0.75, 0.75), (0.25, 0.75, 0.75), 
          (0.75, 0.25, 0.75), (0.75, 0.75, 0.25), (0.25, 0.25, 0.75),
          (0.25, 0.75, 0.25), (0.75, 0.25, 0.25), (0.5, 0.5, 0.5)]
for point in points:
    ax.scatter(point[0], point[1], point[2], c='r')

#misc
ax.set_xticks([])
ax.set_yticks([])
plt.xticks([])
plt.yticks([])
ax.set_yticklabels([])

#spin cube

while True:
    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)

plt.show()
