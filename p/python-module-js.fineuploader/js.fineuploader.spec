# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20130226.2
%define oname js.fineuploader

%def_with python3

Name: python-module-%oname
Version: 3.3.0
#Release: alt1.git20130226.1
Summary: Fanstatic packaging of Fine Uploader
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.fineuploader/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/disko/js.fineuploader.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires js js.jquery

%description
This library packages Fine Uploader for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of Fine Uploader
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jquery

%description -n python3-module-%oname
This library packages Fine Uploader for fanstatic.

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

cp -fR js/fineuploader/resources \
	%buildroot%python_sitelibdir/js/fineuploader/
%if_with python3
pushd ../python3
cp -fR js/fineuploader/resources \
	%buildroot%python3_sitelibdir/js/fineuploader/
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1.git20130226.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt1.git20130226.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt1.git20130226.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.git20130226
- Initial build for Sisyphus

