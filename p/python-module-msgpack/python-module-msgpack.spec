%define oname msgpack

%def_with python3

Name: python-module-%oname
Version: 0.4.6
Release: alt1.git20150323

Summary: A Python MessagePack (de)serializer

Group: Development/Python
License: ASL 2.0
URL: http://pypi.python.org/pypi/msgpack-python/

# https://github.com/msgpack/msgpack-python.git
Source: %name-%version.tar

BuildRequires: python-module-distribute python-module-Cython python-module-nose
BuildPreReq: gcc-c++

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.

%if_with python3
%package -n python3-module-%oname
Group: Development/Python3
Summary: A Python3 MessagePack (de)serializer
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3-module-Cython python3-module-nose

%description -n python3-module-%oname
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python3 (de)serializer for MessagePack.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python3
pushd ../python3
popd
%endif

%files
%doc COPYING
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20150323
- Version 0.4.6

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.git20150126
- Version 0.4.5

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140326
- Version 0.4.2

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.2.2-alt1.1
- Rebuild with Python-3.3

* Thu Dec 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.2-alt1
- New version

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.12-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.12-alt1
- initial
