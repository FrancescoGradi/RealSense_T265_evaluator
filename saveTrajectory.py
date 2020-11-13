import pyrealsense2 as rs
import numpy as np

pipe = rs.pipeline()

cfg = rs.config()
cfg.enable_stream(rs.stream.pose)

pipe.start(cfg)

trajectory = []

try:
    for _ in range(500):
        frames = pipe.wait_for_frames()

        pose = frames.get_pose_frame()
        if pose:
            data = pose.get_pose_data()
            print(data)
            trajectory.append(data)
            print("Frame #{}".format(pose.frame_number))
            print("Position: {}".format(data.translation))
            print("Velocity: {}".format(data.velocity))
            print("Acceleration: {}\n".format(data.acceleration))

finally:

    np.savetxt("trajectory.csv", np.asarray([trajectory]), delimiter=",")
    pipe.stop()