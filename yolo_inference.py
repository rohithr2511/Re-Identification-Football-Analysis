#Import All the Required Libraries
from ultralytics import YOLO

#Load the YOLO Model
model = YOLO("C:\\Users\\Rahul\\OneDrive\\Desktop\\footballprjct\\models\\best.pt")

#Object Detection
results = model.predict(source = "C:\\Users\\Rahul\\OneDrive\\Desktop\\footballprjct\\input_video\\15sec_input_720p.mp4", save=True)

#Tracking
#results = model.track(source = "input_videos/video.mp4", save=True, persist=True)