import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib 


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        
        self.set_default_size(600, 250)
        self.set_title("Quick setup")
        
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)

        self.button = Gtk.Button(label="Flatpak apps")
        self.box1.append(self.button)
        self.button.connect('clicked', self.Flatpak_apps)
        
        self.button = Gtk.Button(label="Dnf apps")
        self.box1.append(self.button)
        self.button.connect('clicked', self.Dnf_apps)
        
        self.button = Gtk.Button(label="Setup base system(restart is advised)")
        self.box1.append(self.button)
        self.button.connect('clicked', self.Setup_base_system)
        
        self.button = Gtk.Button(label="Flatpak setup")
        self.box1.append(self.button)
        self.button.connect('clicked', self.Flatpak_setup)
        
        self.button = Gtk.Button(label="Adw-gtk3 install")
        self.box1.append(self.button)
        self.button.connect('clicked', self.Adw_gtk3_install)
        
        self.button = Gtk.Button(label="combinde(restart is advised)")
        self.box1.append(self.button)
        self.button.connect('clicked', self.combinde)
        
        self.box1.set_spacing(10)
        self.box1.set_margin_top(10)
        self.box1.set_margin_bottom(10)
        self.box1.set_margin_start(10)
        self.box1.set_margin_end(10)
        
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        
        action = Gio.SimpleAction.new("something", None)
        action.connect("activate", self.print_something)
        self.add_action(action)  # Here the action is being added to the window, but you could add it to the
                                 # application or an "ActionGroup"

        # Create a new menu, containing that action
        menu = Gio.Menu.new()
       
        # Create a popover
        self.popover = Gtk.PopoverMenu()  # Create a new popover menu
        self.popover.set_menu_model(menu)

        # Create a menu button
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")  # Give it a nice icon

        # Add menu button to the header bar
        self.header.pack_start(self.hamburger)
        
        GLib.set_application_name("Quick setup")

        # Create an action to run a *show about dialog* function we will create 
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)
        
        menu.append("About", "win.about")  # Add it to the menu we created in previous section

    def show_about(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)  # Makes the dialog always appear in from of the parent window
        self.about.set_modal(self)  # Makes the parent window unresponsive while dialog is showing

        self.about.set_authors(["PNM"])
        self.about.set_copyright("No Copyright 2023 ")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("http://example.com")
        self.about.set_website_label("https://github.com/pnmtech/quick-setup")
        self.about.set_version("1.0")
        self.about.set_logo_icon_name("/usr/share/icons/Adwaita/scalable/devices/auth-face-symbolic.svg")  # The icon will need to be added to appropriate location
                                                 # E.g. /usr/share/icons/hicolor/scalable/apps/org.example.example.svg

        self.about.show()
        

    def print_something(self, action, param):
        print("Something!")
        
    def Flatpak_apps(self, button):
        os.system('flatpak install flathub com.obsproject.Studio -y')
        0
        os.system('flatpak install flathub org.openrgb.OpenRGB -y')
        0
        os.system('flatpak install flathub org.gnome.World.PikaBackup -y')
        0
        os.system('flatpak install flathub com.github.GradienceTeam.Gradience -y')
        0    
        os.system('flatpak install flathub io.github.shiftey.Desktop -y')
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

        
    def Dnf_apps(self, button):
        os.system('sudo dnf install gnome-tweaks -y')
        0
        os.system('sudo dnf install geary -y')
        0
        os.system('sudo dnf install CoreCtrl -y')

        
    def Setup_base_system(self, button):
        os.system('sudo sh setup-base.sh')
        
    def Flatpak_setup(self, button):
        os.system('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
        
    def Adw_gtk3_install(self, button):
        os.system('sudo dnf copr enable nickavem/adw-gtk3 -y')
        0
        os.system('sudo dnf install adw-gtk3 -y')
        
    def combinde(self, button):
        os.system('sudo sh setup-base.sh')
        0
        os.system('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
        0
        os.system('sudo dnf install gnome-tweaks -y')
        0
        os.system('sudo dnf install geary -y')
        0
        os.system('sudo dnf install CoreCtrl -y')
        0
        os.system('sudo dnf copr enable nickavem/adw-gtk3 -y')
        0
        os.system('sudo dnf install adw-gtk3 -y')
        0
        os.system('flatpak install flathub com.obsproject.Studio -y')
        0
        os.system('flatpak install flathub org.openrgb.OpenRGB -y')
        0
        os.system('flatpak install flathub org.gnome.World.PikaBackup -y')
        0
        os.system('flatpak install flathub com.github.GradienceTeam.Gradience -y')
        0    
        os.system('flatpak install flathub io.github.shiftey.Desktop -y')
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

        
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
