__all__ = ["NXCGPlugin"]

class NXCGPlugin(object):
    def __init__(self, parent):
        self.cg = parent
        if hasattr(self, "on_init"):
            self.on_init()
