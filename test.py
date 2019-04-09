#!/usr/bin/env python3

#
# Background images courtesy StockSnap.io
# Cheetah - Dave Meier
# Sunset  - Dan Hannibal
#
# All photos on StockSnap fall under the Creative Commons CC0 license.
#

import os
import time

from nxcg import *
from nxcg.colors import COLOR_PRESETS

if __name__ == "__main__":
    start_time = time.time()

    cg = CG()
    if os.path.exists("backgrounds"):
        cg.glyph("backgrounds/cheetah.jpg")

    texts = [
        (480, 150, 600, 7, "Rich in mystery hearts of the stars. Permanence of the stars gathered by gravity a mote of dust suspended in a sunbeam!"),
        (400, 700, 850, 8, "Preserve and cherish that pale blue dot, hearts of the stars something incredible is waiting to be known take root and flourish extraordinary claims require extraordinary evidence."),
        (1200, 200, 600,9, "Something incredible is waiting to be known cosmic fugue, light years, descended from astronomers? Finite but unbounded."),
        ]

    def nx_highlight(text):
        replacer = [
            ["n", "cyan"],
            ["N", "cyan"],
            ["x", "orange"]
        ]
        for key, color in replacer:
            text = text.replace(key, "<span foreground='{}'>{}</span>".format(color, key))
        return text


    for x,y,wi,align,text in texts:

        text = nx_highlight(text)

        w, h = cg.text(text ,
            font="Roboto Light 36",
            color="white",
            width=wi,
            align=align,
            spacing=0,
            render=False
            )

        cg.set_color("black glass 70")
        cg.rect(x-15, y-5, w+30, h+20)

        cg.text_render(x, y)


    y = 0
    for cname in COLOR_PRESETS:
        color = COLOR_PRESETS[cname]
        if len(color) != 7:
            continue
        text = "<span background='{}' foreground='#cccccc'> {} </span><span background='#101010' foreground='{}'> {} </span>".format(color, cname, color, color)
        w, h = cg.text(text ,
            font="Roboto Medium 26",
            pos=(0, y)
            )
        y += h

    cg.draw_hello("everyone")

    cg.save("test.png")
    print ("** Render done in {:.03f} seconds **".format(time.time() - start_time))\

