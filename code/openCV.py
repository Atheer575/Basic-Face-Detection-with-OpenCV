import cv2
from google.colab.patches import cv2_imshow

class BasicFaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_faces(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            return None, 0
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image, len(faces)

    def show_image(self, image):
        if image is not None:
            cv2_imshow(image)

def main():
    detector = BasicFaceDetector()
    image_path = "test_image.jpg"  # replace with your uploaded image path
    result_image, face_count = detector.detect_faces(image_path)
    print("Faces found:", face_count)
    detector.show_image(result_image)

main()