# Object Detection Python Script

## Description 
### Object_detection_image.py
This python script supports image detection.

### Object_detection_webcam.py
This python script supports the real-time detection from a web camera.

## Detection
Please following the steps:

1. Make sure you have successful installed the required package (TensorFlow, Object Detection API)
2. Please copy all the directory and files in this folder to models/research/object_detection
3. Make sure you have successful export the model and save it in the inference_graph directory
4. If you use image detection, please turn to 5; if you use a real-time detection, please turn to 6

5. Please add the image path at line 34. Such as IMAGE_NAME = ['demo1.jpg']  
   The example means demo1.jpg in the current folder, you can enter the absolute path of a image  
   Then please set the class label at line 43, and change the number of classes you want to detect at line 50  
   Finally, you can run the program through IDLE

6. Please set the class label at line 45m, then edit the class number at line 48  
   Finally, you can run the program through IDLE, the program will use the web camera to deteation cloud.

