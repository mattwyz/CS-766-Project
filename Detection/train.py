from ultralytics import YOLO

# Initialize the YOLO model
model = YOLO('yolov8l.pt')

# Tune hyperparameters on COCO8 for 30 epochs

space = {
    'epochs' : [100, 200, 300],
    'batch': [64, 256, 1024],

}
##change the directory of data
model.tune(data='/home/hp/bdd_in_YOLOV5/dataset.yaml', space = space, plots=False, save=False, val=False, device = [0, 1])