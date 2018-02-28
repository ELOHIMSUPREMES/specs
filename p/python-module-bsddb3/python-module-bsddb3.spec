%define _name bsddb3
# sometime 1 test out of 501 fails only in girar
%def_disable check

Name: python-module-%_name
Version: 6.2.1
Release: alt1

Summary: Python bindings for BerkleyDB
Group: Development/Python
License: BSD
Url: https://pypi.python.org/pypi/bsddb3/

Source: https://pypi.python.org/packages/source/b/%_name/%_name-%version.tar.gz

BuildRequires: libdb4-devel
BuildRequires: python-devel
BuildRequires: python3-devel rpm-build-python3
# for check
BuildRequires: /proc python-test python3-test

%description
This package provides Python wrappers for Berkeley DB                                          .

%package -n python3-module-%name
Summary: Python3 bindings for BerkleyDB
Group: Development/Python3
License: BSD

%description -n python3-module-%name
This package provides Python3 wrappers for Berkeley DB.


%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build

%build
%python_build

pushd py3build
%python3_build
popd

%install
%python_install

pushd py3build
%python3_install
popd

%if_enabled check
%check
%__python test.py

pushd py3build
%__python3 test.py
popd
%endif

%files
%python_sitelibdir/%_name/
%python_sitelibdir/%_name-%version-py*.egg-info
%doc ChangeLog *.txt

%exclude %python_sitelibdir/%_name/tests/

%files -n python3-module-%name
%python3_sitelibdir/%_name/
%python3_sitelibdir/%_name-%version-py*.egg-info

%exclude %python3_sitelibdir/%_name/tests/

%exclude %_includedir/python*/%_name/bsddb.h

%changelog
* Wed Jun 01 2016 Yuri N. Sedunov <aris@altlinux.org> 6.2.1-alt1
- 6.2.1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 6.1.1-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Feb 19 2016 Yuri N. Sedunov <aris@altlinux.org> 6.1.1-alt1
- 6.1.1

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Jul 06 2014 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- first build for Sisyphus

