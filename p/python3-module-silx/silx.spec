%define _unpackaged_files_terminate_build 1

%define oname silx

Name: python3-module-%oname
Version: 0.10.1
Release: alt1
Summary: Software library for X-Ray data analysis
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/silx

# https://github.com/silx-kit/silx.git
Source: %name-%version.tar

# Until upstream issue is fixed: https://github.com/silx-kit/silx/issues/2029
Patch1: silx-alt-skip-broken-test.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libgomp-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: libnumpy-py3-devel python3(sphinx) python3(h5py)
BuildRequires: python3-module-Cython
BuildRequires: python3(scipy)
# for tests
BuildRequires: python3(fabio)

# circumvent build failures due to relying on headers from libnumpy-devel
BuildRequires: libnumpy-devel

%add_python3_req_skip pyopencl pyopencl.array pyopencl.elementwise
%py3_requires scipy.spatial

%description
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

This package contains tests for %oname.

%package examples
Summary: Examples for %oname
Group: Development/Python3
Requires: %name = %EVR

%description examples
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

This package contains examples for %oname.

%prep
%setup
%patch1 -p1

# remove some third-party bundled stuff
rm -rf silx/third_party/_local

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc CHANGELOG.rst README.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/%oname/*/test
%exclude %python3_sitelibdir/%oname/*/*/test
%exclude %python3_sitelibdir/%oname/*/*/*/test
%exclude %python3_sitelibdir/%oname/*/testutils.*
%exclude %python3_sitelibdir/%oname/*/*/testutils.*
%exclude %python3_sitelibdir/%oname/*/*/*/testutils.*
%exclude %python3_sitelibdir/%oname/*/test_.*
%exclude %python3_sitelibdir/%oname/*/*/test_.*
%exclude %python3_sitelibdir/%oname/examples

%files tests
%python3_sitelibdir/%oname/test
%python3_sitelibdir/%oname/*/test
%python3_sitelibdir/%oname/*/*/test
%python3_sitelibdir/%oname/*/*/*/test
%python3_sitelibdir/%oname/*/testutils.*
%python3_sitelibdir/%oname/*/*/testutils.*
%python3_sitelibdir/%oname/*/*/*/testutils.*
%python3_sitelibdir/%oname/*/test_.*
%python3_sitelibdir/%oname/*/*/test_.*

%files examples
%python3_sitelibdir/%oname/examples

%changelog
* Mon Apr 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.1-alt1
- Updated to latest upstream release.
- Disabled build for python-2.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Initial build for ALT.
