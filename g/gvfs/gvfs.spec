%define ver_major 1.22
%def_enable http
%def_enable avahi
%def_enable cdda
%def_enable fuse
%def_disable hal
%def_enable obexftp
%def_enable gphoto2
%def_enable keyring
%def_enable samba
%def_enable archive
%def_disable gdu
%def_enable afc
%def_enable afp
%def_enable udisks2
%def_enable libmtp
%def_enable goa
%def_enable bluray
%def_enable gtk
%def_enable systemd_login
%def_disable gtk_doc
%def_enable installed_tests

Name: gvfs
Version: %ver_major.2
Release: alt1

Summary: The GNOME virtual filesystem libraries
License: %lgpl2plus
Group: System/Libraries
URL: ftp://ftp.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar
Patch: gvfs-1.11.3-alt-gettext.patch
Patch1: gvfs-1.16.0-archive-integration.patch
Patch3: gvfs-1.14.1-libgvfsdaemon+headers_install.patch
Patch4: gvfs-1.16.2-alt-lfs.patch
Patch5: gvfs-1.15.4-alt-tmpfiles_dir.patch
# https://bugzilla.altlinux.org/show_bug.cgi?id=29047
# https://bugzilla.altlinux.org/show_bug.cgi?id=29171
# https://mail.gnome.org/archives/gvfs-list/2013-May/msg00014.html
Patch6: gvfs-1.19.90-alt-1-logind-state.patch

%{?_enable_gdu:Obsoletes: gnome-mount <= 0.8}
%{?_enable_gdu:Obsoletes: gnome-mount-nautilus-properties <= 0.8}

# From configure.in
%define intltool_ver 0.35.0
%define glib_ver 2.35.3
%define libsoup_ver 2.41.3
%define avahi_ver 0.6
%define libcdio_paranoia_ver 0.82
%define hal_ver 0.5.10
%define bluez_ver 4.0
%define gdu_ver 3.3.91
%define udisks_ver 1.99
%define mtp_ver 1.1.5
%define goa_ver 3.7.90
%define libarchive_ver 3.0.22
%define imobiledevice_ver 1.1.5

Requires: dconf
%{?_enable_hal:Requires: gnome-mount}
%{?_enable_gdu:Requires: gnome-disk-utility >= %gdu_ver}
%{?_enable_udisks2:Requires: udisks2}

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.in
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: gtk-doc
BuildPreReq: openssh-clients
# hotplug backend
BuildRequires: libgudev-devel
# required if autoreconf used
BuildRequires: libgcrypt-devel
%{?_enable_gtk:BuildPreReq: libgtk+3-devel}
%{?_enable_http:BuildPreReq: libsoup-gnome-devel >= %libsoup_ver libxml2-devel}
%{?_enable_avahi:BuildPreReq: libavahi-glib-devel >= %avahi_ver libavahi-devel >= %avahi_ver}
%{?_enable_cdda:BuildPreReq: libcdio-devel >= %libcdio_paranoia_ver}
%{?_enable_fuse:BuildPreReq: libfuse-devel}
%{?_enable_hal:BuildPreReq: libhal-devel >= %hal_ver}
%{?_enable_obexftp:BuildPreReq: libbluez-devel >= %bluez_ver libdbus-glib-devel libexpat-devel}
%{?_enable_gphoto2:BuildPreReq: libgphoto2-devel}
%{?_enable_keyring:BuildPreReq: libsecret-devel}
%{?_enable_samba:BuildPreReq: libsmbclient-devel}
%{?_enable_archive:BuildPreReq: libarchive-devel >= %libarchive_ver}
%{?_enable_gdu:BuildPreReq: libgdu-devel >= %gdu_ver libgudev-devel}
%{?_enable_afc:BuildPreReq: libimobiledevice-devel >= %imobiledevice_ver}
%{?_enable_afp:BuildPreReq: libgcrypt-devel}
%{?_enable_udisks2:BuildPreReq: libudisks2-devel >= %udisks_ver}
%{?_enable_libmtp:BuildPreReq: libmtp-devel >= %mtp_ver}
%{?_enable_goa:BuildPreReq: libgnome-online-accounts-devel >= %goa_ver}
%{?_enable_bluray:BuildPreReq: libbluray-devel}
%{?_enable_systemd_login:BuildPreReq: libsystemd-login-devel}

BuildPreReq: desktop-file-utils
BuildRequires: gcc-c++ perl-XML-Parser

# for check
#BuildRequires: /proc dbus-tools-gui python3 python3-module-pygobject3 python-module-twisted-core
#BuildRequires:  openssh-server apache2 samba genisoimage
# and more

%package devel
Summary: Libraries and include files for developing gvfs applications
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name = %version-%release

%package -n fuse-%name
Summary: gvfs fuse gateway
Group: System/Kernel and hardware
Requires: %name = %version-%release
Requires: %{get_dep fuse}

%package backend-smb
Summary: Samba backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release
Requires: samba-client

%package backend-obexftp
Summary: Obexftp backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-dnssd
Summary: Dnssd(avahi) backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-cdda
Summary: Music CD-ROM backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-afc
Summary: i{Phone,Pod} backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-afp
Summary: Apple Filing Protocol backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-recent-files
Summary: Recent files backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-goa
Summary: gnome-online-accounts backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release
Requires: gnome-online-accounts

%package backend-mtp
Summary: MTP support for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backends
Summary: All backends for gvfs
Group: System/Libraries
BuildArch: noarch
Requires: gvfs gvfs-backend-smb gvfs-backend-dnssd
%{?_enable_cdda:Requires: gvfs-backend-cdda}
%{?_enable_obexftp:Requires: gvfs-backend-obexftp}
%{?_enable_afc:Requires: gvfs-backend-afc}
%{?_enable_afp:Requires: gvfs-backend-afp}
%{?_enable_gtk:Requires: gvfs-backend-recent-files}
%{?_enable_goa:Requires: gvfs-backend-goa}
%{?_enable_libmtp:Requires: gvfs-backend-mtp}

%package utils
Summary: Command line applications for gvfs.
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%package -n bash-completion-gvfs
Summary: Bash completion for gvfs utils
Group: Development/Other
BuildArch: noarch
Requires: bash-completion
Requires: gvfs-utils

%description
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via dbus. It also contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It also
supports exposing the gvfs mounts to non-gio applications using fuse.

This package contains the gvfs server, libgvfscommon library, gio
modules and backends for gvfs: archive, burn, computer, dav, ftp,
gphoto2, http, localtest, network, sftp and trash.

%description devel
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via dbus. It also contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It also
supports exposing the gvfs mounts to non-gio applications using fuse.

This package contains the libgvfscommon development files.

%description -n fuse-%name
fuse-gvfs is a bridge between the gvfs filesystem design and fuse, a
program to mount user-space filesystems.

%description backend-smb
This package contains the smb and smb-browse backends for gvfs.

%description backend-obexftp
This package contains the obexftp backend for gvfs.

%description backend-dnssd
This package contains the dnssd backend for gvfs.

%description backend-cdda
This package contains the cdda backend for gvfs.

%description backend-afc
This package contains a backend for gvfs, providing access to Apple's
iPhone, and iPod Touch devices.

%description backend-afp
This package contains a backend for gvfs, providing access to Apple
Mac OS X filesystem by AFP (Apple Filing Protocol) network protocol.

%description backend-recent-files
This package contains recent files backend for gvfs.

%description backend-goa
This package contains gnome-online-accounts backend for gvfs.

%description backend-mtp
This package provides support for reading and writing files on MTP based
devices (Media Transfer Protocol) to applications using gvfs.

%description backends
This virtual package contains the all backends for gvfs.

%description utils
This package contains command line tools for gvfs.

%description -n bash-completion-gvfs
Bash completion for gvfs.

%package tests
Summary: GVFS test programms
Group: Development/GNOME and GTK+
Requires: %name-backends = %version-%release fuse-%name

%description tests
The %name-tests package provides programms for testing GVFS.

%define _libexecdir %_prefix/libexec/%name

%prep
%setup
%patch -p1
%patch1 -p1 -b .archive-integration
#%%patch3 -p1 -b .headers-install
%patch4 -p1 -b .lfs
%patch5 -b .tmpfiles
%patch6 -p2 -b .logind-state

[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
        %{subst_enable http} \
        %{subst_enable avahi} \
        %{subst_enable cdda} \
        %{subst_enable fuse} \
        %{subst_enable hal} \
        %{subst_enable obexftp} \
        %{subst_enable gphoto2} \
        %{subst_enable keyring} \
        %{subst_enable samba} \
        %{subst_enable archive} \
        %{subst_enable afc} \
        %{subst_enable afp} \
        %{subst_enable gdu} \
        %{subst_enable udisks2} \
        %{subst_enable libmtp} \
        %{subst_enable bluray} \
        %{subst_enable gtk} \
        %{?_enable_systemd_login:--enable-libsystemd-login} \
        %{?_enable_gtk_doc:--enable-gtk-doc} \
        %{?_enable_installed_tests:--enable-installed-tests}
%make_build

%install
%makeinstall_std

%find_lang %name

%check
#export PATH=/usr/sbin:$PATH
#%%make check

%post
killall -USR1 gvfsd >&/dev/null || :

%files -f %name.lang
%doc AUTHORS NEWS README monitor/udisks2/what-is-shown.txt
%dir %_libdir/%name
%_libdir/%name/libgvfs*.so
%exclude %_libdir/%name/*.la
%dir %_libexecdir
# daemon
%_libexecdir/gvfsd
%config %_datadir/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
# monitors
%_libexecdir/gvfs-gphoto2-volume-monitor
%{?_enable_hal:%_libexecdir/gvfs-hal-volume-monitor}
%{?_enable_gdu:%_libexecdir/gvfs-gdu-volume-monitor}
%{?_enable_udisks2:%_libexecdir/gvfs-udisks2-volume-monitor}
%_datadir/dbus-1/services/*
# gio modules
%_libdir/gio/modules/*.so
# default backends
%_libexecdir/gvfsd-*
%exclude %_libexecdir/gvfsd-fuse

%dir %_datadir/%name
%dir %_datadir/%name/remote-volume-monitors
%_datadir/%name/remote-volume-monitors/gphoto2.monitor
%{?_enable_hal:%_datadir/%name/remote-volume-monitors/hal.monitor}
%{?_enable_gdu:%_datadir/%name/remote-volume-monitors/gdu.monitor}
%{?_enable_udisks2:%_datadir/%name/remote-volume-monitors/udisks2.monitor}

%_datadir/%name/mounts
%_datadir/applications/mount-archive.desktop

# in another packages
%if_enabled samba
    %exclude %_libexecdir/gvfsd-smb
    %exclude %_libexecdir/gvfsd-smb-browse
    %exclude %_datadir/%name/mounts/smb.mount
    %exclude %_datadir/%name/mounts/smb-browse.mount
%endif

%{?_enable_cdda:%exclude %_libexecdir/gvfsd-cdda}

%if_enabled obexftp
    %exclude %_libexecdir/gvfsd-obexftp
    %exclude %_datadir/%name/mounts/obexftp.mount
%endif

%if_enabled afc
    %exclude %_libexecdir/gvfsd-afc
    %exclude %_datadir/%name/mounts/afc.mount
%endif

%if_enabled afp
    %exclude %_libexecdir/gvfsd-afp
    %exclude %_libexecdir/gvfsd-afp-browse
    %exclude %_datadir/%name/mounts/afp.mount
    %exclude %_datadir/%name/mounts/afp-browse.mount
%endif

%{?_enable_cdda:%exclude %_datadir/%name/mounts/cdda.mount}
    %exclude %_libexecdir/gvfsd-dnssd
    %exclude %_datadir/%name/mounts/dns-sd.mount

%if_enabled libmtp
    %exclude %_libexecdir/gvfsd-mtp
    %exclude %_datadir/%name/mounts/mtp.mount
    %exclude %_datadir/dbus-1/services/org.gtk.Private.MTPVolumeMonitor.service
%endif

%if_enabled gtk
%exclude %_libexecdir/gvfsd-recent
%exclude %_datadir/%name/mounts/recent.mount
%endif

%files devel
%_includedir/*

%files -n fuse-%name
%_libexecdir/gvfsd-fuse
/lib/tmpfiles.d/gvfsd-fuse-tmpfiles.conf

%files backend-smb
%_libexecdir/gvfsd-smb
%_libexecdir/gvfsd-smb-browse
%_datadir/%name/mounts/smb.mount
%_datadir/%name/mounts/smb-browse.mount
%config %_datadir/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
%_datadir/GConf/gsettings/gvfs-smb.convert

%if_enabled obexftp
%files backend-obexftp
%_libexecdir/gvfsd-obexftp
%_datadir/%name/mounts/obexftp.mount
%endif

%files backend-dnssd
%_libexecdir/gvfsd-dnssd
%_datadir/%name/mounts/dns-sd.mount
%config %_datadir/glib-2.0/schemas/org.gnome.system.dns_sd.gschema.xml
%_datadir/GConf/gsettings/gvfs-dns-sd.convert

%if_enabled cdda
%files backend-cdda
%_libexecdir/gvfsd-cdda
%_datadir/%name/mounts/cdda.mount
%endif

%if_enabled afc
%files backend-afc
%_libexecdir/gvfsd-afc
%_libexecdir/gvfs-afc-volume-monitor
%_datadir/%name/mounts/afc.mount
%_datadir/%name/remote-volume-monitors/afc.monitor
%endif

%if_enabled afp
%files backend-afp
%_libexecdir/gvfsd-afp
%_libexecdir/gvfsd-afp-browse
%_datadir/%name/mounts/afp.mount
%_datadir/%name/mounts/afp-browse.mount
%endif

%if_enabled gtk
%files backend-recent-files
%_libexecdir/gvfsd-recent
%_datadir/%name/mounts/recent.mount
%endif

%if_enabled goa
%files backend-goa
%_libexecdir/%name-goa-volume-monitor
%_datadir/%name/remote-volume-monitors/goa.monitor
%endif

%if_enabled libmtp
%files backend-mtp
%_libexecdir/gvfsd-mtp
%_libexecdir/gvfs-mtp-volume-monitor
%_datadir/%name/mounts/mtp.mount
%_datadir/%name/remote-volume-monitors/mtp.monitor
%_datadir/dbus-1/services/org.gtk.Private.MTPVolumeMonitor.service
%endif

%files backends

%files utils
%_bindir/*
%_man1dir/*.1.*
%_man7dir/gvfs.7.*

%files -n bash-completion-gvfs
%_datadir/bash-completion/completions/%name

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/
%_datadir/installed-tests/%name/
%endif

%exclude %_libdir/gio/modules/*.la

%changelog
* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.2-alt1
- 1.22.2
- new -tests subpackage

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt2
- rebuilt against libimobiledevice.so.5

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt1
- 1.22.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Mon Aug 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Fri Jun 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt2
- rebuilt against libplist.so.2

* Fri May 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Fri Apr 11 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Fri Mar 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Mon Jan 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt0.1
- 1.18.4 snapshot (fixed BGO ##720482, 598092, 720743, 670534..)

* Fri Nov 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Thu Oct 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Thu Sep 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0
- disabled broken libgvfsdaemon+headers_install.patch

* Mon Jul 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt5
- sem@: new version of the alt-logind-state.patch (ALT #29185)

* Wed Jul 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt4
- sem@: updated alt-logind-state.patch

* Fri Jul 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt3
- new backend-mtp subpackage

* Tue Jul 02 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt2
- fixed afc backend for libimobiledevice new api from upstream
- added dependencies:
  backend-smb -> samba-client (ALT #29107)
- backend-goa -> gnome-online-accounts

* Fri Jun 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt1
- 1.16.3

* Tue Jun 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt2
- boyarsh@, aen@: gvfs-1.16.1-alt-logind-state.patch (ALT #29047)

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Tue Apr 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt2
- rebuilt against libimobiledevice.so.4

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0
- new gnome-online-accounts backend

* Mon Mar 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt3
- rebuilt against libarchive.so.13

* Tue Nov 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt2
- mtp devices support via libmtp (ALT #27989)

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2
- rediffed headers_install.patch

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1 release

* Wed Oct 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt0.1
- 1.14.1 snapshot (407e0eb1b)

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0
- new gvfs-backend-recent-files subpackage
- optional libsystemd-login support

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3 release

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt0.1
- 1.12.3 snapshot (01161473e)

* Wed May 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt2
- rebuild against libimobiledevice-1.1.3
- fixed build of afp backend

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Sep 06 2011 Yuri N. Sedunov <aris@altlinux.org> 1.9.5-alt1
- 1.9.5
- new -backend-afp subpackage

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7
- remove upstreamed patches

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt3
- fixed build against newer libgio
- fixed GNOME bug #633330

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt2
- libbluez4-devel/libbluez-devel

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2
- AFC backend temporarily disabled (not ready for libiphone-0.9.6)

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Thu Dec 03 2009 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1
- new afc backend

* Mon Nov 30 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2
- removed upstreamed patches

* Wed Nov 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt3
- obsoletes gnome-mount{,-nautilus-properties} if enabled gdu
- some upstream patches

* Thu Nov 05 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt2
- rebuild against new libcdio

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- g-d-u support disabled for Sisyphus

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5

* Thu Aug 20 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt2
- g-d-u support enabled

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- 1.3.4
- updated buildreqs

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Apr 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- removed strange dependency on glib2-devel

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Apr 02 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Mar 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Feb 04 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5
- removed upstreamed patch
- enabled obexftp plugin

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4
- updated buildreqs
- temporarily disabled obexftp plugin, requires bluez >= 4.0

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3
- remove obsolete %%post{,un} scripts

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Oct 14 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt3
- remove support synce
- install common, daemon headers. build libgvfsdaemon.so (patch3)

* Mon Oct 13 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt2
- add synce-gvfs-0.1 backend as patch2 from http://sourceforge.net/projects/synce/

* Sat Sep 27 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- new version
- removed gvfs-ftp-read-directory-2.patch and
  gvfs-0.2.4-trash-automount.patch (fixed in upstream)
- updated archive-integration.patch
- updated buildreqs
- updated %%files
- don't rebuild documentation

* Thu Jun 26 2008 Alexey Shabalin <shaba@altlinux.ru> 0.99.1-alt1
- 0.99.1
- enable archive integration (patch1)
- fix GNOME bugs #522933, #525779 (patch2, patch3)
- add update_desktopdb in post-scripts

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Wed Apr 09 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3
- changed libexec dir to %_prefix/libexec/%name

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt2
- fix exclude files (change libdir to libexecdir)

* Thu Mar 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- 0.2.1
- split the package into backends, utils
- move gvfs-bash-completion.sh from /etc/profile.d to /etc/bash_completion.d/,
  and individual package. (#15068)

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt2
- add require gnome-mount

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt1.1
- remove require gnome-mount

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt1
- redesigned spec

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt0.2
- update BuildRequires

* Thu Mar 13 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.2.0.1-alt0.1
- 0.2.0.1
- requires improvement

* Wed Mar 12 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.2.0-alt0.1
- 0.2.0
