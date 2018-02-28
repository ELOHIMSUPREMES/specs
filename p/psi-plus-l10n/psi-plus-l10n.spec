Name: psi-plus-l10n
Version: 0.16.475.1
Release: alt1

Summary: Translations for Psi+
License: GPLv2
Group: Networking/Instant messaging

Url: http://www.psi-plus.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/psi-plus/%name/archive/%version.tar.gz
Source: %name-%version.tar.gz

BuildArch: noarch

BuildPreReq: libqt4-devel

Requires: psi-plus >= %version

%description
Translations for Psi+

%prep
%setup

%build
lrelease-qt4 translations/*.ts

%install
%__mkdir_p %buildroot%_datadir/psi-plus
%__install -Dp -m 0644 translations/*.qm %buildroot%_datadir/psi-plus

%files
%doc AUTHORS COPYING ChangeLog README
%dir %_datadir/psi-plus
%_datadir/psi-plus/*.qm

%changelog
* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 0.16.475.1-alt1
- Version 0.16.475.1

* Fri Mar 07 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.289-alt0.M70T.1
- Build for branch t7

* Fri Mar 07 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.289-alt1
- Version 0.16.289

* Tue Mar 04 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.287-alt0.M70T.1
- Build for branch t7

* Mon Mar 03 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.287-alt1
- Initial release for ALT Linux
