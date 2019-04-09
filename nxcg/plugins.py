__all__ = ["PluginLibrary"]

import os
import imp

from .common import *

class PluginLibrary(object):
    def __init__(self, parent, dirs=False):
        dirs = dirs or ["plugins"]
        self.parent = parent
        logging.info("Loading NXCG Plugin library")
        self.plugins = []
        self.plugin_list = []
        for pdir in dirs:
            if os.path.exists(pdir):
                for fname in os.listdir(pdir):
                    self.load_plugin(pdir, fname)
        logging.info("{} plugins loaded".format(len(self.plugins)))

    def load_plugin(self, pdir, fname):
        ppath = os.path.join(pdir, fname)
        mod_name, file_ext = os.path.splitext(fname)
        if file_ext not in [".py", ".pyc"]:
            return

        if file_ext == ".pyc" and os.path.exists(ppath):
            return

        if file_ext == ".pyc":
            py_mod = imp.load_compiled(mod_name, ppath)
        else:
            py_mod = imp.load_source(mod_name, ppath)

        if not "Plugin" in dir(py_mod):
            logging.warning("No plugin class found in {}".format(fname))
        self.plugins.append(py_mod.Plugin(self.parent))
        self.plugin_list.append(ppath)

    def __iter__(self):
        return self.plugins.__iter__()
