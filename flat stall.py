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
    print("11) get pika backup")
    print("12) get openrgb")
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
        os.system('flatpak install flathub com.github.GradienceTeam.Gradience')
    elif ch == 11:
        os.system('flatpak install flathub org.gnome.World.PikaBackup')
    elif ch == 12:
        os.system('flatpak install flathub org.openrgb.OpenRGB')
    elif ch == 13:
        os.system('flatpak install flathub com.obsproject.Studio')
        0
        os.system('flatpak install flathub org.openrgb.OpenRGB')
        0
        os.system('flatpak install flathub org.gnome.World.PikaBackup')
        0
        os.system('flatpak install flathub com.github.GradienceTeam.Gradience')
        0    
        os.system('flatpak install flathub com.raggesilver.BlackBox')
        0
        os.system('flatpak install flathub io.github.mimbrero.WhatsAppDesktop')
        0
        os.system('flatpak install flathub com.github.tchx84.Flatseal')
        0
        os.system('flatpak install flathub com.mattjakeman.ExtensionManager')
        0
        os.system('flatpak install flathub com.spotify.Client')
        0
        os.system('flatpak install flathub org.blender.Blender')
        0
        ('flatpak install flathub com.discordapp.Discord')
        0
        os.system('flatpak install flathub com.google.Chrome')
    elif ch == 14:
        break
    else:
        print("Invalid Choice")