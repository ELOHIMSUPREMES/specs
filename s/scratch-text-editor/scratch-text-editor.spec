%global upstreamname scratch

Name: scratch-text-editor
Version: 2.0
Release: alt1

Summary: The text editor that works
License: GPLv3
Group: Editors

Url: https://launchpad.net/scratch

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %upstreamname-%version.tar.gz

Patch0: scratch-drop-spell-plugin.patch

# buildreq fail
BuildRequires: libpng-devel cmake gcc-c++ vala libwebkitgtk3-devel libvte3-devel
BuildRequires: libpixman-devel gobject-introspection-devel libGConf-devel
BuildRequires: libXdmcp-devel libxml2-devel libXdamage-devel libXxf86vm-devel
BuildRequires: libharfbuzz-devel libXinerama-devel libXi-devel libXrender-devel
BuildRequires: libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: libxkbcommon-devel libwayland-cursor-devel at-spi2-atk-devel
BuildRequires: libpeas-devel libgtksourceview3-devel libgee-devel libzeitgeist-devel
BuildRequires: libgranite-devel libgail3-devel libdbus-devel libgranite-vala

%description
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you never
lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible. Keep
things super lightweight and simple, or install extensions to turn Scratch
into a full-blown IDE; it's your choice. And with a handful of useful
preferences, you can tweak the behavior and interface to your liking.

It's elementary. Scratch is made to be the perfect text editor for elementary,
meaning it closely follows the high standards of design, speed, and
consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala, scripting with
PHP, or marking things up in HTML, Scratch has you covered. Experience full
syntax highlighting with nearly all programming, scripting, and markup
languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS, .Desktop,
Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua, Makefile,
Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

%package devel
Summary: Development files for scratch text editor
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for scratch.

%package vala
Summary: Vala language bindings for the scratch text editor
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for the scratch text editor.

%prep
%setup -q -n %upstreamname
%patch0 -p1

%build
%cmake_insource
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang scratch-text-editor

%ifarch x86_64
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif

%files -f scratch-text-editor.lang
%_bindir/*
%_libdir/*.so.*
%_libdir/scratch/
%_datadir/applications/scratch-text-editor.desktop
%_datadir/glib-2.0/schemas/org.pantheon.scratch.gschema.xml
%_datadir/glib-2.0/schemas/org.pantheon.scratch.plugins.folder-manager.gschema.xml
%_datadir/scratch/scratch-ui.xml
%_datadir/scratch/scripts/chardetect.py

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%dir %_libdir/scratch
%_includedir/scratch/scratchcore.h

%files vala
%_datadir/vala/vapi/scratchcore.deps
%_datadir/vala/vapi/scratchcore.vapi

%changelog
* Thu Aug 15 2013 Igor Zubkov <icesik@altlinux.org> 2.0-alt1
- build for Sisyphus

