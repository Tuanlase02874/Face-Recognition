# import the necessary packages
import requests
import cv2
 
# define the URL to our face detection API
url = "http://10.3.9.64:8080/face_detection/detect/"
file_path ="Tuan/image_35.jpg"
image = cv2.imread(file_path)
payload = {"image": open(file_path, "rb")}
r = requests.post(url, files=payload).json()
print "obama.jpg: {}".format(r)
url = "http://10.3.9.64:8080/face_recognition/api/"
r = requests.post(url, files=payload).json()
print "obama.jpg: {}".format(r)
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
 
# show the output image
cv2.imshow("adrian.jpg", image)
cv2.waitKey(0)
