Name: libheif
Version: 1.4.0
Release: alt1
Summary: HEIF file format decoder and encoder
License: LGPLv3
Group: System/Libraries
Url: https://github.com/strukturag/libheif
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libde265-devel libjpeg-devel libpng-devel libx265-devel libgdk-pixbuf-devel

%description
HEIF is a new image file format employing HEVC (h.265) image coding for the
best compression ratios currently possible.

%package devel
Group: Development/C
Summary:  Development libraries for %name

%description devel
Development libraries for %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_libdir/%name.so.*
%_libdir/gdk-pixbuf-2.0/2.10.0/loaders/*.so*
%_datadir/mime/packages/heif.xml
%_datadir/thumbnailers/heif.thumbnailer

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Mar 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Aug 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1.S1
- 1.3.2

* Tue Jun 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.S1
- rebuild with libva 2.1.0

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- initial release
