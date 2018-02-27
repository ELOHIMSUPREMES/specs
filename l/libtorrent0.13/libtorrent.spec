%define _optlevel s
%define abiversion 0.13

Name: libtorrent%{abiversion}
Epoch: 3
Version: 0.13.2
Release: alt1

Summary: libTorrent is a BitTorrent library written in C++ for *nix
Group: System/Libraries
License: GPLv2+
Url: http://libtorrent.rakshasa.no/
Packager: Alexey Morsov <swi@altlinux.ru>

%define full_version %version
Source0: %name-%version.tar
Patch0: libtorrent0.12-alt-gcc4.6.patch
Patch1: libtorrent-%version-%release.patch

BuildRequires: gcc-c++ libsigc++2.0-devel libssl-devel
BuildRequires: cppunit-devel
Obsoletes: librtorrent <= 0.12.2-alt1

%def_disable static

%description
libTorrent is designed to avoid redundant copying and storing of data
that other clients and libraries suffer from. libTorrent features:

* The client has full control over the polling of sockets.
* Sigc++ signals makes it easy for the client to react to events.
* Fast resume which checks the file modification time.
* Direct reading and writing from network to mmap'ed files.
* File hash check uses the same thread; client can control the rate;
  non-blocking and preload to memory with the mincore and madvise.
* File handler: fine-grained use of file read/write permissions, allows
  seeding of read-only files; allows torrents with unlimited number of
  files; opens closed files when mapping chunks to memory, with graceful
  error handling; support for files larger than 2 GB; different download
  priorities for files in the torrent.
* Multi-tracker support.
* No dependency on any specific HTTP library, the client implements a
  wrapper class.
* Dynamic request pipe size.
* Upload and download throttle.
* And much more...

%package -n libtorrent-devel
Summary: Development libraries and header files for libTorrent
Group: Development/C
Requires: %name = %epoch:%version-%release
Conflicts: libtorrent-rasterbar0.13-devel

%description -n libtorrent-devel
The libtorrent-devel package contains libraries and header files needed
to develop applications using libTorrent.

%prep
%setup -q -n %name-%full_version
%patch0 -p1
%patch1 -p1
mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.la

%files
%doc AUTHORS ChangeLog NEWS README
%doc --no-dereference COPYING

%_libdir/*.so.*

%files -n libtorrent-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 3:0.13.2-alt1
- first build for Sisyphus, based on libtorrent0.12 spec



