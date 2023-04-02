import cv2

image = cv2.imread('cat.jpg')
# изменение изображения с использованием библиотеки cv2(opencv)

# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def viewImage(im, win_name):
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.imshow(win_name, im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop(im, h1, h2, w1, w2):
    return im[h1:h2, w1:w2]


def resize(scale_percent, im):
    width = int(im.shape[1] * scale_percent / 100)
    height = int(im.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(im, dim, interpolation=cv2.INTER_AREA)


def rotation(im):
    (h, w, d) = im.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 160, 1.0)
    return cv2.warpAffine(image, M, (w, h))


def rectangle(im, x1, y1, x2, y2, w):
    img = im.copy()
    return cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), w)


def line(im, x1, y1, x2, y2, w):
    img = im.copy()
    return cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), w)


viewImage(image, 'cat')

cropped = crop(image, 100, 400, 100, 600)
viewImage(cropped, 'cropped cat')
cv2.imwrite('.\Cropped_cat.jpg', cropped)

resized = resize(40, image)
viewImage(resized, 'resized cat')
cv2.imwrite('.\Resized_cat.jpg', resized)

rotated = rotation(image)
cv2.imwrite('.\Rotated_cat.jpg', rotated)
viewImage(rotated, 'rotated cat')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('.\Gray_cat.jpg', gray_image)
viewImage(gray_image, 'gray cat')

blurred = cv2.GaussianBlur(image, (51, 51), 0)
viewImage(blurred, "blurred cat")
cv2.imwrite('.\Blurred_cat.jpg', blurred)

rec = rectangle(image, 300, 100, 600, 300, 5)
viewImage(rec, "rectangle")
cv2.imwrite('.\Rec_cat.jpg', rec)

output = line(image, 60, 20, 400, 200, 5)
viewImage(output, "line")
cv2.imwrite('.\Line_cat.jpg', output)

output2 = image.copy()
cv2.putText(output2, "cat", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 0, 0), 10)
viewImage(output2, 'text')
cv2.imwrite('.\Text_and_cat.jpg', output2)


def binary_im(im, a):
    ret, threshold_image = cv2.threshold(im, a, 255, cv2.THRESH_BINARY)
    return threshold_image


m = 100
for i in range(10):
    path = '.\BinaryIm\cat' + str(i + 1) + '.jpg'
    cv2.imwrite(path, binary_im(image, m))
    m += 10

for i in range(1, 6):
    path ='.\c' + str(i) + '.jpg'
    im = cv2.imread(path)
    res = rotation(im)
