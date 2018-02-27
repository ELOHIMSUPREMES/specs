%define oname smmap

%def_with python3

Name: python-module-%oname
Version: 0.8.2
Release: alt1.git20140714

Summary:  Sliding window memory map manager

License: BSD
Group: Development/Python
Url: git://github.com/Byron/smmap.git

Source: %name-%version.tar
Patch: smmap-alt-docs.patch

%setup_python_module %oname

BuildRequires: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildArch: noarch

%description
A pure python implementation of a sliding window memory map manager

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A pure python implementation of a sliding window memory map manager

This package contains tests for %oname.

%package -n python3-module-%oname
Summary:  Sliding window memory map manager
Group: Development/Python3

%description -n python3-module-%oname
A pure python implementation of a sliding window memory map manager

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A pure python implementation of a sliding window memory map manager

This package contains tests for %oname.

%prep
%setup
%patch -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONOPATH=%buildroot%python_sitelibdir
%make -C doc html

%files
%doc README.md doc/build/html
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/test
%python_sitelibdir/*.egg-info

%files tests
%python_sitelibdir/%modulename/test

%if_with python3
%files -n python3-module-%oname
%doc README.md doc/build/html
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/test
%python3_sitelibdir/*.egg-info

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/test
%endif

%changelog
* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140714
- New snapshot
- Added module for Python 3

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- initial
