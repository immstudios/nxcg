#!/usr/bin/env python3
"""

This script creates a markdown table with a preview of all color presets available.
Resulting table is a part of README.md

"""

from nxcg.colors import COLOR_PRESETS

COLUMNS = 4

with open("color-palette.md", "w") as f:
    data = list(COLOR_PRESETS.keys())
    f.write("|" + "|".join([" Color | Name "]*COLUMNS) + "|\n")
    f.write("|" + "|".join(["-------|------"]*COLUMNS) + "|\n")

    while True:
        d = []
        for i in range(COLUMNS):
            try:
                d.append(data.pop(0))
            except IndexError:
                d.append(False)
        if not any(d):
            break
        f.write("|" + "|".join([" ![{}](https://placehold.it/20/{}/000000?text=+) | {} ".format(COLOR_PRESETS[key], COLOR_PRESETS[key][0:7].lstrip("#") , key) for key in d if key]) + "|\n")
