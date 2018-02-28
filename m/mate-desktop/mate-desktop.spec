Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel libgtk+2-gir-devel libgtk+3-gir-devel pkgconfig(dconf) pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libstartup-notification-1.0) pkgconfig(x11) pkgconfig(xrandr)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-desktop
%define version 1.12.1
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

# Settings used for build from snapshots.
%{!?rel_build:%global commit a6a0a5879533b0915901ab69703eaf327bbca846 }
%{!?rel_build:%global commit_date 20141215}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Summary:        Shared code for mate-panel, mate-session, mate-file-manager, etc
Name:           mate-desktop
License:        GPLv2+ and LGPLv2+ and MIT
Version:        %{branch}.1
%if 0%{?rel_build}
Release:        alt2_1
%else
Release:        alt2_1
%endif
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-desktop.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

Source1:        mate-fedora-f23.gschema.override

BuildRequires:  libdconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mate-common
BuildRequires:  libstartup-notification-devel
BuildRequires:  libunique-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libcairo-gobject-devel

Requires: lib%{name} = %{version}-%{release}
Requires: altlinux-freedesktop-menu-common
Requires: pygtk2
Requires: xdg-user-dirs-gtk
Requires: mate-control-center-filesystem
Requires: mate-panel
Requires: mate-notification-daemon
Requires: mate-user-guide

Obsoletes: libmate
Obsoletes: libmate-devel
Obsoletes: libmatecanvas
Obsoletes: libmatecanvas-devel
Obsoletes: libmatecomponent
Obsoletes: libmatecomponent-devel
Obsoletes: libmatecomponentui
Obsoletes: libmatecomponentui-devel
Obsoletes: libmateui
Obsoletes: libmateui-devel
Obsoletes: mate-conf
Obsoletes: mate-conf-devel
Obsoletes: mate-conf-editor
Obsoletes: mate-conf-gtk
Obsoletes: mate-mime-data
Obsoletes: mate-mime-data-devel
Obsoletes: mate-vfs
Obsoletes: mate-vfs-devel
Obsoletes: mate-vfs-smb
Obsoletes: libmatekeyring
Obsoletes: libmatekeyring-devel
Obsoletes: mate-keyring
Obsoletes: mate-keyring-pam
Obsoletes: mate-keyring-devel
Obsoletes: mate-bluetooth < 1:1.6.0-6
Obsoletes: mate-bluetooth-libs < 1:1.6.0-6
Obsoletes: mate-bluetooth-devel < 1:1.6.0-6
Obsoletes: mate-doc-utils
Obsoletes: mate-character-map
Obsoletes: mate-character-map-devel 
Obsoletes: libmatewnck
Obsoletes: libmatewnck-devel
Obsoletes: mate-dialogs
#Obsoletes: mate-user-share
Source44: import.info
Patch33: mate-desktop-1.12.1-alt-font-settings.patch
Patch34: mate-desktop-1.12.1-alt-default_background_path.patch
Requires:      altlinux-mime-defaults > 0.31


%description
The mate-desktop package contains an internal library
(libmatedesktop) used to implement some portions of the MATE
desktop, and also some data files and other shared components of the
MATE user environment.

%package -n libmate-desktop
Group: System/Libraries
Summary:   Shared libraries for libmate-desktop
License:   LGPLv2+

%description -n libmate-desktop
Shared libraries for libmate-desktop

%package devel
Group: Development/C
Summary:    Libraries and headers for libmate-desktop
License:    LGPLv2+
Requires:   libmate-desktop = %{version}-%{release}

%description devel
Libraries and header files for the MATE-internal private library
libmatedesktop.

%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

# for releases
%patch33 -p0
%patch34 -p0

%build
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%configure                                                 \
     --enable-desktop-docs                                 \
     --disable-schemas-compile                             \
     --with-gtk=2.0                                        \
     --with-x                                              \
     --disable-static                                      \
     --enable-unique                                       \
     --enable-mpaste                                       \
     --with-pnp-ids-path="%{_datadir}/hwdatabase/pnp.ids"      \
     --enable-gtk-doc-html                                 \
     --enable-introspection=yes

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'


desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-about.desktop

desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-color-select.desktop

#install -D -m 0644 %SOURCE1 %{buildroot}%{_datadir}/glib-2.0/schemas/mate-fedora.gschema.override

mkdir -p %{buildroot}%{_datadir}/applications

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/mate-desktop.convert

%find_lang %{name} --with-gnome --all-name

mkdir -p %buildroot%{_datadir}/mate-about

mkdir -p %buildroot%{_datadir}/X11/xorg.conf.d/
ln -sf %{_datadir}/X11/xorg.conf.d/50-synaptics.conf %buildroot%{_datadir}/X11/xorg.conf.d/99-synaptics-mate.conf

%package synaptics
Group: Graphical desktop/MATE
Summary:    Synaptics touchpad support for mate-desktop
Requires:   %name = %version-%release
Requires:   xorg-drv-synaptics
%description synaptics
Synaptics touchpad stops working as MATE starts.
This has to do with libinput, which is going to replace the other input
drivers. As the old synaptics touchpad driver use evdev, we need to give it
a higher priority to be preferred over libinput for your touchpad.

This package contains symlink /usr/share/X11/xorg.conf.d/99-synaptics-mate.conf
that is a hack around this problem.

%files synaptics
%{_datadir}/X11/xorg.conf.d/99-synaptics-mate.conf



%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/mate-about
%{_bindir}/mpaste
%{_bindir}/mate-color-select
%{_datadir}/applications/mate-about.desktop
%{_datadir}/applications/mate-color-select.desktop
%{_datadir}/mate-about
#%{_datadir}/glib-2.0/schemas/mate-fedora.gschema.override
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-symbolic.svg
%{_mandir}/man1/*

%files -n libmate-desktop -f %{name}.lang
%{_libdir}/libmate-desktop-2.so.*
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml
%{_libdir}/girepository-1.0/MateDesktop-2.0.typelib

%files devel
%{_libdir}/libmate-desktop-2.so
%{_libdir}/pkgconfig/mate-desktop-2.0.pc
%{_includedir}/mate-desktop-2.0
%doc %{_datadir}/gtk-doc/html/mate-desktop
%{_datadir}/gir-1.0/MateDesktop-2.0.gir


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2_1
- no need to obsolete mate-user-share

* Tue Dec 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Fri Nov 06 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt3_0
- updated dependencies (added xrandr)
- not yet Obsoletes: mate-user-share
- yet w/o custom gschema.override

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt2_0
- fixed dependencies
- not yet Obsoletes: mate-user-share
- yet w/o custom gschema.override

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_0
- new version
- not yet Obsoletes: mate-dialogs & Obsoletes: mate-user-share

* Tue Mar 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_0
- intermediat build

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_11
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_10
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_6
- new fc release

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- sync with new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.8-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.7-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1_1
- new fc release

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt2_1
- fixed default background

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt2_5
- dropped transaction hack

* Sat Nov 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_5
- added mate-desktop-1.5.0-alt-settings.patch - font settings

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_4
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.1-alt1_5.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_5
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

