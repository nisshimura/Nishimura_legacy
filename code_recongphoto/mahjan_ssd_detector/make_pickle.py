import numpy as np
import os
from xml.etree import ElementTree, ElementInclude
import pickle

class XML_preprocessor(object):

    def __init__(self, data_path):
        self.path_prefix = data_path
        self.num_classes = 34 #クラス数を指定
        self.data = {}
        self._preprocess_XML()

    def _preprocess_XML(self):
        filenames = os.listdir(self.path_prefix)
        
        for filename in filenames:
            tree = ElementTree.parse(self.path_prefix + filename)
            
            root = tree.getroot()

            for image_tree in root.iter('image'):
                file_name = image_tree.attrib['file']
                image_box = []

                for box_tree in image_tree.iter('box'):
                    width = float(box_tree.attrib['width'])
                    height = float(box_tree.attrib['height'])
                    
                    xmin = float(box_tree.attrib['top'])
                    ymin = float(box_tree.attrib['left'])
                    xmax = float(xmin + width)
                    ymax = float(ymin + height)

                    for tag in box_tree.iter('label'):
                        tag_name = tag.text
                        one_hot_class = self._to_one_hot(tag_name)                    
                    
                    image_data = np.asarray([one_hot_class, xmin, ymin, xmax, ymax])
                    image_box.append(image_data)

                self.data[file_name] = image_box      
                print(self.data)

    def _to_one_hot(self,name):
        one_hot_vector = [0] * self.num_classes
        if name == '1wan':
            one_hot_vector[0] = 1
        elif name == '2wan':
            one_hot_vector[1] = 1
        elif name == '3wan':
            one_hot_vector[2] = 1
        elif name == '4wan':
            one_hot_vector[3] = 1
        elif name == '5wan':
            one_hot_vector[4] = 1
        elif name == '6wan':
            one_hot_vector[5] = 1
        elif name == '7wan':
            one_hot_vector[6] = 1
        elif name == '8wan':
            one_hot_vector[7] = 1
        elif name == '9wan':
            one_hot_vector[8] = 1
        elif name == '1pin':
            one_hot_vector[9] = 1
        elif name == '2pin':
            one_hot_vector[10] = 1
        elif name == '3pin':
            one_hot_vector[11] = 1
        elif name == '4pin':
            one_hot_vector[12] = 1
        elif name == '5pin':
            one_hot_vector[13] = 1
        elif name == '6pin':
            one_hot_vector[14] = 1
        elif name == '7pin':
            one_hot_vector[15] = 1
        elif name == '8pin':
            one_hot_vector[16] = 1
        elif name == '9pin':
            one_hot_vector[17] = 1
        elif name == '1sou':
            one_hot_vector[18] = 1
        elif name == '2sou':
            one_hot_vector[19] = 1
        elif name == '3sou':
            one_hot_vector[20] = 1
        elif name == '4sou':
            one_hot_vector[21] = 1
        elif name == '5sou':
            one_hot_vector[22] = 1
        elif name == '6sou':
            one_hot_vector[23] = 1
        elif name == '7sou':
            one_hot_vector[24] = 1
        elif name == '8sou':
            one_hot_vector[25] = 1
        elif name == '9sou':
            one_hot_vector[26] = 1
        elif name == 'ton':
            one_hot_vector[27] = 1
        elif name == 'nan':
            one_hot_vector[28] = 1
        elif name == 'sha':
            one_hot_vector[29] = 1
        elif name == 'pe':
            one_hot_vector[30] = 1
        elif name == 'haku':
            one_hot_vector[31] = 1
        elif name == 'hatsu':
            one_hot_vector[32] = 1
        elif name == 'chun':
            one_hot_vector[33] = 1
        else:
            print('unknown label: %s' %name)

        return one_hot_vector

obj = XML_preprocessor('./code_recongphoto/mahjan_ssd_detector/Anotation/').data
pickle.dump(obj, open('./code_recongphoto/mahjan_ssd_detector/Pickel/mahjongpie.pkl', 'wb'))

            # for i, size_tree in enumerate(root.iter('box')):

            #     print(size_tree.attrib)


            #     bounding_box = [xmin, ymin, xmax, ymax]
            #     bounding_boxes.append(bounding_box)

            #     tag_name = root.iter('label')[i]
            #     file_name = name.attrib['file'][i]

            #     for index in root.iter('image'):
            #         file_name = name.attrib['file']
            #         for obj in index:
            #             tag_name = obj.attrib['file']

            #     tag_name[i]
            #     for i in tag_name:
            #         print()           

            #     for name in root.iter('image'):
            #         file_name = name.attrib['file']
            #         print(file_name)                


                
 #{majhan.jpg:np[]}




