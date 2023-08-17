flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.obsproject.Studio -y
flatpak install flathub com.github.tchx84.Flatseal -y
flatpak install flathub com.mattjakeman.ExtensionManager -y
flatpak install flathub com.spotify.Client -y
flatpak install flathub org.blender.Blender -y
flatpak install flathub com.discordapp.Discord -y
flatpak install flathub com.google.Chrome -y
flatpak install flathub com.usebottles.bottles -y
flatpak install flathub org.blender.Blender -y
flatpak install flathub org.gimp.GIMP -y
flatpak install flathub fr.handbrake.ghb -y
flatpak install flathub org.kde.kdenlive -y
sudo dnf install gnome-tweaks -y
sudo dnf install geary -y
sudo dnf install CoreCtrl -y
sudo dnf install solaar -y
sudo dnf install timeshift
sudo sh -c 'echo "fastestmirror=True" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "max_parallel_downloads=10" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "defaultyes=True" >>/etc/dnf/dnf.conf'
