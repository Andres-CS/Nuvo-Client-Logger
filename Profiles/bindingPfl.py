#Class for Spiral Binding Profiles

import os
import json
from .ProfileB import profile

class SprBnd(profile):
    def __init__(self):
        #Let base class constructor run as normal
        super().__init__()
        #Get binding config file
        self.spiralbiding_configfile = os.path.join(os.path.dirname(__file__),"SpiralBindingProfiles.json")

        self._loadProfiles(self.spiralbiding_configfile)

    def get_binding_profileAttr(self,bdingprofile):
        return self.allProfileSpecs[bdingprofile]
