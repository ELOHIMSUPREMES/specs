Name: xfdashboard
Version: 0.3.91
Release: alt1

Summary: A Gnome shell like dashboard for Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/applications/xfdashboard/start

# Upstream: git://git.xfce.org/apps/xfdashboard
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses rpm-build-xdg

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel libgarcon-devel libxfce4util-devel
BuildRequires: libgtk+3-devel libwnck3-devel libclutter-devel libdbus-glib-devel

%description
xfdashboard provides a GNOME shell dashboard like interface for use with
Xfce desktop. It can be configured to run to any keyboard shortcut and
when executed provides an overview of applications currently open
enabling the user to switch between different applications. The search
feature works like Xfce's app finder which makes it convenient to search
for and start applications.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfdashboard_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%{name}*
%_xdgconfigdir/autostart/*.desktop
%_datadir/appdata/*.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/themes/%{name}*/
%_datadir/%name/

%changelog
* Mon Mar 30 2015 Mikhail Efremov <sem@altlinux.org> 0.3.91-alt1
- Updated url.
- Updated to 0.3.91.

* Fri Mar 20 2015 Mikhail Efremov <sem@altlinux.org> 0.3.90-alt1
- Updated to 0.3.90.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1
- Updated to 0.3.9.

* Mon Oct 20 2014 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Sep 08 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Wed Aug 27 2014 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Wed Jul 23 2014 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Tue Jul 01 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu May 29 2014 Mikhail Efremov <sem@altlinux.org> 0.1.92-alt1
- Updated to 0.1.92.

* Mon May 26 2014 Mikhail Efremov <sem@altlinux.org> 0.1.91-alt1
- Updated to 0.1.91.

* Mon Mar 31 2014 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt2
- Rebuild with libcogl-1.18.0.

* Thu Mar 20 2014 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- Updated to 0.1.6.

* Wed Mar 12 2014 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Updated url and description.
- Updated to 0.1.5.

* Tue Feb 25 2014 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Wed Feb 12 2014 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Mon Jan 27 2014 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Mon Jan 13 2014 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20131125
- Initial build.

