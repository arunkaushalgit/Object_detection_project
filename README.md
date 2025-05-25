# Custom Object Detection Using YOLOv8

## Dataset Information
- Total Images: 166
- Source: Images collected from Unsplash and Pexels.ai — high-quality, royalty-free images.
- Annotation Tool: Used CVAT for annotating the dataset to prepare bounding boxes for training.
- Dataset Split: Dataset is divided into Training and Validation sets to evaluate model generalization.

## Model Choice
- YOLOv8 (You Only Look Once, version 8) was chosen due to its:
  - State-of-the-art real-time object detection capabilities.
  - Balance of accuracy and inference speed.
  - Easy integration with custom datasets.
- Trained a custom YOLOv8 model using the annotated images to detect the target classes specific to the dataset.

## Challenges Faced and Solutions

## Limited Dataset Size: 
  With only 166 images, training a deep learning model was challenging.  
Solution:
  - Applied data augmentation techniques during training to artificially increase dataset diversity.  
  - Used transfer learning by initializing weights from a pretrained YOLOv8 model, helping the model generalize better.

## Annotation Consistency:  
  Ensuring accurate and consistent bounding box annotations was critical.  
  Solution:  
  - Used CVAT for precise manual annotations.  
  - Reviewed and corrected annotations multiple times to maintain quality.

## Model Overfitting:  
  Small dataset size led to risk of overfitting.  
Solution: 
  - Implemented early stopping during training.  
  - Monitored validation loss and accuracy closely.  
  - Used regularization techniques as necessary.

Deployment Considerations:**  
  Managing model size and inference speed for deployment in real-time applications.  
Solution: 
  - Chose YOLOv8 due to its lightweight architecture.  
  - Optimized confidence thresholds and non-max suppression parameters.

## Performance Metrics
- Training Dataset Size: ~80% of images  
- Validation Dataset Size:** ~20% of images  
- Mean Average Precision (mAP@0.5): 0.574  
- Precision: 0.98 @ 1.0 
- Recall: 0.80 


## How to Use
- The custom YOLOv8 model is integrated into a Streamlit application for easy interaction:
  - Upload images or videos.
  - See bounding boxes and detection labels in real time.
  - Adjust confidence threshold dynamically.

## Future Work
- Expand dataset size with more varied images.  
- Incorporate more object classes if needed.  
- Experiment with model quantization for faster deployment.  
- Enhance UI with live webcam support and batch processing.

---

This project demonstrates a practical application of YOLOv8 for custom object detection with limited data, emphasizing clean annotations, model optimization, and user-friendly deployment.
