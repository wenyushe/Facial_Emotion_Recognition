# Facial_Emotion_Recognition
 Creating a web app to detect emotion by looking at user's face
 
 ## Steps to run:
 1. Setup + install dependencies
      - Clone this repository onto local drive
      - Install dependencies:
         ```
         pip install -r requirements.txt
         ```
 2. Run webapp.py file
    ```
    python webapp.py
    ```
    
 ## Currently working on:
 1. improving the model accuracy
 2. using CSS to make the webapp look nicer =)
 3. implementing a live histogram to display percentages of all emotions detected
 
 ## Resources:
 1.  [Facial expression recognition (FER 2013) dataset](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset) from Kaggle
      - 35,000+ images of faces (48x48 pixel jpgs) sorted into folders by emotion
 2. haarcascade_frontalface_default.xml from [OpenCV GitHub](https://github.com/kipr/opencv)
      - Software developed as part of OpenCV. Used to detect faces with camera 
