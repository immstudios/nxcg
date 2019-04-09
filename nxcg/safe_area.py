__all__ = ["SafeArea"]

class SafeArea(object):
    def __init__(self, parent):
        self.parent = parent

    @property
    def t(self):
        return self("t")

    @property
    def b(self):
        return self("b")

    @property
    def l(self):
        return self("l")

    @property
    def r(self):
        return self("r")

    @property
    def w(self):
        return self.r - self.l

    @property
    def h(self):
        return self.b - self.t

    def __call__(self, side, t="t"):
        if t == "t": #title safe
            ph = self.parent.safe_vals["th"]
            pv = self.parent.safe_vals["tv"]
        else: # action safe
            ph = self.parent.safe_vals["ah"]
            pv = self.parent.safe_vals["av"]
        val = int({
                "t" : self.parent.height * pv,
                "b" : self.parent.height - (self.parent.height * pv),
                "l" : self.parent.width * ph,
                "r" : self.parent.width - (self.parent.width * ph)
            }[side])
        return val
