%define rname kdenetwork-filesharing
%define pkg_samba samba

Name: kde5-network-filesharing
Version: 15.12.1
Release: alt2
%K5init

Group: Graphical desktop/KDE
Summary: Fileshare Konqueror Directory Properties Page
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

#Requires: %pkg_samba

Source: %rname-%version.tar
Patch1: alt-allow-guest.patch
Patch2: alt-find-samba.patch

# Automatically added by buildreq on Wed Jan 13 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K5build \
    -DSAMBA_INSTALL=OFF \
    -DSAMBA_PACKAGE_NAME=%pkg_samba \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5plug/*shareplugin.so
%_K5srv/*shareplugin.desktop

%changelog
* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt2
- fix find samba

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
