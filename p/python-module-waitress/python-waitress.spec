# vim: set ft=spec: -*- rpm-spec -*-

%define modulename waitress
%define oldname python-%modulename

%def_with python3

%if_with python3
%define py3name python3-module-%modulename
%define py3dir %py3name-%version
%endif

Name: python-module-waitress
Version: 0.8.2
Release: alt2

%setup_python_module %modulename

Summary: Waitress WSGI server
License: ZPLv2.1
Group: Development/Python

Url: https://github.com/Pylons/%modulename
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

# http://pypi.python.org/packages/source/w/%modulename/%modulename-%version.tar.gz
# git://github.com/Pylons/%modulename.git
Source: %name-%version.tar
Source44: import.info

BuildPreReq: python-module-nose
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx

%description
Waitress is meant to be a production-quality pure-Python WSGI server with
very acceptable performance. It has no dependencies except ones which live
in the Python standard library. It runs on CPython on Unix and Windows under
Python 2.6+ and Python 3.2. It is also known to run on PyPy 1.6.0 on UNIX.
It supports HTTP/1.0 and HTTP/1.1.

For more information, see %_docdir/%oldname-%version/docs or
http://docs.pylonsproject.org/projects/%modulename/en/latest/ .

%package tests
Summary: Tests for Waitress WSGI server
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description tests
%summary

This package contains tests for Waitress.

%if_with python3
%package -n %py3name
Summary: Waitress WSGI server
Group: Development/Python
BuildArch: noarch

BuildPreReq: rpm-build-python3
BuildPreReq: python3-module-distribute
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-coverage
BuildPreReq: python3-module-sphinx

%description -n %py3name
Waitress is meant to be a production-quality pure-Python WSGI server with
very acceptable performance. It has no dependencies except ones which live
in the Python standard library. It runs on CPython on Unix and Windows under
Python 2.6+ and Python 3.2. It is also known to run on PyPy 1.6.0 on UNIX.
It supports HTTP/1.0 and HTTP/1.1.

For more information, see %_docdir/%oldname-%version/docs or
http://docs.pylonsproject.org/projects/%modulename/en/latest/ .

%package -n %py3name-tests
Summary: Tests for Waitress WSGI server
Group: Development/Python
BuildArch: noarch
Requires: %py3name = %EVR

%description -n %py3name-tests
%summary

This package contains tests for Waitress.

%endif

%prep
%setup
rm -rf %modulename.egg-info
rm -f .gitignore docs/.gitignore
# this script has devel paths, not useful in a user system
rm -f docs/rebuild

%if_with python3
rm -rf ../%py3dir
cp -a . ../%py3dir
%endif

%build
%python_build

%if_with python3
pushd ../%py3dir
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../%py3dir
%python3_install
popd
%endif

%check
# by setting the PYTHONPATH to the current dir
# we make the package %modulename importable
# Usually the testsuite is run after installing
# the package in develop mode but we can't install
# in develop mode here.
PYTHONPATH=. %__python setup.py test -q

%if_with python3
pushd ../%py3dir
PYTHONPATH=. %__python3 setup.py test -q
popd
%endif

%files
%doc README.rst CHANGES.txt COPYRIGHT.txt LICENSE.txt docs
%python_sitelibdir_noarch/%modulename
%exclude %python_sitelibdir_noarch/%modulename/test*
%python_sitelibdir_noarch/%modulename-%version-py2.?.egg-info

%files tests
%python_sitelibdir_noarch/%modulename/test*

%if_with python3
%files -n %py3name
%doc README.rst CHANGES.txt COPYRIGHT.txt LICENSE.txt docs
%python3_sitelibdir_noarch/%modulename
%exclude %python3_sitelibdir_noarch/%modulename/test*
%python3_sitelibdir_noarch/%modulename-%version-py3.?.egg-info

%files -n %py3name-tests
%python3_sitelibdir_noarch/%modulename/test*
%endif

%changelog
* Wed Mar 06 2013 Aleksey Avdeev <solo@altlinux.ru> 0.8.2-alt2
- Add python{,3}-module-waitress-test subpackages

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_4
- update to new release by fcimport

* Thu Jan 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_3
- initial fc import
