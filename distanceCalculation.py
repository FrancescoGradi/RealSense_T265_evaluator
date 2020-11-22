import numpy as np
import math
import csv

from trajectory_plot import plot_data


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

# per ora questo e' sbagliato
def getSquare(total_points=2000, max_dimension=100):
    square = []
    increment_value = max_dimension / total_points
    for i in range(int(total_points / 4)):
        square.append([0, - (i * increment_value), 0])
    for i in range(int(total_points / 4)):
        square.append([- (i * increment_value), - max_dimension, 0])
    for i in range(int(total_points / 4)):
        square.append([- max_dimension, - max_dimension + (i * increment_value), 0])
    for i in range(int(total_points / 4)):
        square.append([- max_dimension + (i * increment_value), 0, 0])

    return square


def distanceCalculation(filename, total_points=500, type_test="line"):

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

    print("Sampling Frequency: " + str(sampling_frequency))
    print("Effective total points: " + str(len(points)))

    if (type_test == "line"):
        true_points = getLine(len(points), 100)
    elif (type_test == "square"):
        true_points = getSquare(len(points), 100)
    else:
        raise ValueError("Please, insert a valid test type")

    return distance(points, true_points)


if __name__ == '__main__':

    filename = "data/indoor_2d/line_00_00_14.csv"
    print("Total indoor test distance error: " + str(distanceCalculation(filename=filename, type_test="line")))
    plot_data(filename=filename, true_trajectory=getLine())
    print("")

    filename = "data/outdoor_2d/line_00_00_11.csv"
    print("Total outdoor test distance error: " + str(distanceCalculation(filename=filename, type_test="line")))
    plot_data(filename=filename, true_trajectory=getLine())

