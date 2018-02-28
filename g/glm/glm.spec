Name: glm
Version: 0.9.7.6
Release: alt1
License: MIT
Summary: GLM is a header only C++ mathematics library for graphics software based on the GLSL specification
Group: Development/C++
Url: http://glm.g-truc.net/
BuildRequires: gcc-c++ cmake ctest

Source: %version.tar.gz

%package -n lib%name-devel
Summary: GLM is a header only C++ mathematics library for graphics software based on the GLSL specification
Group: Development/C++
BuildArch: noarch

%package -n lib%name-devel-doc
Summary: Documentation for OpenGL Mathematics (GLM) library
Group: Development/Documentation
BuildArch: noarch
Requires: lib%name-devel = %version-%release

%description
C++ library for OpenGL GLSL type-based mathematics OpenGL Mathematics
(GLM) is a header only C++ mathematics library for graphics software
based on the OpenGL Shading Language (GLSL) specification.

GLM provides classes and functions designed and implemented with the
same naming conventions and functionalities as GLSL, so that when a
programmer knows GLSL, he knows GLM as well, which makes it easy to use.

This project isn't limited to GLSL features. An extension system, based
on the GLSL extension conventions, provides extended capabilities:
matrix transformations, quaternions, half-based types, random nums, etc.

%description -n lib%name-devel
C++ library for OpenGL GLSL type-based mathematics OpenGL Mathematics
(GLM) is a header only C++ mathematics library for graphics software
based on the OpenGL Shading Language (GLSL) specification.

GLM provides classes and functions designed and implemented with the
same naming conventions and functionalities as GLSL, so that when a
programmer knows GLSL, he knows GLM as well, which makes it easy to use.

This project isn't limited to GLSL features. An extension system, based
on the GLSL extension conventions, provides extended capabilities:
matrix transformations, quaternions, half-based types, random nums, etc.

Header files for GLM library.

%description -n lib%name-devel-doc
Documentation for the OpenGL Mathematics (GLM) library.
OpenGL Mathematics (GLM) is a header only C++ mathematics library for
graphics software based on the OpenGL Shading Language (GLSL) specs.

This package contains the GLM in HTML and PDF formats.

%prep
%setup

%build
%cmake -DGLM_TEST_ENABLE=True -DGLM_TEST_ENABLE_CXX_11=True -DCMAKE_CXX_FLAGS="-std=c++11" -DCMAKE_VERBOSE_MAKEFILE=True
%ifarch %ix86
# Thees tests fail on GCC up to 5.2.1
sed -i 's/-O[0-9]/-O0/' BUILD/test/core/CMakeFiles/test-core_func_exponential.dir/flags.make
sed -i 's/-O[0-9]/-O0/' BUILD/test/gtc/CMakeFiles/test-gtc_packing.dir/flags.make
%endif
%cmake_build

%install
mkdir -p %buildroot%_includedir
cp -a glm %buildroot%_includedir
rm %buildroot%_includedir/glm/CMakeLists.txt
mkdir -p %buildroot%_docdir/lib%name-devel/
cp -a copying.txt readme.md doc/*.pdf doc/api/ %buildroot%_docdir/lib%name-devel/

%check
%make_build -C BUILD test

%files -n lib%name-devel
%_includedir/%name/
%dir %_docdir/lib%name-devel/
%_docdir/lib%name-devel/copying.txt
%_docdir/lib%name-devel/readme.md

%files -n lib%name-devel-doc
%dir %_docdir/lib%name-devel/
%_docdir/lib%name-devel/*.pdf
%_docdir/lib%name-devel/api/

%changelog
* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.9.7.6-alt1
- Autobuild version bump to 0.9.7.6

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 0.9.7.5-alt1
- Autobuild version bump to 0.9.7.5

* Wed Sep 16 2015 Fr. Br. George <george@altlinux.ru> 0.9.7.1-alt1
- Autobuild version bump to 0.9.7.1
- Provide tests

* Mon Jul 30 2012 Ivan Ovcherenko <asdus@altlinux.org> 0.9.3.4-alt1
- initial build for ALT Linux Sisyphus
