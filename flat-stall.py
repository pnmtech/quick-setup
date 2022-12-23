import prep
import os
while (True):
    print("1) get chrome")
    print("2) get discord")
    print("3) get blender")
    print("4) get spotify")
    print("5) get extention manager")
    print("6) get flatseal")
    print("7) get obs")
    print("8) get whatsapp")
    print("9) get gradience")
    print("10) get extention manager")
    print("11) flatpak setup")
    print("12) Adw-gtk3 install")
    print("13) want em all")
    print("14) Exit")
    
    ch = int(input("Enter Your Choice : "))
 
    if ch == 1:
        os.system('flatpak install flathub com.google.Chrome')
    elif ch == 2:
        os.system('flatpak install flathub com.discordapp.Discord')
    elif ch == 3:
        os.system('flatpak install flathub org.blender.Blender')
    elif ch == 4:
        os.system('flatpak install flathub com.spotify.Client')
    elif ch == 5:
        os.system('flatpak install flathub com.mattjakeman.ExtensionManager')
    elif ch == 6:
        os.system('flatpak install flathub com.github.tchx84.Flatseal')
    elif ch == 7:
        os.system('flatpak install flathub com.obsproject.Studio')
    elif ch == 8:
        os.system('flatpak install flathub io.github.mimbrero.WhatsAppDesktop')
    elif ch == 8:
        os.system('flatpak install flathub com.raggesilver.BlackBox')
    elif ch == 10:
        os.system('sudo sh -c 'echo "fastestmirror=True" >>/etc/dnf/dnf.conf'')
        0
        os.system('sudo sh -c 'echo "max_parallel_downloads=10" >>/etc/dnf/dnf.conf'')
        0
        os.system('sudo sh -c 'echo "defaultyes=True" >>/etc/dnf/dnf.conf'
    elif ch == 11:
        os.system('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
    elif ch == 12:
        os.system('sudo dnf copr enable nickavem/adw-gtk3')
        0
        os.system('sudo dnf install adw-gtk3')
    elif ch == 13:
        os.system('flatpak install flathub com.obsproject.Studio -y')
        0
        os.system('flatpak install flathub org.openrgb.OpenRGB -y')
        0
        os.system('flatpak install flathub org.gnome.World.PikaBackup -y')
        0
        os.system('flatpak install flathub com.github.GradienceTeam.Gradience -y')
        0    
        os.system('flatpak install flathub com.raggesilver.BlackBox -y')
        0
        os.system('flatpak install flathub io.github.mimbrero.WhatsAppDesktop -y')
        0
        os.system('flatpak install flathub com.github.tchx84.Flatseal -y')
        0
        os.system('flatpak install flathub com.mattjakeman.ExtensionManager -y')
        0
        os.system('flatpak install flathub com.spotify.Client -y')
        0
        os.system('flatpak install flathub org.blender.Blender -y')
        0
        os.system('flatpak install flathub com.discordapp.Discord -y')
        0
        os.system('flatpak install flathub com.google.Chrome -y')
        0
        os.system('flatpak install flathub com.visualstudio.code -y')
        0
        os.system('flatpak install flathub com.usebottles.bottles -y')
    elif ch == 14:
        break
    else:
        print("Invalid Choice")
