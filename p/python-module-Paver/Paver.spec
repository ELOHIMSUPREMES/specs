%define oname Paver

%def_with python3

Name: python-module-%oname
Version: 1.2.3
Release: alt1.git20140810
Summary: Easy build, distribution and deployment scripting
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Paver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/paver/paver.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-sphinx-devel bzr
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
Paver is a Python-based build/distribution/deployment scripting tool
along the lines of Make or Rake. What makes Paver unique is its
integration with commonly used Python libraries. Common tasks that were
easy before remain easy. More importantly, dealing with your
applications specific needs and requirements is also easy.

%package pickles
Summary: Pickles for Paver
Group: Development/Python

%description pickles
Paver is a Python-based build/distribution/deployment scripting tool
along the lines of Make or Rake. What makes Paver unique is its
integration with commonly used Python libraries. Common tasks that were
easy before remain easy. More importantly, dealing with your
applications specific needs and requirements is also easy.

This package contains pickles for Paver.

%package docs
Summary: Documentation for Paver
Group: Development/Documentation
BuildArch: noarch

%description docs
Paver is a Python-based build/distribution/deployment scripting tool
along the lines of Make or Rake. What makes Paver unique is its
integration with commonly used Python libraries. Common tasks that were
easy before remain easy. More importantly, dealing with your
applications specific needs and requirements is also easy.

This package contains documentation for Paver.

%package -n python3-module-%oname
Summary: Easy build, distribution and deployment scripting
Group: Development/Python3
%add_python3_req_skip bzrlib

%description -n python3-module-%oname
Paver is a Python-based build/distribution/deployment scripting tool
along the lines of Make or Rake. What makes Paver unique is its
integration with commonly used Python libraries. Common tasks that were
easy before remain easy. More importantly, dealing with your
applications specific needs and requirements is also easy.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
sphinx-build -b pickle -d build/doctrees source build/pickle
%make html
popd

cp -fR docs/build/pickle %buildroot%python_sitelibdir/paver/

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/samples
%doc docs/build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.git20140810
- Initial build for Sisyphus

