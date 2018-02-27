
Name:           bleachbit
Version:        1.6
Release:        alt1

Summary:        Remove unnecessary files, free space, and maintain privacy
License:        GPLv3+
Group:          Archiving/Other
URL:            http://bleachbit.sourceforge.net/

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        http://downloads.sourceforge.net/%name/%name-%version.tar.lzma
BuildArch:      noarch

BuildRequires(pre): rpm-build-gnome python-devel

%add_python_req_skip Windows

%description
BleachBit deletes unnecessary files to free valuable disk space,
maintain privacy, and remove junk. Rid your system of old clutter
including cache, cookies, Internet history, localizations, logs,
temporary files, and broken shortcuts. It wipes clean the cache
and history list of many common programs.

%prep
%setup -q

%build
make -C po local 
%python_build

%install
%makeinstall_std prefix=%_prefix

sed -i -e '/^#!\//, 1d' %buildroot%_datadir/bleachbit/CLI.py
sed -i -e '/^#!\//, 1d' %buildroot%_datadir/bleachbit/GUI.py
rm -f %buildroot%_datadir/%name/Windows.py*

%find_lang %name

%files -f %name.lang
%doc COPYING README
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_pixmapsdir/%name.png

%changelog
* Wed Jan 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- New version

* Tue Sep 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- New version

* Wed Jul 09 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- New version

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- New version

* Mon Nov 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version

* Tue Feb 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt1
- New version 0.9.5

* Fri Sep 07 2012 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- Initial build in Sisyphus (ALT #23106)

