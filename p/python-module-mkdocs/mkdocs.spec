%define oname mkdocs

%def_with python3

Name: python-module-%oname
Version: 0.11.1
Release: alt1
Summary: Project documentation with Markdown
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mkdocs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jinja2 python-module-markdown
BuildPreReq: python-module-yaml python-module-watchdog
BuildPreReq: ghp-import python-module-argh python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jinja2 python3-module-markdown
BuildPreReq: python3-module-yaml python3-module-watchdog
BuildPreReq: ghp-import.py3 python3-module-argh
%endif

%py_provides %oname
Requires: ghp-import

%description
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Project documentation with Markdown
Group: Development/Python3
%py3_provides %oname
Requires: ghp-import.py3

%description -n python3-module-%oname
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|ghp-import|ghp-import.py3|' \
	../python3/%oname/gh_deploy.py
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
export PYTHONPATH=$PWD
python setup.py test
python %oname/test.py
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
python3 %oname/test.py
popd
%endif

%files
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

