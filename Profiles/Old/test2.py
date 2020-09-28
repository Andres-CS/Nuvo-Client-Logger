#Test profile_mgt.py -> profiles

from pp import profiles
from pp import profile_mngt

def main():
    #obj = profiles()

    #print(obj.get_profiles())

    #print(obj.get_profiles_specs())

    O  = profile_mngt()

    print(O.get_profiles())

main()