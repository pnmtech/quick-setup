#!/usr/bin/sudo bash
sudo sh -c 'echo "fastestmirror=True" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "max_parallel_downloads=10" >>/etc/dnf/dnf.conf'
sudo sh -c 'echo "defaultyes=True" >>/etc/dnf/dnf.conf'
sudo dnf install android-tools
GRUB_CMDLINE_LINUX="mitigations=off"
