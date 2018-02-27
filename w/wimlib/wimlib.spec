%define libname libwim
Name: wimlib
Version: 1.4.2
Release: alt1

Summary: Library to extract, create, modify, and mount WIM files

License: GPLv3+
Group: System/Libraries
Url: http://sourceforge.net/projects/wimlib

Source: http://prdownloads.sourceforge.net/wimlib/wimlib-%version.tar

# manually removed: glibc-devel-static  ruby ruby-stdlibs  python3
# Automatically added by buildreq on Thu Aug 29 2013
# optimized out: libntfs-3g pkg-config python3-base
BuildRequires: libattr-devel libfuse-devel libntfs-3g-devel libssl-devel libxml2-devel

%description
wimlib is a C library for creating, extracting, modifying, and mounting files in
the Windows Imaging Format (WIM files).  It is similar to Microsoft's WIMGAPI
but is designed for both UNIX and Windows.

%package -n %libname
Summary: Library to extract, create, modify, and mount WIM files
Group: System/Libraries

%description -n %libname
wimlib is a C library for creating, extracting, modifying, and mounting files in
the Windows Imaging Format (WIM files).  It is similar to Microsoft's WIMGAPI
but is designed for both UNIX and Windows.

%package -n %libname-devel
Summary: Development files for wimlib
Group: Development/Other
Requires: %libname = %version-%release

%description -n %libname-devel
Development files for wimlib.

%package -n wimtools
Summary: Tools to create, extract, modify, and mount WIM files
Group: File tools
Requires: %libname = %version-%release

%description -n wimtools
Tools to create, extract, modify, and mount files in the Windows Imaging Format
(WIM files).  These files are normally created by using the `imagex.exe' utility
on Windows, but this package contains a free implementation of ImageX called
"wimlib-imagex" that is designed to work on both UNIX and Windows.

%prep
%setup -n %name-%version

%build
# helps with rpath
%autoreconf

%configure \
           --disable-static		\
           --disable-rpath		\
	   --with-libcrypto		\
	   --with-ntfs-3g		\
	   --with-fuse			\
	   --enable-xattr
%make_build

%install
%makeinstall_std

#%check
#make check

%files -n %libname
%doc AUTHORS README
%_libdir/libwim.so.*

%files -n wimtools
%_bindir/wimlib-imagex
%_bindir/imagex
%_bindir/mkwinpeimg
%_man1dir/*

%files -n %libname-devel
#%_libdir/libwim.a
%_libdir/libwim.so
#%exclude %_libdir/libwim.la
%_includedir/wimlib.h
%_pkgconfigdir/wimlib.pc

%changelog
* Thu Aug 29 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- initial build for ALT Linux Sisyphus

