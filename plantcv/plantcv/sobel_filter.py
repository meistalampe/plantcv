# Sobel filtering

import cv2
import os
from plantcv.plantcv import print_image
from plantcv.plantcv import plot_image
from plantcv.plantcv import params


def sobel_filter(img, dx, dy, k):
    """This is a filtering method used to identify and highlight gradient edges/features using the 1st derivative.
       Typically used to identify gradients along the x-axis (dx = 1, dy = 0) and y-axis (dx = 0, dy = 1) independently.
       Performance is quite similar to Scharr filter. Used to detect edges / changes in pixel intensity. ddepth = -1
       specifies that the dimensions of output image will be the same as the input image.

    Inputs:
    # img    = image
    # dx     = derivative of x to analyze (1-3)
    # dy     = derivative of x to analyze (1-3)
    # k      = specifies the size of the kernel (must be an odd integer: 1,3,5...)

    Returns:
    sb_img   = Sobel filtered image

    :param img: numpy array
    :param dx: int
    :param dy: int
    :param k: int
    :param scale: int
    :return sb_img: numpy array
    """
    params.device += 1
    sb_img = cv2.Sobel(src=img, ddepth=-1, dx=dx, dy=dy, ksize=k)

    if params.debug == 'print':
        name = os.path.join(params.debug_outdir,
                            str(params.device) + '_sb_img_dx' + str(dx) + '_dy' + str(dy) + '_k' + str(k) + '.png')
        print_image(sb_img, name)
    elif params.debug == 'plot':
        plot_image(sb_img, cmap='gray')
    return sb_img
