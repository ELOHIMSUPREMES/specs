%set_automake_version 1.11

%define _name abiword
%define abi_ver 3.0
%define ver_major 3.0
%def_enable spell
%def_with goffice
%def_with champlain
%def_with libical
%def_with eds
%def_with python

Name: %_name-%abi_ver
Version: %ver_major.0
Release: alt7

Summary: Lean and fast full-featured word processor
Group: Office
License: GPL
Url: http://www.abisource.com/

Source: http://www.abisource.com/downloads/abiword/%version/source/%_name-%version.tar.gz
# http://bugzilla.abisource.com/show_bug.cgi?id=13564
Patch: abiword-3.0-up-13564.patch
Patch2: abiword-boost54.patch

#fedora patches
Source11: abiword.mime
Source12: abiword.keys
Source13: abiword.xml

Patch11: abiword-2.8.3-desktop.patch
Patch12: abiword-2.6.0-boolean.patch
Patch13: abiword-3.0.0-fixintrospection.patch
Patch14: abiword-3.0.0-fix-redraw.patch
Patch15: abiword-3.0.0-gnutls-no-libgcrypt.patch
Patch16: abiword-3.0.0-librevenge.patch
Patch17: abiword-3.0.0-libebook.patch
Patch18: abiword-3.0.0-link-grammar-5.patch
Patch19: abiword-3.0.0-link-grammar-5-second.patch

Obsoletes: abisuite, abisuite-koi8, abisuite-cp1251, abisuite-iso8859-8
Conflicts: %_name %_name-light
Requires: %name-data = %version-%release

BuildRequires: gcc-c++ boost-devel asio libreadline-devel flex
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libgsf-gir-devel
BuildRequires: libgtk+3-devel librsvg-devel libfribidi-devel libredland-devel libots-devel
BuildRequires: liblink-grammar-devel libgsf-devel bzlib-devel zlib-devel libjpeg-devel libpng-devel libxslt-devel
BuildRequires: libwv-devel libwpd10-devel libwpg-devel libwmf-devel libexpat-devel
BuildRequires: telepathy-glib-devel libdbus-glib-devel libgnutls-devel libsoup-devel libgcrypt-devel
%{?_enable_spell:BuildRequires: libenchant-devel}
%{?_with_goffice:BuildRequires: libgnomeoffice0.10-devel}
%{?_with_champlain:BuildRequires: libchamplain-gtk3-devel}
%{?_with_libical:BuildRequires: libical-devel}
%{?_with_eds:BuildRequires: evolution-data-server-devel}
%{?_with_python:BuildRequires: python-module-pygobject3-devel python-module-setuptools}

%description
AbiWord is a cross-platform, Open Source Word Processor developed
by the people at AbiSource, Inc. and by developers from around the world.
(http://www.abisource.com)
It is a lean and fast full-featured word processor. It works on Microsoft
Windows and most Unix Systems. Features include:

   * Basic character formatting (bold, underline, italics, etc.)
   * Paragraph alignment
   * Spell-check
   * Import of Word97 and RTF documents
   * Export to RTF, Text, HTML, and LaTeX formats
   * Document Templates
   * Interactive rulers and tabs
   * Styles
   * Unlimited undo/redo
   * Multiple column control
   * Widow/orphan control
   * Find/Replace
   * Images
   and much more...

%package data
Summary: Arch independent files for AbiWord
Group: Office
BuildArch: noarch

%description data
This package provides noarch data needed for AbiWord to work.

%package devel
Group: Development/C++
Summary: Headers for Abiword plugins
Requires: %name = %version-%release

%description devel
Headers and pkgconfig support for  Abiword plugin building.
Conflicts: %_name-devel %_name-light-devel

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the AbiWord

%package -n python-module-%_name
Summary: Python bindings for developing with AbiWord
Group: Development/Python
Requires: %name-gir = %version-%release

%description -n python-module-%_name
Python bindings for developing with AbiWord library

%prep
%setup -n %_name-%version
%patch -p1
%patch2 -p1

# fedora patches
%patch11 -p1 -b .desktop
%patch12 -p1 -b .boolean
%patch13 -p1 -b .introspection
%patch14 -p1 -b .redraw
%patch15 -p1 -b .nogcrypt
%patch16 -p0 -b .librevenge
%patch17 -p1 -b .libebook
%patch18 -p1 -b .link-grammar-5
%patch19 -p1 -b .link-grammar-5-second

%build
find plugins -name Makefile.am | sed  's|.am$||g' > plugin-makefiles.m4
(cd ./plugins && find . -maxdepth 1 -type d | grep -v '^\.$' | grep -v '\./\.' | sed 's|\./||g' | xargs echo) > plugin-list.m4
(for plugin in `cat plugin-list.m4`; do
  u=`echo $plugin | tr '[:lower:]' '[:upper:]'`
  echo 'AM_CONDITIONAL(['$u'_BUILTIN], test "$enable_'$plugin'_builtin" = "yes")'
done) > plugin-builtin.m4
find plugins -name plugin.m4 | xargs cat > plugin-configure.m4
for f in ` find ./plugins -name '*.m4' | grep -v 'plugin\.m4'`; do
    ln -sf $f
done

%autoreconf
%configure \
	--enable-print \
	--enable-plugins \
	--enable-templates \
	--enable-clipart \
	--enable-introspection \
	%{subst_enable spell} \
	%{subst_with goffice} \
	%{subst_with champlain} \
	%{subst_with libical} \
	%{?_without_eds:--without-evolution-data-server} \
	--disable-static

# failed paralell build
%make

%install
%makeinstall_std

install -p -m 0644 -D %SOURCE11 %buildroot%_datadir/mime-info/abiword.mime
install -p -m 0644 -D %SOURCE12 %buildroot%_datadir/mime-info/abiword.keys
install -p -m 0644 -D %SOURCE13 %buildroot%_datadir/mime/packages/abiword.xml

%files
%_bindir/%_name
%_libdir/lib%_name-%ver_major.so
%dir %_libdir/%_name-%ver_major
%dir %_libdir/%_name-%ver_major/plugins
%_libdir/%_name-%ver_major/plugins/*.so
%exclude %_libdir/abiword-%ver_major/plugins/*.la
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
%_datadir/telepathy/clients/AbiCollab.client

%files data
%_desktopdir/%_name.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/%_name-%ver_major/
%_datadir/mime-info/*
%_datadir/mime/packages/*
%_man1dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%files -n python-module-%_name
%python_sitelibdir/gi/overrides/*

%changelog
* Tue Dec 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt7
- updated fedora patches for link-grammar-5 support

* Sun Jun 29 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt6
- new python-module-abiword subpackage (ALT #30134)
- e-d-s support enabled
- built against liblink-grammar.so.5

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt5
- add patches from fedora for porting to librevenge framework

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt4
- updated buildreqs

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt3
- rebuilt against libical.so.1

* Fri Oct 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- fixed http://bugzilla.abisource.com/show_bug.cgi?id=13564

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Nov 29 2012 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- first build for Sisyphus

