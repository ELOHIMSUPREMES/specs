%define oname qmatrixclient

Name: libqmatrixclient
Version: 0.4.2.1
Release: alt1

Summary: A Qt5 library to write cross-platfrom clients for Matrix

License: LGPLv2.1
Group: System/Libraries
Url: https://github.com/QMatrixClient/libqmatrixclient

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/QMatrixClient/libqmatrixclient/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5 rpm-macros-cmake

#BuildRequires(pre): rpm-build-compat >= 2.1.5
#BuildRequires(pre): rpm-build-intro >= 2.1.5
# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
#_tune_parallel_build_by_procsize 3000

BuildRequires: cmake gcc-c++ libstdc++-devel

BuildRequires: qt5-base-devel libqt5-gui libqt5-network

%description
libQMatrixClient is a Qt5-based library to make IM clients for the Matrix protocol.
It is the backbone of Quaternion, Spectral and some other projects.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Header files for %EVR.

%prep
%setup
%__subst "s|add_library(QMatrixClient|add_library(QMatrixClient SHARED|" CMakeLists.txt

%build
%cmake_insource -DCMAKE_INSTALL_INCLUDEDIR=include/qmatrixclient \
                -DQMATRIXCLIENT_INSTALL_EXAMPLE=OFF
%make_build

%install
%makeinstall_std
rm -rfv %buildroot%_bindir/qmc-example

%files
%doc README.md CONTRIBUTING.md
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%oname/
%_libdir/cmake/QMatrixClient/
%_pkgconfigdir/QMatrixClient.pc
#_bindir/qmc-example

%changelog
* Mon Jan 21 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.1-alt1
- initial build for ALT Sisyphus
