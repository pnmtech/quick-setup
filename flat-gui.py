import sys
import gi
import subprocess
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

        
                # Set app name
        GLib.set_application_name("My App")

        # Create an action to run a *show about dialog* function we will create 
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)
        
        menu.append("About", "win.about")  # Add it to the menu we created in previous section


    def show_about(self, action, param):

        dialog = Adw.AboutWindow(transient_for=app.get_active_window()) 
        dialog.set_application_name=("Quick setup") 
        dialog.set_version("1.0")
        dialog.set_developer_name("Quick setup")
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0))
        dialog.set_comments("Adw about Window example")
        dialog.set_website("https://github.com/pnmtech/quick-setup")
        dialog.set_issue_url("https://github.com/pnmtech/quick-setup/issues")
        dialog.add_credit_section("Contributors", ["PNM https://github.com/pnmtech"])
        dialog.set_copyright("© 2022 developer")
        dialog.set_developers(["PNM https://github.com/pnmtech"])
        dialog.set_application_icon("battery-level-0-charging-symbolic")# icon must be uploaded in ~/.local/share/icons or /usr/share/icons
        dialog.present()
        
    def Flatpak_apps(self, button):
    
        rc = subprocess.call("./flatpakapps.sh", shell=True)
 
    def Dnf_apps(self, button):
    
        rc = subprocess.call("./dnfapps.sh", shell=True)
        
    def Setup_base_system(self, button):
    
        rc = subprocess.call("./setup-base.sh", shell=True)
        
    def Flatpak_setup(self, button):
    
        rc = subprocess.call("./flatpak-remote.sh", shell=True)
        
    def Adw_gtk3_install(self, button):
    
        rc = subprocess.call("./adw-gtk3in.sh", shell=True)
        
    def combinde(self, button):
    
        rc = subprocess.call("./combind.sh", shell=True)
  
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id=("com.example.GtkApplication"))
app.run(sys.argv)
