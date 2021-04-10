import dlib

if __name__ == "__main__":

    train_xml = "./code_recongphoto/beer-detector/images/train/beer2.xml"
    svm_file = "./code_recongphoto/beer-detector/beer.svm"
    options = dlib.simple_object_detector_training_options()
    options.add_left_right_image_flips = True
    options.C = 5
    options.num_threads = 4
    options.be_verbose = True
    dlib.train_simple_object_detector(train_xml, svm_file, options)
