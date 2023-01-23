# CMPUT412
Course project repository.

## Update Log
#### 22/Jan/2023:
- Added all the Exercise 1 codes under directory `exercise1`.
- File/directory descriptions in `exercise1`:
	- `dt-sample-program/`: Sample Python environment for completing section B2, created from Duckietown template. Submodule of this repo (i.e. link to another repo).
	- `Dockerfile`: Dockerfile for building a container to do the task on Duckiebot.
	- `color_detector.py`: Python file to run in container. Communicate with camera on a Duckiebot and process the given image (mainly averaging colors).
	- `requirements.txt`: Usually used for building a custom Python environment in container. In this lab, we did not use it as all the requirements were included in a base image.
- *Note: For `dt-sample-program`, please refer to v2 branch for updated codes.*
