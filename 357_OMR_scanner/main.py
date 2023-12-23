from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

ANSWER_KEY = {0:1, 1:4, 2:0, 3:3, 4:1}
"""
0 = 1st question, 1 signifies "B" as the correct answer
i.e., key of 0 maps to a value of 1(which is B)
"""

# load the image
image = cv2.imread(args["image"])
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur the image
blurred = cv2.GaussianBlur(gray, (5,5), 0)
# find edges
edges = cv2.Canny(blurred, 75, 200)

# cv2.imshow("Edges", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""We have the outline of our exam, so we find contours"""
# find contours
cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None

# ensure at least one contour was found
if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True) # larger contours will be placed at front of list
    for c in cnts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c, 0.02*peri, True)

        # if approximated contour has 4 points, then we assume we have found the paper
        if len(approx) == 4:
            docCnt = approx
            # Draw the contour on the original image
            # cv2.drawContours(image, [docCnt], -1, (0, 255, 0), 2)
            break

# Display the image with contours
# cv2.imshow("Contours", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
        
# apply a 4 point perspective transform to both original image and grayscale image to obtain a top-down view of paper
paper = four_point_transform(image, docCnt.reshape(4,2))
warped = four_point_transform(gray, docCnt.reshape(4,2))

# Display the image after 4-point perspective transform
# cv2.imshow("4 point perspective transform", warped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Binarization - Thresholding/Segmenting the foreground from the background of the image
# Apply Otsu's thresholding method
thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Display the image after Otsu's Threshold
# cv2.imshow("after Otsu's threshold", thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Binarization will allow us to once again apply contour extraction techniques to find each of the bubbles in the exam
# find contours in the thresholded image, then initialize the list of contours that correspond to questions
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []

# loop over the contours
for c in cnts:
    # compute the bounding box of the contour, then use the bounding box to derive the aspect ratio
    (x,y,w,h) = cv2.boundingRect(c)
    ar = w/float(h)

    # Region should be sufficiently wide and tall to label the contour as a question
    
    if w>=20 and h>=20 and ar>=0.9 and ar<=1.1:
        questionCnts.append(c)

# Draw the question contours on the original image (warped)
# cv2.drawContours(warped, questionCnts, -1, (0, 255, 0), 2)

# Display the image with question contours
# cv2.imshow("Question Contours", warped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
        
# sort the question contours top-to-bottom, then initialize the total number of correct answers
questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
correct = 0 # track of the number of correct answers.

# each question has 5 possible answers to loop over the question in batches of 5
for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
    # sort contours for the current question from left to right, then initialize the index of the bubbled answer
    cnts = contours.sort_contours(questionCnts[i:i+5])[0]
    bubbled = None

    # loop over the sorted contours
    for (j, c) in enumerate(cnts):
        # construct a mask that reveals only the current "bubble" for the question
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)

        # apply the mask to the thresholded image, then count the number of non-zero pixels in the bubble area
        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)

        # if the current total has a larger number of total non-zero pixels, then we are examining the currently bubbled-in answer
        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)

    # Lookup the correct answer
    # initialize the contour color and the index of the *correct* answer
    color = (0, 0, 255)
    k = ANSWER_KEY[q]

    # check to see if the bubbled answer is correct
    if k == bubbled[1]:
        color = (0, 255, 0)
        correct += 1

    # draw the outline of the correct answer on the test
    cv2.drawContours(paper, [cnts[k]], -1, color, 3)

# grab the test taker
score = (correct / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper, "{:.2f}%".format(score), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", paper)
cv2.waitKey(0)
