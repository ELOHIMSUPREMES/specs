
Name: deepsolver
Version: 0.1.0
Release: alt1

Packager: Michael Pozhidaev <msp@altlinux.ru>
License: GPL v2+
URL: http://deepsolver.org

Summary: The package manager
Group: System/Configuration/Packaging

Source: %name-%version.tar.gz

BuildRequires: gcc-c++ librpm-devel libcurl-devel zlib-devel

%package -n lib%name
Summary: The dynamically linked library with Deepsolver functions
Group: System/Libraries

%package -n lib%name-devel
Summary: C/C++ development files for lib%name
Group: Development/C
Requires: lib%name 

%package -n lib%name-devel-static
Summary: The static library with Deepsolver functions
Group: Development/C
Requires: lib%name-devel 

%package repo
Summary: The utilities for Deepsolver repository administration
Group: System/Configuration/Packaging
Requires: %name

%description
Deepsolver is a package manipulation tool for GNU/Linux system. It
basically designed for ALT Linux RPM environment but in hope it can be
useful for other distributions or even for other package managers.

Main design goals include flexibility, reliability and small execution
time. The core system for package dependency processing is based on
robust 2-SAT algorithm. The tool aims to be a useful instrument both for
users and system administrators. It also includes features to be
appropriate for ALT Linux package building environment.

%description -n lib%name
Deepsolver is a package manipulation tool for GNU/Linux system. It
basically designed for ALT Linux RPM environment but in hope it can be
useful for other distributions or even for other package managers.

Main design goals include flexibility, reliability and small execution
time. The core system for package dependency processing is based on
robust 2-SAT algorithm. The tool aims to be a useful instrument both for
users and system administrators. It also includes features to be
appropriate for ALT Linux package building environment.

This package contains the dynamically linked library with Deepsolver functions

%description -n lib%name-devel
C/C++ development files for lib%name.

%description -n lib%name-devel-static
The static library with Deepsolver functions.

%description repo
This package contains set of utilities purposed for various tasks of
Deepsolver repository administration. With these utilities you can
create new repository and change set of packages in it. Deepsolver
supports package including/excluding without full reconstruction of
repository index data what significantly reduces time.

%prep
%setup -q
%build
%__libtoolize
%autoreconf
%configure
%make_build

%install
make DESTDIR=%buildroot install 

%__rm -f %buildroot%_libdir/lib%name.la

%files
%doc AUTHORS COPYING NEWS README

%files -n lib%name
%_libdir/lib%name-*.so*

%files -n lib%name-devel
%_libdir/lib%name.so

%files -n lib%name-devel-static
%_libdir/lib%name.a

%files repo
%_bindir/ds-repo
%_bindir/ds-patch
%_bindir/ds-provides

%changelog
* Fri Sep 28 2012 Michael Pozhidaev <msp@altlinux.ru> 0.1.0-alt1
-Initial package 

