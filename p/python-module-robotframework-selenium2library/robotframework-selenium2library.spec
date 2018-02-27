%define oname robotframework-selenium2library

%def_with python3

Name: python-module-%oname
Version: 1.7
Release: alt1.dev.git20150217
Summary: Web testing library for Robot Framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-selenium2library/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rtomac/robotframework-selenium2library.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-decorator
BuildPreReq: python-module-selenium python-module-robotframework
BuildPreReq: python-module-docutils
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests python3-module-decorator
BuildPreReq: python3-module-selenium python3-module-robotframework
BuildPreReq: python3-module-docutils
BuildPreReq: python-tools-2to3
%endif

%description
Selenium2Library is a web testing library for Robot Framework that
leverages the Selenium 2 (WebDriver) libraries.

%package -n python3-module-%oname
Summary: Web testing library for Robot Framework
Group: Development/Python3

%description -n python3-module-%oname
Selenium2Library is a web testing library for Robot Framework that
leverages the Selenium 2 (WebDriver) libraries.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst doc/*.html demo
%python_sitelibdir/Selenium2Library
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst doc/*.html demo
%python3_sitelibdir/Selenium2Library
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev.git20150217
- Version 1.7.dev
- Added module for Python 3

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141102
- Version 1.6.0

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141008
- Initial build for Sisyphus

