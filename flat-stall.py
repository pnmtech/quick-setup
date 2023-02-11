import os
while (True):
    print("1: dnf apps")
    print("2: setup base system(it will disable mitigations)")
    print("3: flatpak setup")
    print("4: Adw-gtk3 install")
    print("5: flatpak apps")
    print("6:s Exit")
    
    ch = int(input("Enter Your Choice : "))
 
    if ch == 1:
        os.system('sudo dnf install gnome-tweaks')
        0
        os.system('sudo dnf install geary')
        0
        os.system('sudo dnf install CoreCtrl')
    elif ch == 2:
        os.system('sudo sh setup-dnf.sh')
        0
        os.system('sudo dnf install zsh')
        0
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    elif ch == 3:
        os.system('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
    elif ch == 4:
        os.system('sudo dnf copr enable nickavem/adw-gtk3 -y')
        0
        os.system('sudo dnf install adw-gtk3 -y')
    elif ch == 5:
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
    elif ch == 6:
        break
    else:
        print("Invalid Choice")
