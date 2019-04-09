from nxcg.plugin import NXCGPlugin

class Plugin(NXCGPlugin):
    def on_init(self):
        self.cg.colors.update({"plugin red" : "#ff0000"})

    def draw_hello(self, who="world"):
        self.cg.text("<span background='#161616'>Hello {}! I am a plugin</span>".format(who),
            font="TeXGyre Heros CN Bold",
            size=60,
            color="plugin red",
            pos=(500, 50)
            )
