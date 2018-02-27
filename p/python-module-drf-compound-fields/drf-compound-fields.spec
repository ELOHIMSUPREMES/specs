%define oname drf-compound-fields

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20141012
Summary: Django-REST-framework serializer fields for compound types
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/drf-compound-fields/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/estebistec/drf-compound-fields.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-django-tests python-module-djangorestframework
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django-tests python3-module-djangorestframework
BuildPreReq: python3-module-coverage
%endif

%py_provides drf_compound_fields

%description
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package expands on that and provides fields allowing:

* Lists of simple (non-object) types, described by other serializer
  fields.
* Fields that allow values to be a list or individual item of some type.
* Dictionaries of simple and object types.
* Partial dictionaries which include keys specified in a list.

%package -n python3-module-%oname
Summary: Django-REST-framework serializer fields for compound types
Group: Development/Python3
%py3_provides drf_compound_fields

%description -n python3-module-%oname
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package expands on that and provides fields allowing:

* Lists of simple (non-object) types, described by other serializer
  fields.
* Fields that allow values to be a list or individual item of some type.
* Dictionaries of simple and object types.
* Partial dictionaries which include keys specified in a list.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Python
BuildArch: noarch

%description docs
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package contains documentation for %oname.

%prep
%setup

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

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
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141012
- Initial build for Sisyphus

