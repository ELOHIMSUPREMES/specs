%define oname docker
%def_with python3

Name: python-module-%oname
Version: 1.10.3
Release: alt1

Summary: Python client for Docker.

License: %asl
Group: Development/Python
Url: https://github.com/docker/docker-py

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute
Requires: python-module-backports.ssl_match_hostname >= 3.5
Requires: python-module-ipaddress >= 1.0.16
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
An API client for docker written in Python

%if_with python3
%package -n python3-module-%oname
Summary: Python client for Docker. (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
An API client for docker written in Python
%endif


%prep
%setup -n %oname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
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

%files
%doc LICENSE README.md
# Exclude Windows specific stuff
%exclude %python_sitelibdir/%oname/transport/npipesocket.py
%exclude %python_sitelibdir/%oname/transport/npipeconn.py
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
# Exclude Windows specific stuff
%exclude %python3_sitelibdir/%oname/transport/npipesocket.py
%exclude %python3_sitelibdir/%oname/transport/npipeconn.py
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Wed Aug 3 2016 Vladimir Didenko <cow@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Fri Mar 11 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0
