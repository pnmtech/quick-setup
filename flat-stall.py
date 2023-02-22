import subprocess
while (True):
    print("1: dnf apps")
    print("2: setup base system")
    print("3: flatpak setup")
    print("4: Adw-gtk3 install")
    print("5: flatpak apps")
    print("6: Exit")
    
    ch = int(input("Enter Your Choice : "))
 
    if ch == 1:
       
       rc = subprocess.call("./dnfapps.sh", shell=True)
       
    elif ch == 2:
    
        rc = subprocess.call("./setup-base.sh", shell=True)
        
    elif ch == 3:
    
        rc = subprocess.call("./flatpak-remote.sh", shell=True)
        
    elif ch == 4:
    
        rc = subprocess.call("./adw-gtk3in.sh", shell=True)
        
    elif ch == 5:
        
        rc = subprocess.call("./flatpakapps.sh", shell=True)
        
    elif ch == 6:
        break
    else:
        print("Invalid Choice")
