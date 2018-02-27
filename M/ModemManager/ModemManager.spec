#define git_date .git20130531
%define git_date %nil

%define dbus_version 1.1
%define libdbus_glib_version 0.76
%define libgudev_version 143

%def_with qmi
%def_with mbim

Name: ModemManager
Version: 0.7.991
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: Mobile broadband modem management service
Url: http://gitorious.org/projects/modemmanager
Source: %name-%version.tar
Source1: %name-launcher
Patch0: %name-%version-%release.patch

Requires: dbus >= %dbus_version

BuildRequires(pre): rpm-build-licenses

BuildRequires: libdbus-glib-devel
BuildRequires: libgudev-devel >= %libgudev_version
%{?_with_qmi:BuildRequires: libqmi-glib-devel}
%{?_with_mbim:BuildRequires: libmbim-glib-devel}
BuildRequires: intltool
BuildRequires: ppp-devel
BuildRequires: libpolkit-devel
BuildRequires: gtk-doc dia

# For tests
BuildRequires: /dev/pts

%description
ModemManager provides a DBus interface to communicate with
mobile broadband (GSM, CDMA, UMTS, ...) cards. Implements
a loadable plugin interface to add work-arounds for
non standard devices.

%package devel
License: %lgpl2plus
Group: Development/C
Summary: Headers for adding ModemManager support to applications

%description devel
This package contains various headers accessing some ModemManager
functionality from applications.

%package devel-doc
Group: Development/Documentation
Summary: Development documentation for %name
BuildArch: noarch

%description devel-doc
%summary

%package -n libmm-glib
License: %lgpl2plus
Summary: Libraries for adding ModemManager support to applications that use glib
Group: System/Libraries

%description -n libmm-glib
This package contains the libraries that make it easier to use some
ModemManager functionality from applications that use glib.

%package -n libmm-glib-devel
License: %lgpl2plus
Summary: Development files for libmm-glib
Group: Development/C
Requires: libmm-glib = %version-%release

%description -n libmm-glib-devel
This package contains libraries and header files for
developing applications that use libmm-glib.

%package -n libmm-glib-devel-doc
Group: Development/Documentation
Summary: Development documentation for libmm-glib
BuildArch: noarch

%description -n libmm-glib-devel-doc
%summary

%prep
%setup -n %name-%version
%patch0 -p1

%build
%autoreconf
%configure \
	--disable-static \
	--with-udev-base-dir=/lib/udev \
	--with-polkit \
	--with-systemdsystemunitdir=%_unitdir \
	%{subst_with qmi} \
	%{subst_with mbim} \
	--enable-gtk-doc \
	--with-tests

%make_build

%check
make check

%install
%makeinstall_std
install -Dm0755 %SOURCE1 %buildroot%_sbindir/%name-launcher
%find_lang %name

%post
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
	"$SYSTEMCTL" daemon-reload ||:
	if [ "$1" -eq 1 ]; then
		"$SYSTEMCTL" -q preset "%name.service" ||:
	else
		"$SYSTEMCTL" try-restart "%name.service" ||:
	fi
fi

%preun
SYSTEMCTL=systemctl
if [ "$1" -eq 0 ] && sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
		"$SYSTEMCTL" --no-reload -q disable "%name.service"
		"$SYSTEMCTL" stop "%name.service"
fi

%files -f %name.lang
%doc ChangeLog NEWS AUTHORS README
%_datadir/dbus-1/system-services/*.service
%dir %_libdir/ModemManager/
%_libdir/ModemManager/*.so
%_sbindir/*
%_bindir/mmcli
%_sysconfdir/dbus-1/system.d/*.conf
%_datadir/dbus-1/interfaces/*.xml
/lib/udev/rules.d/*
%_iconsdir/hicolor/*/apps/*
%_datadir/polkit-1/actions/*.policy
%_unitdir/*.service
%doc %_man8dir/*.*

%exclude %_libdir/ModemManager/*.la
%exclude %_libdir/pppd/*/mm-test-pppd-plugin.la
%exclude %_libdir/pppd/*/mm-test-pppd-plugin.so

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%files devel-doc
%doc %_datadir/gtk-doc/html/%name

%files -n libmm-glib
%_libdir/libmm-glib.so.*

%files -n libmm-glib-devel
%_libdir/libmm-glib.so
%_includedir/libmm-glib
%_pkgconfigdir/mm-glib.pc

%files -n libmm-glib-devel-doc
%doc %_datadir/gtk-doc/html/libmm-glib

%changelog
* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 0.7.991-alt1
- Updated to 0.7.991.

* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130531
- Build with MBIM support.
- Upstream git snapshot (master branch).

* Tue Apr 23 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130422
- Upstream git snapshot (master branch).

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130326
- Preset/disable MM service in case of systemd.
- Upstream git snapshot (master branch).

* Tue Mar 05 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130304
- Start ModemManager on non-systemd systems.
- Package doc subpackages as noarch.
- Upstream git snapshot (master branch).

* Mon Feb 25 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130225
- upstream git snapshot (master branch).

* Tue Feb 19 2013 Mikhail Efremov <sem@altlinux.org> 0.6.0.0-alt1.git20130215
- upstream git snapshot (MM_06 branch).

* Sun Sep 16 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.0-alt1
- Updated to 0.5.4.0.

* Fri Jul 20 2012 Mikhail Efremov <sem@altlinux.org> 0.5.3.96-alt1
- Updated to 0.5.3.96 (0.5.4-rc2).

* Tue Apr 03 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt2
- Patches from upstream git:
  + option: hso_get_cid() always returns >= 0.
  + serial: fix crash when sending some commands to a closed port.
  + gsm: define the PPP auth preferences for STATIC and DHCP device use.

* Mon Mar 19 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Thu Mar 01 2012 Mikhail Efremov <sem@altlinux.org> 0.5.1.97-alt1
- Updated to 0.5.1.97 (0.5.2 RC).

* Thu Dec 08 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20111208
- upstream git snapshot (MM_05 branch).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20110821
- upstream git snapshot (0.5 release and some bugfixes).

* Mon Aug 01 2011 Mikhail Efremov <sem@altlinux.org> 0.4.998-alt1.git20110728
- upstream git snapshot (MM_05 branch) (closes: #25834).

* Fri Jun 24 2011 Mikhail Efremov <sem@altlinux.org> 0.4.997-alt1.git20110624
- upstream git snapshot (MM_05 branch) (closes: #25766).

* Sun May 01 2011 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20110501
- upstream git snapshot

* Tue Nov 30 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20101130
- upstream git snapshot

* Wed Sep 22 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100922
- upstream git snapshot (#23978 may be closed).

* Mon Sep 06 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100906
- upstream git snapshot

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100722
- upstream git snapshot

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100628
- upstream git snapshot

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.3.997-alt1
- 0.3.997 (0.4-beta1)

* Tue Apr 27 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100227
- upstream git snapshot

* Fri Feb 05 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100204
- upstream git snapshot

* Mon Jan 18 2010 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt3.git20100105
- get version of pppd during build.

* Sat Jan 09 2010 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt2.git20100105
- BuildRequire ppp-devel.
- upstream git snapshot

* Fri Dec 25 2009 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt2.git20091225
- upstream git snapshot

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt1
- 0.2.997

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.git20091124
- upstream git snapshot

* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.git20091026
- upstream git snapshot

* Mon Feb 09 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- initial build for Sisyphus

