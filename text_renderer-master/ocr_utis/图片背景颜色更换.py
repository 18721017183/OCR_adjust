import cv2
import numpy as np
import os

def f2():
    dir_path = r'C:\Users\pc\Desktop\tmp\test\characters\9'
    save_dir_path = r'C:\Users\pc\Desktop\tmp\test\thresh\9'
    if not os.path.exists(save_dir_path):
        os.makedirs(save_dir_path)
    image_names = os.listdir(dir_path)
    for image_name in image_names:
        print(image_name)
        # b31. 构建图像的路径
        image_path = os.path.join(dir_path, image_name)
        img = cv2.imread(image_path)
        # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv = img
        # lower_blue=np.array([90,70,70])
        # upper_blue=np.array([110,255,255])
        image = np.asarray(hsv)  # (422, 903, 3)
        lower_blue = np.array([90, 90, 90])
        upper_blue = np.array([255, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # cv2.imshow('Mask', mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        rows, cols, channels = img.shape
        for i in range(rows):
            for j in range(cols):
                if mask[i, j] == 255:
                    img[i, j] = (255, 255, 255)  # 此处替换颜色，为BGR通道

        save_image_name = os.path.join(save_dir_path,image_name)
        cv2.imwrite(save_image_name, img)
        # cv2.imshow('res', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

def f3():
    dir_path = r'C:\Users\pc\Desktop\tmp\test\characters'
    save_dir_path = r'C:\Users\pc\Desktop\tmp\test\thresh'
    list_dir_paths = os.listdir(dir_path)
    for character_dir in list_dir_paths:
        full_dir_path = os.path.join(dir_path,character_dir)
        full_save_dir_path = os.path.join(save_dir_path,character_dir)

        if not os.path.exists(full_save_dir_path):
            os.makedirs(full_save_dir_path)
        image_names = os.listdir(full_dir_path)
        for image_name in image_names:
            print(image_name)
            # b31. 构建图像的路径
            image_path = os.path.join(full_dir_path, image_name)
            img = cv2.imread(image_path)
            # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hsv = img
            # lower_blue=np.array([90,70,70])
            # upper_blue=np.array([110,255,255])
            #image = np.asarray(hsv)  # (422, 903, 3)
            lower_blue = np.array([90, 90, 90])
            upper_blue = np.array([255, 255, 255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            # cv2.imshow('Mask', mask)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            rows, cols, channels = img.shape
            for i in range(rows):
                for j in range(cols):
                    if mask[i, j] == 255:
                        img[i, j] = (255, 255, 255)  # 此处替换颜色，为BGR通道

            save_image_name = os.path.join(full_save_dir_path,image_name)
            cv2.imwrite(save_image_name, img)
            # cv2.imshow('res', img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

if __name__ == '__main__':
    # f2()
    f3()