import csv
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors, cm, colorbar

filename = 'circle_28_secondi.csv'
planar_trajectory = True
xs = []
ys = []
zs = []
posX = []
posY = []
posZ = []
velocities = []
with open('data/{fn}'.format(fn=filename)) as f:
    csv_reader = csv.reader(f, delimiter=',')
    # get positions from file
    for row in csv_reader:
            xs.append(float(row[0]))
            ys.append(float(row[2]))
            zs.append(-float(row[1]))

old_pos = (0., 0., 0.)
for pos in zip(xs, ys, zs):
    # compute velocity for each point
    vx = pos[0] - old_pos[0]
    vy = pos[1] - old_pos[1]
    vz = pos[2] - old_pos[2]
    v = (vx, vy, vz)
    velocities.append(math.sqrt(pow(v[0], 2) + pow(v[1], 2) + pow(v[2], 2)))
    old_pos = pos

# chart preprocessing for color coherence
max_v = max(velocities)
min_v = min(velocities)
for i in range(len(velocities)):
    velocities[i] = (velocities[i] - min_v) / (max_v - min_v)


# build the trajectory chart with velocity as color
fig = plt.figure(constrained_layout=True, figsize=(12.8, 12.8))
fig.suptitle(filename)
spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
ax = fig.add_subplot(spec2[0, 0], projection='3d')
ax.set_xlim(min(xs), max(xs))
ax.set_ylim(min(ys), max(ys))
ax.set_zlim(min(min(xs), min(ys)), max(max(xs), max(ys)))
ax.plot(xs, ys, zs)
ax.set_title('3D trajectory')
ax2 = fig.add_subplot(spec2[0, 1])
ax2.plot(xs, ys)
ax2.set_title('XY plane')
ax3 = fig.add_subplot(spec2[1, 0])
ax3.plot(xs, zs)
if planar_trajectory:
    ax3.set_ylim(min(xs), max(xs))
ax3.set_title('XZ plane')
ax4 = fig.add_subplot(spec2[1, 1])
ax4.plot(ys, zs)
if planar_trajectory:
    ax4.set_ylim(min(xs), max(xs))
ax4.set_title('YZ plane')
plt.show()
fig.savefig('figures/{fn}.png'.format(fn=filename))
