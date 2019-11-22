img1 = cv2.imread('logo.jpg')
img2 = cv2.imread('lena5.jpg')
img3 = cv2.imread('1.jpg')
img4 = cv2.imread('2.jpg')
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
add = cv2.add(img1,img2)
sub = cv2.subtract(img3, img4)
cv2.imshow('img3',img4)
cv2.imshow('img4',img3)
cv2.imshow('logo',img1)
cv2.imshow('lena',img2)
cv2.imshow('dst',dst)
cv2.imshow('add',add)
cv2.imshow('sub',sub)
cv2.waitKey(0)
cv2.destroyAllWindows()