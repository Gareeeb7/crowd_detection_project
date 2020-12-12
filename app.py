# importing libraries
import cv2
import matplotlib.pyplot as plt
from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if (functionName == "add"):
        if "x" not in postedData:
            return 301 #Missing parameter
        else:
            return 200

class Add(Resource):
    def post(self):
        
        postedData = request.get_json()
        #Verify validity of posted data
        status_code = 200
        
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        # face ditection haarcascade classifier
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # importing image
        img = cv2.imread(x)
        # Converting RGB to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        count_faces = len(faces)

        if(count_faces < 30):  #provide value based upon how much view your camera can caputres
            ret = "Crowd Not Detected"
        else:
            ret = "Crowd Detected"
        
        retMap = {
            'Message': ret,
            'No of Peoples': count_faces,
            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="__main__":
    app.run(debug=True)
