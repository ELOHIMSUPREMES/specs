%define rname kldap

Name: kde5-%rname
Version: 15.12.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: LDap support library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Aug 11 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-widgets libqt5-xml libsasl2-3 libstdc++-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kcompletion-devel kf5-ki18n-devel kf5-kwidgetsaddons-devel libdb4-devel libldap-devel libsasl2-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: libldap-devel libsasl2-devel
BuildRequires: kf5-kcompletion-devel kf5-ki18n-devel kf5-kwidgetsaddons-devel

%description
%summary.

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

%package -n libkf5ldap
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5ldap
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
#%find_lang %name --with-kde --all-name

#files common -f %name.lang
%files common
#%doc COPYING*

%files devel
%_K5inc/kldap_version.h
%_K5inc/KLDAP/
%_K5link/lib*.so
%_K5lib/cmake/KF5Ldap/
%_K5archdata/mkspecs/modules/qt_Ldap.pri

%files -n libkf5ldap
%_K5lib/libKF5Ldap.so.*

%changelog
* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- initial build
