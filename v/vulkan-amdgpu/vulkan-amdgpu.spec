%define _vklib amdvlk
%define _vkdir %_datadir/vulkan/icd.d
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%define optflags_debug -g1

%def_with wayland

%ifarch x86_64
%define bits 64
%endif
%ifarch %ix86
%define bits 32
%endif

Name: vulkan-amdgpu
Version: 2019.Q2.3
Release: alt2
License: MIT
Url: https://github.com/GPUOpen-Drivers/AMDVLK
Summary: AMD Open Source Driver For Vulkan
Group: System/X11

ExclusiveArch: %ix86 x86_64

Requires: vulkan-filesystem

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc7-c++ cmake python3-devel curl libstdc++7-devel libxcb-devel
BuildRequires: libX11-devel libxshmfence-devel libXrandr-devel spirv-headers libspirv-tools-devel glslang-devel
%if_with wayland
BuildRequires: wayland-devel libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel
%endif

Source0: xgl.tar.xz
Source1: pal.tar.xz
Source2: llpc.tar.xz
Source3: spvgen.tar.xz
Source4: llvm.tar.xz
Source5: amd_icd.json

Patch: spvgen-alt-shared.patch

%description
The AMD Open Source Driver for Vulkan(r) is an open-source Vulkan driver for
Radeon(tm) graphics adapters on Linux(r). It is built on top of AMD's Platform
Abstraction Library (PAL), a shared component that is designed to encapsulate
certain hardware and OS-specific programming details for many of AMD's 3D and
compute drivers. Leveraging PAL can help provide a consistent experience across
platforms, including support for recently released GPUs and compatibility with
AMD developer tools.

%prep
%setup -n xgl -b0 -b1 -b2 -b3 -b4
pushd %_builddir/spvgen
%patch -p2
popd

%build
# build amdvlk.so
pushd %_builddir/xgl
export GCC_VERSION=7 \
%cmake \
	-DCMAKE_AR:PATH=%_bindir/gcc-ar \
	-DCMAKE_NM:PATH=%_bindir/gcc-nm \
	-DCMAKE_RANLIB:PATH=%_bindir/gcc-ranlib \
	-DCMAKE_BUILD_TYPE=Release \
%if_with wayland
	-DBUILD_WAYLAND_SUPPORT=ON \
%endif
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON

%cmake_build
popd

%install
mkdir -p %buildroot{%_vkdir,%_libdir,%_sysconfdir/amd}
touch %buildroot%_sysconfdir/amd/amdPalSettings.cfg

install -p -m644 %_builddir/xgl/BUILD/icd/%_vklib%bits.so %buildroot%_libdir/%_vklib.so
install -p -m644 %SOURCE5 %buildroot%_vkdir/amd_icd.json

%files
%_libdir/*.so
%_vkdir/*.json
%dir %_sysconfdir/amd
%ghost %attr(644,root,root) %config(missingok) %_sysconfdir/amd/*.cfg

%changelog
* Mon May 13 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q2.3-alt2
- spvgen: fix build.

* Mon May 13 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q2.3-alt1
- 2019-05-12 update:
  + xgl: eaecf6b9ad7bc3d310e752528f84fd52fba23747
  + pal: fb9a4dc951c0afd737460b26afb716c96e966b77
  + llpc: fdd5e24be2d9031ab685690cad1c9259d96518f6
  + llvm: f41e1a873108a371ae5574d518c1ee6eb3814cee
- json: bump vulkan version.

* Mon Apr 15 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q2.1-alt1
- 2019-4-10 update:
  + xgl: 5b4058dc288a25f6554fcc61f80bf3f27eb35d8d
  + pal: 99901922d67e502ff4233a8bfcbfa0347c0ffa1b
  + llpc: 6c6de1dab3927bfb0f6659ba89c6fe80be8a4a04
  + spvgen: 69311f7c1e220d190909298b9c7bd702ecc237ff
- json: bump vulkan version.

* Sat Apr 13 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.9-alt2
- Rebuild w/ gcc7.

* Tue Mar 26 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.9-alt1
- 2019-3-26 update:
  + llvm: 97cc33415120ae3ed472b6dd5cb234b74a80bd80
  + spvgen: 1560d287f779b342e0019499dda85890cb07affc
  + llpc: 32c0c28b1b7fd36b2f9cb17411af2963f6cfc48a
  + pal: e17272e1581ae6e222293880db08e0df7b1f1f75
  + xgl: a082b41ad4a8aed476cb39e6b63cddd25ab9e0b4
- .json: make biarch friendly.

* Wed Mar 06 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.7-alt1
- 2019-3-1 update:
  + llvm: c7a5a5c3bac75699d45824523b4fcf045913413f
  + llpc: 8eecb4baef898f0a5b9902406626887c3646dbb6
  + pal: e8a5acd90310871053a40015ebcea5b32391a824
  + xgl: f2af4b0c33963842f544107d005f0a6c82ea513f

* Tue Feb 26 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.6-alt1
- 2019-2-25 update:
  + llvm: 666d463e73a67dd3ccb304a5b13a5b1f09f784f0
  + llpc: b26545220db28772ac07491e17d31bbcf9c249ec
  + pal: 534ab72b967e07934dade777caf15686dc04b940
  + xgl: 1d35effd11e3d47a8e5281f06b75dd334641476e

* Fri Feb 01 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.4-alt1
- 2019-2-1 update:
  + llvm: d3c2b9d104f0de0be59d914578a28275c8b4784d
  + llpc: a1ee25169453ba909ba940d7d25e2739d2f453ed
  + pal: 3bb2d4082ef9b95a114258a90c7044939a5f0638
  + xgl: dbabc93bc9c3a5a1e7e73672b3d4594b0611fa36
- icd.json: bump vulkan version.

* Tue Jan 22 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.2-alt1
- 2019-1-15 update:
  + llvm: 3c7dbb214c3680803f7d3e3c3aed02fddb2f7dbb
  + spvgen: d26082d54930ad2ea97da94a2443137e7325b64c
  + llpc: 797be964eb8d65f2ec162a783708b36834a62000
  + pal: 2e94fa1533a606d076061db8d5be514bb69adfc3
  + xgl: 0d7c5a69ba314bfabe2d5dbe3e5e4d1ea3228845
- .spec: added missing conf dir.

* Sat Jan 12 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.1-alt3
- Rebuild w/ gcc5 (as it does ubuntu).

* Sat Jan 12 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.1-alt2
- Added wayland knob.
- Fix llvm merge.

* Wed Jan 09 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.1-alt1
- Initial build for ALTLinux:
  + do not build spvgen for now (only tests rely on it);
  + use gcc7 (gcc8 still unsupported by icd);
- Checkout from github:
  + xgl: master--bca286c1146f9f0662bbb7c10d193e487579e6f0
  + pal: master--f924a4fb84efde321f7754031f8cfa5ab35055d3
  + llpc: master--f36099d4c778327f22b050432f09e17dc815474a
  + spvgen: master--328a0990a958f21eb2c6b1ecb092a43629fe5554
  + llvm: master--0843ddd6f5a03468d42b90715e98e9798f772555
