Name: btrfs-progs
Version: 4.4.1
Release: alt1

Summary: Utilities for managing the Btrfs filesystem
License: GPLv2
Group: System/Kernel and hardware
Url: http://btrfs.wiki.kernel.org/

Source: %name-%version-%release.tar

BuildRequires: libacl-devel libe2fs-devel libuuid-devel zlib-devel libblkid-devel libattr-devel liblzo2-devel asciidoc xmlto

%description
Btrfs (B-tree FS or usually pronounced "Butter FS") is a copy-on-write
file system for Linux. It was created as a response to the ZFS filesystem,
in order to replace the ext3 file system while removing a number of its
limitations, particularly with respect to file size, total file system size
and filesystem check duration; it is also expected to implement modern
filesystem features not supported by ext3, like writable snapshots,
snapshots of snapshots, builtin RAID support, and subvolumes. In addition,
Btrfs claims a "focus on fault tolerance, repair and easy administration.

This package contains utilities for managing the Btrfs filesystem

%package -n libbtrfs-devel
Summary:	btrfs filesystem-specific libraries and headers
Group:		Development/C
Requires:	libbtrfs = %version-%release
Provides:	%name-devel

%description -n libbtrfs-devel
btrfs-progs-devel contains the libraries and header files needed to
develop btrfs filesystem-specific programs.

You should install btrfs-progs-devel if you want to develop
btrfs filesystem-specific programs.


%package -n libbtrfs
Summary:	btrfs filesystem-specific libraries and headers
Group:		System/Kernel and hardware

%description -n libbtrfs
btrfs-progs-devel contains shared libraries needed to
btrfs filesystem-specific programs.


%prep
%setup -q -n %name-%version-%release

%build
autoreconf -fisv
automake --add-missing ||:
%configure
%make_build

%install
%makeinstall bindir=%buildroot/sbin libdir=%buildroot/%_lib incdir=%buildroot/%_includedir/btrfs
mkdir -p %buildroot%_libdir
LIBNAME=`basename \`ls $RPM_BUILD_ROOT/%{_lib}/libbtrfs.so.*.*\``
ln -s ../../%_lib/$LIBNAME %buildroot%_libdir/libbtrfs.so 

%files
/sbin/*
%_man8dir/*
%_man5dir/*

%files -n libbtrfs
/%_lib/*.so.*

%files -n libbtrfs-devel
%_libdir/*.so
%_includedir/btrfs

%changelog
* Wed Apr 06 2016 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- new version

* Mon Nov 23 2015 Anton Farygin <rider@altlinux.ru> 4.3.1-alt1
- new version

* Sat Oct 17 2015 Anton Farygin <rider@altlinux.ru> 4.2.2-alt1
- new version

* Thu Jun 25 2015 Anton Farygin <rider@altlinux.ru> 4.1-alt1
- new version

* Mon May 25 2015 Anton Farygin <rider@altlinux.ru> 4.0.1-alt1
- new version

* Wed May 20 2015 Anton Farygin <rider@altlinux.ru> 4.0-alt1
- new version

* Tue Mar 31 2015 Anton Farygin <rider@altlinux.ru> 3.19.1-alt1
- new version

* Sun Mar 15 2015 Anton Farygin <rider@altlinux.ru> 3.19-alt1
- new version

* Fri Jan 30 2015 Anton Farygin <rider@altlinux.ru> 3.18.2-alt1
- new version

* Mon Jan 19 2015 Anton Farygin <rider@altlinux.ru> 3.18.1-alt1
- new version

* Fri Jan 16 2015 Anton Farygin <rider@altlinux.ru> 3.18-alt1
- new version

* Tue Nov 18 2014 Anton Farygin <rider@altlinux.ru> 3.17.1-alt1
- new version

* Mon Oct 06 2014 Anton Farygin <rider@altlinux.ru> 3.16.2-alt1
- new version

* Mon Sep 08 2014 Anton Farygin <rider@altlinux.ru> 3.16-alt1
- new version

* Thu Jun 05 2014 Anton Farygin <rider@altlinux.ru> 3.14.2-alt1
- new version

* Mon Apr 21 2014 Anton Farygin <rider@altlinux.ru> 3.14.1-alt1
- new version

* Fri Apr 18 2014 Anton Farygin <rider@altlinux.ru> 3.14-alt1
- new version

* Wed Mar 26 2014 Anton Farygin <rider@altlinux.ru> 3.12-alt2
- fixed build on ARM

* Tue Mar 25 2014 Anton Farygin <rider@altlinux.ru> 3.12-alt1
- new version

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19-alt3.1
- Fixed build

* Sun Feb 20 2011 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt3
- v0.19-35-g1b444cd
- Relocate binaries to /sbin

* Tue Nov 24 2009 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt2
- v0.19-4-gab8fb4c
- Fix BuildRequires

* Sun Sep 06 2009 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt1
- v0.19-1-g4f89b6e

* Thu Jan 29 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.18-alt1
- 0.18

* Wed Jan 21 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.17-alt2
- Fixed typo in package name
- Fixed URL

* Tue Jan 13 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.17-alt1
- Initial build for ALT Linux
