%define oname pymetis

%def_with python3

Name: python-module-%oname
Version: 2011.1.1
Release: alt5.git20120417
Summary: Python wrapper for the Metis graph partititioning software
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/pymetis
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/pymetis.git
Source: %oname-%version.tar

BuildPreReq: python-module-setuptools gcc-c++ boost-python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools boost-python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
PyMetis is a Python wrapper for the Metis graph partititioning software
by George Karypis, Vipin Kumar and others. It includes version 5.0pre2
of Metis and wraps it using the Boost Python wrapper generator library.
So far, it only wraps the most basic graph partitioning functionality,
but extending it in case you need more should be quite straightforward.
Using PyMetis to partition your meshes is really easy--essentially all
you need to pass into PyMetis is an adjacency list for the graph and the
number of parts you would like.

%package -n python3-module-%oname
Summary: Python wrapper for the Metis graph partititioning software
Group: Development/Python3

%description -n python3-module-%oname
PyMetis is a Python wrapper for the Metis graph partititioning software
by George Karypis, Vipin Kumar and others. It includes version 5.0pre2
of Metis and wraps it using the Boost Python wrapper generator library.
So far, it only wraps the most basic graph partitioning functionality,
but extending it in case you need more should be quite straightforward.
Using PyMetis to partition your meshes is really easy--essentially all
you need to pass into PyMetis is an adjacency list for the graph and the
number of parts you would like.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|boost_python|boost_python3|' ../python3/setup.py
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt5.git20120417
- Added module for Python 3

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt4.git20120417
- Rebuilt with Boost 1.52.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt3.git20120417
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt2.git20120417
- New snapshot

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt2.git20111128
- Rebuilt with Boost 1.49.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt1.git20111128
- Version 2011.1.1

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20110314
- Rebuilt with Boost 1.48.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110314.1.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110314.1
- Rebuilt with Boost 1.47.0

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110314
- Version 2011.1

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.1-alt1.git20091015.1
- Rebuilt for debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.1-alt1.git20091015
- Initial build for Sisyphus

