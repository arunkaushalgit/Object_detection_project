from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # lightweight pretrained model

model.train(
    data='data.yaml',
    epochs=80,
    imgsz=640,
    batch=16,
    lr0=0.0001,
    augment=True,
    patience=10,
    weight_decay=0.0005,
    verbose=True
)
