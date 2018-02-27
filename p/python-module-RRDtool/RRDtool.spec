%define oname RRDtool

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20141011
Summary: rrdtool bindings for Python
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/rrdtool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/commx/python-rrdtool.git
Source: %name-%version.tar

BuildPreReq: librrd-devel
BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname rrdtool
Conflicts: python-module-rrd python-module-rrdtool

%description
rrdtool binding for Python 2.6+ and 3.3+.

This bindings are based on the original Python rrdtool bindings from
Hye-Shik Chang and are slightly modified to support Python 3.3+ and 2.6+
in the same code base.

%package -n python3-module-%oname
Summary: rrdtool bindings for Python
Group: Development/Python3
%py3_provides %oname rrdtool
Conflicts: python3-module-rrd python3-module-rrdtool

%description -n python3-module-%oname
rrdtool binding for Python 2.6+ and 3.3+.

This bindings are based on the original Python rrdtool bindings from
Hye-Shik Chang and are slightly modified to support Python 3.3+ and 2.6+
in the same code base.

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

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141011
- Initial build for Sisyphus

