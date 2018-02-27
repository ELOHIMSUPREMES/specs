%define oname html5print

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20140927
Summary: HTML5, CSS, Javascript Pretty Print
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/html5print/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/berniey/html5print.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-BeautifulSoup4 python-module-chardet
BuildPreReq: python-module-html5lib python-module-requests
BuildPreReq: python-module-slimit python-module-tinycss2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-BeautifulSoup4 python3-module-chardet
BuildPreReq: python3-module-html5lib python3-module-requests
BuildPreReq: python3-module-slimit python3-module-tinycss2
%endif

%py_provides %oname
%py_requires bs4 chardet html5lib requests slimit tinycss2

%description
This tool pretty print your HTML, CSS and JavaScript file. The package
comes with two parts:

* a command line tool, html5-print
* a python module, html5print

%package -n python3-module-%oname
Summary: HTML5, CSS, Javascript Pretty Print
Group: Development/Python3
%py3_provides %oname
%py3_requires bs4 chardet html5lib requests slimit tinycss2

%description -n python3-module-%oname
This tool pretty print your HTML, CSS and JavaScript file. The package
comes with two parts:

* a command line tool, html5-print
* a python module, html5print

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140927
- Initial build for Sisyphus

