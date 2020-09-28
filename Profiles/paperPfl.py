import os
import json 
from .ProfileB import profile
#----------------------------------------------------------------------------------------------------------------
'''
class paperPfl (base: profiles) ->  This classes is a child of profiles define in ProfileB file profiles.
                                    It adds a new variable member, paper_configfile, which stores the path
                                    to the paper profiles config file
'''
class paperPfl(profile):
    def __init__(self):
        super().__init__()
        self.paper_configfile = os.path.join(os.path.dirname(__file__),"paper_profile.json")
        
        #Load paper profiles into the App.
        self._loadProfiles(self.paper_configfile)
    
    def get_profileAttr(self, profilename):
        return self.allProfileSpecs[profilename]

        


#----------------------------------------------------------------------------------------------------------------
'''
class paperPfl_mgt (base: paperPfl) -> This classes takes care of any type of modification needed to be made 
                                       to the paper profiles.
                                       It creates, adds, deletes, edits profiles.
                                       This class is child class from teh paperPfl.
'''
class paperPfl_mgt(paperPfl):
    #pass allows me to use the same constructor and methods (as default) from the parent class.
    pass
    '''
    _save_profile() -> Parameter: dictionary obj (such obj was read fromt the json file of paper profiles)
                       Action: It takes a paper profile and concatenates it to the profile specs var, then
                               it writes it to the profile file itself. 
                       Return: Void
    '''
    def _save_profile(self, profile):
        #Add Profile -> Get the Profile Name then get the profile attributes.
        self.allProfileSpecs[list(profile.keys())[0]] =profile[list(profile.keys())[0]]

        #Open and write to Profile file
        with open("paper_profile.json","w") as pfs_w:
            json.dump(self.allProfileSpecs,pfs_w)
    
    def create_profile(self, attributes, values):
        profile =dict()
        #create dic of profile attributes
        counter = 1
        attr = dict()
        
        for a in attributes[1:]:
            attr[a] = values[counter]
            counter += 1

        #create profile
        '''Remeber, the 0th item of "values" is the profile name'''
        profile[values[0]] = attr

        return profile
    
    def load_profile(self, profile_name):
        profile_selected = self.allProfileSpecs[profile_name]
        return profile_selected
    
    def modify_profile(self, profile_name, attributes,values):
        print(self.allProfileSpecs[profile_name])


    

