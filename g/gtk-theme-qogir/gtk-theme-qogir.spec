Name: gtk-theme-qogir
Version: 20190503
Release: alt1
Summary: Qogir GTK theme

Group: Graphical desktop/GNOME
License: GPL3
Url: https://github.com/vinceliuice/Qogir-theme

Source: %name-%version.tar.gz

BuildArch: noarch
Packager: Leontiy Volodin <lvol@altlinux.org>
BuildRequires: libgtk+3-devel libgtk+2-devel
#Requires: libgtk-engine-murrine

%description
A flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell.
Based on Arc gtk theme

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/themes/Qogir
./Install -d %buildroot%_datadir/themes

%files
%doc AUTHORS COPYING HACKING README.md
%_datadir/themes/Qogir*

%changelog
* Mon May 06 2019 Leontiy Volodin <lvol@altlinux.org> 20190503-alt1
- New version

* Thu Apr 11 2019 Leontiy Volodin <lvol@altlinux.org> 20190407-alt1
- Initial build for ALT Sysiphus

