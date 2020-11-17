import pyrealsense2 as rs
import numpy as np

pipe = rs.pipeline()

cfg = rs.config()
cfg.enable_stream(rs.stream.pose)

pipe.start(cfg)

trajectory = []
filename = "trajectory"

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

    np.savetxt("../data/{}.csv".format(filename), np.asarray(trajectory), delimiter=",")
    pipe.stop()