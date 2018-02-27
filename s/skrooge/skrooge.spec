Name: 		skrooge
Version: 	1.8.0
Release: 	alt2
License: 	%gpl2plus
Summary: 	Personal finances manager for KDE4
Group: 		Office
URL: 		http://skrooge.org/
Packager: 	Andrey Cherepanov <cas@altlinux.org> 

Source: 	%name-%version.tar.bz2

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libofx-devel
BuildRequires: libqca2-devel
BuildRequires: libsqlite3-devel
BuildRequires: kde4sdk-scripts
BuildRequires: libqt4-sql-sqlite >= 4.7.0
BuildRequires: libsqlite-devel
BuildRequires: grantlee-devel
BuildRequires: kde4pimlibs-devel
BuildRequires: kde4-nepomuk-core-devel
BuildRequires: qjson-devel
BuildRequires: xsltproc

%description
Skrooge is a personal finances manager for KDE4, aiming at being simple
and intuitive.

%prep
%setup

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS CHANGELOG COPYING README TODO
%_K4bindir/*
%_K4apps/*
%_K4cfg/*
%_K4conf/*.knsrc
%_K4srv/*
%_K4srvtyp/*
%_K4libdir/libskg*
%_K4lib/skrooge_*
%_K4lib/*.so
%_iconsdir/hicolor/*/*/*
%_K4xdg_mime/*
%_K4xdg_apps/*
%_K4doc/pt_BR/%name/*
%_datadir/akonadi/agents/skroogeakonadiresource.desktop
%_K4plug/grantlee/*/grantlee_skgfilters.so
%_K4link/*.so

%changelog
* Thu Apr 03 2014 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt2
- Rebuild with new version of grantlee

* Sun Nov 24 2013 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version
- Build with libofx-0.9.9

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version 1.7.1

* Tue Jan 22 2013 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version 1.4.0

* Wed Jan 18 2012 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- Add watch file

* Fri Sep 23 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- New version 0.9.1

* Tue Mar 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version 0.8.0
- Return to Sisyphus

* Sat Nov 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.5.3-alt1
- initial build for Sisyphus
