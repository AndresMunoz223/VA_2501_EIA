import logging

class reportlog():
    def __init__(self):
        try:
            logging.basicConfig(filename="loginfo.log", level=logging.INFO)
            self.logger = logging.getLogger()
        except Exception as e:
            print("error creando el logger info: "+str(e))