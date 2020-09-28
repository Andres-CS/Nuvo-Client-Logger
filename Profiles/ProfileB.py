#Profile Class
import json

#----------------------------------------------------------------------------------------------------------------

'''
Class profiles -> Reads profie file and retrives the json content creating two vars, one for the list of 
                  profiles names a second for the profile specs.
                  It also defines two methods that return the respective var memebers from the class. 
                  The class serves as a base class for other profile classes. 
'''
class profile():
    def __init__(self):
        self.allProfileNames = list()
        self.allProfileSpecs = dict()
    
    def _loadProfiles(self, filePath):
        with open(filePath) as pfs_r:
            p_profiles = json.load(pfs_r)
        pfs_r.close()
        
        #Fill profileName & profileSpecs
        self.allProfileNames = list(p_profiles.keys())
        self.allProfileSpecs = p_profiles
            
    def get_profilesnames(self):
        #Returns a list of string
        return self.allProfileNames

    def get_profilesspecs(self):
        #Returns a Dict
        return self.allProfileSpecs

#----------------------------------------------------------------------------------------------------------------




