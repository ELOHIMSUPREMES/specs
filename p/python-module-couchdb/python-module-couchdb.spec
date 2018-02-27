%define sname couchdb

%def_with python3

Summary: Python library for working with CouchDB. 
Name: python-module-%sname
Version: 0.10
Release: alt2.hg20140707
# hg clone https://code.google.com/p/couchdb-python/
Source0: %name-%version.tar
#Source0: http://pypi.python.org/packages/source/C/CouchDB/CouchDB-%{version}.tar.gz
License: BSD
Group: Development/Python
URL: http://code.google.com/p/couchdb-python/
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%add_findreq_skiplist %python_sitelibdir/%sname/util3.py

%description
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

%package -n python3-module-%sname
Summary: Python library for working with CouchDB
Group: Development/Python3
%add_findreq_skiplist %python3_sitelibdir/%sname/util2.py

%description -n python3-module-%sname
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

%prep
%setup

%if_with python3
cp -fR . ../python3
for i in $(find ../python3 -type f -name '*.py'); do
	2to3 -w -n $i ||:
done
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%doc README.txt ChangeLog.txt COPYING doc/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%doc README.txt ChangeLog.txt COPYING doc/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2.hg20140707
- Added module for Python 3

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.hg20140707
- New snapshot

* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Version 0.10

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Wed Dec 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.8-alt1
- v0.8

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.7-alt1
- v0.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.1
- Rebuilt with python 2.6

* Mon Oct 12 2009 Mikhail Pokidko <pma@altlinux.org> 0.6-alt1
- Initial ALT build



