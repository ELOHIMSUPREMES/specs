%define oname pyramid

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.6
Release: alt2.dev.git20141110
Summary: Small, fast, down-to-earth Python web application development framework
License: Repoze Public License
Group: Development/Python
Url: http://pylonsproject.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-PasteDeploy python-module-translationstring
BuildPreReq: python-module-venusian python-module-zope.deprecation
BuildPreReq: python-module-zope.interface python-module-repoze.lru
BuildPreReq: python-module-webob python-module-mako
BuildPreReq: python-module-chameleon.core python-module-markupsafe
BuildPreReq: python-module-zope.component python-module-virtualenv
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-webtest python-module-zope.event
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-PasteDeploy python3-module-translationstring
BuildPreReq: python3-module-venusian python3-module-zope.deprecation
BuildPreReq: python3-module-zope.interface python3-module-repoze.lru
BuildPreReq: python3-module-webob python3-module-mako
BuildPreReq: python3-module-chameleon.core python3-module-markupsafe
BuildPreReq: python3-module-zope.component python3-module-virtualenv
BuildPreReq: python3-module-repoze.sphinx.autointerface
BuildPreReq: python3-module-webtest python3-module-zope.event
%endif

%py_requires paste.deploy repoze.lru zope.deprecation zope.component

%description
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

%if_with python3
%package -n python3-module-%oname
Summary: Small, fast, down-to-earth Python 3 web application development framework
Group: Development/Python3
%py3_requires paste.deploy repoze.lru zope.deprecation zope.component

%description -n python3-module-%oname
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

%package -n python3-module-%oname-tests
Summary: Tests for Pyramid (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains tests for Pyramid.
%endif

%package tests
Summary: Tests for Pyramid
Group: Development/Python
Requires: %name = %version-%release

%description tests
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains tests for Pyramid.

%package pickles
Summary: Pickles for Pyramid
Group: Development/Python

%description pickles
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains pickles for Pyramid.

%package docs
Summary: Documentation for Pyramid
Group: Development/Documentation

%description docs
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains documentation for Pyramid.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install

export PYTHONPATH=%python_sitelibdir:%buildroot%python_sitelibdir
pushd docs
%make pickle
%make html
cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/py3_*
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/test*
%exclude %python_sitelibdir/%oname/*/test*

%files tests
%python_sitelibdir/%oname/test*
%python_sitelibdir/%oname/*/test*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*
%exclude %python3_sitelibdir/%oname/__pycache__/testing.*
%exclude %python3_sitelibdir/%oname/*/test*
%exclude %python3_sitelibdir/%oname/*/__pycache__/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test*
%python3_sitelibdir/%oname/__pycache__/testing.*
%python3_sitelibdir/%oname/*/test*
%python3_sitelibdir/%oname/*/__pycache__/test*
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.dev.git20141110
- New snapshot

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.dev.git20141020
- Added some other requirements

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.dev.git20141020
- New snapshot
- Added necessary requirements

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.dev.git20140728
- New snapshot

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.dev.git20140714
- Version 1.6dev

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.a2.git20131127
- Version 1.5a2

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.a1.git20130915
- Version 1.5a1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.4-alt2.git20130105.1
- Rebuild with Python-3.3

* Mon Jan 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.git20130105
- New snapshot

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20120503
- New snapshot
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20111212
- Version 1.4dev

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.a0.git20110513.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.a0.git20110513
- Initial build for Sisyphus

