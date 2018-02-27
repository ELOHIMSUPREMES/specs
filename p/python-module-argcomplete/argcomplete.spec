%define oname argcomplete

%def_with python3

Name: python-module-%oname
Version: 0.8.1
Release: alt1.git20141005
Summary: Bash tab completion for argparse
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/argcomplete/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kislyuk/argcomplete.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash or zsh as your shell
* You're using argparse to manage your command line arguments/options

%package -n python3-module-%oname
Summary: Bash tab completion for argparse
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash or zsh as your shell
* You're using argparse to manage your command line arguments/options

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

%files
%doc *.rst docs/*.rst docs/examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst docs/examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20141005
- Initial build for Sisyphus

