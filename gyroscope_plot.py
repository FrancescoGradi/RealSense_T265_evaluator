import csv
import os

def quaternion_to_euler(x, y, z, w):
    import math
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
    i = 0
    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if i % sampling_freq == 0:
                x, y, z = quaternion_to_euler(float(row[9]), float(row[10]), float(row[11]), float(row[12]))

                x_angle_degree.append(x)
                y_angle_degree.append(y)
                z_angle_degree.append(z)

            i += 1

    x1 = sum(x_angle_degree) / len(x_angle_degree)
    y1 = sum(y_angle_degree) / len(y_angle_degree)
    z1 = sum(z_angle_degree) / len(z_angle_degree)

    print('degree x:', int(x1), 'y: ', int(y1), 'z: ', int(z1))


if __name__ == '__main__':
    files = []
    count = 0
    for filename in os.listdir(os.path.abspath(os.curdir)+'/data/static_rotations'):
        files.append(filename)
    files.sort()
    print(' ')
    for file in files:
        print(file)
        plot_data('data/static_rotations/'+file, sampling_freq=1)
        count += 1
        if count % 4 == 0:
            print(' ')
