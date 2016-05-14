from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2
import os
 
# Get API Face Detection
FACE_DETECTOR_PATH = "{base_path}/knowledge/haarcascade_frontalface_default.xml".format(
	base_path=os.path.abspath(os.path.dirname(__file__)))
FACE_RECOGNITION_PATH = "{base_path}/knowledge/T3_model_face_recognition.yaml".format(base_path=os.path.abspath(os.path.dirname(__file__)))
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load(FACE_RECOGNITION_PATH)
detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
@csrf_exempt
def recognition(request):
	# initialize response
	data = {"success": False}
	if request.method == "POST":
		if request.FILES.get("image", None) is not None:
			image = _grab_image(stream=request.FILES["image"])
		else:
			url = request.POST.get("url", None)
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)
			image = _grab_image(url=url)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5,
			minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

		# construct a list of bounding boxes from the detection
		nbr_predicted = 16
		for (x, y, w, h) in rects:
			nbr_predicted, conf = recognizer.predict(image[y: y + h, x: x + w])

		# Return for client
		name = ["Tuan","Thu","Thanh"]
		if nbr_predicted == 16:
			data.update({"num_faces": len(rects), "faces":nbr_predicted, "success": True,"Name":"No Information"})
		else:	
			data.update({"num_faces": len(rects), "faces":nbr_predicted, "success": True,"Name":name[nbr_predicted - 1]})
	return JsonResponse(data)
def _grab_image(path=None, stream=None, url=None):
	if path is not None:
		image = cv2.imread(path)
	else:	
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()
		elif stream is not None:
			data = stream.read()
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

