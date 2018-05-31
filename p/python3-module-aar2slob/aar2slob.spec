%define oname aar2slob

%def_without bootstrap

Name: python3-module-%oname
Version: 0.01
Release: alt2
Summary: converts Aard Dictionary .aar files to slob format
BuildArch: noarch
Group: Development/Other
Url: http://aarddict.org
License: GPL3

#https://github.com/itkach/aar2slob.git
Source: %name.tar

%if_with bootstrap
Requires: python3.3(cssselect)
%endif

BuildPreReq: rpm-build-python3


%description
converts Aard Dictionary .aar files to slob format

%prep
%setup -n %name

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir --record=INSTALLED_FILES

%files
%python3_sitelibdir/%{oname}*
%doc README*

%changelog
* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.01-alt2
- rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.01-alt1.git.x.gf1956a.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Feb 14 2015 Ildar Mulyukov <ildar@altlinux.ru> 0.01-alt1.git.x.gf1956a
- initial build for ALT Linux Sisyphus
