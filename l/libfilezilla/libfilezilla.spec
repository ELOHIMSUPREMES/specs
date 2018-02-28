Name: libfilezilla
Version: 0.5.3
Release: alt1
Summary: Small and modern C++ library
License: GPLv2+
Group: System/Libraries
Url: https://lib.filezilla-project.org/
Source0: http://sourceforge.net/projects/filezilla/files/%name/%version/%name-%version.tar.bz2

# Automatically added by buildreq on Wed Mar 30 2016
# optimized out: fontconfig fonts-bitmap-misc gnu-config libstdc++-devel libwayland-client libwayland-server
BuildRequires: cppunit-devel doxygen gcc-c++ graphviz

%description
libfilezilla is a free, open source C++ library, offering some basic
functionality to build high-performing, platform-independent programs.
Some of the highlights include:

* A typesafe, multi-threaded event system that's very simple to use yet
  extremely efficient.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their
  accuracy, which simplifies dealing with timestamps originating from
  different sources.
* Simple process handling for spawning child processes with redirected
  I/O.

%package -n libfilezilla0
Summary: Small and modern C++ library
Group: System/Libraries

%description -n	libfilezilla0
libfilezilla is a free, open source C++ library, offering some basic
functionality to build high-performing, platform-independent programs.
Some of the highlights include:

* A typesafe, multi-threaded event system that's very simple to use yet
  extremely efficient.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their
  accuracy, which simplifies dealing with timestamps originating from
  different sources.
* Simple process handling for spawning child processes with redirected
  I/O.

%package devel
Summary: Development package for %name
Group: Development/C++
Requires: libfilezilla0 = %version-%release

%description devel
Header files for development with %name.

%prep
%setup

%build
%configure \
	--disable-static \
	#
%make_build

pushd doc
make html
popd

%install
%makeinstall_std

find %buildroot -name '*.la' -delete

%check
LC_ALL=en_US.UTF-8 make check

%files -n libfilezilla0
%doc AUTHORS ChangeLog NEWS README
%_libdir/%name.so.0*

%files devel
%doc AUTHORS ChangeLog NEWS README
%doc doc/doxygen-doc/*
%_includedir/%name/
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Mon Jun 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Thu Jun 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Wed May 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Wed Mar 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0.1-alt1
- Initial build.
