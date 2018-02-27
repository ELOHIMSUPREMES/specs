%define mname scikits
%define oname %mname.scattpy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.2
Release: alt2.git20120523
Summary: Light Scattering methods for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.scattpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/ScattPy/scikits.scattpy.git
Source: %name-%version.tar

BuildPreReq: gcc-fortran ipython
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scipy libnumpy-devel
BuildPreReq: python-module-matplotlib
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
BuildPreReq: python-module-matplotlib-sphinxext
BuildPreReq: python-module-sphinxtogithub
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-matplotlib
%endif

%py_provides %oname
Requires: libradial = %EVR
%py_requires %mname scipy numpy

%description
ScattPy is an open source Python package for light scattering
simulations. Its goal is to provide an easy-to-use and flexible modern
framework for the numerical solving of the diffraction problems with
various kinds of particles.

With the current version of ScattPy it is possible to calculate far- and
near-field optical properties of light scattered by dielectric particles
with axial symmetry. With ScattPy homogeneous and multilayered particles
can be handled.

%if_with python3
%package -n python3-module-%oname
Summary: Light Scattering methods for Python
Group: Development/Python3
%py3_provides %oname
Requires: libradial = %EVR
%py3_requires %mname scipy numpy

%description -n python3-module-%oname
ScattPy is an open source Python package for light scattering
simulations. Its goal is to provide an easy-to-use and flexible modern
framework for the numerical solving of the diffraction problems with
various kinds of particles.

With the current version of ScattPy it is possible to calculate far- and
near-field optical properties of light scattered by dielectric particles
with axial symmetry. With ScattPy homogeneous and multilayered particles
can be handled.
%endif

%package -n libradial
Summary: Radial library of %oname
Group: System/Libraries

%description -n libradial
ScattPy is an open source Python package for light scattering
simulations. Its goal is to provide an easy-to-use and flexible modern
framework for the numerical solving of the diffraction problems with
various kinds of particles.

This package contains radial library of %oname.

%package -n libradial-devel
Summary: Development files of libradial
Group: Development/Other
Requires: libradial = %EVR

%description -n libradial-devel
ScattPy is an open source Python package for light scattering
simulations. Its goal is to provide an easy-to-use and flexible modern
framework for the numerical solving of the diffraction problems with
various kinds of particles.

This package contains development files of libradial.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ScattPy is an open source Python package for light scattering
simulations. Its goal is to provide an easy-to-use and flexible modern
framework for the numerical solving of the diffraction problems with
various kinds of particles.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
ScattPy is an open source Python package for light scattering
simulations. Its goal is to provide an easy-to-use and flexible modern
framework for the numerical solving of the diffraction problems with
various kinds of particles.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags %optflags_shared -fno-strict-aliasing

gfortran -ffixed-form -fno-second-underscore %optflags -O3 \
	-funroll-loops -c src/lib.for \
	-Wl,-soname=libradial.so.0 -o ~/libradial.so.0
ln -s libradial.so.0 ~/libradial.so

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
cp -P ~/libradial.so* %buildroot%_libdir/

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir:$PWD/doc/source/sphinxext
%make -C doc/source pickle
%make -C doc/source html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/source/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%add_optflags %optflags_shared -fno-strict-aliasing

python setup.py test
FFLAGS="%optflags" python setup.py build_ext -i
export PYTHONPATH=$PWD:$PWD/%mname/scattpy
py.test -vv

%if_with python3
pushd ../python3
python3 setup.py test
FFLAGS="%optflags" python3 setup.py build_ext -i
export PYTHONPATH=$PWD:$PWD/%mname/scattpy
py.test-%_python3_version -vv
popd
%endif

%files
%doc README
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%files -n libradial
%_libdir/*.so.*

%files -n libradial-devel
%doc src/*
%_libdir/*.so

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/source/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.git20120523
- Rebuilt with updated NumPy

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20120523
- Initial build for Sisyphus

