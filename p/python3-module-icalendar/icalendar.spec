%define modulename icalendar

Name: python3-module-%modulename
Version: 3.8.3
Release: alt1.1.1
Summary: iCalendar parser/generator
License: GPLv2.1
Group: Development/Python3
BuildArch: noarch
Source: %modulename-%version.tar.gz
Url: http://pypi.python.org/pypi/icalendar

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-jinja2-tests

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-jinja2
BuildRequires: python3-module-setuptools rpm-build-python3

%description
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

%package tests
Summary: Tests for %modulename
Group: Development/Python3
Requires: %name = %EVR

%description tests
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

This package contains tests for %modulename.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/%modulename
%exclude %python3_sitelibdir/%modulename/tests
%python3_sitelibdir/%modulename-*

%files tests
%python3_sitelibdir/%modulename/tests

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.8.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 3.8.3-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Initial build for Sisyphus

