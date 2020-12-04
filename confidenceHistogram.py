import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def drawConfidenceHistogram(filename):

    tracker_confidences = [0, 0, 0, 0]
    frame_best_confidences = [0, 0, 0]
    best_confidence = 0
    found = [False, False, False]
    frame = 1
    frames = []
    confs = []

    with open('{fn}'.format(fn=filename)) as f:
        csv_reader = csv.reader(f, delimiter=',')

        for row in csv_reader:
            confidence = int(float(row[19]))
            if confidence == 3:
                tracker_confidences[3] += 1
                confs.append(3)
                if found[2] is False:
                    if best_confidence < confidence:
                        frame_best_confidences[2] = frame
                        found[2] = True
            elif confidence == 2:
                tracker_confidences[2] += 1
                confs.append(2)
                if found[1] is False:
                    if best_confidence < confidence:
                        frame_best_confidences[1] = frame
                        found[1] = True
            elif confidence == 1:
                tracker_confidences[1] += 1
                confs.append(1)
                if found[0] is False:
                    if best_confidence < confidence:
                        frame_best_confidences[0] = frame
                        found[0] = True
            else:
                tracker_confidences[0] += 1
                confs.append(0)
            frames.append(frame)
            frame += 1


    total_rows = sum(x for x in tracker_confidences)
    tracker_confidences = [x / total_rows for x in tracker_confidences]

    time = []
    for k in range(len(frame_best_confidences)):
        time.append(frame_best_confidences[k]/200)
    print(filename,' best confidence time: ', time, ' (frame', frame_best_confidences, ')')


    data = {'Failed': 0, 'Low': 1, 'Medium': 2, 'High': 3}
    names = list(data.keys())

    fig = plt.figure(figsize=(10, 5))
    fig.suptitle(filename)
    spec = gridspec.GridSpec(ncols=2, nrows=1, figure=fig)
    ax = fig.add_subplot(spec[0, 0])
    ax.bar(names, tracker_confidences)
    #ax.set_title('frames tracking confidence')
    ax.set_title(' ')
    ax2 = fig.add_subplot(spec[0, 1])
    ax2.plot(frames, confs)
    ax2.set_title(' ')
    #ax2.set_title('confidence/frame')
    ax2.set_ylabel('confidence')
    ax2.set_xlabel('frame')


    plt.show()



if __name__ == '__main__':

    directory = 'data/full_outdoor'

    for filename in os.listdir(directory):
        drawConfidenceHistogram(directory + '/' + filename)
