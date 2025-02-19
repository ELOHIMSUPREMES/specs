%define _unpackaged_files_terminate_build 1

Name: blosc
Version: 1.15.1
Release: alt2
Summary: Blosc: A blocking, shuffling and lossless compression library
License: MIT
Group: System/Libraries
Url: http://www.blosc.org/

Source: %name-%version.tar
Patch1: %name-%version-alt-pkgconfigdir.patch

BuildRequires: cmake gcc-c++ libsnappy-devel zlib-devel liblz4-devel libzstd-devel

%description
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

%package -n lib%name
Summary: Blosc: A blocking, shuffling and lossless compression library
Group: System/Libraries

%description -n lib%name
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

%package -n lib%name-devel
Summary: Development files of Blosc library
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

This package contains development files of Blosc library.

%prep
%setup
%patch1 -p1

# remove bundled libraries
rm -rf internal-complibs

%build
%cmake \
	-DBUILD_BENCHMARKS:BOOL=OFF \
	-DBUILD_TESTS:BOOL=OFF \
	-DBUILD_STATIC:BOOL=OFF \
	-DPREFER_EXTERNAL_LZ4:BOOL=ON \
	-DPREFER_EXTERNAL_SNAPPY:BOOL=ON \
	-DPREFER_EXTERNAL_ZLIB:BOOL=ON \
	-DPREFER_EXTERNAL_ZSTD:BOOL=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc *.rst
%_libdir/libblosc.so.*

%files -n lib%name-devel
%_includedir/blosc.h
%_includedir/blosc-export.h
%_libdir/libblosc.so
%_pkgconfigdir/blosc.pc

%changelog
* Tue Mar 26 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15.1-alt2
- Rebuilt with system libraries (Closes: #36400)

* Sat Dec 29 2018 Alexey Melyashinsky <bip@altlinux.org> 1.15.1-alt1
- Updated to upstream release version 1.15.1.

* Thu Nov 15 2018 Alexey Melyashinsky <bip@altlinux.org> 1.14.4-alt1
- Updated to upstream release version 1.14.4.

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.1-alt1
- Updated to upstream release version 1.12.1.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.dev.git20150428
- Version 1.6.1.dev

* Wed Jun 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20140611
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20140501
- Initial build for Sisyphus
