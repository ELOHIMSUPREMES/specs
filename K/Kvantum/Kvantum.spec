Name: Kvantum
Version: 0.11.1
Release: alt1
Summary: SVG-based theme engine for Qt5, KDE and LXQt

License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/tsujan/Kvantum
Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: https://github.com/tsujan/Kvantum/archive/V%version.tar.gz
Source: %name-%version.tar.gz

BuildRequires: gcc-c++ cmake libX11-devel libXext-devel libqt4-devel qt5-base-devel qt5-tools-devel qt5-svg-devel qt5-x11extras-devel kf5-kwindowsystem-devel desktop-file-utils icon-theme-hicolor
Requires: %name-data

%description
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with extra themes that are installed as root with Qt5
installation and can be selected and activated by using Kvantum Manager.

%package data
Summary: SVG-based theme engine for Qt5, KDE and LXQt
Group: Graphical desktop/Other
BuildArch: noarch

%description data
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

This package contains the data needed Kvantum.

%prep
%setup

%build
%cmake
%make -C BUILD

%install
%cmakeinstall_std

# desktop-file-validate doesn't recognize LXQt
%__subst "s|LXQt|X-LXQt|" %buildroot%_desktopdir/kvantummanager.desktop
desktop-file-validate %buildroot%_desktopdir/kvantummanager.desktop

%find_lang %name --all-name --with-qt

%files
%doc COPYING
%doc ChangeLog NEWS README.md
%_bindir/kvantummanager
%_bindir/kvantumpreview
%_qt5_plugindir/styles/libkvantum.so

%files data -f %name.lang
%_datadir/Kvantum
%_desktopdir/kvantummanager.desktop
%dir %_datadir/color-schemes
%_datadir/color-schemes/Kv*
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/kvantum.svg
%dir %_datadir/kde4
%dir %_datadir/kde4/apps
%dir %_datadir/kde4/apps/color-schemes
%_datadir/kde4/apps/color-schemes/Kv*
%dir %_datadir/themes
%dir %_datadir/themes/Kv*
%_datadir/themes/Kv*/*
%dir %_datadir/kvantumpreview
%dir %_datadir/kvantumpreview/translations
%dir %_datadir/kvantummanager
%dir %_datadir/kvantummanager/translations

%changelog
* Mon May 13 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.1-alt1
- 0.11.1

* Mon Mar 25 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.0-alt1
- New release 0.11.0

* Wed Feb 06 2019 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt3
- 0.10.9 (final release)

* Fri Jan 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt2.gitefca972
- Update from git (commit: efca972)
- Fixed post-install files

* Thu Nov 08 2018 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt1
- New release 0.10.9
- Changed spec for update from git

* Wed Nov 07 2018 Leontiy Volodin <lvol@altlinux.org> 0.10.8-alt1
- Initial release for Sisyphus

