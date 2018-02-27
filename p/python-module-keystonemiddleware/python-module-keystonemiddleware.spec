%define pypi_name keystonemiddleware

%def_without python3

Name: python-module-%pypi_name
Version: 1.5.0
Release: alt1
Summary: Middleware for OpenStack Identity
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/keystonemiddleware
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-oslo.config >= 1.9.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.i18n >= 1.3.0
BuildRequires: python-module-oslo.serialization >= 1.2.0
BuildRequires: python-module-oslo.utils >= 1.2.0
BuildRequires: python-module-keystoneclient >= 1.1.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-requests >= 2.2.0
BuildRequires: python-module-pycadf >= 0.8.0
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-oslo.config >= 1.9.0
BuildRequires: python3-module-oslo.context >= 0.2.0
BuildRequires: python3-module-oslo.i18n >= 1.3.0
BuildRequires: python3-module-oslo.serialization >= 1.2.0
BuildRequires: python3-module-oslo.utils >= 1.2.0
BuildRequires: python3-module-keystoneclient >= 1.1.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-requests >= 2.2.0
BuildRequires: python3-module-pycadf >= 0.8.0
BuildRequires: python3-module-webob >= 1.2.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel
%endif


%description
This package contains middleware modules designed to provide authentication
and authorization features to web services other than OpenStack Keystone.
The most prominent module is keystonemiddleware.auth_token.
This package does not expose any CLI or Python API features.

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Oslo Utility library
Group: Development/Python3

%description -n python3-module-%pypi_name
The OpenStack Oslo Utility library.
%endif

%package doc
Summary: Documentation for the Middleware for OpenStack Identity
Group: Development/Documentation

%description doc
Documentation for the Middleware for OpenStack Identity

%prep
%setup
rm -f requirements.txt
# Remove bundled egg-info
rm -rf %pypi_name.egg-info
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif


## generate html docs
#sphinx-build doc/source html
## remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -rf %buildroot%python_sitelibdir/%pypi_name/tests
%if_with python3
rm -rf %buildroot%python3_sitelibdir/%pypi_name/tests
%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

#%files doc
#%doc html LICENSE

%changelog
* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial package.
