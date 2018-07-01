Name:		xmrig
Version:	2.6.2
Release:	alt1
Summary:	Monero (XMR) CPU miner
Url:		https://github.com/xmrig/xmrig
Group:		Office
License:	GPLv3
Source0:	%name.tar.xz

BuildRequires: cmake gcc-c++ libmicrohttpd-devel libstdc++-devel-static libuv-devel

%description
XMRig is high performance Monero (XMR) CPU miner, with the official full Windows support.
Originally based on cpuminer-multi with heavy optimizations/rewrites and removing a lot
of legacy code, since version 1.0.0 complete rewritten from scratch on C++.

%prep
%setup -n %name

%build
mkdir ./build && cd ./build
cmake		../. \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
		-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
cd ./build
install -Dp -m 0755 ./%name %buildroot%_bindir/%name

%files
%doc LICENSE README.md CHANGELOG.md src/config.json
%_bindir/*

%changelog
* Fri Jun 08 2018 Motsyo Gennadi <drool@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sat Apr 21 2018 Motsyo Gennadi <drool@altlinux.ru> 2.6.0-alt0.beta3
- 2.6.0-beta3

* Tue Apr 10 2018 Motsyo Gennadi <drool@altlinux.ru> 2.6.0-alt0.beta2
- 2.6.0-beta2

* Thu Apr 05 2018 Motsyo Gennadi <drool@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Tue Jan 30 2018 Motsyo Gennadi <drool@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Tue Nov 07 2017 Motsyo Gennadi <drool@altlinux.ru> 2.4.3-alt2
- added config.json as example

* Mon Nov 06 2017 Motsyo Gennadi <drool@altlinux.ru> 2.4.3-alt1
- initial build for ALT Linux
