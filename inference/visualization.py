from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/best.pt")  # Global model load

def detect_objects(image, conf=0.5):
    results = model(image, conf=conf)[0]
    return results

def draw_boxes(img, results):
    img_draw = img.copy()
    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = round(float(box.conf[0]), 2)
        cls = int(box.cls[0])
        label = model.names[cls]
        text = f"{label.upper()} {conf:.2f}"

        # Bounding Box
        cv2.rectangle(img_draw, (x1, y1), (x2, y2), (0, 0, 255), 5)

        # Label
        font_scale = 2.0
        font_thickness = 2
        (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)
        cv2.rectangle(img_draw, (x1, y1 - th - 10), (x1 + tw + 6, y1), (0, 255, 0), -1)
        cv2.putText(img_draw, text, (x1 + 3, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), font_thickness + 1)
        cv2.putText(img_draw, text, (x1 + 3, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), font_thickness)

        detections.append({"Label": label, "Confidence": conf})
    return img_draw, detections
