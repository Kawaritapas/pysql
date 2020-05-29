"""
Created on Fri May 29 19:03:49 2020

@author: tapas
"""

import numpy as np 
import cv2
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password=,database=,port=)
print("hey i think iam connected")
cur=mydb.cursor()
img = cv2.imread("test.jpg",1)
img = cv2.resize(img,(600,800))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurr = cv2.GaussianBlur(grey, (5,5),0)
edge = cv2.Canny(blurr, 0, 50)   
_, contours, _ = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse= True)
for i in contours:
	elip =  cv2.arcLength(i, True)
	approx = cv2.approxPolyDP(i,0.08*elip, True)
	if len(approx) == 4 : 
		doc = approx 
		break
cv2.drawContours(img, [doc], -1, (0, 255, 0), 2)
doc=doc.reshape((4,2))
new_doc = np.zeros((4,2), dtype="float32")
Sum = doc.sum(axis = 1)
new_doc[0] = doc[np.argmin(Sum)]
new_doc[2] = doc[np.argmax(Sum)]
Diff = np.diff(doc, axis=1)
new_doc[1] = doc[np.argmin(Diff)]
new_doc[3] = doc[np.argmax(Diff)]
(tl,tr,br,bl) = new_doc
dist1 = np.linalg.norm(br-bl)
dist2 = np.linalg.norm(tr-tl)
maxLen = max(int(dist1),int(dist2))
dist3 = np.linalg.norm(tr-br)
dist4 = np.linalg.norm(tl-bl)
maxHeight = max(int(dist3), int(dist4))
dst = np.array([[0,0],[maxLen-1, 0],[maxLen-1, maxHeight-1], [0, maxHeight-1]], dtype="float32")
N = cv2.getPerspectiveTransform(new_doc, dst)
warp = cv2.warpPerspective(img, N, (maxLen, maxHeight))
img2 = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
img2 = cv2.resize(img2,(600,800))
imaged=cv2.imwrite("countur.jpg",img)
print(imaged)
cv2.imshow("Scanned.jpg", img2)
cv2.imshow("edge.jpg",edge)
cv2.imshow("contour.jpg",img)
cur.execute("insert into testing""(image)""values(%s)",("countur.jpg",) )
mydb.commit();
mydb.close()
cv2.waitKey(0)
cv2.destroyAllWindows()