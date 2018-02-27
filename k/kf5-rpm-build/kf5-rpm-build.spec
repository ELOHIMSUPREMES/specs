
Name: kf5-rpm-build
Version: 5.0.0
Release: alt0.7

Group: Development/KDE and QT
Summary: Development utils for KDE
Url: http://www.altlinux.org
License: GPL

BuildArch: noarch

Source1: macrosd

%description
Set of KF5 RPM macroses.

%package -n rpm-build-kf5
Summary: Set of RPM macros for packaging KF5-based applications
Group: Development/Other
Requires: rpm-build-xdg rpm-macros-qt5 /usr/bin/rpmvercmp
%description -n rpm-build-kf5
Set of RPM macroses for packaging KF5-based applications for ALT Linux.
Install this package if you want to create RPM packages that use KF5.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/kf5

%files -n rpm-build-kf5
%_rpmmacrosdir/kf5

%changelog
* Thu Mar 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.7
- update macroses

* Thu Mar 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.5
- update macroses

* Wed Feb 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.4
- update macroses

* Wed Feb 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.3
- update macroses

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.2
- update paths

* Wed Dec 24 2014 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.1
- initial build
