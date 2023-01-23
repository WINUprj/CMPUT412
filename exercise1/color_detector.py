import cv2
import numpy as np
from time import sleep

def gst_pipeline_string():
    # Parameters from the camera_node
    # Refer here : https://github.com/duckietown/dt-duckiebot-interface/blob/daffy/packages/camera_driver/config/jetson_nano_camera_node/duckiebot.yaml
    res_w, res_h, fps = 640, 480, 30
    fov = 'full'
    # find best mode
    camera_mode = 3  # 
    # compile gst pipeline
    gst_pipeline = f""" \
            nvarguscamerasrc censor-mode={camera_mode} exposuretimerange="100000 80000000" ! \
            video/x-raw(memory:NVMM), width={res_w}, height={res_h}, format=NV12, framerate={fps}/1 ! \
            nvjpegenc ! \
            appsink \
        """ 

    # ---
    # print(gst_pipeline)
    return gst_pipeline


cap = cv2.VideoCapture()
cap.open(gst_pipeline_string(), cv2.CAP_GSTREAMER)

# check if cap is opened
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Output the size of frame
    if not ret:
        print("Cannot receive the frames. Terminating...")
        break
    
    # Get the size of image
    print(f"Received a camera view of size {frame.shape[1]}x{frame.shape[0]}")
    
    # Print mean RGB value (i.e. compute average luminosity per channel)
    lum = frame.mean(axis=(0, 1))
    print(f"Luminosity per channel: R {lum[2]}, G {lum[1]}, B {lum[0]}")

    cv2.imshow("frame", frame)

    sleep(1)

cap.release()
