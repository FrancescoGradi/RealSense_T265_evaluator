import csv
import numpy as np
import matplotlib.pyplot as plt


def drawConfidenceHistogram(filename):

    tracker_confidences = [0, 0, 0, 0]

    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')

        for row in csv_reader:
            confidence = int(float(row[19]))
            if confidence == 3:
                tracker_confidences[3] += 1
            elif confidence == 2:
                tracker_confidences[2] += 1
            elif confidence == 1:
                tracker_confidences[1] += 1
            else:
                tracker_confidences[0] += 1

    total_rows = sum(x for x in tracker_confidences)
    tracker_confidences = [x / total_rows for x in tracker_confidences]

    x = np.arange(4)
    plt.bar(x, tracker_confidences)
    plt.xticks(x, ['Failed', 'Low', 'Medium', 'High'])

    plt.title(filename + ' frames tracking confidence')

    plt.show()


if __name__ == '__main__':
    filename = 'data/full_indoor/square_00_00_26.csv'
    drawConfidenceHistogram(filename)

    filename = 'data/full_outdoor/square_00_00_20.csv'
    drawConfidenceHistogram(filename)