import cv2, time

"""
We create a VideoCapture object from a video file or we can also use our webcam
0 triggers our webcam
for a file we need to provide it the path
"""
video = cv2.VideoCapture(0)

no_of_frames = 0

while True:
    no_of_frames += 1
    # the loop helps us to display a series of frames as captured by the camera.
    check, frame  = video.read()
    # check is a boolean which checks whether the camera is capturing or not
    # frame is a numpy array which specifies the image as an array
    print(check)
    # print(frame)
    print(frame.shape)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # we can also display the gray image

    # time.sleep(2) # To give it some time to capture a video

    cv2.imshow("Capturing", frame) # this shows us the first frame of the video that is being captured
    # cv2.imshow("Capturing gray image", gray)

    key = cv2.waitKey(1) # the window waits for the specified time and then shows the next frame
    # the video is not released before we press a key
    if key == ord('q'):  # q for quit...lol
        break

print("Number of frames = " + str(no_of_frames))

video.release()  # releases the camera...

cv2.destroyAllWindows()
