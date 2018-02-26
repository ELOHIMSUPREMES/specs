Group: Toys
# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel libpam0-devel pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
BuildRequires: libsystemd-login-devel
%define _libexecdir %_prefix/libexec
%define fedora 18
Name:           mate-screensaver
Version:        1.5.1
Release:        alt3_2
Summary:        MATE Screensaver
License:        GPLv2+ and LGPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Requires:       altlinux-freedesktop-menu-common
Requires:       mate-keyring-pam
Requires:       mate-backgrounds
Requires:       mate-power-manager

# PATCH-FIX-UPSTREAM mate-screensaver-1.5.1-only_allow_one_instance.patch - nmo.marques@gmail.com
# only allow one instance per user; fixes dual password prompt after hibernate/suspend, upstreamed
Patch0:        %{name}-1.5.1-only_allow_one_instance.patch

BuildRequires:  gtk2-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  mate-menus-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  libexif-devel
BuildRequires:  pam-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXmu-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libmatenotify-devel
BuildRequires:  libGL-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  gettext
BuildRequires:  nss-devel
BuildRequires:  mate-common
BuildRequires:  libXxf86misc-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXtst-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mate-common
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%if 0%{?fedora} >= 18
BuildRequires:  pkgconfig(libsystemd-login)
BuildRequires:  pkgconfig(libsystemd-daemon)
%else
BuildRequires:  libConsoleKit-devel
%endif
Source44: import.info
Patch33: gnome-screensaver-2.28.0-alt-pam.patch
Patch34: mate-screensaver-2.28.0-user_activity.patch
Patch35: mate-screensaver-1.5.1-alt-ru-po-mate-logo-isnt-foot.patch
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
%setup -q
%patch0 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p0


%build
NOCONFIGURE=1 ./autogen.sh
%configure                                                             \
   --disable-static                                                    \
   --with-xscreensaverdir=%{_datadir}/xscreensaver/config              \
   --with-xscreensaverhackdir=%{_libexecdir}/xscreensaver              \
   --enable-locking                                                    \
%if 0%{?fedora} >= 18
   --with-systemd                                                      \
   --without-console-kit                                               \
%else
   --with-console-kit                                                  \
   --with-systemd=no                                                   \
%endif
   --with-passwd-helper=/usr/libexec/mate-screensaver/mate-screensaver-chkpwd-helper  \
	--disable-pam
#	--enable-pam

make V=1 %{?_smp_mflags}
gcc -o %name-chkpwd-helper $RPM_OPT_FLAGS %SOURCE45 -lpam


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original             \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-screensaver-preferences.desktop

desktop-file-install --delete-original             \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/screensavers    \
  $RPM_BUILD_ROOT%{_datadir}/applications/screensavers/*.desktop

%find_lang %{name} --with-gnome
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
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/MateConf/gsettings/org.mate.screensaver.gschema.migrate
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_mandir}/man1/*.1.*
%attr(2511,root,chkpwd) %_libexecdir/%name/%name-chkpwd-helper

%files devel
%{_libdir}/pkgconfig/*


%changelog
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

