%define oname pytest-flask

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20141103
Summary: A set of py.test fixtures to test Flask applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-flask/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vitalk/pytest-flask.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flask python-module-werkzeug
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flask python3-module-werkzeug
%endif

%py_provides pytest_flask

%description
A set of py.test fixtures to test Flask extensions and applications.

Plugin provides some fixtures to simplify app testing:

* client - an instance of app.test_client,
* client_class - client fixture for class-based tests,
* config - you application config,
* accept_json, accept_jsonp, accept_any - accept headers suitable to use
  as parameters in client.

%package -n python3-module-%oname
Summary: A set of py.test fixtures to test Flask applications
Group: Development/Python3
%py3_provides pytest_flask

%description -n python3-module-%oname
A set of py.test fixtures to test Flask extensions and applications.

Plugin provides some fixtures to simplify app testing:

* client - an instance of app.test_client,
* client_class - client fixture for class-based tests,
* config - you application config,
* accept_json, accept_jsonp, accept_any - accept headers suitable to use
  as parameters in client.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README
%python_sitelibdir/*

%if_with python3
%endif
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*

%changelog
* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141103
- Version 0.5.0

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141028
- Initial build for Sisyphus

