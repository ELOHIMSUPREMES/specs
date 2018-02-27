%define _name udisks
%define api_ver 2.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%def_enable introspection

Name: %{_name}2
Version: 2.1.0
Release: alt2

Summary: Disk Management Service (Second Edition)
License: GPLv2+
Group: System/Libraries
Url: http://www.freedesktop.org/wiki/Software/%_name

#Source: %_name-%version.tar
Source: http://udisks.freedesktop.org/releases/%_name-%version.tar.bz2
Source1: %name.control
Patch1: %_name-1.92.0-alt-udiskd_dir.patch

Obsoletes: %_name

%define glib_ver 2.31.13
%define gi_ver 1.30.0
%define polkit_ver 0.101
%define udev_ver 165
%define libatasmart_ver 0.17
%define dbus_ver 1.4.0

PreReq: control
Requires: lib%name = %version-%release
Requires: /lib/udev/rules.d
Requires: /usr/sbin/cryptsetup
Requires: dbus >= %dbus_ver dbus-tools-gui
Requires: mdadm ntfsprogs parted gdisk acl

BuildRequires: intltool gtk-doc gnome-common
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libpolkit-devel >= %polkit_ver
BuildRequires: libatasmart-devel >= %libatasmart_ver
BuildRequires: libudev-devel libgudev-devel >= %udev_ver
BuildRequires: libacl-devel systemd-devel libsystemd-login-devel libsystemd-daemon-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver}

%description
The udisks project provides a daemon, tools and libraries to access
and manipulate disks and storage devices.

%package -n lib%name
Summary: Dynamic library to access the udisks daemon (Second Edition)
Group: System/Libraries

%description -n lib%name
The udisks project provides a daemon, tools and libraries to access
and manipulate disks and storage devices.

This package contains the dynamic %name library, which provides
access to the udisks daemon.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the development files for the library lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
Conflicts: %name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for lib%name.


%prep
%setup -n %_name-%version
%patch1

%build
%autoreconf
# needed for O_CLOEXEC from bits/fcntl.h
%add_optflags -D_GNU_SOURCE
%configure --disable-static \
	--enable-gtk-doc

%make

%install
%makeinstall_std

mkdir -p %buildroot%_localstatedir/run/%name
touch %buildroot%_localstatedir/lib/%name/mtab

# use /media for mounting by default
mkdir -p %buildroot%_sysconfdir/udev/rules.d
cat > %buildroot%_sysconfdir/udev/rules.d/99-alt-%name-media-mount-point.rules <<_EOF_
ENV{ID_FS_USAGE}=="filesystem|other|crypto",
ENV{UDISKS_FILESYSTEM_SHARED}="0"
_EOF_

# control support
install -pD -m755 %SOURCE1 %buildroot%_controldir/%name

%find_lang %name

%check
%make check

%pre
if [ -f %_controldir/%name ]; then
%pre_control %name
fi

%post
%post_control -s default %name

%files -f %name.lang
%_sbindir/umount.%name
%_bindir/udisksctl
/lib/udev/rules.d/80-%name.rules
%_sysconfdir/udev/rules.d/99-alt-%name-media-mount-point.rules
%dir %_libexecdir/%name
%_libexecdir/%name/udisksd
%_datadir/polkit-1/actions/org.freedesktop.%name.policy
%_datadir/dbus-1/system-services/org.freedesktop.UDisks2.service
%_sysconfdir/dbus-1/system.d/org.freedesktop.UDisks2.conf
%_datadir/bash-completion/completions/udisksctl
%_mandir/man1/*
%_mandir/man8/*
%attr(0700,root,root) %dir %_localstatedir/lib/%name
%ghost %_localstatedir/lib/%name/mtab
%attr(0700,root,root) %dir %_localstatedir/run/%name
%config %systemd_unitdir/udisks2.service
%config %_controldir/%name
%doc README AUTHORS NEWS HACKING

%files -n libudisks2
%_libdir/libudisks2.so.*

%files -n libudisks2-devel
%_libdir/lib%name.so
%_includedir/%name/
%_libdir/pkgconfig/%name.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/udisks2/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/UDisks-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/UDisks-%api_ver.gir
%endif

%changelog
* Thu Jul 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt2
- 99-alt-udisks2-media-mount-point.rules: /media used for mounting
  Control support to switch mount points for removable media (ALT #27256, #29138)

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Sat Mar 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.92-alt2
- Added dependency on dbus-tools-gui (ALT #28692)

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.92-alt1
- 2.0.92

* Thu Dec 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt2
- a time to obsolete old udisks

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- after 2.0.1 snapshot (d2a937d3)

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0 release

* Thu Sep 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.100.0-alt0.1
- 1.100.0 snapshot

* Fri Jul 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.99.0-alt1
- 1.99.0 release

* Wed Jul 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.99.0-alt0.1
- 1.99.0 snapshot

* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.98.0-alt1
- 1.98.0

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.97.0-alt1
- 1.97.0

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.96.0-alt1
- 1.96.0

* Wed Apr 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.94.0-alt1.1
- 1.94.0 release

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.94.0-alt1
- 1.94.0 snapshot (ALT #27198)

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.93.0-alt2
- fixed udisksdprivdir accordingly with %%_libexecdir

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.93.0-alt1
- 1.93.0

* Wed Feb 29 2012 Yuri N. Sedunov <aris@altlinux.org> 1.92.0-alt1
- 1.92.0

* Wed Feb 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.91.0-alt1
- first build for Sisyphus
