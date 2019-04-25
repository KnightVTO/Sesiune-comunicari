import cv2 as cv

alfabetul=cv.imread('Alfabet binarizat.jpg', 0)
cv.imshow('ceva', alfabetul)

cv.waitKey(0)
cv.destroyAllWindows()
