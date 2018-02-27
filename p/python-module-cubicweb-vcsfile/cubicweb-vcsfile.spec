%define oname cubicweb-vcsfile
Name: python-module-%oname
Version: 2.0.2
Release: alt1
Summary: Component to integrate version control systems data into the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-vcsfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb subversion-python
BuildPreReq: python-module-cubicweb-localperms mercurial
BuildPreReq: python-module-cubicweb-tag
BuildPreReq: python-module-cubicweb-folder
BuildPreReq: python-module-logilab-mtconverter
BuildPreReq: python-module-logilab-common
BuildPreReq: python-module-hglib

Requires: cubicweb python-module-cubicweb-localperms
Requires: python-module-cubicweb-tag
Requires: python-module-cubicweb-folder
%py_requires logilab.mtconverter logilab.common svn mercurial hglib

%description
This cube stores the data found in a version content manager repository.
It currently works with subversion or mercurial repository.

It doesn't access to the data directly. All the repository's metadata
(eg revision, file names, commit message, date and autor, etc) are
stored as entities, and thus queryable via RQL, while actual files
content is kept in the repository and fetched from there on demand.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%_bindir/*
%python_sitelibdir/*
%_datadir/cubicweb/*
%_docdir/%oname

%changelog
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.17.0-alt1
- Initial build for Sisyphus

