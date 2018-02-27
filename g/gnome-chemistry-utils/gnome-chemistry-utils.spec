%define ver_major 0.14
%define api_ver 0.14
%define _libexecdir %_prefix/libexec
%def_enable mozilla
%def_enable gnumeric
%if_enabled gnumeric
%define goffice_api_ver 0.10
%define gnumeric_api_ver 1.12
%define gnumeric_plugindir %(pkg-config --variable PluginDir libspreadsheet-%gnumeric_api_ver)
%endif

Name: gnome-chemistry-utils
Version: %ver_major.2
Release: alt7

Summary: A set of chemical utilities
Group: Sciences/Chemistry
License: GPLv2+
Url: http://gchemutils.nongnu.org/

Source: http://mirrors.zerg.biz/nongnu/gchemutils/%ver_major/%name-%version.tar.xz
Patch1: %name-0.10.12-alt-mozplugindir.patch

Requires: %name-data = %version-%release bodr chemical-mime-data

BuildRequires: gcc-c++ doxygen docbook-dtds
BuildRequires: gnome-doc-utils gnome-common intltool scrollkeeper man
BuildRequires: libgio-devel libgnomeoffice%goffice_api_ver-devel
%{?_enable_gnumeric:BuildRequires: libspreadsheet-devel}
BuildRequires: libgsf-devel libopenbabel-devel libGLU-devel
BuildRequires: bodr chemical-mime-data
%{?_enable_mozilla:BuildRequires: xulrunner-devel browser-plugins-npapi-devel}

%description
The Gnome chemistry Utils are a collection of libraries and programs for
the GNOME desktop which migh be useful for chemists and science
students.

This package provides.
* A 3D molecular structure viewer (GChem3D).
* A Chemical calculator (GChemCalc).
* A 2D structure editor (GChemPaint).
* A periodic table of the elements application (GChemTable).
* A crystalline structure editor (GCrystal).
* A spectra viewer (GSpectrum).

%package data
Summary: Arch independent files for the Gnome chemistry Utils
Group: Sciences/Chemistry
BuildArch: noarch

%description data
This package provides noarch data needed for the Gnome chemistry Utils to work.

%package -n mozilla-plugin-%name
Summary: Gnome chemistry Utils browser plugin
Group: Sciences/Chemistry
Requires: %name = %version-%release

%description -n mozilla-plugin-%name
This package contains Gnome chemistry Utils plugin for xullrunner-based
browsers.

%package -n gnumeric-plugin-%name
Summary: Gnome chemistry Utils plugin for Gnumeric
Group: Sciences/Chemistry
Requires: %name = %version-%release

%description -n gnumeric-plugin-%name
This package contains Gnome chemistry Utils plugin for Gnumeric
spreadsheet program.

%prep
%setup -q
%patch1 -b .mozplugindir

[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure --disable-update-databases \
           --disable-schemas-compile \
           --disable-scrollkeeper \
           %{?_disable_mozilla:--disable-mozilla-plugin} \
           %{?_enable_mozilla:--with-mozilla-libdir=%browser_plugins_path}
%make_build

%install
%make DESTDIR=%buildroot install

%define apps gchem3d-%api_ver gchemcalc-%api_ver gchempaint-%api_ver gchemtable-%api_ver gcrystal-%api_ver gspectrum-%api_ver

%find_lang --with-gnome --output=%name.lang gchemutils-%api_ver %apps

%files
%_bindir/*
%_libexecdir/babelserver
%_libdir/gchemutils
%_libdir/goffice/*/plugins/gchemutils
%_libdir/libgccv-%api_ver.so.*
%_libdir/libgcp-%api_ver.so.*
%_libdir/libgcu-%api_ver.so.*
%_libdir/libgcrystal-%api_ver.so.*
%_libdir/libgcugtk-%api_ver.so.*
%doc AUTHORS NEWS README TODO

%exclude %_libdir/*.so
%exclude %_datadir/mimelnk/

%files data -f %name.lang
%_datadir/applications/*
%_datadir/gchemutils/
%_datadir/icons/hicolor/*/*/*
%_datadir/mime/packages/gchemutils.xml
%_man1dir/*
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.crystal.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.paint.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.paint.plugins.arrows.gschema.xml

%if_enabled mozilla
%files -n mozilla-plugin-%name
%_libexecdir/chem-viewer
%browser_plugins_path/libmozgcu.so
%exclude %browser_plugins_path/libmozgcu.la
%endif

%if_enabled gnumeric
%files -n gnumeric-plugin-%name
%gnumeric_plugindir/gchemutils/
%exclude %gnumeric_plugindir/gchemutils/*.la
%endif

%changelog
* Tue Oct 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt7
- rebuilt for new gnumeric-1.12.8

* Sun Sep 01 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt6
- rebuilt for new gnumeric-1.12.7

* Wed Aug 28 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt5
- rebuilt for new gnumeric-1.12.6

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt4
- rebuilt for new gnumeric-1.12.5

* Mon Jul 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt3
- rebuilt for new gnumeric-1.12.4

* Sun Jun 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt2
- rebuilt for new gnumeric-1.12.3

* Sat Apr 27 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt2
- rebuilt for new gnumeric-1.12.1
- arch independent data moved to separate subpackage

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.99-alt1
- 0.13.99

* Sun Nov 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.98-alt1
- 0.13.98

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.13-alt1
- 0.12.13

* Wed Jun 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.10-alt2
- used GSettings instead GConf as in libgnomeoffice-0.8.17-alt2

* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 0.12.10-alt1.1
- NMU: rebuilt against current openbabel

* Mon Nov 28 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.10-alt1
- 0.12.10
- updated buildreqs
- new gnumeric-plugin-%%name subpackage

* Thu Aug 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.8-alt1
- 0.12.8

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.12-alt2
- build mozilla-plugin subpackage

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.12-alt1
- first build for Sisyphus


