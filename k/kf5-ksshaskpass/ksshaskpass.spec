%define rname ksshaskpass
%define openssh_askpass_dir %_libexecdir/openssh

Name: kf5-%rname
Version: 5.4.3
Release: alt3
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 front-end for ssh-add
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

PreReq: alternatives >= 0:0.4, %openssh_askpass_dir
Requires: openssh-askpass-common
Provides: openssh-askpass-kf5 = %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Sat Mar 21 2015 (-bi)
# optimized out: alternatives cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel python-module-google qt5-base-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdelibs4support
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel

%description
Ksshaskpass is a front-end for ssh-add which stores the password of the ssh key in KWallet.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5sshaskpass
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5sshaskpass
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

mkdir -p %buildroot/%openssh_askpass_dir/
mv %buildroot/%_K5bin/%rname \
    %buildroot/%openssh_askpass_dir/%name

# setup alternative
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name<<EOF
%openssh_askpass_dir/ssh-askpass        %openssh_askpass_dir/%name        40
EOF

%find_lang %name --all-name

%files -f %name.lang
%doc COPYING*
%_altdir/%name
%openssh_askpass_dir/%name
%_K5xdgapp/org.kde.ksshaskpass.desktop

%changelog
* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
