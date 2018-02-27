%define mname scikits
%define oname %mname.fitting

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt2.git20121029
Summary: Framework for fitting functions to data with SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.fitting/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ludwigschwardt/scikits.fitting.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scipy libnumpy-devel
BuildPreReq: python-module-matplotlib python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-matplotlib python3-module-nose
%endif

%py_provides %oname
%py_requires %mname numpy scipy matplotlib scikits.delaunay

%description
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose

%description tests
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Framework for fitting functions to data with SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy matplotlib

%description -n python3-module-%oname
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose

%description -n python3-module-%oname-tests
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/fitting
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/fitting/tests

%files tests
%python_sitelibdir/%mname/fitting/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/fitting
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/fitting/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/fitting/tests
%endif

%changelog
* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2.git20121029
- Rebuilt with updated NumPy

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20121029
- Initial build for Sisyphus

