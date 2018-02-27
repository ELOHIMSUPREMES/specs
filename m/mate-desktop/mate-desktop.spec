Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xrandr)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary:        Shared code for mate-panel, mate-session, mate-file-manager, etc
Name:           mate-desktop
Version:        1.6.0
Release:        alt1_2
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
License:        GPLv2+ and LGPLv2+ and MIT

BuildRequires:  desktop-file-utils
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk-doc
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  libstartup-notification-devel
BuildRequires:  libunique-devel

Requires: lib%{name} = %{version}-%{release}
Requires: altlinux-freedesktop-menu-common
Requires: pygtk2
Requires: xdg-user-dirs-gtk

Obsoletes: libmate 
Obsoletes: libmatecanvas 
Obsoletes: libmatecomponent 
Obsoletes: libmatecomponentui 
Obsoletes: libmatenotify 
Obsoletes: libmateui 
Obsoletes: mate-conf-editor
Obsoletes: mate-conf-gtk
Obsoletes: mate-mime-data
Obsoletes: mate-vfs
Requires:  libnotify
Requires:  mate-panel
Source44: import.info
Patch33: mate-desktop-1.5.0-alt-settings.patch
Patch34: mate-desktop-1.5.5-alt-default_background_path.patch

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
%setup -q
%patch33 -p1
%patch34 -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure \
     --disable-scrollkeeper                                \
     --disable-schemas-compile                             \
     --with-gtk=2.0                                        \
     --with-x                                              \
     --disable-static                                      \
     --enable-unique                                       \
     --enable-gtk-doc                                      \
     --with-pnp-ids-path="%{_datadir}/hwdatabase/pnp.ids"      \
     --with-omf-dir=%{_datadir}/omf/mate-desktop

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'


desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-about.desktop

#install -D -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/xdg/autostart/user-dirs-update-mate.desktop

%find_lang %{name}

mkdir -p %buildroot%{_datadir}/mate-about


%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/mate-about
#%{_sysconfdir}/xdg/autostart/user-dirs-update-mate.desktop
%{_datadir}/applications/mate-about.desktop
%{_datadir}/mate/help/*/*/*.xml
%{_datadir}/omf/mate-desktop/
%{_datadir}/mate-about/
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml
%{_mandir}/man1/mate-about.1*
%{_datadir}/MateConf/gsettings/mate-desktop.convert

%files -n libmate-desktop
%{_libdir}/libmate-desktop-2.so.*

%files devel
%{_datadir}/gtk-doc/html/mate-desktop
%{_libdir}/libmate-desktop-2.so
%{_libdir}/pkgconfig/mate-desktop-2.0.pc
%{_includedir}/mate-desktop-2.0


%changelog
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

