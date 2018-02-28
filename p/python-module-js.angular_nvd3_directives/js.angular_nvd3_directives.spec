# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.2.1
%define oname js.angular_nvd3_directives

%def_with python3

Name: python-module-%oname
Version: 2.3.11
#Release: alt1.2
Summary: Fanstatic packaging of angularjs-nvd3-directives
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.angular_nvd3_directives/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-fanstatic python-module-js.angular
#BuildPreReq: python-module-js.nvd3 python-module-shutilwhich
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-fanstatic python3-module-js.angular
#BuildPreReq: python3-module-js.nvd3 python3-module-shutilwhich
%endif

%py_provides %oname
%py_requires js js.angular js.nvd3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-fanstatic python-module-js python-module-js.d3 python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-module-shutilwhich python-module-webob python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-fanstatic python3-module-js python3-module-js.d3 python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools python3-module-webob xz
BuildRequires: python-module-js.angular python-module-js.nvd3 python-module-setuptools-tests python3-module-js.angular python3-module-js.nvd3 python3-module-setuptools-tests rpm-build-python3 time

%description
This library packages angularjs-nvd3-directives for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of angularjs-nvd3-directives
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.angular js.nvd3

%description -n python3-module-%oname
This library packages angularjs-nvd3-directives for fanstatic.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.11-alt1.2.1
- (AUTO) subst_x86_64.

* Tue Mar 15 2016 Denis Medvedev <nbr@altlinux.org> 2.3.11-alt1.2
- NMU just rebuild.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.11-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt1
- Initial build for Sisyphus

