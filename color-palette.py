#!/usr/bin/env python3

from nxcg.colors import COLOR_PRESETS


with open("color-palette.md", "w") as f:
    f.write("| Color | Name |\n")
    f.write("|-------|------|\n")
    for color_name in COLOR_PRESETS:

        value = COLOR_PRESETS[color_name][0:7]
        img = "![{}](https://placehold.it/20/{}/000000?text=+)".format(value, value.lstrip("#"))

        f.write("| {} | {} |\n".format(img, color_name))
