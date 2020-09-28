import json
from pp import profile_mngt

def main():
    with open("paper_profile.json") as PF:
        profile = json.load(PF)
        PF.close()
    
    for k in profile:
        print()
        print(type(profile[k]))
        for i in profile[k]:
            print(i +": "+ str(profile[k][i]))
    
    #Populate a profile
    pf = ["profile_paper","type_paper", "rim_per_carton","sheet_per_rim", "width_paper"]
    pv = list()
    
    for i in pf:
        pv.append(input(i))
    
    #PROFILE MANAGMENT
    x  = profile_mngt()
    print(x.get_profiles())
    ppp = x.create_profile(pf,pv)
    x._save_profile(ppp)
    print(x.get_profiles())
    ppp = input("Select a profile: ")
    print(x.load_profile(ppp))
    ppp = input("Select a profile: ")
    print(x.load_profile(ppp))
    ppp = input("Select a profile: ")
    print(x.load_profile(ppp))
    
    
    
    
        
    

#------------------------------------------------
main()
