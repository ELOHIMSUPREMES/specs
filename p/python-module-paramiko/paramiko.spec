%define oname paramiko
%def_with python3

Summary: SSH2 protocol for python
Packager: Andriy Stepanov <stanv@altlinux.ru>
Name: python-module-%oname
Version: 2.2.1
Release: alt1
Source: %name-%version.tar
Patch: %name-%version-%release.patch

License: GPL
Group: Development/Python
Url: http://www.lag.net/%oname
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-ecdsa python-module-pycrypto python-module-pyasn1
BuildPreReq: python-module-cryptography python-module-bcrypt python-module-pynacl
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-ecdsa python3-module-pycrypto python3-module-pyasn1
BuildPreReq: python3-module-cryptography python3-module-bcrypt python3-module-pynacl
%endif

%description
paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines. It is written
entirely in python (no C or platform-dependent code).

This module is built for python %_python_version.

%package -n python3-module-%oname
Summary: SSH2 protocol for python
Group: Development/Python3

%description -n python3-module-%oname
paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines. It is written
entirely in python (no C or platform-dependent code).

This module is built for python %_python3_version.

%package doc
Summary: %oname documentation and example programs
Group: Development/Python

%description doc
paramiko is a module for python that implements the SSH2 protocol
for secure (encrypted and authenticated) connections to remote machines. This
package contain API documentation and examples for python-%oname module.

%prep
%setup
%patch -p1

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
%python_install --install-lib %python_sitelibdir

%if_with python3
pushd ../python3
%python3_install --install-lib %python3_sitelibdir
popd
%endif

%check
python ./test.py --no-sftp --no-big-file
%if_with python3
pushd ../python3
python3 ./test.py --no-sftp --no-big-file
popd
%endif

%files
%python_sitelibdir/*
%doc README.rst LICENSE

%files doc
%doc demos

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%doc README.rst LICENSE
%endif

%changelog
* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.16.0-alt2.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.16.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Jan 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt2
- 1.16.0 Release

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.0-alt1.git20150429
- Version 1.16.0

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.2-alt1
- Version 1.15.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.1-alt1
- Version 1.15.1

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

