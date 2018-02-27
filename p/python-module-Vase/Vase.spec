%define oname Vase

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20140811
Summary: Async Web framework based on Tulip/asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Vase/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vkryachko/Vase.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-enum34 python-module-asyncio-tests
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-enum34 python3-module-asyncio-tests
%endif

%py_provides vase
%py_requires enum34 asyncio

%description
Vase is a webframework for Tulip/asyncio.

Inspired by Flask.
It currently has a basic WSGI interface and WebSocket support.
A demo websocket app is available here http://vase-chat.herokuapp.com/

%package -n python3-module-%oname
Summary: Async Web framework based on Tulip/asyncio
Group: Development/Python3
%py3_provides vase
%py3_requires enum34 asyncio

%description -n python3-module-%oname
Vase is a webframework for Tulip/asyncio.

Inspired by Flask.
It currently has a basic WSGI interface and WebSocket support.
A demo websocket app is available here http://vase-chat.herokuapp.com/

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
python runtests.py -v
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py -v
popd
%endif

%if_with python2
%files
%doc *.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20140811
- Initial build for Sisyphus

