# Render base image for dts (with suitable version)
FROM duckietown/dt-duckiebot-interface:daffy-arm32v7 

# Set working directory
WORKDIR /color_detector_dir

COPY color_detector.py .

# CMD python3 ./color_detector.py
CMD gst-launch-1.0 nvarguscamerasrc ! "video/x-raw(memory:NVMM)" ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! omxh265enc ! matroskamux ! filesink location=testX.mkv
