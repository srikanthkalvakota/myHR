import cv2

def capture_image(candid):
    camera = cv2.VideoCapture(0)
    while True:
        return_value, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('image', gray)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('./captured_images/candidate_{0}.jpg'.format(candid), image)
            break
    camera.release()
    cv2.destroyAllWindows()
