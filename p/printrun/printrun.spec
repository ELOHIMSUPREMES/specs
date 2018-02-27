# prontserve is not yet ready for production
%def_without prontserve

Name:           printrun
Version:        20131019
Release:        alt1
Summary:        RepRap printer interface and tools

License:        GPLv3+
Group:          Engineering
URL:            https://github.com/kliment/Printrun
Packager:	Andrey Cherepanov <cas@altlinux.org>

# Source
Source0:        https://github.com/kliment/Printrun/archive/%name-%version.tar.gz

# Desktop files
Source1:        pronsole.desktop
Source2:        pronterface.desktop
Source3:        plater.desktop

# AppData files
Source4:        pronsole.appdata.xml
Source5:        pronterface.appdata.xml
Source6:        plater.appdata.xml

# Both desktop files and AppData files are already in upstream git as well

# https://github.com/kliment/Printrun/issues/438
Patch0:         %{name}-issue438a.patch
Patch1:         %{name}-issue438b.patch
Patch2:         %{name}-simarrange.patch

#BuildRequires:  Cython
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-Cython
BuildRequires:  python-module-Polygon
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       pronterface = %{version}-%{release}
Requires:       pronsole = %{version}-%{release}
Requires:       plater = %{version}-%{release}

%description
Printrun is a set of G-code sending applications for RepRap.
It consists of printcore (dumb G-code sender), pronsole (featured command line
G-code sender), pronterface (featured G-code sender with graphical user
interface), and a small collection of helpful scripts. Together with skeinforge
they form a pretty powerful softwarecombo. This package installs whole Printrun.

%package        common
Group:          Engineering
Summary:        Common files for Printrun

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

%package     -n pronsole
Summary:        CLI interface for RepRap
Group:          Engineering
Requires:       python-module-serial
Requires:       skeinforge
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

%if_with prontserve
%package     -n prontserve
Summary:        Web interface for RepRap
Group:          Engineering
Requires:       python-module-tornado
Requires:       pronsole = %{version}-%{release}
BuildArch:      noarch

%description -n prontserve
Pronserve is a featured web G-code sender.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.
%endif

%package     -n pronterface
Summary:        GUI interface for RepRap
Group:          Engineering
Requires:       wxPython
Requires:       python-module-cairosvg
Requires:       python-module-pyglet
Requires:       simarrange
Requires:       pronsole = %{version}-%{release}
BuildArch:      noarch

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

%package     -n plater
Summary:        RepRap STL plater
Group:          Engineering
Requires:       wxPython
Requires:       %{name}-common = %{version}-%{release}
Requires:       python-module-pyglet
Requires:       simarrange
BuildArch:      noarch

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.


%prep
%setup -q -n Printrun-%name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

# use launchers for skeinforge
sed -i 's|python skeinforge/skeinforge_application/skeinforge.py|skeinforge|' %{name}/pronsole.py
sed -i 's|python skeinforge/skeinforge_application/skeinforge_utilities/skeinforge_craft.py|skeinforge-craft|' %{name}/pronsole.py

%build
#CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%python_build

# rebuild locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || :
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || :
done
cd ..

%install
#python setup.py install --skip-build --prefix %{buildroot}%{_prefix}
%python_install

# Remove .py extension fron executable files
cd %buildroot%_bindir
for FILE in *.py; do
  mv -f "$FILE" "${FILE%.py}"
done
cd -

# desktop files
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}

# appdata files
mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE4} %{SOURCE5} %{SOURCE6} %{buildroot}%{_datadir}/appdata/

# locales
mkdir -p %{buildroot}%{_datadir}/locale
cp -ar %{buildroot}%{_datadir}/pronterface/locale/* %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{_datadir}/pronterface/locale
ln -s -f %{_datadir}/locale/ %{buildroot}%{_datadir}/pronterface/ # the app expects the locale folder in here

%if_without prontserve
rm -f %buildroot%_bindir/prontserve
rm -f %buildroot%python_sitelibdir/%name/prontserve.py
%endif

%find_lang pronterface
%find_lang plater

%files
%doc README* COPYING

%files common
%doc README* COPYING
%python_sitelibdir/%name
%python_sitelibdir/Printrun-*.egg-info
%_bindir/printcore*
%_pixmapsdir/plater.ico

%files -n pronsole
%doc README* COPYING
%_bindir/pronsole*
%_pixmapsdir/pronsole.ico
%_desktopdir/pronsole.desktop
%_datadir/appdata/pronsole.appdata.xml

%if_with prontserve
%files -n prontserve
%doc README* COPYING
%_bindir/prontserve*
%endif

%files -n pronterface -f pronterface.lang
%doc README* COPYING
%_bindir/pronterface*
%_datadir/pronterface
%_pixmapsdir/P-face.ico
%_desktopdir/pronterface.desktop
%_datadir/appdata/pronterface.appdata.xml

%files -n plater -f plater.lang
%doc README* COPYING
%_bindir/plater*
%_desktopdir/plater.desktop
%_datadir/appdata/plater.appdata.xml

%changelog
* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 20131019-alt1
- Import from Fedora

