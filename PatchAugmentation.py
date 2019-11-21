# Copyright (c) 2019 Marcus D. Bloice <marcus.bloice@medunigraz.at>
# This file is subject to the terms and conditions defined in
# the file 'LICENSE', which is part of the source code package.
import numpy as np
from keras.utils import Sequence
import math


class PatchAugmentation(Sequence):
    def __init__(self, batch_size, x, y, probability=1.0, min_patch_dimension=0.1, 
                 max_patch_dimension=0.9, image_area=1024):
        self.batch_size = batch_size
        self.x_train = x
        self.y_train = y
        self.probability = probability
        self.image_area = image_area
        self.min_patch_dimension = min_patch_dimension
        self.max_patch_dimension = max_patch_dimension
        
        self.dim = int(round(math.sqrt(self.image_area)))

    def __len__(self):
        return int(np.ceil(len(self.x_train) / float(self.batch_size)))
    
    def __getitem__(self, idx):
        
        batch_x = np.copy(self.x_train[idx * self.batch_size:(idx+1) * self.batch_size])
        batch_y = np.copy(self.y_train[idx * self.batch_size:(idx+1) * self.batch_size])
        
        for i in range(len(batch_x)):
            
            if np.random.uniform(0, 1) <= self.probability:
                
                # Get the minimum width and maximum width of a patch.
                min_width = round(self.min_patch_dimension * self.dim)
                max_width = round(self.max_patch_dimension * self.dim)
                
                # Get the minimum height and maximum height of a patch.
                min_height = round(self.min_patch_dimension * self.dim)
                max_height = round(self.max_patch_dimension * self.dim)
                
                # Get the random patch dimensions, between min/max height and width.
                horizontal_dim = np.random.randint(min_width, max_width+1)
                vertical_dim = np.random.randint(min_height, max_height+1)
                
                # Get a random location from where to extract the patch.
                x1 = np.random.randint(0, self.dim - horizontal_dim)
                y1 = np.random.randint(0, self.dim - vertical_dim)
                x2 = x1 + horizontal_dim
                y2 = y1 + vertical_dim
                 
                # Get random placement coordinates.
                x1p = np.random.randint(0, self.dim - horizontal_dim)
                y1p = np.random.randint(0, self.dim - vertical_dim) 
                x2p = x1p + horizontal_dim
                y2p = y1p + vertical_dim
                
                # Get a random sample from the entire training set.
                r_i = np.random.randint(0, len(self.x_train))
                
                # Place the patch in to the current image in batch.
                # This replaces the current image in the batch with the augmented image.
                batch_x[i][x1p:x2p, y1p:y2p, :] = self.x_train[r_i][x1:x2, y1:y2, :]
                
                # Generate the augmented image's new label.
                # This replaces the current label in the batch with the new label.
                lambda_value = (horizontal_dim * vertical_dim) / (self.dim * self.dim)
                batch_y[i] = (1 - lambda_value) * batch_y[i] + lambda_value * self.y_train[r_i]
            
        return batch_x, batch_y
