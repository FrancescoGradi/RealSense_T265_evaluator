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
                                   data.acceleration.x, data.acceleration.y, data.acceleration.z,
                                   data.rotation.x, data.rotation.y, data.rotation.z, data.rotation.w,
                                   data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z,
                                   data.angular_acceleration.x, data.angular_acceleration.y, data.angular_acceleration.z,
                                   data.tracker_confidence, data.mapper_confidence])

    finally:
        print("Saving...")
        print("Total frames: #{}".format(pose.frame_number))
        end = time.time()
        elapsed_time = end - start
        print("Time elapsed: " + str(elapsed_time))

        np.savetxt("../data/{}_{}.csv".format(filename, str(time.strftime("%H_%M_%S", time.gmtime(elapsed_time)))),
                   np.asarray(trajectory), delimiter=",")
        pipe.stop()