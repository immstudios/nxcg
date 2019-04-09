__all__ = ["COLOR_PRESETS", "FALLBACK_COLOR", "colors"]

FALLBACK_COLOR = (.7, .7, .7, 1)

COLOR_PRESETS = {
    "iron"            : "#807c8b",
    "graphite"        : "#454343",
    "graphite dark"   : "#353333",
    "steel"           : "#536b77",
    "gold"            : "#fbb829",
    "cyan"            : "#00b4ff",
    "orange"          : "#ff6600",
    "red"             : "#cc0000",
    "green"           : "#a1c820",
    "blue"            : "#025d8c",
    "yellow"          : "#edde45",

    # tv broadcast related color presets

    "white" : "#ebebeb",
    "black" : "#101010",

    "black glass 60"  : "#00000099",
    "black glass 65"  : "#000000a6",
    "black glass 70"  : "#000000b3",
    "black glass 75"  : "#000000cc",
    "black glass 80"  : "#000000e6",

    "logo gray"       : "#f5f5f5b3",

    # pantone colors of past years

    "living coral"    : "#ff6d70", # Color of the year 2019
    "ultra violet"    : "#654ea3", # Color of the year 2018
    "greenery"        : "#84BD00", # Color of the year 2017
    "rose quartz"     : "#F2DDDE", # Color of the year 2016
    "serenity"        : "#89ABE3", # Color of the year 2016
    "marsala"         : "#AD655F", # Color of the year 2015
    "radiant orchid"  : "#B565A7", # Color of the year 2014
    "emerald"         : "#009b77", # Color of the year 2013
    "tangerine"       : "#dd4124", # Color of the year 2012 (Tangerine tango)
    "honeysuckle"     : "#d65076", # Color of the year 2011
    "turquoise"       : "#45b8ac", # Color of the year 2010
    "mimosa"          : "#efc050", # Color of the year 2009
    "blue iris"       : "#5b5ea6", # Color of the year 2008
    "pepper"          : "#9b2335", # Color of the year 2007
    "sand"            : "#dfcfbe", # Color of the year 2006
    }


def hex_color(hex_string):
    h = hex_string.lstrip("#")
    try:
        r = int(h[0:2], 16) / 255.0
        g = int(h[2:4], 16) / 255.0
        b = int(h[4:6], 16) / 255.0
    except:
        return FALLBACK_COLOR
    try:
        a = int(h[6:8], 16) / 255.0
    except:
        a = 1.0
    return r, g, b, a


class Colors():
    default_color = FALLBACK_COLOR

    def __init__(self):
        self.data = {}
        for k in COLOR_PRESETS:
            self[k] = COLOR_PRESETS[k]

    def __call__(self, key):
        return self[key]

    def __setitem__(self, key, value):
        if type(value) == str and value.startswith("#"):
            self.data[key] = hex_color(value)

    def __getitem__(self, key):
        if type(key) == str:
            key = key.lower()
        if not key in self.data:
            if type(key) == str and key.startswith("#"):
                self.data[key] = hex_color(key)
            else:
                return self.default_color

        return self.data[key]

    def update(self, data):
        for key in data:
            self[key] = data[key]

colors = Colors()
