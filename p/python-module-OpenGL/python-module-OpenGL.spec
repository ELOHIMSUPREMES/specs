%define oname OpenGL

%def_with python3

Name: python-module-%oname
Version: 3.1.0
Release: alt1

Summary: A Python module for interfacing with the OpenGL library
Summary(ru_RU.KOI8-R): ���������� ����� Python ��� ������ � ����������� OpenGL

Group: Development/Python
License: see license.txt
Url: http://pyopengl.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: PyOpenGL-%version.tar.gz
Patch: PyOpenGL-swig.patch
Patch1: %name.patch

BuildArch: noarch

%setup_python_module OpenGL

#add_python_req_skip WGL__init__

BuildPreReq: python-module-setuptools python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package -n python3-module-%oname
Summary: A Python module for interfacing with the OpenGL library
Group: Development/Python3

%description -n python3-module-%oname
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package -n python3-module-%oname-tests
Summary: PyOpenGL tests
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip pygame

%description -n python3-module-%oname-tests
PyOpenGL tests.

%package demo
Summary: PyOpenGL demo files
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip items win32ui

%description demo
Demo for PyOpenGL

%package doc
Summary: PyOpenGL documentation
Group: Development/Python
Requires: %name = %version-%release

%description doc
PyOpenGL documentation

%package tests
Summary: PyOpenGL tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
PyOpenGL tests.

%prep
%setup -n PyOpenGL-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!%_bindir/python|#!%_bindir/python3|' '{}' +
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#! %_bindir/env python|#!%_bindir/python3|' '{}' +
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
touch tests/__init__.py
cp -fR tests %buildroot/%python_sitelibdir/%modulename/

%if_with python3
pushd ../python3
%python3_install
touch tests/__init__.py
cp -fR tests %buildroot/%python3_sitelibdir/%modulename/
popd
%endif

%files
%python_sitelibdir/*.egg-info
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/tests

%files tests
%python_sitelibdir/%modulename/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/tests
%endif

%changelog
* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Version 3.1.0
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Version 3.0.1
- Added tests subpackage

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt3.1
- Rebuilt with python 2.6

* Mon Feb 16 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt3
- new version 3.0.0c1
- build package as noarch

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- new version 3.0.0b8
- remove tests packing (fix bug #18378)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0)
- cleanup spec, update buildreqs

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.2.01-alt2
- fix Source tag

* Tue Jul 19 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.2.01-alt1
- first build for ALT Linux Sisyphus
