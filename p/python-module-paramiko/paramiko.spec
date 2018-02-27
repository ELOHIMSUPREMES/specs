%define	version	1.14.0
%define release alt1
%define source_version %version
%define source_name  paramiko
%setup_python_module paramiko

%def_with python3

Summary: SSH2 protocol for python
Packager: Andriy Stepanov <stanv@altlinux.ru>
Name: %packagename
Version: %version
Release: %release
Source: %modulename-%version.tar.gz
License: GPL
Group: Development/Python
Prefix: %_prefix
%py_requires Crypto
Url: http://www.lag.net/paramiko
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines. It is written
entirely in python (no C or platform-dependent code).

This module is built for python %_python_version.

%package -n python3-module-%source_name
Summary: SSH2 protocol for python
Group: Development/Python3

%description -n python3-module-%source_name
paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines. It is written
entirely in python (no C or platform-dependent code).

This module is built for python %_python3_version.

%package doc
Summary: %modulename documentation and example programs
Group: Development/Python
Prefix: %_prefix
Requires: python-module-%modulename = %version
%description doc
%modulename paramiko is a module for python that implements the SSH2 protocol
for secure (encrypted and authenticated) connections to remote machines. This
package contain API documentation and examples for python-%modulename module.

%prep
%setup -q -n %source_name-%source_version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --install-lib %python_sitelibdir

%if_with python3
pushd ../python3
%python3_install --install-lib %python3_sitelibdir
popd
%endif

%files
%python_sitelibdir/%source_name
%python_sitelibdir/*.egg-info
%doc README LICENSE

%files doc
%doc demos

%if_with python3
%files -n python3-module-%source_name
%python3_sitelibdir/%source_name
%python3_sitelibdir/*.egg-info
%doc README LICENSE
%endif

%changelog
* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.0-alt1
- Version 1.14.0
- Added module for Python 3

* Fri Aug 09 2013 Anatoly Kitaykin <cetus@altlinux.org> 1.11.0-alt1
- Version 1.11.0 (ALT #29340)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.6-alt1.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.6-alt1
- Version 1.7.6 (ALT #23843)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.1.1
- Rebuilt with python 2.6

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 1.7.2-alt1.1
- Rebuilt with python-2.5.

* Mon Feb 04 2008 Andriy Stepanov <stanv@altlinux.ru> 1.7.2-alt1
- Up to new version

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.3-alt2.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Fri Mar 31 2006 Andriy Stepanov <stanv@altlinux.ru> 1.5.3-alt2
- Modifications in spec file for doc package

* Fri Mar 31 2006 Stepanov Andriy <stanv@altlinux.ru> 1.5.3-alt1
- Initial build

