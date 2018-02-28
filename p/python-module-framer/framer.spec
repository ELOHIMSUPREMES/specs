%define _unpackaged_files_terminate_build 1
%define oname framer

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1
Summary: Network Framer Library
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/framer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/klmitch/framer.git
Source0: https://pypi.python.org/packages/19/11/b551fe240404fa52f2813a1e28210076acf5243079edb3efefa2fd2fb711/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-cobs python-module-six
BuildPreReq: python-module-mock python-module-trollius
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-cobs python3-module-six
BuildPreReq: python3-module-mock python3-module-asyncio
%endif

%py_provides %oname
%py_requires cobs six trollius

%description
The Framer library is a network communications library, built on top of
asyncio, for managing these units, which it calls frames. The Framer
library is built as an asyncio protocol which also happens to implement
the behavior of an asyncio transport. The protocol object can have
framers set on both directions of the communication; these framers
translate between the stream interface provided by TCP and the sequence
of frames desired by the application.

A framer is simply an object implementing a couple of methods which
implement the transformation from a stream to a frame and from a frame
to a sequence of bytes to transmit on the stream. These framers can
range from rather trivial--as in a text-oriented protocol like SMTP--all
the way to a complex binary data transmission protocol such as some
forms of RPC.

%package -n python3-module-%oname
Summary: Network Framer Library
Group: Development/Python3
%py3_provides %oname
%py3_requires cobs six asyncio

%description -n python3-module-%oname
The Framer library is a network communications library, built on top of
asyncio, for managing these units, which it calls frames. The Framer
library is built as an asyncio protocol which also happens to implement
the behavior of an asyncio transport. The protocol object can have
framers set on both directions of the communication; these framers
translate between the stream interface provided by TCP and the sequence
of frames desired by the application.

A framer is simply an object implementing a couple of methods which
implement the transformation from a stream to a frame and from a frame
to a sequence of bytes to transmit on the stream. These framers can
range from rather trivial--as in a text-oriented protocol like SMTP--all
the way to a complex binary data transmission protocol such as some
forms of RPC.

%prep
%setup -q -n %{oname}-%{version}

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

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20140531.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140531
- Initial build for Sisyphus

