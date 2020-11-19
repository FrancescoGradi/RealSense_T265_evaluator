import pyrealsense2 as rs
import numpy as np
import time


def saveTrajectory(filename='trajectory'):
    pipe = rs.pipeline()

    cfg = rs.config()
    cfg.enable_stream(rs.stream.pose)

    pipe.start(cfg)

    trajectory = []
    start = time.time()

    try:
        while True:
            frames = pipe.wait_for_frames()

            pose = frames.get_pose_frame()
            if pose:
                data = pose.get_pose_data()
                trajectory.append([data.translation.x, data.translation.y, data.translation.z,
                                   data.velocity.x, data.velocity.y, data.velocity.z,
                                   data.acceleration.x, data.acceleration.y, data.acceleration.z])

    finally:
        print("Saving...")
        print("Total frames: #{}".format(pose.frame_number))
        end = time.time()
        elapsed_time = end - start
        print("Time elapsed: " + elapsed_time)

        np.savetxt("data/{}_{}.csv".format(filename, str(time.strftime("%H_%M_%S", time.gmtime(elapsed_time)))),
                   np.asarray(trajectory), delimiter=",")
        pipe.stop()