import cv2 as cv
frame = cv.imread('pucture3.png ')


def figures(src):
    gr = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # bl = cv.medianBlur(gr, 5)
    canny = cv.Canny(gr, 100, 250)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    closed = cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)

    contours = cv.findContours(closed.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    for cont in contours:
            sm = cv.arcLength(cont, True)
            apd = cv.approxPolyDP(cont, 0.03*sm, True)

            y = 0
            x = 0
            for i in range(len(apd)):
                x += apd[i][0][1]
                y += apd[i][0][0]
            y //= len(apd)
            x //= len(apd)
            red = src[x, y, 2]
            green = src[x, y, 1]
            blue = src[x, y, 0]
            color = [blue, green, red].index(max(red, green, blue))
            if red == 255 and green == 242:
                name = "yellow"
            elif red == 255 and green == 127 and blue == 39:
                name = "orange"
            elif color == 0:
                name = "blue"
            elif color == 1:
                name = "green"
            else:
                name = "red"




            if len(apd) == 4:
                print("4")
                # cv.drawContours(src, [apd], -1, (0, 0, 0), 2)
                print(apd)
                cv.putText(src, name + " rectangle",(apd[1][0]),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) == 3:
                print("3")
                # cv.drawContours(src, [apd], -1, (255, 0, 0), 2)
                print(apd)

                cv.putText(src, name + " triangle", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) == 5:
                print("5")
                print(apd)

                # cv.drawContours(src, [apd], -1, (0, 0, 255), 2)
                cv.putText(src, name + " pentagon", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) == 6:
                print("6")
                print(apd)

                # cv.drawContours(src, [apd], -1, (0, 0, 255), 2)
                cv.putText(src, name + " hexagon", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) > 7:
                print("круг")
                print(apd)

                cv.putText(src, name + " circle", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    return src



# cap = cv.VideoCapture("video.mp4")
#
#
# while True:
#
#     ret, frame = cap.read()
#     cv.imshow('result', figures(frame))
#
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release
cv.imshow('result', figures(frame))
cv.waitKey(0)
# cv.destroyAllWindows()
