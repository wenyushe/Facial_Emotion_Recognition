# Facial Emotion Recognition
 Web app to detect emotion by looking at user's face
 
 <img width="700" height="370" src="https://github.com/wenyushe/Facial_Emotion_Recognition/blob/main/demo.gif">
 
 ## Steps to run app:
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
 
 ## Steps to train model:
 1. Setup: (same as step 1 for "Steps to run app"
 2. Download [Facial expression recognition (FER 2013) dataset](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset) and save as folder called "images"
 3. Run all cells in create_model.ipynb file to train the model
 4. Feel free to further improve on my model + let me know if you have any questions!
    
 ## Currently working on:
 - implementing a live histogram to display percentages of all emotions detected
 
 ## Resources:
 1.  [Facial expression recognition (FER 2013) dataset](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset) from Kaggle
      - 35,000+ images of faces (48x48 pixel jpgs) sorted into folders by emotion
 2. haarcascade_frontalface_default.xml from [OpenCV GitHub](https://github.com/kipr/opencv)
      - OpenCV algorithm used to detect faces through camera 
