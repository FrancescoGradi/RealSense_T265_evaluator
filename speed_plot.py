import csv
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from numpy import linalg
import math


def plot_data(filename, sampling_freq=20):
    x_pos = []
    y_pos = []
    z_pos = []

    x_speed = []
    y_speed = []
    z_speed = []

    x_acc = []
    y_acc = []
    z_acc = []

    final_speed = []
    final_pos = []
    final_acc = []
    frame = []
    i = 0

    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:

            if i % sampling_freq == 0:
                x_pos.append(float(row[0]))
                y_pos.append(float(row[2]))
                z_pos.append(float(row[1]))

                x_speed.append(linalg.norm(float(row[3])) * 3.6)
                y_speed.append(linalg.norm(float(row[4])) * 3.6)
                z_speed.append(linalg.norm(float(row[5])) * 3.6)

                final_pos.append(math.sqrt(
                    pow(linalg.norm(float(row[0])), 2) + pow(linalg.norm(float(row[1])), 2) + pow(
                        linalg.norm(float(row[2])), 2)))

                final_speed.append(math.sqrt(
                    pow(linalg.norm(float(row[3])), 2) + pow(linalg.norm(float(row[4])), 2) + pow(
                        linalg.norm(float(row[5])), 2)) * 3.6)

                frame.append(i)
            i += 1

    last_speed = 0.0
    for i in range(len(x_speed)):
        """final_acc.append((x_speed[i] / final_speed[i]) * x_acc[i] +
                         (y_speed[i] / final_speed[i]) * y_acc[i] +
                         (z_speed[i] / final_speed[i]) * z_acc[i])"""
        final_acc.append(final_speed[i] - last_speed)
        last_speed = final_speed[i]

    final_acc.pop(0)
    final_acc.insert(0, 0.0)
    final_pos_avg = sum(final_pos) / len(final_pos)
    final_speed_avg = sum(final_speed) / len(final_speed)
    final_acc_avg = sum(final_acc) / len(final_acc)

    print('Avg pos:', final_pos_avg, 'Avg speed: ', final_speed_avg, 'Avg acc: ', final_acc_avg)

    fig = plt.figure(figsize=(10, 7))
    fig.suptitle(filename)
    spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

    ax = fig.add_subplot(spec[0, 0])
    ax.plot(frame, final_pos)
    ax.set_title(' ')
    ax.set_ylabel('position (m)')
    ax.set_xlabel('frame')

    ax2 = fig.add_subplot(spec[0, 1])
    ax2.plot(frame, final_speed)
    ax2.set_title(' ')
    ax2.set_ylabel('speed (km/h)')
    ax2.set_xlabel('frame')

    ax3 = fig.add_subplot(spec[1, 1])
    ax3.plot(frame, final_acc)
    ax3.set_title(' ')
    ax3.set_ylabel('acc (m/s^2)')
    #ax3.set_ylim(-1, 1)
    ax3.set_xlabel('frame')

    plt.show()


if __name__ == '__main__':
    directory = 'data/very_long_bike'
    files = []
    count = 0

    for filename in os.listdir(os.path.abspath(os.curdir) + '/' + directory):
        files.append(filename)
    files.sort()

    print(' ', files)

    for file in files:
        print(file)
        plot_data(directory + '/' + file, sampling_freq=20)
        count += 1
        if count % 4 == 0:
            print(' ')