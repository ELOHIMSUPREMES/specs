Group: System/Servers
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/glib-genmarshal /usr/bin/glib-gettextize gcc-c++ libICE-devel libgio-devel pkgconfig(dbus-1) pkgconfig(dbus-glib-1) pkgconfig(dconf) pkgconfig(fontconfig) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libmatekbd) pkgconfig(libmatekbdui) pkgconfig(libmatemixer) pkgconfig(libnotify) pkgconfig(libpulse) pkgconfig(libxklavier) pkgconfig(mate-desktop-2.0) pkgconfig(nss) pkgconfig(polkit-gobject-1)
# END SourceDeps(oneline)
BuildRequires: libXext-devel libXi-devel
BuildRequires: mate-common
%define _libexecdir %_prefix/libexec
%define fedora 22
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-settings-daemon
%define version 1.10.2
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.10

# Settings used for build from snapshots.
%{!?rel_build:%global commit 83fe1f587f5c6328b10a899a880275d79bf88921}
%{!?rel_build:%global commit_date 20141215}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-settings-daemon
Version:        %{branch}.2
%if 0%{?rel_build}
Release:        alt2_1
%else
Release:        alt2_0.1%{?git_rel}
%endif
Summary:        MATE Desktop settings daemon
License:        GPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-settings-daemon.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

# http://git.mate-desktop.org/mate-settings-daemon/commit/?id=ed55854
# http://git.mate-desktop.org/mate-settings-daemon/commit/?id=33cb903
Patch0:         mate-settings-daemon_touchpad.patch

BuildRequires:  libdbus-glib-devel
BuildRequires:  libdconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  libmatemixer-devel
BuildRequires:  libcanberra-devel
# needed for f23
%if 0%{?fedora} > 22
BuildRequires: libcanberra-gtk2
%endif
BuildRequires:  libmatekbd-devel
BuildRequires:  libnotify-devel
BuildRequires:  libSM-devel
BuildRequires:  libXxf86misc-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-polkit-devel
BuildRequires:  nss-devel
BuildRequires:  libpulseaudio-devel

Requires:       libmatekbd%{?_isa} >= 0:1.6.1-1
# needed for xrandr capplet
#Requires:       mate-control-center-filesystem
Source44: import.info
Requires: dconf

%description
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%package devel
Group: Development/C
Summary:        Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%patch0 -p1 -b .touchpad

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure                             \
   --enable-pulse                      \
   --disable-static                    \
   --disable-schemas-compile           \
   --enable-polkit                     \
   --with-x                            \
   --with-nssdb                        \
   --with-gtk=2.0

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'

# remove needless gsettings convert file
rm -f %{buildroot}%{_datadir}/MateConf/gsettings/mate-settings-daemon.convert

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%dir %{_sysconfdir}/mate-settings-daemon
%dir %{_sysconfdir}/mate-settings-daemon/xrandr
%config %{_sysconfdir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_sysconfdir}/xrdb/
%{_libdir}/mate-settings-daemon
%{_libexecdir}/mate-settings-daemon
%{_libexecdir}/msd-datetime-mechanism
%{_libexecdir}/msd-locate-pointer
%{_datadir}/mate-control-center/keybindings/50-accessibility.xml
%{_datadir}/dbus-1/services/org.mate.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/icons/mate/*/*/*
%{_datadir}/mate-settings-daemon
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy
%{_mandir}/man1/*

%files devel
%{_includedir}/mate-settings-daemon
%{_libdir}/pkgconfig/mate-settings-daemon.pc


%changelog
* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt0_1.gstreamer
- new fc release

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_0.1.gitd2d3aa7
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_3
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt1_1
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_3
- new fc release

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_2
- new fc release

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_5
- new fc release

* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_4
- added dconf dependency (closes: 28110)

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3_1.1
- Build for Sisyphus
- dep on mate-control-center-filesystem temporary disabled

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- adapted alt patches

* Sun Oct 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- fixed localstatedir in macros

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

