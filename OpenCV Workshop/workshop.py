
# It contains the basic libraryes on the open cv libraries just as contur,thresshold,detect edges, garyscale,expand and contract image objects
import cv2
import imutils
#code

image = cv2.imread("block.jpg",1)
image = cv2.resize(image,dsize=(600,600))

# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5),0)
edged1 = cv2.Canny(gray, 10, 50)
edged = cv2.Canny(gray, 50, 200)
cv2.imshow("Edged",edged)
cv2.imshow("Edged1",edged1)



#threshold invere the background
cv2.imshow("gray",gray)
thress = cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshold",thress)



# contour drawing
contur = cv2.findContours(thress.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
contur = imutils.grab_contours(contur)
output = image.copy()


for  c in contur:
    cv2.drawContours(output,[c],-1,(240,55,159),3)
    #cv2.imshow("Contours",output)
    


text = "It found {} objects!".format(len(contur))
cv2.putText(output,text,(10,25),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,0),2)
cv2.imshow("Contours",output)


cv2.waitKey(0)
cv2.destroyAllWindows()



