%define oname thumbor
Name: python-module-%oname
Version: 4.11.1
Release: alt1.git20150310
Summary: thumbor is an open-source photo thumbnail service by globo.com
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/thumbor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thumbor/thumbor.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests libvpx-devel
BuildPreReq: python-module-tornado python-module-pycrypto
BuildPreReq: python-module-pycurl python-module-Pillow
BuildPreReq: python-module-derpconf python-module-libmagic
BuildPreReq: python-module-pexif python-module-simplejson
BuildPreReq: python-module-pymongo python-module-redis-py
BuildPreReq: python-module-gevent python-module-pyvows-tests
BuildPreReq: python-module-preggy python-module-tornado_pyvows
BuildPreReq: python-module-coverage python-module-mock
BuildPreReq: python-module-raven python-module-nose
BuildPreReq: python-module-colorama libnumpy-devel
BuildPreReq: python-module-certifi python-module-opencv
BuildPreReq: python-module-unidecode python-module-pymongo-gridfs
BuildPreReq: python-module-statsd python-module-libthumbor

%py_provides %oname
Requires: python-module-pexif python-module-libmagic
%py_requires statsd libthumbor

%description
Thumbor is a smart imaging service. It enables on-demand crop, resizing
and flipping of images.

It also features a VERY smart detection of important points in the image
for better cropping and resizing, using state-of-the-art face and
feature detection algorithms (more on that in Detection Algorithms).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Thumbor is a smart imaging service. It enables on-demand crop, resizing
and flipping of images.

It also features a VERY smart detection of important points in the image
for better cropping and resizing, using state-of-the-art face and
feature detection algorithms (more on that in Detection Algorithms).

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md *.mkd
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/integration_tests

%files tests
%python_sitelibdir/*/integration_tests

%changelog
* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.1-alt1.git20150310
- Version 4.11.1

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.1-alt1.git20141127
- Version 4.7.1

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.0-alt1.git20141126
- Version 4.7.0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20141105
- Initial build for Sisyphus

