from flask import Flask, render_template, Response
import cv2
import numpy as np
from tensorflow.keras.models import model_from_json  
from tensorflow.keras.preprocessing import image
  

# load model  
model = model_from_json(open("./static/model.json", "r").read())  

# load weights  
model.load_weights('./static/model_weights.h5')  

# model for face detection
face_haar_cascade = cv2.CascadeClassifier('./static/haarcascade_frontalface_default.xml')  

# app
app = Flask(__name__)

# camera
camera = cv2.VideoCapture(0)


# function to generate frame by frame from camera
def gen_frames(): 
    max_index=4
    while True:
        # Capture frame by frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # gray_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        
            # faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)  
            faces_detected = face_haar_cascade.detectMultiScale(frame, 1.32, 5)  

            for (x,y,w,h) in faces_detected:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=7)  
                # roi_gray=gray_img[y:y+w,x:x+h]          #cropping region of interest i.e. face area from  image  
                roi_gray=frame[y:y+w,x:x+h]          #cropping region of interest i.e. face area from  image  
                roi_gray=cv2.resize(roi_gray,(48,48))  
                img_pixels = image.img_to_array(roi_gray)  
                img_pixels = np.expand_dims(img_pixels, axis = 0)  
                img_pixels /= 255  
        
                print(img_pixels.shape)
                
                predictions = model.predict(img_pixels)  
                print(predictions)


                # Adjustments:
                predictions[0][3]*=400
                predictions[0][4]/=50
                predictions[0][5]/=30
                
                #find max indexed array  
                pred = np.argmax(predictions[0])  

                # Threshold (at least 50% confidence)
                # if (predictions[0][pred]/sum(predictions[0]) > 0.5):     
                max_index = pred

                emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']  
                predicted_emotion = emotions[max_index]  
                print(predicted_emotion)
                cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)  
        
            resized_img = cv2.resize(frame, (1000, 700))  
            
            ret, buffer = cv2.imencode('.jpg', frame)
            
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

    # After the loop release the video capture object
    camera.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)