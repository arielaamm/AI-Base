def SubMatrix_g(self, image,filter_size = 2):
    '''
    Generates all possible filter_size x filter_size image regions using valid padding.
    - image is a 2d numpy array.
    '''
    h, w = image.shape

    for i in range(h - filter_size + 1):
        for j in range(w - filter_size + 1):
            im_region = image[i:(i + filter_size), j:(j + filter_size)]
            yield im_region, i, j