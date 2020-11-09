import os
import cv2 as cv
import xml.dom.minidom

path = r'C:\Users\pc\Desktop\tmp\test\xml'    #xml文件夹路径
xmls = os.listdir(path=path)

classes_dir = r'C:\Users\pc\Desktop\tmp\test\characters'  #截取的图片保存路径，类别路径

def f1():
    '''
    1、用labelImg标注原始图片，得到xml文件
    2、解析xml文件，并且在原图中截取需要的部分
    3. 将每个类别的图片分别放入对应的文件夹中。
    :return:
    '''
    for x in xmls:
        print(x)
        if x == 'desktop.ini':
            continue
        xml_dir = os.path.join(path,x)

        # 要解析的xml文件
        DOMTree = xml.dom.minidom.parse(xml_dir)
        collection = DOMTree.documentElement

        #获取图片名称
        filename = collection.getElementsByTagName('filename')[0].childNodes[0].data
        print(filename)

        #获取图片路径
        dir_path = collection.getElementsByTagName('path')[0].childNodes[0].data
        print(dir_path)
        #获取边框objects
        objects = collection.getElementsByTagName('object')
        # 路径中有中文，opencv没法解析，所以转成临时路径
        # name = collection.getElementsByTagName('name')[0].childNodes[0].data
        # dir_path = os.path.join(tmp_path,name,filename)
        # print(dir_path)

        #读取整张图片
        img = cv.imread(dir_path)
        # 可视化
        # cv.imshow('img',img)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        #获取边框数量
        picture_num = len(objects)
        for idx,object in enumerate(objects):
            # 获取类别名name，窗口xmin,ymin,xmax,ymax坐标
            name = object.getElementsByTagName('name')[0].childNodes[0].data
            bndbox = object.getElementsByTagName('bndbox')[0]
            xmin = bndbox.getElementsByTagName('xmin')[0].childNodes[0].data
            ymin = bndbox.getElementsByTagName('ymin')[0].childNodes[0].data
            xmax = bndbox.getElementsByTagName('xmax')[0].childNodes[0].data
            ymax= bndbox.getElementsByTagName('ymax')[0].childNodes[0].data

            xmin,xmax,ymin,ymax=int(xmin),int(xmax),int(ymin),int(ymax)
            box = img[ymin:ymax,xmin:xmax]

            #将图片resize为相同大小
            # box = cv.resize(box, (118, 308))
            # box = np.asarray(box).resize((118,308,3))

            #截取图片保存位置
            picture_name = '{}_{}_{}'.format(picture_num, idx+1, filename)
            class_dir = os.path.join(classes_dir,name)
            #建类别路径文件夹
            if not os.path.exists(class_dir):
                os.makedirs(class_dir)
            picture_save_full_name = os.path.join(class_dir,picture_name)
            # 图片保存
            cv.imwrite(picture_save_full_name,box)

if __name__ == '__main__':
    f1()