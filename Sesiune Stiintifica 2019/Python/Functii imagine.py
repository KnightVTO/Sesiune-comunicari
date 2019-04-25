#Aceasta comanda este acelasi lucru cu "include" din C++, "cv2" fiind libraria de functii pentru imagini
import cv2

#Incarca imaginea. 0=Grayscale, 1=Color.  Va ramane 0 pentru aplicarea filtrelor.
img = cv2.imread('25.jpg', 0)

#Afiseaza imaginea sub numele de "my image" prin variabila "img"
cv2.imshow('my image', img)

#Scrie imaginea "img" sub forma de grayscale
img1=cv2.imwrite('poza grayscale.jpg', img)

#Citeste imaginea originala
alfabet=cv2.imread('Alphabet.jpg',0)
img2=cv2.imread('25.jpg', 1)
cv2.imshow("imaginea originala", img2)

#Imagine alb-negru prin Threshold+Aplicare filtru Gaussian(cica)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('imagine binarizata',thresh1)

alfabet_bin=cv2.adaptiveThreshold(alfabet,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

th3 = cv2.adaptiveThreshold(thresh1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('imagine filtrata-gaussiana',th3)


img3=cv2.imwrite('imaginea binarizata.jpg',thresh1)
img4=cv2.imwrite('Alfabet binarizat.jpg', alfabet_bin)
cv2.imshow("ce",alfabet_bin)
#La apasarea oricarei taste ferestele imaginilor se vor inchide
cv2.waitKey(0)
cv2.destroyAllWindows()
