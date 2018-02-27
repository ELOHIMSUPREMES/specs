%define oname ClientForm
%define _python_egg_info %python_sitelibdir/%oname-%version-py%__python_version.egg-info

%def_with python3

Name: python-module-%oname
Version: 0.2.10
Release: alt4

Summary: Python module for handling HTML forms on the client side

License: BSD-like
Group: Development/Python
Url: http://wwwsearch.sourceforge.net/ClientForm

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://wwwsearch.sourceforge.net/ClientForm/src/%oname-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-compat >= 1.2

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %oname

%description
ClientForm is a Python module for handling HTML forms on the client side,
useful for parsing HTML forms, filling them in and returning the completed
forms to the server. It developed from a port of Gisle Aas' Perl module
HTML::Form, from the libwww-perl library, but the interface is not the same.

%package -n python3-module-%oname
Summary: Python module for handling HTML forms on the client side
Group: Development/Python3

%description -n python3-module-%oname
ClientForm is a Python module for handling HTML forms on the client side,
useful for parsing HTML forms, filling them in and returning the completed
forms to the server. It developed from a port of Gisle Aas' Perl module
HTML::Form, from the libwww-perl library, but the interface is not the same.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc ChangeLog.txt COPYING.txt COPYRIGHT.txt GeneralFAQ.html README.txt
%python_sitelibdir/ClientForm.*
%_python_egg_info

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog.txt COPYING.txt COPYRIGHT.txt GeneralFAQ.html README.txt
%python3_sitelibdir/ClientForm.*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt4
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.10-alt3.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt3
- Rebuilt with python 2.6

* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.10-alt2
- cleanup spec (thanks to Dmitry Levin)
- build as noarch

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.10-alt1
- new version 0.2.10, cleanup spec
- change Packager

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.1.17-alt1.1
- Rebuilt with python-2.5.

* Sat Apr 2 2005 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.17-alt1
- Updated to 0.1.17

* Sat Aug 7 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.16-alt1
- Updated to 0.1.16

* Thu Feb 26 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.15-alt2
  Fixed URL

* Tue Feb 24 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.1.15-alt1
  Initial build
