Summary: Simple debugging utility
Name: scanmem
Version: 0.15.2
Release: alt1
Url: http://taviso.decsystem.org/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: Development/Debuggers

BuildRequires: libreadline-devel intltool /proc

%description
scanmem is a simple interactive debugging utility for linux, used to
locate the address of a variable in an executing process. This can be
used for the analysis or modification of a hostile process on a
compromised machine, reverse engineering, or as a "pokefinder"
to cheat at video games.

%prep
%setup

%build
./autogen.sh
%configure
%make

%install
install -D -m 755 scanmem %buildroot%_sbindir/scanmem
install -D -m 644 scanmem.1 %buildroot%_man1dir/scanmem.1

%files
%_sbindir/scanmem
%_man1dir/scanmem.1.gz
%doc ChangeLog COPYING NEWS README TODO

%changelog
* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.2-alt1
- New version

* Fri Jun 20 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14-alt1
- New version

* Fri Oct 04 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.13-alt1
- New version

* Sat Mar 02 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.07-alt1
- Initial build

