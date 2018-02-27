Name: python-module-potr
Version: 1.0.1
Release: alt1
Summary: Python Off-The-Record encryption
Group: Development/Python
License: LGPLv3+
Url: http://python-otr.pentabarf.de
BuildArch: noarch
Source: python-potr-%version.zip

BuildRequires(pre): rpm-build-python3 unzip

BuildRequires: python-module-distribute  python-devel
BuildRequires: python3-module-distribute python3-devel

%description
This is a pure Python OTR implementation; it does not bind to libotr.

%package -n python3-module-potr
Group: Development/Python
Summary: %summary
%description -n python3-module-potr
This is a pure Python OTR implementation; it does not bind to libotr.

%prep
%setup -n python-potr-%version

%build
cp -a . ../python3
%python_build
cd ../python3 && %python3_build

%install
%python_install
cd ../python3 && %python3_install

%files
%doc src/tools/convertkey.py CHANGELOG PKG-INFO
%python_sitelibdir_noarch/*

%files -n python3-module-potr
%doc src/tools/convertkey.py CHANGELOG PKG-INFO
%python3_sitelibdir_noarch/*

%changelog
* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Autobuild version bump to 1.0.0

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 0.9.9-alt1
- Initial build from scratch

