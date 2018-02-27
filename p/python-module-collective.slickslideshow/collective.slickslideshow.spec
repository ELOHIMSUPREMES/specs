%define mname collective
%define oname %mname.slickslideshow
Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141106
Summary: Slick Slideshow solution for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.slickslideshow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/intk/collective.slickslideshow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-PasteScript
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-collective.slideshow
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.slideshow Products.CMFPlone plone.theme
%py_requires zope.component zope.interface

%description
Slick Slideshow solution for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Slick Slideshow solution for Plone.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
export PYTHONPATH=$PWD
python collective/slickslideshow/tests.py

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141106
- Initial build for Sisyphus

