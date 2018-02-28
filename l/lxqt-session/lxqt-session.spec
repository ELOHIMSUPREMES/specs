Name: lxqt-session
Version: 0.10.0
Release: alt1

Summary: Session manager
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source0: %name-%version.tar
Source1: 08lxqt
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libqtxdg-devel xdg-utils

Requires: lxqt-common
Requires: xdg-utils

Provides: razorqt-session = %version
Obsoletes: razorqt-session < 0.7.0

%description
%summary

%prep
%setup

%build
%cmake_insource -DBUNDLE_XDG_UTILS=No
%make_build

%install
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/X11/wmsession.d/08lxqt

%files
%_bindir/*
%_datadir/lxqt/*
%_desktopdir/*.desktop
%_sysconfdir/X11/wmsession.d/08lxqt
%doc AUTHORS

%changelog
* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- replace razorqt-session

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- added wmsession file

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

