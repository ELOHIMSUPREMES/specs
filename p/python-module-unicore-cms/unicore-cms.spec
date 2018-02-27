%define oname unicore-cms

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 1.0.4
Release: alt1
Summary: JSON based CMS for Universal Core
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unicore-cms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-pyramid_chameleon
BuildPreReq: python-module-pyramid_debugtoolbar python-module-memcached
BuildPreReq: python-module-pyramid_beaker python-module-waitress
BuildPreReq: python-module-webtest python-module-cornice
BuildPreReq: python-module-praekelt_pyramid_celery python-module-babel
BuildPreReq: python-module-pyramid_redis python-module-lingua
BuildPreReq: python-module-arrow python-module-markdown
BuildPreReq: python-module-raven python-module-elastic-git
BuildPreReq: python-module-slugify python-module-pyramid_mako
BuildPreReq: python-module-GitDB python-module-mako
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-pyramid_chameleon
BuildPreReq: python3-module-pyramid_debugtoolbar python3-module-memcached
BuildPreReq: python3-module-pyramid_beaker python3-module-waitress
BuildPreReq: python3-module-webtest python3-module-cornice
BuildPreReq: python3-module-praekelt_pyramid_celery python3-module-babel
BuildPreReq: python3-module-pyramid_redis python3-module-lingua
BuildPreReq: python3-module-arrow python3-module-markdown
BuildPreReq: python3-module-raven python3-module-elastic-git
BuildPreReq: python3-module-slugify
%endif

%py_provides cms
%py_provides unicore
Conflicts: python-module-django-cms3.0
Conflicts: python-module-django-cms2.3
Conflicts: python-module-django-cms

%description
JSON based CMS for Universal Core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JSON based CMS for Universal Core.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: JSON based CMS for Universal Core
Group: Development/Python3
%py3_provides cms
%py3_provides unicore
Conflicts: python3-module-django-cms3.0
Conflicts: python3-module-django-cms2.3
Conflicts: python3-module-django-cms

%description -n python3-module-%oname
JSON based CMS for Universal Core.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JSON based CMS for Universal Core.

This package contains tests for %oname.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus

