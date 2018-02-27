%define oname PyPDF2

%def_with python3

Name: python-module-%oname
Version: 1.23
Release: alt1.git20140815
Summary: A utility to read and write PDFs with Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyPDF2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mstamy2/PyPDF2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

Requires: python-module-Reportlab

%description
A Pure-Python library built as a PDF toolkit. It is capable of:

* extracting document information (title, author, ...)
* splitting documents page by page
* merging documents page by page
* cropping pages
* merging multiple pages into a single page
* encrypting and decrypting PDF files
* and more!

%package -n python3-module-%oname
Summary: A utility to read and write PDFs with Python
Group: Development/Python3
Requires: python3-module-Reportlab

%description -n python3-module-%oname
A Pure-Python library built as a PDF toolkit. It is capable of:

* extracting document information (title, author, ...)
* splitting documents page by page
* merging documents page by page
* cropping pages
* merging multiple pages into a single page
* encrypting and decrypting PDF files
* and more!

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc CHANGELOG *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.23-alt1.git20140815
- Initial build for Sisyphus

