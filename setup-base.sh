#!/usr/bin/sudo bash
sudo dnf install zsh -y
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
sudo sh -c 'echo "fastestmirror=True" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "max_parallel_downloads=10" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "defaultyes=True" >>/etc/dnf/dnf.conf'
GRUB_CMDLINE_LINUX="mitigations=off"
