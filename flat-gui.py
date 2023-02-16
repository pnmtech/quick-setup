import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("_Flatpak apps")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Dnf apps")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Setup base system")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)
        
        button = Gtk.Button.new_with_mnemonic("_Flatpak setup")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Adw-gtk3 install")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)
        
        button = Gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)


    def on_click_me_clicked(self, button):
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

    def on_open_clicked(self, button):
        os.system('sudo dnf install gnome-tweaks -y')
        0
        os.system('sudo dnf install geary -y')
        0
        os.system('sudo dnf install CoreCtrl -y')

    def on_close_clicked(self, button):
        os.system('sudo sh setup-dnf.sh')

    def on_open_clicked(self, button):
        os.system('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')

    def on_close_clicked(self, button):
        os.system('sudo dnf copr enable nickavem/adw-gtk3 -y')
        0
        os.system('sudo dnf install adw-gtk3 -y')

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()
        
        
win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
