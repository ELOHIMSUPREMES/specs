%define api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable python
%def_enable dconf
%def_disable gconf
%def_enable wayland
%def_disable emoji_dict

Name: ibus
Version: 1.5.14
Release: alt1

Summary: Intelligent Input Bus for Linux OS
License: LGPLv2+
Group: System/Libraries
Url: https://github.com/ibus/ibus/wiki

Source: https://github.com/%name/%name/releases/download/%version/%name-%version.tar.gz
Source1: ibus-xinput

#Patch: ibus-%version-up.patch

%define gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)
%define gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)

Requires: iso-codes setxkbmap xmodmap
Requires: lib%name = %version-%release
Requires: lib%name-gir = %version-%release

%{?_enable_gconf:Requires(post,preun):GConf}
%{?_enable_dconf:Requires: dconf}

BuildRequires: vala-tools >= 0.18
BuildRequires: python-modules-compiler
BuildRequires: rpm-build-python
BuildPreReq: libgtk+2-devel
BuildPreReq: libgtk+3-devel
BuildRequires: libdbus-devel
BuildRequires: python-module-dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gnome-icon-theme-symbolic
BuildRequires: libXi-devel
BuildRequires: libnotify-devel
%{?_enable_python:BuildRequires: rpm-build-python python-module-pygobject3-devel}
%{?_enable_gconf:BuildRequires: libGConf-devel}
# required if autoreconf used
BuildRequires: libGConf-devel
%{?_enable_dconf:BuildRequires: libdconf-devel /proc dbus-tools-gui dconf}
%{?_enable_wayland:BuildRequires: libwayland-client-devel libxkbcommon-devel}
# gsettings-schema-convert
BuildRequires: GConf
# since 1.5.14
%{?_enable_emoji_dict:BuildRequires: libjson-glib-devel nodejs-emojione-json}

%define _xinputconf %_sysconfdir/X11/xinit/xinput.d/ibus.conf

%description
IBus means Intelligent Input Bus. It is an input framework for Linux OS.

%package -n lib%name
Summary: IBus libraries
Group: System/Libraries
Requires: dbus

%description -n lib%name
This package contains the libraries for IBus

%package -n lib%name-gir
Summary: GObject introspection data for the IBus library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
This package contains typelib file for the IBus library.

%package gtk2
Summary: IBus im module for gtk2
Group: System/Libraries
PreReq: libgtk+2
Requires: lib%name = %version-%release

%description gtk2
This package contains IBus im module for gtk2.

%package gtk3
Summary: IBus im module for gtk3
Group: System/Libraries
PreReq: libgtk+3
Requires: lib%name = %version-%release

%description gtk3
This package contains IBus im module for gtk3.

%package -n lib%name-devel
Summary: Development tools for ibus
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files for IBus library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for IBus
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
This package contains gir files for IBus library.

%package -n lib%name-devel-docs
Summary: Developer documents for IBus
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release
Requires: gtk-doc

%description -n lib%name-devel-docs
This package contains developer documentation for IBus.

%if_enabled python
%package -n python-module-ibus
Summary: IBus im module for python
Group: Development/Python
BuildArch: noarch

%description -n python-module-ibus
This package contains IBus im module for python.

%package -n python-module-ibus-overrides
Summary: IBus Python override library
Group: Development/Python

%description -n python-module-ibus-overrides
This package provides Python override library for IBus. The Python files
override some functions in GObject-Introspection.
%endif

%prep
%setup
#%%patch -p1

%build
%autoreconf
%configure \
    --disable-static \
    --enable-gtk2 \
    --enable-gtk3 \
    --enable-xim \
    --disable-gtk-doc \
    %{?_enable_python:--enable-python-library} \
    %{subst_enable dconf} \
    %{?_enable_dconf:--disable-schemas-compile} \
    %{subst_enable gconf} \
    %{?_enable_gconf:--disable-schemas-install} \
    %{subst_enable wayland} \
    --enable-surrounding-text \
    --enable-introspection \
    %{?_disable_emoji_dict:--disable-emoji-dict}
%make_build

%install
%makeinstall_std

# install xinput config file
install -pm 644 -D %SOURCE1 %buildroot%_xinputconf

%find_lang %{name}10

%check
# FAIL: test-stress
#%%make check

%if_enabled gconf
%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi
%endif

%files -f %{name}10.lang
%dir %_datadir/ibus/
%_bindir/%name
%_bindir/%name-daemon
%_bindir/%name-setup
%_datadir/%name/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_libexecdir/%name-ui-gtk3
%_libexecdir/%name-x11
%_libexecdir/%name-engine-simple
%{?_enable_wayland:%_libexecdir/%name-wayland}

%if_enabled gconf
%_libexecdir/%name-gconf
%_sysconfdir/gconf/schemas/ibus.schemas
%endif

%if_enabled dconf
%dir %_sysconfdir/dconf/db/%name.d
%_sysconfdir/dconf/db/%name.d/00-upstream-settings
%_sysconfdir/dconf/profile/%name
%_libexecdir/%name-dconf
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.freedesktop.%name.gschema.xml
%endif
%_datadir/dbus-1/services/org.freedesktop.IBus.service

%config %_xinputconf
%_man1dir/%name-daemon.1.*
%_man1dir/%name-setup.1.*
%_man1dir/%name.1.*
%doc AUTHORS README

%exclude %_datadir/bash-completion/completions/ibus.bash

%files -n lib%name
%_libdir/lib%name-1.0.so.*

%files -n lib%name-gir
%_typelibdir/IBus-%api_ver.typelib

%files gtk2
%_libdir/gtk-2.0/%gtk2_binary_version/immodules/im-ibus.so

%files gtk3
%_libdir/gtk-3.0/%gtk3_binary_version/immodules/im-ibus.so

%exclude %_libdir/gtk-*.0/*/immodules/*.la

%files -n lib%name-devel
%_libdir/lib*.so
%_pkgconfigdir/*
%_includedir/*
%_datadir/vala/vapi/ibus-1.0.vapi
%_datadir/vala/vapi/ibus-1.0.deps

%files -n lib%name-gir-devel
%_girdir/IBus-%api_ver.gir

%files -n python-module-ibus
%dir %python_sitelibdir_noarch/ibus
%python_sitelibdir_noarch/ibus/*

%files -n lib%name-devel-docs
%_datadir/gtk-doc/html/*

%files -n python-module-ibus-overrides
%python_sitelibdir/gi/overrides/IBus.py*

%changelog
* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.14-alt1
- 1.5.14

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.13-alt1
- 1.5.13

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.12-alt1
- 1.5.12

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.11-alt1
- 1.5.11

* Fri Apr 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.10-alt1
- 1.5.10

* Thu Oct 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.9-alt1
- 1.5.9
- remove upstreamed patches

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- 1.5.7
- updated fc patchset

* Fri Feb 07 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5
- updated fc patchset

* Wed Oct 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4
- updated fc patchset

* Mon Sep 02 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3
- updated fc patchset

* Sun May 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2
- updated fc patchset

* Wed Mar 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt2
- rebuilt for people/gnome

* Wed Mar 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1
- updated fc patchset

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.99.20121006-alt1
- updated to 1.4.99.20121006

* Tue Oct 02 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.99.20120917-alt1
- 1.4.99.20120917

* Thu Jul 19 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Jan 19 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt4
- fixed GConf support, made it optional
- really built with dconf support

* Fri Dec 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3
- gir subpackages separated

* Wed Nov 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2
- lib%name-devel dependences fixed

* Tue Nov 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1
- build for Sisyphus, based on upstream spec

