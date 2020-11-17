import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from mpl_toolkits.mplot3d.art3d import Line3DCollection
from mpl_toolkits.axes_grid1 import make_axes_locatable


def plot_data(filename, planar_trajectory, show_velocity=True, sampling_freq=20):
    xs = []
    ys = []
    zs = []
    i = 0
    with open('data/{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')
        # get positions from file
        for row in csv_reader:
            if i % sampling_freq == 0:
                # conversion in cm
                xs.append(float(row[0]) * 100)
                ys.append(float(row[2]) * 100)
                zs.append(-float(row[1]) * 100)
            i += 1

    if show_velocity:
        velocities = []
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
        points = np.array([xs, ys, zs]).T.reshape(-1, 1, 3)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc = Line3DCollection(segments, cmap=plt.get_cmap('YlOrRd'),
                              norm=plt.Normalize(min(velocities), max(velocities)))
        lc.set_array(np.asarray(velocities))
        lc.set_linewidth(2)

    # build the trajectory chart with velocity as color
    fig = plt.figure(figsize=(12.8, 12.8))
    fig.suptitle(filename)
    spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
    ax = fig.add_subplot(spec[0, 0], projection='3d')
    ax.set_xlim(min(xs), max(xs))
    ax.set_ylim(min(ys), max(ys))
    ax.set_zlim(min(min(xs), min(ys)), max(max(xs), max(ys)))
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.set_zlabel('z (cm)')
    ax.plot(xs, ys, zs)
    if show_velocity:
        ax.add_collection3d(lc, zs=zs, zdir='z')
        cbar = fig.colorbar(lc, ax=ax, orientation='horizontal', aspect=10)
        cbar.set_label('Velocity (cm/s)')
    ax.set_title('3D trajectory')
    ax2 = fig.add_subplot(spec[0, 1])
    ax2.plot(xs, ys)
    ax2.set_title('XY plane')
    ax3 = fig.add_subplot(spec[1, 0])
    ax3.plot(xs, zs)
    if planar_trajectory:
        ax3.set_ylim(min(xs), max(xs))
    ax3.set_title('XZ plane')
    ax4 = fig.add_subplot(spec[1, 1])
    ax4.plot(ys, zs)
    if planar_trajectory:
        ax4.set_ylim(min(xs), max(xs))
    ax4.set_title('YZ plane')
    plt.show()
    if show_velocity:
        fig.savefig('figures/{fn}_velocity.png'.format(fn=filename))
    else:
        fig.savefig('figures/{fn}.png'.format(fn=filename))


if __name__ == '__main__':
    plot_data('circle_28_secondi.csv', planar_trajectory=True, show_velocity=True, sampling_freq=20)
