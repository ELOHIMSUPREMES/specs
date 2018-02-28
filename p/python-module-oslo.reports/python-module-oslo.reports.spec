%define pypi_name oslo.reports

%def_with python3

Name: python-module-%pypi_name
Version: 0.5.0
Release: alt1
Summary: Openstack common reports library

Group: Development/Python
License: ASL 2.0
URL: https://launchpad.net/oslo
Source: %name-%version.tar
BuildArch:      noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-psutil >= 1.1.1
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.utils >= 2.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-psutil >= 1.1.1
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.

%if_with python3
%package -n python3-module-oslo.reports
Summary: Openstack common reports library
Group: Development/Python3

%description -n python3-module-oslo.reports
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.
%endif

%package doc
Summary: Documentation for the Oslo common reports library
Group: Development/Documentation

%description doc
Documentation for the Oslo common reports library.


%prep
%setup

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


# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-oslo.reports
%python3_sitelibdir/*
%endif

%files doc
%doc html
%doc README.rst LICENSE

%changelog
* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT

