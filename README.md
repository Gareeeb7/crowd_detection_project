crowd_detection_project
# Detecting crowd in given images based upon no of peoples faces found in image 
 
# Requirements
1. OpenCV
2. Flask
3. Haar cascade classifier
4. Python
5. Postman ( for Testing crowd Api )

# Steps to run project

1. Install all the requirements
a. pip install opencv-contrib-python
b. pip install flask_restful
c. pip install matplotlib (Optional if you want to analys picture)

2. Open CMD in Project file 

3. run flask on cmd via ( flask run )

4. Now Test the created API on postman 
a. route "http://127.0.0.1:5000/add"
b. method POST
c. Body should be in JASON data format:
{
    "x":"img1.jpg"
}
4. Send request
5. Reult:
{
    "Message": "Crowd Not Detected",
    "No of Peoples": 22,
    "Status Code": 200
}


