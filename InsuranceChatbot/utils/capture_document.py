import cv2
import numpy as np

image = ""
refPt = []
cropping = False


class CaptureWebcam:

    @classmethod
    def click_and_crop(self, event, x, y, flags, param):
        # grab references to the global variables
        global refPt, cropping, image
        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being
        # performed
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]
            cropping = True
        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            refPt.append((x, y))
            cropping = False
            # draw a rectangle around the region of interest
            res = cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
            return res

    @classmethod
    def capture_document(self):
        print("inside capture document")
        try:
            img_str_cropped = ""
            cam = cv2.VideoCapture(0)
            cv2.namedWindow("test")
            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)

                k = cv2.waitKey(1) & 0xFF
                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed
                    captured_img_name = "Document.png"
                    img_as_str = cv2.imencode('.jpg', frame)[1].tostring()
                    print("{} written!".format(captured_img_name))
                elif k == ord("e"):
                    print("e is pressed")
                    img_str_cropped = self.crop_document(img_as_str)
            cam.release()
            cv2.destroyAllWindows()
            if img_str_cropped == "":
                return img_as_str
            else:
                return img_str_cropped
        except:
            return "Image not clicked Correctly"


    @classmethod
    def crop_document(self, img_str):
        global image
        nparr = np.fromstring(img_str, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        clone = image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.click_and_crop)
        # keep looping until the 'q' key is pressed
        while True:
            # display the image and wait for a keypress
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF
            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                image = clone.copy()
            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break
        # if there are two reference points, then crop the region of interest
        # from teh image and display it
        if len(refPt) == 2:
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            cv2.imshow("Cropped Image", roi)
            img_str_cropped = cv2.imencode('.jpg', roi)[1].tostring()
            cv2.waitKey(0)
            print("Given image is been cropped and saved..!!")
            return img_str_cropped

            # close all open windows
        cv2.destroyAllWindows()
