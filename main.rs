use gtk::{glib, Application, ApplicationWindow, Button, HeaderBar, MenuButton, PopoverMenu};
use gtk::prelude::*;
use std::process::Command;
use libadwaita::prelude::{ActionMapExt, GtkWindowExt, ButtonExt};

fn main() {
    const APP_ID: &str = "com.appback.backup";

    // Create a new application
    let app = Application::new(Some(APP_ID), Default::default()).expect("Initialization failed...");

    // Connect to "activate" signal of `app`
    app.connect_activate(build_ui);

    // Run the application
    app.run();
}

// Custom TallButton widget
struct TallButton {
    button: Button,
}

impl TallButton {
    fn new(label_text: &str) -> Self {
        let button = Button::builder()
            .label(label_text)
            .margin_top(12)
            .margin_bottom(12)
            .margin_start(12)
            .margin_end(12)
            .build();

        Self { button }
    }
}

fn build_ui(app: &Application) {
    // Create the main window
    let window = ApplicationWindow::builder()
        .application(app)
        .title("ppback")
        .default_width(500)
        .default_height(200)
        .build();

    // Create header bar
    let header = HeaderBar::new();
    header.set_title("Quick setup");
    window.set_titlebar(Some(&header));

    // Create main vertical box
    let main_box = gtk::Box::new(gtk::Orientation::Horizontal, 10);
    window.set_child(Some(&main_box));

    // Create and populate left vertical box
    let left_box = gtk::Box::new(gtk::Orientation::Vertical, 5);
    main_box.append(&left_box);

    let fedora_button = TallButton::new("Fedora");
    fedora_button.button.connect_clicked(|_| {
        // Create a message dialog for the popup
        let dialog = gtk::MessageDialog::new(
            Some(&window),
            gtk::DialogFlags::MODAL,
            gtk::MessageType::Info,
            gtk::ButtonsType::Close,
            "Popup Dialog",
        );
        dialog.set_secondary_text(Some("This is a popup window!"));

        // Run the dialog
        dialog.run();
        dialog.close(); // Use close instead of destroy
    });
    left_box.append(&fedora_button.button);

    let debian_button = TallButton::new("Debian");
    debian_button.button.connect_clicked(|_| {
    // Create a message dialog for the popup
        let dialog = gtk::MessageDialog::new(
            Some(&window),
            gtk::DialogFlags::MODAL,
            gtk::MessageType::Info,
            gtk::ButtonsType::Close,
            "Popup Dialog",
        );
        dialog.set_secondary_text(Some("This is a popup window!"));

        // Run the dialog
        dialog.run();
        dialog.destroy();
    });
    left_box.append(&debian_button.button);

    let arch_button = TallButton::new("Arch");
    arch_button.button.connect_clicked(|_| {
    // Create a message dialog for the popup
        let dialog = gtk::MessageDialog::new(
            Some(&window),
            gtk::DialogFlags::MODAL,
            gtk::MessageType::Info,
            gtk::ButtonsType::Close,
            "Popup Dialog",
        );
        dialog.set_secondary_text(Some("This is a popup window!"));

        // Run the dialog
        dialog.run();
        dialog.destroy();
    });
    left_box.append(&arch_button.button);


  let ubuntu_button = TallButton::new("Ubuntu");
    ubuntu_button.button.connect_clicked(|_| {
     // Create a message dialog for the popup
        let dialog = gtk::MessageDialog::new(
            Some(&window),
            gtk::DialogFlags::MODAL,
            gtk::MessageType::Info,
            gtk::ButtonsType::Close,
            "Popup Dialog",
        );
        dialog.set_secondary_text(Some("This is a popup window!"));

        // Run the dialog
        dialog.run();
        dialog.destroy();
    });
    left_box.append(&ubuntu_button.button);

  let fpko_button = TallButton::new("flatpaks only");
    fpko_button.button.connect_clicked(|_| {
      // Create a message dialog for the popup
        let dialog = gtk::MessageDialog::new(
            Some(&window),
            gtk::DialogFlags::MODAL,
            gtk::MessageType::Info,
            gtk::ButtonsType::Close,
            "Popup Dialog",
        );
        dialog.set_secondary_text(Some("This is a popup window!"));

        // Run the dialog
        dialog.run();
        dialog.destroy();
    });
    left_box.append(&fpko_button.button);



    // Create menu button and popover
    let popover_menu = PopoverMenu::new();
    let hamburger = MenuButton::new();
    hamburger.set_popover(Some(&popover_menu));
    hamburger.set_icon_name(Some("open-menu-symbolic"));
    header.pack_start(&hamburger);

    // Set app name
    glib::set_application_name("My App");

    // Create an action to run the "show about dialog" function
    let about_action = SignalAction::new("about",);
    about_action.connect_activate(|_, _| show_about_dialog());
    app.add_action(&about_action);

    // Add "About" to the menu
    let menu = gio::Menu::new();
    menu.append("About", "app.about");
    popover_menu.set_menu_model(Some(&menu));

    // Present the window
    window.present();
}

fn show_about_dialog() {
    let dialog = libadwaita::AboutDialog::new();
    dialog.set_application_name("Quick setup");
    dialog.set_version("1.0");
    dialog.set_developer_name("Quick setup");
    dialog.set_license_type(libadwaita::License::Gpl30);
    dialog.set_comments("Adw about Window example");
    dialog.set_website("https://github.com/pnmtech/quick-setup");
    dialog.set_issue_url("https://github.com/pnmtech/quick-setup/issues");
    dialog.add_credit_section("Contributors", &["PNM https://github.com/pnmtech"]);
    dialog.set_copyright("© 2022 developer");
    dialog.set_developers(&["PNM https://github.com/pnmtech"]);
    dialog.set_application_icon_name(Some("battery-level-0-charging-symbolic"));
    dialog.present();
}

