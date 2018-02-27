
Name: ryu
Version: 3.19
Release: alt1
Summary: Component-based Software-defined Networking Framework
Group: Development/Python
License: ASL 2.0
Url: http://osrg.github.io/ryu/
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%description
Ryu is a component-based software defined networking framework.

Ryu provides software components with well defined API that make it
easy for developers to create new network management and control
applications. Ryu supports various protocols for managing network
devices, such as OpenFlow, Netconf, OF-config, etc. About OpenFlow,
Ryu supports fully 1.0, 1.2, 1.3, 1.4 and Nicira Extensions.

All of the code is freely available under the Apache 2.0 license. Ryu
is fully written in Python.

%package -n python-module-%name
Summary: Component-based Software-defined Networking Framework
Group: Development/Python

%description -n python-module-%name
Ryu is a component-based software defined networking framework.

Ryu provides software components with well defined API that make it
easy for developers to create new network management and control
applications. Ryu supports various protocols for managing network
devices, such as OpenFlow, Netconf, OF-config, etc. About OpenFlow,
Ryu supports fully 1.0, 1.2, 1.3, 1.4 and Nicira Extensions.

All of the code is freely available under the Apache 2.0 license. Ryu
is fully written in Python.

%package doc
Summary: Documentation for Software-defined Networking Framework
Group: Development/Documentation

%description doc
Documentation for Software-defined Networking Framework

%package -n python-module-%name-tests
Summary: Tests for Software-defined Networking Framework
Group: Development/Documentation

%description -n python-module-%name-tests
Tests for Software-defined Networking Framework

%prep
%setup

# Remove bundled egg-info
#rm -rf %name.egg-info

%build
%python_build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install

rm -f %buildroot/usr/etc/ryu/ryu.conf
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_logrotatedir
install -m 644 debian/ryu.conf %buildroot%_sysconfdir/%name
install -m 644 debian/log.conf %buildroot%_logrotatedir/%name

%files
%doc README.rst
%_bindir/*
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/%name/*

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

# mininet? xml_compare?
#%files -n python-module-%name-tests
#%python_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 3.19-alt1
- Initial release
