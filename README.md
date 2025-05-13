 ## **Sports Performance Analysis System**

# **Purpose:**
  This project creates a basic sports performance analysis system that detects and tracks moving players or objects in a sports video using OpenCV and background subtraction techniques. It is designed to:
Detect and highlight moving players or objects in sports videos.Track and visualize player movement using bounding boxes.Display the processed video in real-time with overlays.Serve as a base for further sports analytics tasks such as player tracking, speed estimation, and heatmaps.

# **Technologies Used:**

# *1.OpenCV (cv2):*

  *For video capture, image processing, and display.
  *Background Subtraction (MOG2) to separate moving players from the static background.
  *Contour detection for identifying and tracking objects.

# *2.NumPy:*

  *Used for array operations and support for OpenCV image processing.

# *3.Computer Vision Techniques:*

  *Background subtraction using MOG2 algorithm.
  *Morphological operations (opening) to clean noise from the foreground mask.
  *Contour detection and bounding box drawing.

# **Usage:**

# *1. Prepare the sports video:* 

   *Place your video file (e.g., sports_video.mp4) in the project directory.

# *2. Run the script using Python:*

   python sports_analysis.py

# *3. Controls:*

 *The video will play with detected players highlighted.
 *Press 'q' to exit the video window.
  
# **Key Features:**

  *Real-time player and object detection in sports videos.
  *Background Subtraction (MOG2) for foreground extraction.
  *Morphological filtering to remove small noise.
  *Bounding boxes to highlight significant movements.
  *Easy to use and extend for further sports analytics.

# **Conclusion:**

   This implementation demonstrates a simple but effective approach to sports performance analysis using computer vision techniques. The system:Provides real-time visual feedback of detected players and objects.Uses background subtraction and contour detection for efficient motion tracking.Can be further enhanced to support player tracking, speed estimation, team classification, and activity heatmaps.
