%define mname scikits
%define oname %mname.samplerate

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.4.0
Release: alt1.git20090722
Summary: A python module for high quality audio resampling
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.samplerate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/cournape/samplerate.git
Source: %name-%version.tar
Source1: site.cfg

BuildPreReq: libsamplerate-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
%endif

%py_provides %oname
%py_requires %mname numpy

%description
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

Samplerate is a wrapper around the Secret Rabbit Code from Erik de
Castro Lopo (http://www.mega-nerd.com/SRC/), which has high quality
converters based on the work of J.O Smith from CCRMA (see
http://ccrma.stanford.edu/~jos/resample/optfir.pdf).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A python module for high quality audio resampling
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy

%description -n python3-module-%oname
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

Samplerate is a wrapper around the Secret Rabbit Code from Erik de
Castro Lopo (http://www.mega-nerd.com/SRC/), which has high quality
converters based on the work of J.O Smith from CCRMA (see
http://ccrma.stanford.edu/~jos/resample/optfir.pdf).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains pickles for %oname.

%prep
%setup

rm -f scikits/samplerate/_samplerate.c
install -m644 %SOURCE1 .
%ifarch x86_64
sed -i 's|\(library_dirs =\).*|\1 %_libdir|' site.cfg
%endif

%if_with python3
cp -fR . ../python3
mv ../python3/scikits/samplerate/setup.py \
	../python3/scikits/samplerate/setup.py.bak
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv ../python3/scikits/samplerate/setup.py.bak \
	../python3/scikits/samplerate/setup.py
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/src/

%build
cython scikits/samplerate/_samplerate.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 scikits/samplerate/_samplerate.pyx
sed -i '1a\#define PyString_FromStringAndSize PyUnicode_FromStringAndSize' \
	scikits/samplerate/_samplerate.c
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

python setup.py build_ext -i
export PYTHONPATH=$PWD:$PWD/docs/ext
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
pushd ~
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -v %oname
popd
%if_with python3
pushd ../python3
pushd ~
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v %oname
popd
popd
%endif

%files
%doc Changelog README TODO docs/src/examples docs/build/html
%python_sitelibdir/%mname/samplerate
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/samplerate/tests

%files tests
%python_sitelibdir/%mname/samplerate/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc Changelog README TODO docs/src/examples
%python3_sitelibdir/%mname/samplerate
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/samplerate/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/samplerate/tests
%endif

%changelog
* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.4.0-alt1.git20090722
- Initial build for Sisyphus

