%define mname dogpile
%define oname %mname.cache

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.6
Release: alt1.git20150202
Summary: A caching front-end based on the Dogpile lock
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dogpile.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/zzzeek/dogpile.cache.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-%mname-core python-module-coverage
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-mako
BuildPreReq: python-module-sphinx-devel python-module-changelog
BuildPreReq: python-module-sphinx-paramlinks
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-%mname-core python3-module-coverage
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-mako
%endif

%py_provides %oname
%py_requires %mname.core

%description
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

dogpile.cache builds on the dogpile.core locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract. Overall, dogpile.cache is intended as a replacement to the
Beaker caching system, the internals of which are written by the same
author. All the ideas of Beaker which "work" are re-implemented in
dogpile.cache in a more efficient and succinct manner, and all the cruft
(Beaker's internals were first written in 2005) relegated to the trash
heap.

%package -n python3-module-%oname
Summary: A caching front-end based on the Dogpile lock
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname.core

%description -n python3-module-%oname
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

dogpile.cache builds on the dogpile.core locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract. Overall, dogpile.cache is intended as a replacement to the
Beaker caching system, the internals of which are written by the same
author. All the ideas of Beaker which "work" are re-implemented in
dogpile.cache in a more efficient and succinct manner, and all the cruft
(Beaker's internals were first written in 2005) relegated to the trash
heap.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/build/

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

%make -C docs/build pickle
%make -C docs/build html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/output/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%dir %python_sitelibdir/*/pickle
%python_sitelibdir/%mname/cache
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/output/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/cache
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1.git20150202
- Initial build for Sisyphus

