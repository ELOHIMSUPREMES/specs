Name:           libnftnl
Version:        1.0.0
Release:        alt2
Summary:        Netfilter nf_tables infrastructure library
Group:          System/Libraries
License:        LGPLv2.1+
URL:            http://netfilter.org/projects/libmnl
Source:        %name-%version.tar
BuildRequires: libmnl-devel libmxml-devel libjansson-devel

%description
libnftnl is a userspace library providing a low-level netlink programming interface (API) to the
in-kernel nf_tables subsystem. The library libnftnl has been previously known as libnftables.
This library is currently used by nftables.

%package	devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, %name = %version-%release

%description   devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package	devel-static
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, %name = %version-%release

%description   devel-static
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package	examples
Summary:        Examples for %name
Group:          System/Libraries

%description	examples
The %name-examples package contains examples files for %name.


%prep
%setup

%build
%autoreconf
%configure --with-xml-parsing --with-json-parsing --enable-static
%make_build

%check
%make check
pushd tests
    ./test-script.sh
popd
mkdir -p %buildroot%_sbindir
cp examples/.libs/* %buildroot%_sbindir/

%install
%makeinstall_std

%files
%doc COPYING
%_libdir/%name.so.*

%files devel
%_libdir/*.so
%_includedir/%name
%_libdir/pkgconfig/*.pc

%files devel-static
%_libdir/*.a

%files examples
%doc examples/*.c
%_sbindir/*

%changelog
* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt2
- move examples to own package

* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- first build for ALT Linux
