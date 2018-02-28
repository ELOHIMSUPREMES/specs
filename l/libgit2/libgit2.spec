Name: libgit2
Version: 0.23.4
Release: alt1

Summary: linkable library for Git
License: GPLv2 with linking exception

Group: System/Libraries
URL: http://libgit2.github.com

Source: %name-%version.tar.gz

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake python-modules zlib-devel libssl-devel libssh2-devel libcurl-devel

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing you
to write native speed custom Git applications in any language which
supports C bindings.

%package devel
Group: Development/C
Summary: linkable library for Git - development files
Requires: %name = %version-%release

%description devel
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing you
to write native speed custom Git applications in any language which
supports C bindings.
This package contains development files.

%prep
%setup
rm -rf deps/{regex,zlib}
sed -i 's/LIB_INSTALL_DIR lib/LIB_INSTALL_DIR lib${LIB_SUFFIX}/' CMakeLists.txt
sed -i 's/@CMAKE_INSTALL_PREFIX@\///' %name.pc.in

%build
%cmake -DTHREADSAFE:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/%name.so.*
%doc README.md AUTHORS COPYING

%files devel
%_includedir/git2
# exclude headers for windows
%exclude %_includedir/git2/inttypes.h
%exclude %_includedir/git2/stdint.h
%_includedir/git2.h
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.4-alt1
- 0.23.4

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.3-alt1
- 0.23.3

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.2-alt1
- 0.23.2

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.2-alt1
- 0.22.2

* Sun Jan 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0
- enabled ssh support via libssh2

* Wed Jan 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.4-alt1
- 0.21.4

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.2-alt1
- 0.21.2

* Tue Jul 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt2
- built as threadsafe

* Mon Jun 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0_16e7596d

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Jul 23 2013 Alexey Shabalin <shaba@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Sun Oct 21 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17.0-alt1.c497a6
- git snapshot c497a6

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17.0-alt1
- initial release
