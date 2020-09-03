import os
import array

from nxtools import *

import gi
import cairo

gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')

from gi.repository import Pango, PangoCairo

try:
    import PIL
except ImportError:
    logging.warning("PIL is not available")


def surface2image(surface):
    return PIL.Image.frombuffer(
            "RGBA",
            (surface.get_width(), surface.get_height()),
            surface.get_data(),
            "raw",
            "RGBA",
            0,
            1
        )

def image2surface(image):
    w, h = image.size
    stride = w * 4
    img_bytes = image.tobytes()
    return cairo.ImageSurface.create_for_data(
            array.array('B',img_bytes),
            cairo.FORMAT_ARGB32,
            w, 
            h, 
            stride
        )