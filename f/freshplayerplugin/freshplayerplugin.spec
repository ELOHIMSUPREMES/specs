%define _libname libfreshwrapper-pepperflash

Name: freshplayerplugin
Version: 0.2.3
Release: alt2
Summary: PPAPI-host NPAPI-plugin adapter
License: MIT
Group: System/Libraries
Url: https://github.com/i-rinat/freshplayerplugin

# git clone https://github.com/i-rinat/freshplayerplugin.git
Source: %name-%version.tar

ExclusiveArch: %ix86 x86_64

# Automatically added by buildreq on Tue Mar 10 2015 (-bb)
# optimized out: cmake cmake-modules elfutils fontconfig fontconfig-devel glib2-devel libEGL-devel libGL-devel libX11-devel libXrender-devel libatk-devel libcairo-devel libcloog-isl4 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libjson-c libpango-devel libstdc++-devel libwayland-client libwayland-server pkg-config python-base xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: ctest gcc-c++ libGLES-devel libXrandr-devel libalsa-devel libconfig-devel libevent-devel libgtk+2-devel libpulseaudio-devel libssl-devel ragel

%{?!_without_check:%{?!_disable_check:BuildPreReq: ctest}}

Requires: update-pepperflash

%description
The main goal of this project is to get PPAPI (Pepper) Flash player
working in Firefox. This wrapper implements some kind of adapter which
will look like browser to PPAPI plugin and look like NPAPI plugin for
browser.

%prep
%setup
sed -i 's|^pepperflash_path = .*|pepperflash_path = "%_libdir/pepper-plugins/libpepflashplayer.so"|' data/freshwrapper.conf.example

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS='%optflags' \
  -DCMAKE_CXX_FLAGS='%optflags' \
  #
%cmake_build

%install
install -Dm 0644 BUILD/%_libname.so %buildroot%_libdir/browser-plugins/%_libname.so
install -Dm 0664 data/freshwrapper.conf.example %buildroot%_sysconfdir/freshwrapper.conf

%check
make -C BUILD check

%files
%doc COPYING LICENSE.MIT README.md
%_libdir/browser-plugins/%_libname.so
%config %_sysconfdir/freshwrapper.conf

%changelog
* Tue Mar 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.3-alt2
- Rebuilt with new update-pepperflash (arepo).
- Add R: update-pepperflash.

* Tue Mar 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.3-alt1
- Updated to 0.2.3.

* Wed Jan 21 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Mon Jan 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt2.gitad99227
- Updated to v0.2.1-152-gad99227.

* Thu Nov 06 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt1.git05da25f
- Initial build (v0.2.1-58-g05da25f).
