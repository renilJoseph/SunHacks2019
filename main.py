import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
import json
import logging
from flask import Flask
from flask import request
from viewsh import Sunhacks
# import cloudstorage as gcs

# from google.appengine.api import app_identity
app = Flask(__name__)

bucket = '/' + 'newsunhack.appspot.com'

# def create_file(self, byt):
#     bucket = '/' + 'newsunhack.appspot.com'
#     filename = bucket + '/input.jpg'
#     #self.response.write('Creating file %s\n' % filename)
#     write_retry_params = gcs.RetryParams(backoff_factor=1.1)
#     gcs_file = gcs.open(filename,'w',options={'x-goog-meta-foo': 'foo','x-goog-meta-bar': 'bar'},retry_params=write_retry_params)
#     gcs_file.write(byt)
#     #gcs_file.write('f'*1024*4 + '\n')
#     gcs_file.close()
#     #self.tmp_filenames_to_clean_up.append(filename)

# #filename : YOUR_BUCKET_NAME/PATH_IN_GCS
# def read_file(self, filename):
#     #bucket = '/' + 'newsunhack.appspot.com'
#     filename = bucket + '/input.jpg'
#     self.response.write('Reading the full file contents:\n')

#     gcs_file = gcs.open(filename)
#     contents = gcs_file.read()
#     gcs_file.close()
#     self.response.write(contents)

@app.route("/")
def hello():
    return "Hello World!"

def home(bytes):
    print('INSIDE home')
    # b = bytearray(bytes)
    # newFile = open('input.jpg', 'wb')
    # newFile.write(b)
    # newFile.close()
    args = {}
    args["detector"] = 'face_detection_model'
    args["embedding_model"] = 'openface_nn4.small2.v1.t7'
    args["recognizer"] = 'recognizer.pickle'
    args["le"] = 'le.pickle'
    args["image"] = 'input.jpg'
    args["confidence"] = 0.4


    # load our serialized face detector from disk
    print("[INFO] loading face detector...")
    protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
    modelPath = os.path.sep.join([args["detector"],
        "res10_300x300_ssd_iter_140000.caffemodel"])
    detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)



    # load our serialized face embedding model from disk
    print("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

    # load the actual face recognition model along with the label encoder
    recognizer = pickle.loads(open(args["recognizer"], "rb").read())
    le = pickle.loads(open(args["le"], "rb").read())

    # load the image, resize it to have a width of 600 pixels (while
    # maintaining the aspect ratio), and then grab the image dimensions
    nparr = np.fromstring(bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1
    #image = cv2.imread('input.jpg')
    image = imutils.resize(image, width=600)
    (h, w) = image.shape[:2]

    # construct a blob from the image
    imageBlob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 1.0, (300, 300),
        (104.0, 177.0, 123.0), swapRB=False, crop=False)

    # apply OpenCV's deep learning-based face detector to localize
    # faces in the input image
    detector.setInput(imageBlob)
    detections = detector.forward()
    name = ''

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections
        if confidence > args["confidence"]:
            # compute the (x, y)-coordinates of the bounding box for the
            # face
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # extract the face ROI
            face = image[startY:endY, startX:endX]
            (fH, fW) = face.shape[:2]

            # ensure the face width and height are sufficiently large
            if fW < 20 or fH < 20:
                continue

            # construct a blob for the face ROI, then pass the blob
            # through our face embedding model to obtain the 128-d
            # quantification of the face
            faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
                (0, 0, 0), swapRB=True, crop=False)
            embedder.setInput(faceBlob)
            vec = embedder.forward()

            # perform classification to recognize the face
            preds = recognizer.predict_proba(vec)[0]
            j = np.argmax(preds)
            proba = preds[j]
            name = le.classes_[j]
        return name

@app.route('/test', methods=['POST'])
def test():
    print('yeahhhhh')
    imagefile = request.files['media']
    bytes = imagefile.read()
    b = bytes
    res = Sunhacks.localize_byte_input(b)
    for i in res:
        if i['type'] == 'Person':
            i['type'] = str(home(b))
            print('result of opencv call')
            print(i['type'])
        break
    logging.info('res')
    print(res)
    print('end')
    print(json.dumps(res))
    return json.dumps(res)

app.run()
