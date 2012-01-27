# Show files by size, biggest last
ls -lSr

# Show top disk users in current dir. See also dutop
du -s * | sort -k1,1rn | head

# Show free space on mounted filesystems
df -h

# Show free inodes on mounted filesystems
df -i

# Show disks partitions sizes and types (run as root)
fdisk -l

# List all packages by installed size (Bytes) on rpm distros
rpm -q -a --qf '%10{SIZE}\t%{NAME}\n' | sort -k1,1n

# List all packages by installed size (KBytes) on deb distros
dpkg-query -W -f='${Installed-Size;10}\t${Package}\n' | sort -k1,1n