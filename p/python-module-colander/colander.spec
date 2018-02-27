%define oname colander

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.b1.git20140910
Summary: A serialization/deserialization/validation library for strings, mappings and lists
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/colander/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/colander.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-iso8601 python-module-translationstring
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires iso8601

%description
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A serialization/deserialization/validation library for strings, mappings and lists
Group: Development/Python3
%py3_provides %oname
%py3_requires iso8601

%description -n python3-module-%oname
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
cp -fR %_datadir/pylons_sphinx_theme docs/_themes

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
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b1.git20140910
- Initial build for Sisyphus

