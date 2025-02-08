# filtros espaciales
import cv2

path = r"images\4.png"

imgcolor = cv2.imread(path, 1)
cv2.imshow("Imagen original", imgcolor)
cv2.waitKey(0)
cv2.destroyAllWindows()