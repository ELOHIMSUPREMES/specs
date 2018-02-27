%define modulename py3dns

Summary: Python DNS library
Version: 3.0.2
Release: alt1.bzr20120722

%add_python3_req_skip winreg

Name: python3-module-%modulename
# bzr branch lp:py3dns
Source0: %name-%version.tar
License: Python Software Foundation License
Group: Development/Python
URL: http://pydns.sourceforge.net/
BuildArch: noarch
Packager: Aleksey Avdeev <solo@altlinux.ru>
Provides: python3-module-pydns = %EVR

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-distribute

%description
PyDNS provides a module for performing DNS queries from python applications.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir_noarch/*

%changelog
* Sat Mar 16 2013 Aleksey Avdeev <solo@altlinux.ru> 3.0.2-alt1.bzr20120722
- 3.0.2 (bzr20120722)
- Rename package to python3-module-py3dns

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.3-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1.1
- Rebuilt with python 2.6

* Sun May 03 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt1
- Initial build for ALT Linux
