%define module_name django-picklefield

%def_with python3

Name: python-module-%module_name
Version: 0.3.1
Release: alt1.git20131115
Group: Development/Python
License: BSD License
Summary: django-picklefield provides an implementation of a pickled object field
URL: http://github.com/gintas/django-picklefield.git
Source: %module_name-%version.tar.gz

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%endif

%description
django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

%package -n python3-module-%module_name
Summary: django-picklefield provides an implementation of a pickled object field
Group: Development/Python

%description -n python3-module-%module_name
django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

%prep
%setup -n %module_name-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc README
%python_sitelibdir/django_picklefield*
%python_sitelibdir/picklefield*

%if_with python3
%files -n python3-module-%module_name
%doc README
%python3_sitelibdir/django_picklefield*
%python3_sitelibdir/picklefield*
%endif

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20131115
- Version 0.3.1
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.1-alt1
- build for ALT
