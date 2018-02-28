Name: yad
Version: 0.31.2
Release: alt1
Summary: Display graphical dialogs from shell scripts or command line

Group: Graphical desktop/GNOME
License: GPLv3+
Url: http://sourceforge.net/projects/yad-dialog/
Source0: http://downloads.sourceforge.net/%name-dialog/%name-%version.tar.xz
Patch0: fix-missing-buttons.patch

BuildRequires: desktop-file-utils
# Automatically added by buildreq on Fri Oct 10 2014
# optimized out: at-spi2-atk fontconfig glib2-devel libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcloog-isl4 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-cursor libwayland-server perl-Encode perl-XML-Parser pkg-config xorg-xproto-devel xz
BuildRequires: intltool libgtk+3-devel

%description
Yad (yet another dialog) is a fork of zenity with many improvements, such as
custom buttons, additional dialogs, pop-up menu in notification icon and more.

%prep
%setup
%patch0 -p0

%build
%configure \
    --with-gtk=gtk3 \
    --with-rgb=/usr/share/X11/rgb.txt \
    --enable-icon-browser \
    #

%make_build

%install
%makeinstall_std

%find_lang %name

desktop-file-install --remove-key Encoding     \
    --remove-category Development              \
    --add-category    Utility                  \
    --dir=%buildroot%_desktopdir \
    %buildroot%_desktopdir/%name-icon-browser.desktop

%files -f %name.lang
%doc README ChangeLog AUTHORS COPYING NEWS THANKS TODO
%_bindir/*
%_iconsdir/hicolor/*/apps/*
%exclude %_datadir/aclocal/%name.m4
%_man1dir/*
%_desktopdir/*

%changelog
* Wed Oct 21 2015 Fr. Br. George <george@altlinux.ru> 0.31.2-alt1
- Autobuild version bump to 0.31.2

* Fri Oct 10 2014 Fr. Br. George <george@altlinux.ru> 0.27.0-alt1
- Fresh build from FC

* Thu Oct 31 2013 Afanasov Dmitry <ender@altlinux.org> 0.23.1-alt1
- initial build

