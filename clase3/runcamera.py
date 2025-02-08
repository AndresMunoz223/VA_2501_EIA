import cv2
import threading
import reportlog
import time

class runcamara():
    def __init__(self, src=0, name="camarathread"):
        try:
            self.name = name
            self.src = src
            self.capture = None
            self.frame = None
            self.grabbed = False
            self.logreport = reportlog.reportlog()
            self.logreport.logger.info("Iniciando camara ok")

        except Exception as e:
            self.logreport.logger.error("Error iniciando camara: "+str(e))
    
    def start(self):
        try:
            self.capture = cv2.VideoCapture(0)
            self.grabbed, self.frame = self.capture.read()
            if (self.capture.isOpened()):
                self.camerathread = threading.Thread(target=self.get, name=self.name, daemon=True)
                self.camerathread.start()

        except Exception as e:
            self.logreport.logger.error("Error estar camara: "+str(e))

    def get(self):
        try:
            while self.grabbed:
                self.grabbed, self.frame = self.capture.read()
                if not self.grabbed:
                    break
                self.processframe()
            cv2.destroyAllWindows()
        except Exception as e:
            self.logreport.logger.error("Error get frame: "+str(e))

    def processframe(self):
        cv2.imshow(self.name, self.frame)
        time.sleep(0.1)