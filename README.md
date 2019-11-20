# Patch Augmentation
*Patch Augmentation* is an novel image augmentation technique designed to improve model generalisation and mitigate against adversarial attacks.

For details, see the following paper: **Patch augmentation: Towards efficient decision boundaries for neural networks**, *arXiv:1911.07922*, Nov. 2019, <https://arxiv.org/abs/1911.07922>

## How it works

*Patch Augmentation* is a data-independent approach that creates new image data based on image/label pairs, where a patch from one of the two images in the pair is superimposed on to the other image, creating a new augmented sample. 

A notebook containing a reproducible experiment (training ResNetv1 using the CIFAR-100 data set) can be found in the following notebook:

[Patch-Augmentation-CIFAR-100.ipynb](Patch-Augmentation-CIFAR-100.ipynb)

In the notebook above, *Patch Augmentation* improves a baseline accuracy of about 45% to over 61%.

## Robustness Against Adversarial Attacks

Initial experiments show networks trained with *Patch Augmentation* are more robust to adversarial attacks, see the following notebook for details:

[Adversarial-Examples.ipynb](Adversarial-Examples.ipynb)

Using the Fast Gradient Sign Method to create adversarial examples, the network trained with *Patch Augmentation* had an accuracy of 72.5% versus 64.3% for the network trained without augmentation.

## Visual Example

Below is a visual example of the technique:

![simple-patch-aug-example](./DemoImages/patch-augmentation-simple-example.png)

In the case of the example above, a 15% area patch from Class B is superimposed on to the image from Class A. Its new label is `y = [0.85, 0.15]`.

## Publication
Publication in review.

Pre-print availble here: **Patch augmentation: Towards efficient decision boundaries for neural networks**, *arXiv:1911.07922*, Nov. 2019, <https://arxiv.org/abs/1911.07922>

Repository made public on the 25th of October 2019.
