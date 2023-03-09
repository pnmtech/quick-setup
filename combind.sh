#!/usr/bin/sudo bash
sudo sh -c 'echo "fastestmirror=True" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "max_parallel_downloads=10" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "defaultyes=True" >>/etc/dnf/dnf.conf'
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo dnf install gnome-tweaks -y
sudo dnf install geary -y
sudo dnf install CoreCtrl -y
sudo dnf copr enable nickavem/adw-gtk3 -y
sudo dnf install adw-gtk3 -y
flatpak install flathub com.obsproject.Studio -y
flatpak install flathub org.openrgb.OpenRGB -y
flatpak install flathub org.gnome.World.PikaBackup -y
flatpak install flathub com.github.GradienceTeam.Gradience -y
flatpak install flathub com.raggesilver.BlackBox -y
flatpak install flathub io.github.mimbrero.WhatsAppDesktop -y
flatpak install flathub com.github.tchx84.Flatseal -y
flatpak install flathub com.mattjakeman.ExtensionManager -y
flatpak install flathub com.spotify.Client -y
flatpak install flathub org.blender.Blender -y
flatpak install flathub com.discordapp.Discord -y
flatpak install flathub com.google.Chrome -y
flatpak install flathub com.visualstudio.code -y
flatpak install flathub com.usebottles.bottles -y
sudo dnf install zsh -y
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
chsh -s /bin/zsh
GRUB_CMDLINE_LINUX="mitigations=off"
