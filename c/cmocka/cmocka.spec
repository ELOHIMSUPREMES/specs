%def_disable static
%def_with doc

Name: cmocka
Version: 1.1.3
Release: alt2

Summary: Lightweight library to simplify and generalize unit tests for C
License: ASL 2.0
Group: Development/Tools

Url: http://cmocka.org
Source: %name-%version.tar

BuildRequires: cmake ctest
BuildRequires: doxygen
BuildRequires: glibc-devel

%description
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

Cmocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka
Group: System/Libraries
Summary: Lightweight library to simplify and generalize unit tests for C

%description -n libcmocka
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

CMocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka-devel-static
Group: Development/C
Summary: Lightweight library to simplify and generalize unit tests for C

%description -n libcmocka-devel-static
Static version of the cmocka library.

%package -n libcmocka-devel
Group: Development/C
Summary: Development headers for the cmocka library
Requires: libcmocka = %version-%release

%description -n libcmocka-devel
Development headers for the cmocka unit testing library.

%prep
%setup

%build
%cmake \
%if_enabled static
  -DWITH_STATIC_LIB=ON \
%else
  -DWITH_STATIC_LIB=OFF \
%endif
  -DUNIT_TESTING=ON


%cmake_build VERBOSE=1
%if_with doc
# BR: cmake >= 3.9
%cmake_build docs
%endif

%install
%cmakeinstall_std

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%cmake_build  test

%files -n libcmocka
%doc AUTHORS README.md ChangeLog COPYING
%_libdir/*.so.*

%files -n libcmocka-devel
%if_with doc
%doc BUILD/doc/html
%endif
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/cmocka/*.cmake

%if_enabled static
%files -n libcmocka-devel-static
%_libdir/*.a
%endif

%changelog
* Sat Apr 06 2019 Michael Shigorin <mike@altlinux.org> 1.1.3-alt2
- introduce doc knob (on by default)

* Thu Mar 21 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.1.3-alt1
- 1.1.3

* Mon Dec 03 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.1.1-alt2
- Disable ubt macros due binary package identity changes

* Mon Apr 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.1-alt1%ubt
- 1.1.1
- Build package with unified build tag aka ubt macros

* Mon Apr 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Jun 11 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Fri Mar 14 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt3
- rename libcmocka-static to libcmocka-devel-static
- disable build static lib

* Wed Feb 19 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt2
- increased release for Obsoletes package from Autoimports/Sisyphus

* Tue Feb 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- initial build
