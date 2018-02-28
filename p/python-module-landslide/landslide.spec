%define oname landslide

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt1.git20150525
Summary: Lightweight markup language-based html5 slideshow generator
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/landslide
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/adamzap/landslide.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jinja2 python-module-markdown
BuildPreReq: python-module-Pygments python-module-docutils
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jinja2 python3-module-markdown
BuildPreReq: python3-module-Pygments python3-module-docutils
BuildPreReq: python3-module-six
%endif

%py_provides %oname
%py_requires jinja2 markdown pygments docutils six

%description
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.

%if_with python3
%package -n python3-module-%oname
Summary: Lightweight markup language-based html5 slideshow generator
Group: Development/Python3
%py3_provides %oname
%py3_requires jinja2 markdown pygments docutils six

%description -n python3-module-%oname
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.
%endif

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
python setup.py test -v
python tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 tests.py -v
popd
%endif

%files
%doc *.md examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150525
- Initial build for Sisyphus

