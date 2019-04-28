import sys

from io import BytesIO

from .common import *
from .colors import *
from .fonts import *
from .plugins import *
from .safe_area import *


def text_escape(s):
    s = str(s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class CGPango(object):
    def __init__(self, parent):
        self.parent = parent
        self.surface = cairo.ImageSurface(
                cairo.FORMAT_ARGB32,
                parent.width,
                parent.height
            )
        self.context = cairo.Context(self.surface)
        self.context.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
        self.layout = PangoCairo.create_layout(
                cairo.Context(self.surface)
            )

    def set_color(self, color):
        self.context.set_source_rgba(*colors(color))

    def set_font(self, font_description):
        font = fonts[font_description]
        self.layout.set_font_description(font)

    def set_line_width(self, width):
        self.context.set_line_width(width)


class CG(object):
    def __init__(self, width=1920, height=1080, **kwargs):
        self.new(width, height)
        plugin_dirs = kwargs.get("plugin_dirs", False)
        self.plugins = PluginLibrary(self, plugin_dirs)
        for plugin in self.plugins:
            if hasattr(plugin, "on_init"):
                plugin.on_init()

    def __nonzero__(self):
        return True

    def new(self, width, height):
        self.width  = int(width)
        self.height = int(height)
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        self.context = cairo.Context(self.surface)
        self.pango = False
        self.safe_vals = {
                "ah" : .35,
                "av" : .35,
                "th" : .1,
                "tv" : .05
            }
        self.safe = SafeArea(self)

    def __getattr__(self, attr):
        for plugin in self.plugins:
            if hasattr(plugin, attr):
                return getattr(plugin, attr)
        raise Exception("No such method: {}".format(attr))

    @property
    def plugin_list(self):
        return self.plugins.plugin_list

    @property
    def colors(self):
        return colors

    @property
    def fonts(self):
        return fonts

    def save(self, file_name):
        with open(file_name, "wb") as image_file:
            self.surface.write_to_png(image_file)

    @property
    def png(self):
        output = BytesIO()
        self.surface.write_to_png(output)
        return output.getvalue()

    def set_color(self, color):
        self.context.set_source_rgba(*colors(color))

    def rect(self, x, y, w, h):
        self.context.rectangle(x, y, w, h)
        self.context.fill()

    def polygon(self, *args, **kwargs):
        first = True
        for x, y in args:
            if first:
                self.context.move_to(x, y)
                first = False
                continue
            self.context.line_to(x, y)
        #TODO: fill, draw... whatever options you can get from kwargs
        self.context.fill()


    def glyph(self, g, x=0, y=0, **kwargs):
        alignment = kwargs.get("alignment", 7)
        if type(g) == str:
            g = cairo.ImageSurface.create_from_png(g)
        elif type(g) != cairo.ImageSurface:
            return
        w, h = g.get_width(), g.get_height()

        if alignment in [4,5,6]:
            y -= int(h/2)
        elif alignment in [1,2,3]:
            y -= h
        if alignment in [8,5,2]:
            x -= int(w/2)
        elif alignment in [9,6,3]:
            x -= w

        self.context.set_source_surface(g, x, y)
        self.context.rectangle(x, y, x + w, y + h)
        self.context.fill()
        return True


    def text(self, text, **kwargs):
        self.pango = CGPango(self)

        if "spacing" in kwargs:
            self.pango.layout.set_spacing(kwargs["spacing"] * Pango.SCALE)

        if "width" in kwargs:
            self.pango.layout.set_wrap(Pango.WrapMode.WORD)
            self.pango.layout.set_width(kwargs["width"] * Pango.SCALE)

        if "align" in kwargs:
            self.pango.layout.set_alignment({
                    7 : Pango.Alignment.LEFT,
                    8 : Pango.Alignment.CENTER,
                    9 : Pango.Alignment.RIGHT
                    }[int(kwargs["align"])]
                )

        if kwargs.get("escape", True):
            text = text_escape(text)

        if Pango.find_base_dir(text, len(text)) == Pango.Direction.RTL:
            text = "<span gravity=\"west\">{}</span>".format(text)

        self.pango.set_line_width(kwargs.get("border", 0))
        self.pango.set_font(kwargs.get("font", "Sans 36"))
        self.pango.set_color(kwargs.get("color", FALLBACK_COLOR))

        self.pango.layout.set_markup(text.strip())
        PangoCairo.update_layout(self.pango.context, self.pango.layout)

        if kwargs.get("render", True):
            self.text_render(*kwargs.get("pos", (0, 0)))

        w, h = self.pango.layout.get_size()
        if "width" in kwargs and kwargs.get("align", "l") != "l":
            w = kwargs["width"] * Pango.SCALE
        return w / Pango.SCALE, h / Pango.SCALE

    def text_render(self, x, y):
        self.pango.context.move_to(0, 50)
        PangoCairo.show_layout(self.pango.context, self.pango.layout)
        self.glyph(self.pango.surface, x, y - 50 )
