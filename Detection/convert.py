##This code is for converted the BDD100k format to YOLO format 
##Before converting, download the dataset at https://dl.cv.ethz.ch/bdd100k/data/
import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.types as types

classes = ['traffic light'
  , 'traffic sign'
  , 'car'
  , 'pedestrian'
  , 'bus'
  , 'truck'
  , 'rider'
  , 'bicycle'
  , 'motorcycle'
  ,'train'
  ,'other vehicle'
  ,'other person'
  ,'trailer']

# The path to the source files that you manually downloaded
source_dir = "bdd100k/"

dataset = foz.load_zoo_dataset(
    "bdd100k",
    split='validation',
    source_dir=source_dir,
    copy_files = True
)

# The Dataset or DatasetView containing the samples you wish to export
dataset_or_view = dataset

# The directory to which to write the exported dataset
export_dir = "bdd_in_YOLOV5_val/"


# The type of dataset to export
# Any subclass of `fiftyone.types.Dataset` is supported

#Uncomment what ever format you wish to conver to

#YOLOV5
dataset_type = types.YOLOv5Dataset()  # for example


# Export the dataset
dataset_or_view.export(
    export_dir=export_dir,
    dataset_type=dataset_type,
    classes = classes
    #export_media="copy",
    #label_field=label_field,
)
