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

## Basic usage

Hello world
```python

from nxcg import *

cg = CG(1920, 1080)
cg.text("Hello World!", pos=(100,100), color="#cc0000", font="Sans 36")
cg.save("hello.png")
```

## Documentation

Code is quite self-documenting see `nxcg/core.py` for build-ins
and `plugins/test_plugin.py` to see how to write your own plug-ins :-)

See NXTV sources for more advanced usage tips and underlying libraries documentation:

 - http://www.pygtk.org/pygtk2reference/class-pangolayout.html
 - https://developer.gnome.org/pygtk/stable/pango-markup-language.html
