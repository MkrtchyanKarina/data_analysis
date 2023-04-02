import cv2
import os


def write(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def find_contours_of_cards(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    T, thresh_img = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)  # если значение меньше 150 - оно равно нулю
    # (черный цвет)
    cv2.imshow('1', write(thresh_img, 30))
    cv2.waitKey(0)
    (cnts, _) = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # RETR_EXTERNAL - находим внешние контуры
    # CHAIN_APPROX_SIMPLE - удаляем лишние контуры
    print(cnts)
    return cnts


def find_coordinates_of_cards(cnts, image):
    cards_coordinates = {}
    for i in range(0, len(cnts)):
        x, y, w, h = cv2.boundingRect(cnts[i])  # boundingRect - находим коорединаты левого верхнего угла
        # получившихся контуров
        if w > 50 and h > 50:
            img_crop = image[y - 15:y + h//3 + 15, x - 15:x + w + 15]
            cards_name = find_features(img_crop)
            cards_coordinates[cards_name] = (x - 15, y - 15, x + w + 15, y + h//3 + 15)
    return cards_coordinates


def find_features(img1):
    correct_matches_dct = {}
    directory = 'winx/cards/'
    for image in os.listdir(directory):
        img2 = cv2.imread(directory+image, 0)  # 0=cv2.IMREAD_GRAYSCALE - читываем изображение в оттенках серого
        orb = cv2.ORB_create()  
        kp1, des1 = orb.detectAndCompute(img1, None)  # функция для поиска ключевых точек и дескрипторов
        kp2, des2 = orb.detectAndCompute(img2, None)
        bf = cv2.BFMatcher()  # функция для сопоставления дескрипторов двух изображений
        # (поиска расстояния между их точками)
        matches = bf.knnMatch(des1, des2, k=2)  # поиск k лучших совпадений по матрице ключевых точек 
        # на расстоянии 0,8*distance
        correct_matches = []
        for m, n in matches:
            if m.distance < 0.8*n.distance:
                correct_matches.append([m])
                correct_matches_dct[image.split('.')[0]] = len(correct_matches)
    correct_matches_dct = dict(sorted(correct_matches_dct.items(), key=lambda item: item[1], reverse=True))
    return list(correct_matches_dct.keys())[0]


def draw_rectangle_aroud_cards(cards_coordinates, image):
    for key, value in cards_coordinates.items():
        rec = cv2.rectangle(image, (value[0], value[1]), (value[2], value[3]), (255, 255, 0), 2)  # (x0, y0),(x, y)
        cv2.putText(rec, key, (value[0], value[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 3, (36, 255, 12), 1)
    cv2.imshow('Image', write(image, 50))
    cv2.waitKey(0)


if __name__ == '__main__':
    main_image = cv2.imread('winx/test/test1.JPG')
    gray_main_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    contours = find_contours_of_cards(gray_main_image)
    cards_location = find_coordinates_of_cards(contours, gray_main_image)
    draw_rectangle_aroud_cards(cards_location, main_image)
