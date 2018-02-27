Name: emotion_generic_players
Version: 1.14.0
Release: alt0.1

Summary: A set of players for Emotion
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

Source: http://download.enlightenment.org/releases/%name-%version-beta3.tar.xz

BuildRequires: efl-libs-devel >= 1.11.0 libvlc-devel >= 2.0

%description
These are additional "generic" players for Evas that are stand-alone
executables that Emotion may run from its generic loader module. This means
that if they crash, the application loading the image does not crash
also. In addition the licensing of these binaries will not affect the
license of any application that uses Evas as this uses a completely
generic execution system that allows anything to be plugged in as a
loader.


%prep
%setup -n %name-%version-beta3

%build
%configure
%make_build

%check
%make check

%install
%makeinstall_std

%files
%_libdir/emotion/generic_players/*
%doc AUTHORS COPYING README

%changelog
* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt0.1
- 1.14.0-beta3

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Jan 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus

