Group: Toys
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto libICE-devel libSM-devel libgio-devel libpam0-devel pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libsystemd-login)
# END SourceDeps(oneline)
BuildRequires: libsystemd-login-devel
%define _libexecdir %_prefix/libexec
%define fedora 21
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-screensaver
%define version 1.8.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.8

# Settings used for build from snapshots.
%{!?rel_build:%global commit d5b35083e4de1d7457ebd937172bb0054e1fa089}
%{!?rel_build:%global commit_date 20140125}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-screensaver
Version:        %{branch}.0
Release:        alt1_1
#Release:        0.1%{?git_rel}%{?dist}
Summary:        MATE Screensaver
License:        GPLv2+ and LGPLv2+
URL:            http://pub.mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-screensaver.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

Requires:       altlinux-freedesktop-menu-common

# switch to gnome-keyring > f19
%if 0%{?fedora} > 19
Requires:       pam_gnome-keyring
%else
Requires:       mate-keyring-pam
%endif

BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXxf86misc-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libnotify-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-menus-devel
BuildRequires:  libGL-devel
BuildRequires:  pam-devel
BuildRequires:  systemd-devel
BuildRequires: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-evieproto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-pmproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcbproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86rushproto-devel xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel
BuildRequires:  xmlto
Source44: import.info
Patch33: mate-screensaver-1.8.0-alt-pam.patch
Source45: unix2_chkpwd.c

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.


%package devel
Group: Toys
Summary: Development files for mate-screensaver
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-screensaver


%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}
%patch33 -p1

# needed for git snapshots
#NOCONFIGURE=1 ./autogen.sh

%build
%configure                          \
            --with-x                \
            --with-gtk=2.0          \
            --disable-schemas-compile \
            --enable-docbook-docs   \
            --with-mit-ext          \
            --with-xf86gamma-ext    \
            --with-libgl            \
            --with-shadow           \
            --enable-authentication-scheme=helper \
           --with-passwd-helper=%_libexecdir/%name/%name-chkpwd-helper \
	   --enable-locking        \
            --with-systemd          \
            

make %{?_smp_mflags} V=1
gcc -o %name-chkpwd-helper $RPM_OPT_FLAGS %SOURCE45 -lpam


%install
%{makeinstall_std}

desktop-file-install --delete-original             \
  --dir %{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mate-screensaver-preferences.desktop

desktop-file-install                                          \
   --delete-original                                          \
   --dir %{buildroot}%{_datadir}/applications/screensavers    \
%{buildroot}%{_datadir}/applications/screensavers/*.desktop

# remove needless gsetting convert file
rm -f %{buildroot}%{_datadir}/MateConf/gsettings/org.mate.screensaver.gschema.migrate

# fix versioned doc dir
mkdir -p %{buildroot}%{_datadir}/doc/mate-screensaver
mv %{buildroot}%{_datadir}/doc/mate-screensaver-%{version}/mate-screensaver.html %{buildroot}%{_datadir}/doc/mate-screensaver/mate-screensaver.html

%find_lang %{name} --with-gnome --all-name
install -m 755 %name-chkpwd-helper %buildroot%_libexecdir/%name/

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/mate-screensaver*
%{_sysconfdir}/pam.d/mate-screensaver
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%{_libexecdir}/mate-screensaver-*
%{_libexecdir}/mate-screensaver/
%{_datadir}/applications/mate-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/*.desktop
%{_datadir}/mate-screensaver/
%{_datadir}/backgrounds/cosmos/
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/pixmaps/gnome-logo-white.svg
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_mandir}/man1/*
%attr(2511,root,chkpwd) %_libexecdir/%name/%name-chkpwd-helper

%files devel
%{_libdir}/pkgconfig/*


%changelog
* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2_1
- new fc release

* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- password check fixed: use setgid helper

* Sun Apr 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt3_3
- new fc release

* Tue Feb 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt3_2
- dropped obsolete dependencies

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_2
- new fc release

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_1
- bugfix release (closes: 28151)

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new version; updated ru translation

* Sat Nov 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- dropped gdialog compat script (conflicts with real gdialog)

* Tue Oct 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3
- chkpwd usage and rights fixed

* Mon Oct 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Tue Aug 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

