%define rname signon-kwallet-extension

Name: kde5-%rname
Version: 15.08.1
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: Sign-on KWallet extension
Url: http://www.kde.org
License: GPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Aug 04 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libqt5-x11extras libsignon-extension1 libstdc++-devel libxcbutil-keysyms pkg-config python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kwallet-devel libdb4-devel python-module-google rpm-build-python3 rpm-build-ruby signon-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-kwallet-devel signon-devel

%description
%summary

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
#%find_lang %name --with-kde --all-name

%files
%_libdir/signon/extensions/*kwallet*.so*

%changelog
* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- initial build
