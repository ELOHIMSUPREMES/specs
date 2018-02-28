Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgtk+3-gir-devel libpolkit-gir-devel pkgconfig(appindicator-0.1) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-introspection-1.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(polkit-agent-1) pkgconfig(polkit-gobject-1)
# END SourceDeps(oneline)
BuildRequires: libgtk+2-gir-devel
BuildRequires: mate-common
%define _libexecdir %_prefix/libexec
Name:		mate-polkit
Version:	1.10.2
Release:	alt1_1
Summary:	Integrates polkit authentication for MATE desktop
License:	LGPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.10/%name-%version.tar.xz

# needed for gobject-introspection support somehow,
# https://bugzilla.redhat.com/show_bug.cgi?id=847419#c17 asserts this is a bug (elsewhere)
# but I'm not entirely sure -- rex

Provides:	PolicyKit-authentication-agent
Source44: import.info


%description
Integrates polkit with the MATE Desktop environment

%package devel
Group: Development/C
Summary:	Integrates polkit with the MATE Desktop environment

%description devel
Development libraries for mate-polkit

%prep
%setup -q

%build
%configure  \
        --disable-static       \
        --with-gtk=3.0         \
        --enable-introspection \
        --enable-accountsservice \
        --enable-gtk-doc-html


make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

%find_lang %{name}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'


%files -f %{name}.lang
# yes, license really is LGPLv2+, despite included COPYING is about GPL, poke upstreamo
# to include COPYING.LIB here instead  -- rex
%doc AUTHORS COPYING README
%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libdir}/libpolkit-gtk-mate-1.so.0
%{_libdir}/libpolkit-gtk-mate-1.so.0.0.0
%{_libdir}/girepository-1.0/PolkitGtkMate-1.0.typelib
%{_libexecdir}/polkit-mate-authentication-agent-1

%files devel
%{_libdir}/libpolkit-gtk-mate-1.so
%{_libdir}/pkgconfig/polkit-gtk-mate-1.pc
%{_includedir}/polkit-gtk-mate-1
%{_datadir}/gir-1.0/PolkitGtkMate-1.0.gir


%changelog
* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

