Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize libSM-devel libgio-devel libgtk+2-gir-devel libgtk+3-gir-devel pkgconfig(gdk-2.0) pkgconfig(gdk-3.0) pkgconfig(gdk-x11-2.0) pkgconfig(gdk-x11-3.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libxklavier)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libmatekbd
%define version 1.12.1
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

# Settings used for build from snapshots.
%{!?rel_build:%global commit 5e8b69cf7c6d031cbb0b0f01a7518e72146c0af1}
%{!?rel_build:%global commit_date 20151009}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           libmatekbd
Version:        %{branch}.1
Release:        alt2_1
Summary:        Libraries for mate kbd
License:        LGPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R libmatekbd.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  desktop-file-utils
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk2-devel
BuildRequires:  libICE-devel
BuildRequires:  libxklavier-devel
BuildRequires:  mate-common
BuildRequires:  gobject-introspection-devel
Source44: import.info
Requires: iso-codes

%description
Libraries for matekbd

%package devel
Group: Development/C
Summary:  Development libraries for libmatekbd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for libmatekbd

%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
autoreconf -fisv

%configure                   \
   --disable-static          \
   --with-gtk=2.0            \
   --disable-schemas-compile \
   --with-x                  \
   --enable-introspection=yes
  
make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/matekbd.convert

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/libmatekbd
%{_datadir}/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml
%{_libdir}/libmatekbd.so.4*
%{_libdir}/libmatekbdui.so.4*
%{_libdir}/girepository-1.0/Matekbd-1.0.typelib

%files devel
%{_datadir}/gir-1.0/Matekbd-1.0.gir
%{_includedir}/libmatekbd
%{_libdir}/pkgconfig/libmatekbd.pc
%{_libdir}/pkgconfig/libmatekbdui.pc
%{_libdir}/libmatekbdui.so
%{_libdir}/libmatekbd.so

%changelog
* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2_1
- moved gir to devel (closes: #31926)

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new fc release

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- new fc release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Tue Nov 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- added Requires: iso-codes

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

