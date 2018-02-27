%define module_name html5lib

%def_with python3
%def_without docs

Name: python-module-%module_name
Epoch: 1
Version: 0.999999
Release: alt1

Summary: Library for working with HTML5 documents

License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://github.com/html5lib/html5lib-python

Source: %module_name-%version.tar

BuildRequires: python-module-setuptools
BuildPreReq: python-module-sphinx-devel

%setup_python_module %module_name

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

%package tests
Summary: Tests for html5lib
Group: Development/Python
Requires: %name = %EVR

%description tests
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

This package contains tests for html5lib.

%package pickles
Summary: Pickles for html5lib
Group: Development/Python

%description pickles
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

This package contains pickles for html5lib.

%package doc
Summary: Documentation for html5lib
Group: Development/Documentation

%description doc
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

This package contains documentation for html5lib.

%if_with python3
%package -n python3-module-%module_name
Summary: Library for working with HTML5 documents (Python 3)
Group: Development/Python3

%description -n python3-module-%module_name
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

%package -n python3-module-%module_name-tests
Summary: Tests for html5lib (Python 3)
Group: Development/Python3
Requires: python3-module-%module_name = %EVR

%description -n python3-module-%module_name-tests
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

This package contains tests for html5lib.
%endif

%prep
%setup -n %module_name-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%if_with docs
%make -C doc pickle
%make -C doc html
%endif

%install
%python_install --record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with docs
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%module_name/
%endif

%files -f INSTALLED_FILES
%doc README.rst
#exclude %python_sitelibdir/*/tests
%if_with docs
%exclude %python_sitelibdir/*/pickle
%endif

#files tests
#python_sitelibdir/*/tests

%if_with docs
%files pickles
%python_sitelibdir/*/pickle

%files doc
%doc doc/_build/html/*
%endif

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/tests

#files -n python3-module-%module_name-tests
#python3_sitelibdir/*/tests
%endif

%changelog
* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.999999-alt1
- Version 0.999999

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.999-alt1
- Version 0.999

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b3
- Version 1.0b3

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt4
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.95-alt3.1
- Rebuild with Python-3.3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt3
- Added modules for Python 3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt2
- Extracted tests into separate package

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt1
- Version 0.95

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.1-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt2.1
- Rebuilt with python 2.6

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 0.11.1-alt2
- install over --record option
- add README file

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 0.11.1-alt1
- Initial build for ALT Linux

