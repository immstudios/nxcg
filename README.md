NXCG
====
This library combines power of PIL (or Pillow), PyCairo and Pango and focuses on
2d graphics for broadcast applications.

## Installation

```bash
apt install -y python3 python3-pip
apt install -y python3-pil python3-cairo gir1.2-gtk-3.0 python3-gi-cairo
pip3 install nxtools
```

## Usage

Hello world
```python

from nxcg import *

cg = CG(1920, 1080)
cg.text("Hello World!", pos=(100,100), color="#cc0000", font="Sans 36")
cg.save("hello.png")
```

## Color presets

| Color | Name |
|-------|------|
| ![#807c8b](https://placehold.it/20/807c8b/000000?text=+) | iron |
| ![#454343](https://placehold.it/20/454343/000000?text=+) | graphite |
| ![#353333](https://placehold.it/20/353333/000000?text=+) | graphite dark |
| ![#536b77](https://placehold.it/20/536b77/000000?text=+) | steel |
| ![#fbb829](https://placehold.it/20/fbb829/000000?text=+) | gold |
| ![#00b4ff](https://placehold.it/20/00b4ff/000000?text=+) | cyan |
| ![#ff6600](https://placehold.it/20/ff6600/000000?text=+) | orange |
| ![#cc0000](https://placehold.it/20/cc0000/000000?text=+) | red |
| ![#a1c820](https://placehold.it/20/a1c820/000000?text=+) | green |
| ![#025d8c](https://placehold.it/20/025d8c/000000?text=+) | blue |
| ![#edde45](https://placehold.it/20/edde45/000000?text=+) | yellow |
| ![#ebebeb](https://placehold.it/20/ebebeb/000000?text=+) | white |
| ![#101010](https://placehold.it/20/101010/000000?text=+) | black |
| ![#000000](https://placehold.it/20/000000/000000?text=+) | black glass 60 |
| ![#000000](https://placehold.it/20/000000/000000?text=+) | black glass 65 |
| ![#000000](https://placehold.it/20/000000/000000?text=+) | black glass 70 |
| ![#000000](https://placehold.it/20/000000/000000?text=+) | black glass 75 |
| ![#000000](https://placehold.it/20/000000/000000?text=+) | black glass 80 |
| ![#f5f5f5](https://placehold.it/20/f5f5f5/000000?text=+) | logo gray |
| ![#ff6d70](https://placehold.it/20/ff6d70/000000?text=+) | living coral |
| ![#654ea3](https://placehold.it/20/654ea3/000000?text=+) | ultra violet |
| ![#84BD00](https://placehold.it/20/84BD00/000000?text=+) | greenery |
| ![#F2DDDE](https://placehold.it/20/F2DDDE/000000?text=+) | rose quartz |
| ![#89ABE3](https://placehold.it/20/89ABE3/000000?text=+) | serenity |
| ![#AD655F](https://placehold.it/20/AD655F/000000?text=+) | marsala |
| ![#B565A7](https://placehold.it/20/B565A7/000000?text=+) | radiant orchid |
| ![#009b77](https://placehold.it/20/009b77/000000?text=+) | emerald |
| ![#dd4124](https://placehold.it/20/dd4124/000000?text=+) | tangerine |
| ![#d65076](https://placehold.it/20/d65076/000000?text=+) | honeysuckle |
| ![#45b8ac](https://placehold.it/20/45b8ac/000000?text=+) | turquoise |
| ![#efc050](https://placehold.it/20/efc050/000000?text=+) | mimosa |
| ![#5b5ea6](https://placehold.it/20/5b5ea6/000000?text=+) | blue iris |
| ![#9b2335](https://placehold.it/20/9b2335/000000?text=+) | pepper |
| ![#dfcfbe](https://placehold.it/20/dfcfbe/000000?text=+) | sand |





## Documentation

Code is quite self-documenting see `nxcg/core.py` for build-ins
and `plugins/test_plugin.py` to see how to write your own plug-ins :-)

See NXTV sources for more advanced usage tips and underlying libraries documentation:

 - http://www.pygtk.org/pygtk2reference/class-pangolayout.html
 - https://developer.gnome.org/pygtk/stable/pango-markup-language.html
