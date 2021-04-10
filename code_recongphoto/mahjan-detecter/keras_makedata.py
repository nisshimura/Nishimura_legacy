import keras 
import numpy

def make_data(img_dir_list):
    train_data = []
    teach_data = []

    for i, path in enumerate(img_dir_list):
        print(path)
        for picture in list_pictures(path):
            img = img_to_array(load_img(picture, target_size=(64,64)))
            train_data.append(img)
            teach_data.append(i)



if __name__ == "__main__":
    make_data()
    
