%define oname urllib3

%def_with python3

Name: python-module-%oname
Version: 20150222
Release: alt1

Summary: Library with thread-safe connection pooling, file post support, sanity friendly etc
License: MIT
Group: Development/Python

Url: https://github.com/shazow/urllib3/

# make all imports of things in packages try system copies first
Patch0:         python-urllib3-unbundle.patch

# https://github.com/shazow/urllib3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires:  python-module-six python-module-backports.ssl_match_hostname
BuildRequires: python-module-ndg-httpsclient
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%setup_python_module %oname

Requires: python-module-ndg-httpsclient
Requires: python-module-six python-module-backports.ssl_match_hostname ca-certificates
%py_requires ndg.httpsclient

%description
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

%package -n python3-module-%oname
Summary: Library with thread-safe connection pooling, file post support, sanity friendly etc
Group: Development/Python3
Requires: python3-module-ndg-httpsclient
Requires: python3-module-six ca-certificates

%description -n python3-module-%oname
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

%package -n python3-module-%oname-tests
Summary: Tests for urllib3
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains tests for urllib3.

%package tests
Summary: Tests for urllib3
Group: Development/Python
Requires: %name = %EVR

%description tests
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains tests for urllib3.

%package pickles
Summary: Pickles for urllib3
Group: Development/Python

%description pickles
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains pickles for urllib3.

%package docs
Summary: Documentation for urllib3
Group: Development/Documentation

%description docs
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains documentation for urllib3.

%prep
%setup

#rm -rf urllib3/packages/

#patch0 -p1

%if_with python3
cp -fR . ../python3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make html
%make pickle
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

#files tests
#python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/test*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/test*
%endif

%changelog
* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150222-alt1
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150210-alt1
- New snapshot

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20141214-alt1
- New snapshot

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140810-alt2
- New snapshot

* Tue Jul 22 2014 Lenar Shakirov <snejok@altlinux.ru> 20140708-alt2
- Unbundle ssl_match_hostname, ordereddict and six package
- Use system python-module-{six,backports.ssl_match_hostname,ordereddict}

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140708-alt1
- New snapshot
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20131126-alt1
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130915-alt1
- New snapshot

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130204-alt1
- Initial build for Sisyphus

