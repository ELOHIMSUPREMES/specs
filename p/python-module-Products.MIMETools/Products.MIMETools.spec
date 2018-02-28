%define oname Products.MIMETools

#def_disable check

Name: python-module-%oname
Version: 2.14.0
Release: alt2.dev0.git20150618
Summary: MIMETools provides the <!--#mime--> tag for DocumentTemplate
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.MIMETools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.MIMETools.git
Source: %name-%version.tar

BuildPreReq: python-module-%oname-tests
BuildPreReq: python-module-setuptools-tests python-module-Zope2
BuildPreReq: python-module-DocumentTemplate

%py_provides %oname
Requires: python-module-Zope2
%py_requires DocumentTemplate

%description
Currently, the MIMETools product's only function is to provide the
<!--#mime--> DTML tag for the DocumentTemplate distribution.

The <!--#mime--> tag is used to construct MIME containers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Currently, the MIMETools product's only function is to provide the
<!--#mime--> DTML tag for the DocumentTemplate distribution.

The <!--#mime--> tag is used to construct MIME containers.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test -v
export PYTHONPATH=$PWD/src
python -m unittest %oname.tests

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests.*

%files tests
%python_sitelibdir/Products/*/tests.*

%changelog
* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt2.dev0.git20150618
- Enabled check

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt1.dev0.git20150618
- Version 2.14.0.dev0
- Disabled check for bootstrap

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

