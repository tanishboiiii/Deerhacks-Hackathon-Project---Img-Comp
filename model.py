import cv2
import matplotlib.pyplot as plt


def gagan(path):
  # print("\n\n\n\n")
  # print(path)
  # raise ValueError
  # print("\n\n\n\n\n")
  config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
  frozen_model = 'frozen_inference_graph.pb'

  model = cv2.dnn_DetectionModel(frozen_model, config_file)

  classLabels = []
  file_name = 'labels.txt'
  with open(file_name, 'rt') as fpt:
      classLabels = fpt.read().rstrip('\n').split('\n')


  model.setInputSize(320, 320)
  model.setInputScale(1.0/127.5)
  model.setInputMean((127.5, 127, 127.5, 127.5))
  model.setInputSwapRB(True)

  img = cv2.imread(path)
  ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
  print(ClassIndex)

  font_scale = 2
  font = cv2.FONT_HERSHEY_PLAIN

  mid = (0, 0)
  width, length, smth = img.shape
  left = length // 3
  right = 2 * left
  down = width // 3
  up = 2 * down
  start_point = (0, 0)

  # Line thickness of 9 px
  thickness = 9
  img = cv2.line(img, (left, up), (right, up), (0, 255, 0), 9)
  img = cv2.line(img, (left, down), (right, down), (0, 255, 0), 9)
  img = cv2.line(img, (left, up), (left, down), (0, 255, 0), 9)
  img = cv2.line(img, (right, up), (right, down), (0, 255, 0), 9)

  for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
    lat, lon = (boxes[0] + boxes[2]//2), (boxes[1] + boxes[3]//2)

    if (lat * lon) > (mid[0] * mid[1]):
      mid = (lat, lon)
    cv2.rectangle(img, boxes, (255, 0, 0), 2)
    cv2.putText(img, classLabels[ClassInd-1], (boxes[0]+10, boxes[1]+40),
                font, fontScale=font_scale, color=(0, 255, 0), thickness=3)


  if mid[0] >= right:
    if mid[1] <= down:
      img = cv2.line(img, (right, down), mid, (0, 0, 255), 8)
    elif mid[1] >= up:
      img = cv2.line(img, (right, up), mid, (0, 0, 255), 8)
    else:
      img = cv2.line(img, (right, mid[1]), mid, (0, 0, 255), 8)
  elif mid[0] <= left:
    if mid[1] <= down:
      img = cv2.line(img, (left, down), mid, (0, 0, 255), 8)
    elif mid[1] >= up:
      img = cv2.line(img, (left, up), mid, (0, 0, 255), 8)
    else:
      img = cv2.line(img, (left, mid[1]), mid, (0, 0, 255), 8)
  elif mid[1] >= up:
    img = cv2.line(img, mid, (mid[0], up), (0, 0, 255), 8)
  elif mid[1] <= down:
    img = cv2.line(img, mid, (mid[0], down), (0, 0, 255), 8)
  else:
    img = cv2.line(img, mid, (right, down),  (0, 0, 255), 8)
    img = cv2.line(img, (right, up), mid, (0, 0, 255), 8)
    img = cv2.line(img, (left, down), mid, (0, 0, 255), 8)
    img = cv2.line(img, (left, up), mid, (0, 0, 255), 8)


  # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  cv2.imwrite('savedImage.jpg', img)


# try:
#   gagan("photo.jpg")
# except:
#   pass