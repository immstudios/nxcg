__all__ = ["glyph"]

import time
import json

from nxcg.common import *

class Glyph():
    def __init__(self):
        self.data = {}

    def __call__(self, name, **kwargs):
        w = kwargs.get("w", False)
        h = kwargs.get("h", False)
        caching = kwargs.get("caching", False)
        key = json.dumps([name, kwargs])
        if caching and key in self.data:
            g, mtime = self.data[key]
            if not os.path.exists(name) or mtime >= os.path.getmtime(name):
                return g
        if os.path.splitext(name)[1].lower() == ".png" and not (w or h):
            g = cairo.ImageSurface.create_from_png(name)
        im = Image.open(name)
        if w or h:
            sw, sh = im.size
            w = w or sw
            h = h or sh
            im = im.resize((w, h), Image.BILINEAR)
        g = pil2cairo(im)
        if caching:
            self.data[key] = g, time.time()
        return g

glyph = Glyph()
