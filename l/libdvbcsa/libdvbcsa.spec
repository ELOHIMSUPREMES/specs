Name: libdvbcsa
Version: 1.1.0
Release: alt4

Summary: DVB Common Scrambling Algorithm with encryption and decryption capabilities
License: GPLv2
Group: System/Libraries
Url: http://www.videolan.org/developers/libdvbcsa.html
Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

%description
libdvbcsa is a free implementation of the DVB Common
Scrambling Algorithm - DVB/CSA - with encryption and
decryption capabilities.
Features
    * Portability. This library has been successfully
      tested on different processors with 32 bits,
      64 bits and 128 bits word width, little-endian
      and big-endian bytes ordering.
    * Performance. It comes in two flavors: a classical
      single packet implementation and a faster parallel
      bitslice implementation.
    * The parallel implementation can take advantages
      of MMX, SSE or Altivec instruction sets. Parallel
      implementation can process Mpeg TS packets at
      300Mbps or more on recent processors.
    * Freedom. libdvbcsa is released under the General
      Public License, ensuring it will stay free, and used
      only for free software products.
    * Simplicity. The API comes with only 5 functions
      fot the single packet implementation, and 6 functions
      for the parallel bitslice implementation.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup
%patch0 -p1

%build
./bootstrap
%configure --enable-sse2
%make

%install
%make_install DESTDIR="%buildroot" install

%files
%doc COPYING README INSTALL AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/dvbcsa
%_libdir/libdvbcsa.so

%changelog
* Sun Mar 01 2015 Alexei Takaseev <taf@altlinux.org> 1.1.0-alt4
- Fix C++ compilation using the library

* Thu Oct 16 2014 Alexei Takaseev <taf@altlinux.org> 1.1.0-alt3
- Enable SSE2

* Sat Aug 30 2014 Alexei Takaseev <taf@altlinux.org> 1.1.0-alt2
- Disable SSE

* Tue Apr 29 2014 Alexei Takaseev <taf@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux Sisyphus.
