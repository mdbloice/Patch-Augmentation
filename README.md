# Patch Augmentation
*Patch Augmentation* is an image augmentation technique designed to improve model generalisation and mitigate adversarial attacks.

## How it works

Patch Augmentation is a data-independent approach that creates new image data based on image/label pairs, where a patch from one of the two images in the pair is superimposed on to the other image, creating a new augmented sample. 

A notebook containing a reproducible experiment (using ResNetv1 and ResNetv2 on the CIFAR-10 and CIFAR-100 datasets) can be found in the following notebook:

[Patch-Augmentation.ipynb](Patch-Augmentation.ipynb)

Initial experiments show several percent improvements over baseline accuracies.  

## Visual Example

Below some examples are to appear to highlight its functionality.

## Publication

Repository made public on the 25th of October 2019.
