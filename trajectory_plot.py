import csv
import math
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from mpl_toolkits.mplot3d.art3d import Line3DCollection
from mpl_toolkits.axes_grid1 import make_axes_locatable


def plot_data(filename, planar_trajectory=True, show_velocity=True, sampling_freq=20, true_trajectory=None, scale='cm'):
    xs = []
    ys = []
    zs = []
    vxs = []
    vys = []
    vzs = []
    i = 0
    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')
        # get positions from file
        for row in csv_reader:
            if i % sampling_freq == 0:
                if scale == 'cm':
                    # conversion in cm
                    xs.append(-float(row[0]) * 100)
                    ys.append(float(row[2]) * 100)
                    zs.append(float(row[1]) * 100)
                else:
                    xs.append(-float(row[0]))
                    ys.append(float(row[2]))
                    zs.append(float(row[1]))
                vxs.append(float(row[3]))
                vys.append(float(row[5]))
                vzs.append(float(row[4]))
            i += 1

    if show_velocity:
        velocities = []
        for pos in zip(vxs, vys, vzs):
            # compute velocity for each point
            velocities.append(math.sqrt(pow(pos[0], 2) + pow(pos[1], 2) + pow(pos[2], 2)))

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
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.set_zlabel('z (cm)')
    absolute_min = min(xs + ys + zs)
    absolute_max = max(xs + ys + zs)
    ax.plot(xs, ys, zs)
    ax.auto_scale_xyz([absolute_min, absolute_max], [absolute_min, absolute_max], [absolute_min, absolute_max])
    if show_velocity:
        ax.add_collection3d(lc, zs=zs, zdir='z')
        cbar = fig.colorbar(lc, ax=ax, orientation='horizontal', aspect=10)
        cbar.set_label('Velocity (m/s)')
    ax.set_title('3D trajectory')
    ax2 = fig.add_subplot(spec[0, 1])
    ax2.plot(xs, ys)
    ax2.axis('scaled')
    ax2.set_title('XY plane')
    ax3 = fig.add_subplot(spec[1, 0])
    ax3.plot(xs, zs)
    ax3.axis('scaled')
    if planar_trajectory:
        ax3.set_ylim(min(xs), max(xs))
    ax3.set_title('XZ plane')
    ax4 = fig.add_subplot(spec[1, 1])
    ax4.plot(ys, zs)
    ax4.axis('scaled')
    if planar_trajectory:
        ax4.set_ylim(min(xs), max(xs))
    ax4.set_title('YZ plane')

    if true_trajectory is not None:
        ax.plot([x[0] for x in true_trajectory], [y[1] for y in true_trajectory], [z[2] for z in true_trajectory])
        ax2.plot([x[0] for x in true_trajectory], [y[1] for y in true_trajectory], color='r')
        ax3.plot([x[0] for x in true_trajectory], [z[2] for z in true_trajectory], color='r')
        ax4.plot([y[1] for y in true_trajectory], [z[2] for z in true_trajectory], color='r')

    plt.show()

    '''if show_velocity:
        fig.savefig('figures/{fn}_velocity.png'.format(fn=filename))
    else:
        fig.savefig('figures/{fn}.png'.format(fn=filename))'''


if __name__ == '__main__':
    directory = 'data/very_long/'

    for filename in os.listdir(directory):
        plot_data(directory + filename, planar_trajectory=True, show_velocity=True, sampling_freq=10, scale='m')

