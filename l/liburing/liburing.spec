Name: liburing
Version: 0.1
Release: alt3

Summary: Linux-native io_uring I/O access library
License: LGPL-2.1-or-later
Group: System/Libraries

Url: http://git.kernel.dk/cgit/liburing
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

%description
Provides native async IO for the Linux 5.1+ kernel, in a fast
and efficient manner, for both buffered and O_DIRECT.

%package devel
Summary: Development files for Linux-native io_uring I/O access library
Group: Development/C

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%package devel-static
Summary: Static library for developing apps using Linux-native io_uring
Group: Development/C
Requires: %name-devel

%description devel-static
This package contains the static library needed to develop statically
linked programs that use Linux-native io_uring.

%prep
%setup

%build
%make_build

%install
%makeinstall_std prefix=%_prefix libdir=%_libdir mandir=%_mandir

%files
%_libdir/liburing.so.*
%doc COPYING

%files devel
%_includedir/*
%_libdir/%name.so
%_man2dir/*

%files devel-static
%_libdir/%name.a

%changelog
* Mon May 20 2019 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt3
- Updated to upstream commit 375bed76ba7292122f828fbf49c2b530506fdce8
  that adds support for all mainline architectures.

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- added ExclusiveArch: since aarch64 is not supported yet

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- built for sisyphus (based on upstream spec with cleanups)

* Tue Jan 8 2019 Jens Axboe <axboe@kernel.dk> - 0.1
- Initial version
