%define oname pysrt

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20140527
Summary: SubRip (.srt) subtitle parser and writer
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pysrt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/byroot/pysrt.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-chardet python-module-nose
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-chardet python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires chardet

%description
pysrt is a Python library used to edit or create SubRip files.

%package -n python3-module-%oname
Summary: SubRip (.srt) subtitle parser and writer
Group: Development/Python3
%py3_provides %oname
%py3_requires chardet

%description -n python3-module-%oname
pysrt is a Python library used to edit or create SubRip files.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140527
- Initial build for Sisyphus

