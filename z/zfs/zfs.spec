%def_enable shared
%def_enable static
%def_with selinux

Name: zfs
%define lname lib%name
Version: 0.6.2
Release: alt1
Summary: ZFS on Linux
License: GPLv2+
Group: System/Kernel and hardware
URL: http://zfsonlinux.org
Source: http://archive.zfsonlinux.org/downloads/zfsonlinux/%name/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: zlib-devel libuuid-devel %{?_with_selinux:libselinux-devel} rpm-build-kernel

%description
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.


%if_enabled shared
%package -n %lname
Summary: ZFS shared libraries
Group: System/Libraries

%description -n %lname
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.
This package contains ZFS shared libraries.
%endif


%package -n %lname-devel
Summary: ZFS development files
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.
This package contains ZFS evelopment files.


%if_enabled static
%package -n %lname-devel-static
Summary: ZFS static libraries
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.
This package contains ZFS static libraries.
%endif


%package utils
Summary: Utilities for doing and managing mounts of the Linux ZFS filesystem
Group: System/Kernel and hardware
%{?_enable_shared:Requires: %lname = %version-%release}

%description utils
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.
This package contains utilities for doing and managing mounts of the Linux ZFS
filesystem.


%package -n kernel-source-%name
Summary: ZFS modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release
Requires: kernel-source-spl = %version

%description -n kernel-source-%name
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.
This package contains ZFS modules sources for Linux kernel.


%prep
%setup -q
%patch -p1
sed -i '/^AC_OUTPUT/itest "x$ZFS_CONFIG" != "xkernel" || ac_config_files="module/Makefile module/avl/Makefile module/nvpair/Makefile module/unicode/Makefile module/zcommon/Makefile module/zfs/Makefile module/zpios/Makefile"\n' configure.ac


%build
./autogen.sh

tar -C .. \
	--exclude .gitignore \
	--exclude 'include/*Makefile.*' \
	-cJf %name-%version.tar.xz \
	%name-%version/module \
	%name-%version/config/{{install-,ltmain.}sh,config.{awk,guess,sub},missing} \
	%name-%version/include \
	%name-%version/{AUTHORS,COPYRIGHT,DISCLAIMER,META,OPENSOLARIS.LICENSE,configure,%name{.release,_config.h}.in}

%configure \
	--with-config=user \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_with selinux} \
	--with-gnu-ld
%make_build


%install
install -pD -m 0644 {,%kernel_srcdir/}%name-%version.tar.xz
%makeinstall_std DEFAULT_INIT_DIR=%_initddir udevdir=/lib/udev dracutdir=/lib/dracut


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif



%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files utils
%doc AUTHORS COPYRIGHT DISCLAIMER META OPENSOLARIS.LICENSE README*
/sbin/*
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man5dir/*
%_man8dir/*
%_sysconfdir/%name
%_datadir/%name
/lib/udev/rules.d/*
/lib/udev/*_id
%exclude %_initddir/*
%exclude /lib/dracut
%exclude %_datadir/%name/zpios*
%exclude %_datadir/%name/smb.sh


%files -n kernel-source-%name
%_usrsrc/kernel


%changelog
* Tue Aug 27 2013 Led <led@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Sun Aug 18 2013 Led <led@altlinux.ru> 0.6.1-alt12
- upstream updates and fixes

* Thu Aug 15 2013 Led <led@altlinux.ru> 0.6.1-alt11
- upstream updates

* Sun Aug 11 2013 Led <led@altlinux.ru> 0.6.1-alt10
- upstream updates and fixes

* Fri Aug 02 2013 Led <led@altlinux.ru> 0.6.1-alt9
- kernel modules: upstream updates

* Sat Jul 27 2013 Led <led@altlinux.ru> 0.6.1-alt8
- zpool: upstream fixes

* Thu Jul 18 2013 Led <led@altlinux.ru> 0.6.1-alt7
- upstream fixes

* Wed Jul 17 2013 Led <led@altlinux.ru> 0.6.1-alt6
- upstream fixes

* Fri Jul 12 2013 Led <led@altlinux.ru> 0.6.1-alt5
- upstream updates

* Sat Jul 06 2013 Led <led@altlinux.ru> 0.6.1-alt4
- kernel-source-%name: add config/missing

* Thu Jul 04 2013 Led <led@altlinux.ru> 0.6.1-alt3
- upstream fixes
- kernel-source-%%name requires kernel-source-spl

* Tue Jul 02 2013 Led <led@altlinux.ru> 0.6.1-alt2
- upstream fixes

* Tue Jun 18 2013 Led <led@altlinux.ru> 0.6.1-alt1
- initial build
