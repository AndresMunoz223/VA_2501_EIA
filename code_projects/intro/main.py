import cv2
from icecream import ic
import numpy as np



def nothing(x):
    pass



# image_binary = np.zeros()

def main():
    #Show the image on a matrix-like form

    #* read images with their respective color spaces

    image_abs = cv2.imread("C:/Users/juan.nunez/Documents/repos/VA_2501_EIA/resources/test_images/des.png", cv2.IMREAD_COLOR_RGB)
    image_rel = cv2.imread("resources/test_images/des.png", cv2.IMREAD_COLOR_RGB)

    #* read the grayscale version on the images
    # ! Remember to use the cv2.---- defines to improve code readability

    image_abs_BW = cv2.imread("C:/Users/juan.nunez/Documents/repos/VA_2501_EIA/resources/test_images/dog.png", cv2.IMREAD_GRAYSCALE)
    image_rel_BW = cv2.imread("resources/test_images/dog.png", cv2.IMREAD_GRAYSCALE)

    # * Resize the images
    #Note that we can use proportions or tuples to express the required image rezise
    # image_abs_BW = cv2.resize(image_abs_BW, (0, 0), fx = 0.1, fy = 0.1)
    # image_abs_BW = cv2.resize(image_abs_BW, (400,400))





    
    cv2.namedWindow("image_gray_conv")
    cv2.createTrackbar("Rmin", "image_gray_conv", 1, 255, nothing)
    cv2.createTrackbar("Rmax", "image_gray_conv", 0, 255, nothing)

    cv2.createTrackbar("Gmin", "image_gray_conv", 1, 255, nothing)
    cv2.createTrackbar("Gmax", "image_gray_conv", 0, 255, nothing)

    cv2.createTrackbar("Bmin", "image_gray_conv", 1, 255, nothing)
    cv2.createTrackbar("Bmax", "image_gray_conv", 0, 255, nothing)


    while 1:    
        # * Now, creating trackbars

        threshR2 = cv2.getTrackbarPos("Rmin", "image_gray_conv")
        threshR1 = cv2.getTrackbarPos("Rmax", "image_gray_conv")
        threshG2 = cv2.getTrackbarPos("Gmin", "image_gray_conv")
        threshG1 = cv2.getTrackbarPos("Gmax", "image_gray_conv")
        threshB2 = cv2.getTrackbarPos("Bmin", "image_gray_conv")
        threshB1 = cv2.getTrackbarPos("Bmax", "image_gray_conv")




        # * Create thresholds for images, pretty handy but remember the astype()
        image_abs_1_R = np.where(image_abs[:,:,0] < threshR2, 0, 250).astype(np.uint8)
        image_abs_2_R = np.where(image_abs[:,:,0] > threshR1, 0, 250).astype(np.uint8)

        image_abs_1_G = np.where(image_abs[:,:,1] < threshG2, 0, 250).astype(np.uint8)
        image_abs_2_G = np.where(image_abs[:,:,1] > threshG1, 0, 250).astype(np.uint8)

        image_abs_1_B = np.where(image_abs[:,:,2] < threshB2, 0, 250).astype(np.uint8)
        image_abs_2_B = np.where(image_abs[:,:,2] > threshB1, 0, 250).astype(np.uint8)


        image_abs_BW_R = image_abs_1_R*image_abs_2_R
        image_abs_BW_G = image_abs_1_G*image_abs_2_G
        image_abs_BW_B = image_abs_1_B*image_abs_2_B

        image_abs_rec = np.zeros(image_abs.shape)

        ic(image_abs_rec)

        image_abs_rec[:,:,0]  = image_abs_BW_R 
        image_abs_rec[:,:,1]  = image_abs_BW_G 
        image_abs_rec[:,:,2]  = image_abs_BW_B 

        image_abs_rec =  (image_abs_BW_R+ image_abs_BW_G+ image_abs_BW_B)/3.

        cv2.imshow("image_gray_conv", image_abs_rec)

        if cv2.waitKey(1) & 0xFF == ord("q"):  break





    # * Resize the image

    # * Wait for the kay to close the image
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()