# import the necessary packages
import requests
import cv2
 
# define the URL to our face detection API
url = "http://10.3.9.64:8080/face_detection/detect/"
# load our image and now use the face detection API to find faces in
# images by uploading an image directly
name = "Train_data/subject01/image_0.jpg"
image = cv2.imread(name)
payload = {"image": open(name, "rb")}
r = requests.post(url, files=payload).json()
print "adrian.jpg: {}".format(r)
 
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
 
# show the output image
cv2.imshow("adrian.jpg", image)
cv2.waitKey(0)

