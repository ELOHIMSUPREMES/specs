# need because asm used
%set_verify_elf_method textrel=relaxed

%define oname objc2

Name: gnustep-%oname
Version: 1.7.0
Release: alt4.git20130312
Summary: GNUstep Objective-C Runtime
License: BSD
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-libobjc2.git
Source: %name-%version.tar
Source1: Makefile
Patch: gnustep-objc2-1.6.1-alt-i586.patch

BuildRequires(pre): rpm-macros-make
BuildPreReq: gnustep-make-devel gcc-objc gcc-c++ libstdc++-devel
BuildPreReq: cmake llvm-devel clang-devel

%description
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

%package -n lib%name
Summary: Shared libraries of GNUstep Objective-C Runtime
Group: System/Libraries

%description -n lib%name
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains shared libraries of GNUstep Objective-C Runtime.

%package -n lib%name-devel
Summary: Development files of GNUstep Objective-C Runtime
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains development files of GNUstep Objective-C Runtime.

%package -n lib%name-opts
Summary: Shared libraries of GNUstep Runtime Optimisations
Group: System/Libraries

%description -n lib%name-opts
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains shared libraries of GNUstep Runtime Optimisations.

%package -n lib%name-opts-devel
Summary: Development files of GNUstep Runtime Optimisations
Group: Development/Objective-C
Requires: lib%name-opts = %version-%release

%description -n lib%name-opts-devel
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains development files of GNUstep Runtime Optimisations.

%prep
%setup

#ifnarch x86_64
#patch -p1
#endif

cp -fR objc objc2
#chmod +x build_opts.sh

%build
#./build_opts.sh
%add_optflags -I$PWD %optflags_shared -fpermissive
%add_optflags -D__STDC_LIMIT_MACROS -D__STDC_CONSTANT_MACROS
export CPPFLAGS="%optflags"
cmake \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_ASM_FLAGS:STRING="%optflags" \
	-DCMAKE_ASM_COMPILER:FILEPATH='%_bindir/gcc' \
	-DCMAKE_C_COMPILER:FILEPATH='%_bindir/gcc' \
	-DCMAKE_CXX_COMPILER:FILEPATH='%_bindir/g++' \
	-DLLVM_DIR:PATH='%_datadir/CMake/Modules' \
	-DCMAKE_STRIP:FILEPATH='/bin/echo' \
	-DCPACK_STRIP_FILES:BOOL=OFF \
	-DCXX_RUNTIME:FILEPATH='-lpthread -lstdc++' \
	-DGNUSTEP_INSTALL_TYPE:STRING='SYSTEM' \
	-DINCLUDE_DIRECTORY:STRING=objc2 \
	-DLEGACY_COMPAT:BOOL=ON \
	-DLIBOBJC_NAME:STRING=objc2 \
	-DLLVM_ON_UNIX:BOOL=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DTESTS:BOOL=OFF \
	.

%make_build_ext \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	PREFIX=%prefix \
	LIB_DIR=%_libdir \
	HEADER_DIR=%_includedir

%install
cp -f %SOURCE1 GNUmakefile
%make_install \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	PREFIX=%buildroot%prefix \
	LIB_DIR=%buildroot%_libdir \
	HEADER_DIR=%buildroot%_includedir \
	install

sed -i 's|#include "visibility.h"|#include "objc2/visibility.h"|' \
	class.h
install -p -m644 class.h visibility.h method_list.h \
	%buildroot%_includedir/objc2/

%files -n lib%name
%doc ANNOUNCE* API README
%_libdir/*.so.*
%exclude %_libdir/libGNUObjCRuntime.so.*

%files -n lib%name-devel
%_includedir/*
%exclude %_includedir/objc2/opts
%_libdir/*.so
%exclude %_libdir/libGNUObjCRuntime.so

%files -n lib%name-opts
%doc opts/README
%_libdir/libGNUObjCRuntime.so.*

%files -n lib%name-opts-devel
%_includedir/objc2/opts
%_libdir/libGNUObjCRuntime.so

%changelog
* Mon Mar 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt4.git20130312
- Set CMAKE_BUILD_TYPE to Release (ALT #28693)

* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3.git20130312
- New snapshot

* Tue Mar 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3.git20130130
- Rebuilt with clang 3.2

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt2.git20130130
- Back to previous snapshot

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20130301
- New snapshot
- Rebuilt with clang 3.2

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20130130
- Version 1.7.0

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt6.svn20130112
- Avoid use Method_t

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt5.svn20130112
- New snapshot

* Sun Dec 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt5.svn20121223
- New snapshot
- Built with llvm
- Added libGNUObjCRuntime.so

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt4.svn20121115
- Added synonym: lib%name-devel -> %name-devel

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt3.svn20121115
- Rebuilt with fixed gnustep-make

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.svn20121115
- Applied patch only for i586

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.svn20121115
- Initial build for Sisyphus

