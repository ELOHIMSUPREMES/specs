%define cid            uBlock0@raymondhill.net
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cidf_dir       %firefox_noarch_extensionsdir/%cid

Name: uBlock
Version: 1.0.0.1
Release: alt1.2

Summary: uBlock: an efficient blocker extension for your browser. Fast, potent, and lean
License: GPLv3
Group: Other
Url: https://github.com/chrisaljoudi/uBlock
BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name.tar

# Automatically added by buildreq on Tue Jul 28 2015
# optimized out: python-base python-module-Zope2 python-modules python-modules-compiler python-modules-encodings python-modules-json
BuildRequires: libdb4-devel
BuildRequires: python-module-distribute
BuildRequires: python-modules-json


%package -n palemoon-uBlock
Group: System/Libraries
Summary: Plugin  uBlock for palemoon
Requires: palemoon

%package -n firefox-uBlock
Group: System/Libraries
Summary: Plugin  uBlock for fitefox
Requires: firefox

BuildRequires(pre):	rpm-build-palemoon
BuildRequires(pre):	rpm-build-firefox

%description
An efficient blocker: easy on memory and CPU footprint, and yet can load and enforce
thousands more filters than other popular blockers out there.


%description -l ru_RU.utf8
uBock-origin - эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.

%description -n palemoon-uBlock
Plugin uBlock: an efficient blocker extension for palemoon. Fast, potent, and lean.

%description  -l ru_RU.utf8 -n palemoon-uBlock
Плагин uBlock  эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.

%description -n firefox-uBlock
Plugin uBlock: an efficient blocker extension for palemoon. Fast, potent, and lean.

%description  -l ru_RU.utf8 -n firefox-uBlock
uBock-origin - эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.

%prep
%setup -n %name

%build
tools/make-firefox.sh

%install
pushd dist/build/uBlock0.firefox/
mkdir -p %buildroot/%cid_dir
cp -r * %buildroot/%cid_dir

mkdir -p %buildroot/%cidf_dir
cp -r * %buildroot/%cidf_dir

popd

%files -n palemoon-uBlock
%cid_dir

%files -n firefox-uBlock
%cidf_dir

%changelog
* Fri Jul 31 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0.1-alt1.2
- Add  Requires

* Tue Jul 28 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0.1-alt1.1
- Fix Builds

* Mon Jul 27 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.0,0.1-alt1
- initial build for ALT Linux Sisyphus
