import csv
import os
import math
import matplotlib.pyplot as plt


def quaternion_to_euler(x, y, z, w):

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    X = math.degrees(math.atan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    Y = math.degrees(math.asin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    Z = math.degrees(math.atan2(t3, t4))

    return X, Y, Z


def plot_data(filename, sampling_freq=20):
    x_angle_degree = []
    y_angle_degree = []
    z_angle_degree = []
    frame = []
    i = 0

    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if i % sampling_freq == 0:
                y, z, x = quaternion_to_euler(float(row[9]), float(row[10]), float(row[11]), float(row[12]))
                frame.append(i)
                x_angle_degree.append(int(x))
                y_angle_degree.append(int(y))
                z_angle_degree.append(int(z))
            i += 1

    x_avg = sum(x_angle_degree) / len(x_angle_degree)
    y_avg = sum(y_angle_degree) / len(y_angle_degree)
    z_avg = sum(z_angle_degree) / len(z_angle_degree)

    print('Avg degree x:', int(x_avg), 'y: ', int(y_avg), 'z: ', int(z_avg))

    plt.plot(frame, x_angle_degree, 'r', label='x')
    plt.plot(frame, y_angle_degree, 'g', label='y')
    plt.plot(frame, z_angle_degree, 'b', label='z')
    plt.legend()
    plt.title(filename)
    plt.ylabel('degrees')
    plt.xlabel('frame')
    plt.show()


if __name__ == '__main__':
    files = []
    count = 0
    for filename in os.listdir(os.path.abspath(os.curdir)+'/data/z_rotations'):
        files.append(filename)
    files.sort()
    print(' ')
    for file in files:
        print(file)
        plot_data('data/z_rotations/'+file, sampling_freq=1)
        count += 1
        if count % 4 == 0:
            print(' ')
