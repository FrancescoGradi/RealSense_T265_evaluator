import numpy as np
import math
import csv


def distance(points, true_points):
    if(len(points) != len(true_points)):
        raise ValueError("Arrays with different dimension")

    return np.linalg.norm(np.asarray(points) - np.asarray(true_points))


# Crea una lista che rappresenta una linea 3D sull'asse y negativa fino al valore max dimension (in cm)
def getLine(total_points=500, max_dimension=100):
    line = []
    increment_value = max_dimension / total_points
    for i in range(total_points):
        line.append([0, - (i * increment_value), 0])

    return line


if __name__ == '__main__':

    filename = 'data/line_00_00_14.csv'

    # Punti da valutare totali (approssimati, il valore reale sarà superiore in base al campionamento)
    total_points = 500

    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')
        total_rows = sum(1 for row in csv_reader)
        sampling_frequency = int(total_rows / total_points)

    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')
        points = []
        i = 0
        for row in csv_reader:
            if (i % sampling_frequency) == 0:
                points.append([float(row[0]) * 100, float(row[2]) * 100, float(row[1]) * 100])
            i += 1

    true_points = getLine(len(points), 100)

    print(distance(points, true_points))
