%define sname networking-ofagent

%def_without python3

Name: python-module-%sname
Version: 2015.1.2
Release: alt2
Summary: OpenStack Networking ofagent
Group: Development/Python
License: ASL 2.0
Url: http://git.openstack.org/cgit/stackforge/%sname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-ryu >= 3.19

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-ryu >= 3.19
%endif

%description
This is OpenStack/Networking (Neutron) "ofagent" ML2 driver and its agent.

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack Networking ofagent
Group: Development/Python3

%description -n python3-module-%sname
This is OpenStack/Networking (Neutron) "ofagent" ML2 driver and its agent.
%endif


%package doc
Summary: Documentation for Openstack ofagent driver
Group: Development/Documentation

%description doc
Documentation for Openstack ofagent drivers.

%prep
%setup

# Remove bundled egg-info
#rm -rf %sname.egg-info

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
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

mkdir -p %buildroot%_sysconfdir/neutron/plugins/ml2
mkdir -p %buildroot%_sysconfdir/neutron/rootwrap.d
mv %buildroot/usr/etc/neutron/plugins/ml2/ml2_conf_ofa.ini %buildroot%_sysconfdir/neutron/plugins/ml2/ml2_conf_ofa.ini
mv %buildroot/usr/etc/neutron/rootwrap.d/ofagent.filters %buildroot%_sysconfdir/neutron/rootwrap.d/ofagent.filters

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
%if_with python3
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests
%endif

%files
%doc README.rst
#%_bindir/neutron-ofagent-agent
#%config(noreplace) %_sysconfdir/neutron/plugins/ml2/ml2_conf_ofa.ini
#%config(noreplace) %_sysconfdir/neutron/rootwrap.d/ofagent.filters
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Fri Apr 03 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt2
- don't package config

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- Initial release
