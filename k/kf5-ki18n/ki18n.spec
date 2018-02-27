%define rname ki18n

Name: kf5-%rname
Version: 5.11.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 gettext-based UI text internationalization
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-fallback.diff

# Automatically added by buildreq on Tue Feb 10 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt5-concurrent libqt5-core libqt5-script libqt5-test libstdc++-devel python-base python-modules qt5-base-devel ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google python-modules-encodings qt5-script-devel rpm-build-gir rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-script-devel python-modules-encodings

%description
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

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

%package -n libkf5i18n
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5i18n
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data locale
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
%dir %_K5i18n/*/
%dir %_K5i18n/*/LC_MESSAGES/
%_K5i18n/*/LC_SCRIPTS/

%files devel
%_K5inc/ki18n_version.h
%_K5inc/KI18n/
%_K5link/lib*.so
%_K5lib/cmake/KF5I18n
%_K5archdata/mkspecs/modules/qt_KI18n.pri

%files -n libkf5i18n
%_K5lib/libKF5I18n.so.*
%_K5plug/kf5/ktranscript.so

%changelog
* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt0.1
- initial build
