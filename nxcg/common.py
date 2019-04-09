import os
import array

import gi
import cairo

gi.require_version('Gtk', '3.0')
gi.require_version('PangoCairo', '1.0')

from gi.repository import Gtk, Pango, PangoCairo

from PIL import Image

from nxtools import *



def pil2cairo(im):
    w, h = im.size
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    s = im.tobytes('raw', 'BGRA')
    a = array.array('B', s)
    dest = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(dest)
    non_premult_src_wo_alpha = cairo.ImageSurface.create_for_data(a, cairo.FORMAT_RGB24, w, h)
    non_premult_src_alpha = cairo.ImageSurface.create_for_data(a, cairo.FORMAT_ARGB32, w, h)
    ctx.set_source_surface(non_premult_src_wo_alpha)
    ctx.mask_surface(non_premult_src_alpha)
    return dest


def cairo2pil(surface):
    assert type(surface) == cairo.ImageSurface
    w = surface.get_width()
    h = surface.get_height()
    return Image.frombuffer("RGBA", (w, h), surface.get_data(), "raw", "BGRA", 0, 1)
