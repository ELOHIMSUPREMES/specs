%define mname xstatic
%define oname %mname-twikidraw-moin

%def_with python3

Name: python-module-%oname
Version: 2004.10.23.2
Release: alt1
Summary: TWikiDraw-moin 2004.10.23 (XStatic packaging standard)
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-TWikiDraw-moin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.twikidraw_moin
%py_requires %mname.pkg

%description
TWikiDraw-moin java library packaged for setuptools (easy_install) /
pip.

This is a modified version from TWikiDrawPlugin of 29 Jan 2003 - 21:47
adding:

* basename argument
* indexed PNG support
* deprecated name attribute of the <map> tag replaced by the id
  attribute
* corrects object stacking order for the map

This package is intended to be used by any project that needs these
files.

%package -n python3-module-%oname
Summary: TWikiDraw-moin 2004.10.23 (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.twikidraw_moin
%py3_requires %mname.pkg

%description -n python3-module-%oname
TWikiDraw-moin java library packaged for setuptools (easy_install) /
pip.

This is a modified version from TWikiDrawPlugin of 29 Jan 2003 - 21:47
adding:

* basename argument
* indexed PNG support
* deprecated name attribute of the <map> tag replaced by the id
  attribute
* corrects object stacking order for the map

This package is intended to be used by any project that needs these
files.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2004.10.23.2-alt1
- Initial build for Sisyphus

