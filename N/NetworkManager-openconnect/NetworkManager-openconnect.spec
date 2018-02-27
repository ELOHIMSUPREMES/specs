%define nm_version 0.9.8
%define nm_applet_version 0.9.8
%define nm_applet_name NetworkManager-applet-gtk
%define gtkver 3

Name: NetworkManager-openconnect
Version: 0.9.8.4
Release: alt2
License: %gpl2plus
Group: System/Configuration/Networking
Summary: NetworkManager VPN integration for openconnect

Url: http://www.gnome.org/projects/NetworkManager/

Source: %name-%version.tar
Patch1: %name-%version-%release.patch
Requires: NetworkManager >= %nm_version
Requires: openconnect

BuildRequires(pre): rpm-build-licenses
BuildRequires: libopenconnect-devel >= 3.02
BuildRequires: perl-XML-Parser
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgtk+%gtkver-devel
BuildRequires: libdbus-glib-devel >= 0.74
BuildRequires: libGConf-devel libgnome-keyring-devel
BuildRequires: libssl-devel
BuildRequires: intltool gettext
BuildRequires: libxml2-devel


%description
This package contains software for integrating the openconnect VPN software
with NetworkManager and the GNOME desktop

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: GConf2
Requires: %nm_applet_name >= %version
Requires: NetworkManager-openconnect = %version-%release

Obsoletes: %name-gnome < 0.9.8.4
Provides: %name-gnome = %version-%release

%description gtk
This package contains applications for use with
NetworkManager panel applet.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
    --disable-static \
    --libexecdir=%_libexecdir/NetworkManager \
    --localstatedir=%_var \
    --with-gtkver=%gtkver

%make_build

%install
%makeinstall_std
%find_lang %name

%files
%doc AUTHORS ChangeLog COPYING
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-openconnect-service.conf
%config(noreplace) %_sysconfdir/NetworkManager/VPN/nm-openconnect-service.name
%_libexecdir/NetworkManager/nm-openconnect-service
%_libexecdir/NetworkManager/nm-openconnect-service-openconnect-helper

%files gtk -f %name.lang
%_libdir/NetworkManager/lib*.so*
%_libexecdir/NetworkManager/nm-openconnect-auth-dialog
%_datadir/gnome-vpn-properties/openconnect

%exclude %_libdir/NetworkManager/lib*.la

%changelog
* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt2
- Fix build: Avoid deprecation warnings.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt1
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.
- 0.9.8.4

* Tue Feb 26 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.8.0-alt1
- 0.9.8.0

* Thu Oct 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.6.2-alt1
- 0.9.6.2

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.5.95-alt1
- 0.9.5.95

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.4.0-alt2
- upstream snapshot 12e173e93b1fc2559c24d870bcf1d0aba41e3d32

* Wed Apr 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.4.0-alt1
- 0.9.4.0

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Thu Sep 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.999-alt1
- 0.8.999

* Mon Apr 04 2011 Mikhail Efremov <sem@altlinux.org> 0.8.3.995-alt1
- Minor spec cleanup.
- Changed libexecdir to %%_libexecdir/NetworkManager.
- 0.8.3.995 (0.8.4-beta1).

* Fri Nov 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Tue Oct 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun May 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.0.997-alt1
- 0.8.0.997 (0.8.1-beta1)

* Wed Mar 03 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8-alt1
- 0.8

* Sun Jan 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.997-alt1
- initial build
