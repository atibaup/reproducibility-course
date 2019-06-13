""" Generates vector representations of the provided images using a VGG16 model """

if __name__== '__main__':
    from keras.applications.vgg16 import VGG16
    from keras.preprocessing import image
    from keras.applications.vgg16 import preprocess_input
    import numpy as np
    import pandas as pd
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('examples_path_fn', type=str)
    parser.add_argument('representations_path', type=str)
    parser.add_argument('representations_paths_path', type=str)
    parser.add_argument('max_samples', type=int)

    args = parser.parse_args()

    car_class_to_paths = pd.read_csv(args.examples_path_fn)

    model = VGG16(weights='imagenet', include_top=False, pooling='avg')

    n_images = car_class_to_paths.shape[0]
    features = []
    paths = []
    i = 0
    for (label, label_path) in car_class_to_paths.iterrows():
        label_path = label_path[2]
        try:
            img = image.load_img(label_path, target_size=(224, 224))
        except Exception as ex:
            print('Skipping: {}, error: {}'.format(label_path, str(ex)))
            pass
        else:
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            features.append(model.predict(x))
            paths.append(label_path)
            i += 1
            if i > args.max_samples:
                break
                break

    features_arr = np.concatenate(features, axis=0)
    print('Representations computed for {} images'.format(i))
    np.save(args.representations_path, features_arr)
    np.save(args.representations_paths_path, paths)
