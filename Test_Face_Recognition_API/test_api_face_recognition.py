# import the necessary packages
import requests
import cv2
 
# define the URL to our face detection API
url = "http://10.3.9.64:8080/face_recognition/api/"
payload = {"image": open("Train_data/subject01/image_0.jpg", "rb")}
r = requests.post(url, files=payload).json()
print "image00.jpg: {}".format(r)
 
payload = {"image": open("Train_data/subject03/image_2.jpg", "rb")}
r = requests.post(url, files=payload).json()
print "image00.jpg: {}".format(r)
payload = {"image": open("Train_data/subject03/image_1.jpg", "rb")}
r = requests.post(url, files=payload).json()
print "image00.jpg: {}".format(r)
payload = {"image": open("Train_data/subject02/image_4.jpg", "rb")}
r = requests.post(url, files=payload).json()
print "image00.jpg: {}".format(r)


