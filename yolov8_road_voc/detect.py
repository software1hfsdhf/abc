from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('trained/weights/best.pt')

# Run inference on 'bus.jpg' with arguments
model.predict('images', save=True, imgsz=640, conf=0.25)
