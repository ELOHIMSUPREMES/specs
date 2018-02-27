%set_verify_elf_method unresolved=strict

Name: libdispatch-objc2
Version: 1.2
Release: alt1.svn20140108
Summary: Linux port of Apple's open-source concurrency library
License: Apache License v2
Group: System/Libraries
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/etoile/trunk/Dependencies/libdispatch-objc2
Source: %name-%version.tar

BuildPreReq: clang-devel libBlocksRuntime-devel cmake
BuildPreReq: libpthread_workqueue-devel libkqueue-devel
BuildPreReq: gcc-c++ gnustep-corebase-devel

%description
libdispatch, aka Grand Central Dispatch (GCD) is Apple's
high-performance event-handling library, introduced in OS X Snow
Leopard. It provides asynchronous task queues, monitoring of file
descriptor read and write-ability, asynchronous I/O (for sockets and
regular files), readers-writer locks, parallel for-loops, sane signal
handling, periodic timers, semaphores and more.

%package devel
Summary: Development files for libdispatch-objc2
Group: Development/C++
Requires: %name = %EVR

%description devel
libdispatch, aka Grand Central Dispatch (GCD) is Apple's
high-performance event-handling library, introduced in OS X Snow
Leopard. It provides asynchronous task queues, monitoring of file
descriptor read and write-ability, asynchronous I/O (for sockets and
regular files), readers-writer locks, parallel for-loops, sane signal
handling, periodic timers, semaphores and more.

This package contains development files for libdispatch-objc2.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%add_optflags -I%_includedir/kqueue
cd libdispatch
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCMAKE_C_COMPILER:FILEPATH=%_bindir/clang \
	-DCMAKE_CXX_COMPILER:FILEPATH=%_bindir/clang++ \
	.

%make_build VERBOSE=1
 
%install
%makeinstall_std -C libdispatch

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/*.so* %buildroot%_libdir/
%endif

%files
%doc libdispatch/Readme.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_man3dir/*

%changelog
* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20140108
- Initial build for Sisyphus

