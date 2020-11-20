import cv2
import os

try:
    if not os.path.exists('output'):
        os.makedirs('output')
except OSError:
    print('Error: Creating Directory of Data')

outputLocation = 'output'
# to read the video
print('reading video')

videoPath = 'PATH/TO/VIDEO'  # path to Video
frame_set_no = 100
cap = cv2.VideoCapture(videoPath)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
print('starting annotation')
frameIndex = 0
imageNo = 0
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_set_no)

while(True):
    ret, frame = cap.read()
    frameIndex += 1
    if ret:
        if (frameIndex % 120 == 0):
            filename = outputLocation + '/{clip}_frame{frameNo}.jpg'.format(clip = videoPath.split('/')[-1][:-4], frameNo = str(imageNo)) #output path
            cv2.imwrite(filename, frame)
            imageNo += 1
            print("image: " + str(imageNo))
    else:
        break

cap.release()
cv2.destroyAllWindows()
print("complete")
