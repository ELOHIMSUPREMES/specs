
Summary: Python bindings for the libvirt library
Name: python-module-libvirt
Version: 1.3.0
Release: alt1
Url: http://libvirt.org
#http://libvirt.org/git/?p=libvirt-python.git
Source: %name-%version.tar
License: LGPLv2+
Group: Development/Python

Requires: libvirt-client
BuildRequires: libvirt-devel >= 0.9.11
BuildPreReq: rpm-build-python rpm-build-python3
BuildRequires: python-devel python-module-distribute python-module-nose
BuildRequires: python3-devel python3-module-distribute python3-module-nose

Obsoletes: libvirt-python < %version-%release
Provides: libvirt-python = %version-%release

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%package -n python3-module-libvirt
Summary: The libvirt virtualization API python3 binding
Url: http://libvirt.org
License: LGPLv2+
Group: Development/Python3
Obsoletes: libvirt-python3 < %version-%release
Provides: libvirt-python3 = %version-%release

%description -n python3-module-libvirt
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep
%setup -q

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/*
%doc  NEWS README COPYING COPYING.LESSER examples

%files -n python3-module-libvirt
%python3_sitelibdir/*
%doc  NEWS README COPYING COPYING.LESSER examples

%changelog
* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Fri Nov 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.21-alt1
- 1.2.21

* Thu Oct 22 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.20-alt1
- 1.2.20

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.18-alt1
- 1.2.18

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.13-alt1
- 1.2.13

* Fri Jul 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Jun 10 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Thu Apr 03 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt1
- 1.2.3
- add python3 package

* Mon Dec 02 2013 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- initial build; split off from main libvirt package
