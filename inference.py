from ultralytics import YOLO


model = YOLO("/Users/aftaabhussain/Work/yolo segmentation/runs/segment/train2/weights/last.pt")  # load a custom model

# Predict with the model
results = model("/Users/aftaabhussain/Work/yolo segmentation/B4/Side/images/1_b4-3_s_87_M.jpg")  # predict on an image
print(results)
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk