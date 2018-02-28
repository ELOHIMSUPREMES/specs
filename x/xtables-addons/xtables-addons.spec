Name: xtables-addons
Version: 2.8
Release: alt1
Summary: IP tables addons
Group: System/Kernel and hardware

URL: http://xtables-addons.sourceforge.net/
License: GPLv2

# git://xtables-addons.git.sf.net/gitroot/xtables-addons/xtables-addons.git
# git://git.altlinux.org/gears/x/xtables-addons.git
Source: %name-%version.tar
Source1: %name.watch
Patch: %name-%version-%release.patch

%define _libexecdir /usr/libexec

BuildRequires: libiptables-devel libmnl-devel perl-Text-CSV_XS
Requires: iptables
ExclusiveArch: %ix86 x86_32 x86_64

%description
Xtables-addons is the proclaimed successor to patch-o-matic(-ng).
It contains extensions that were not accepted in the main Xtables

%package geoip-utils
Summary: Tools for build and update geoip data
License: GPLv2
Group: System/Kernel and hardware
BuildArch: noarch

%description geoip-utils
Tools for build and update geoip data

%package -n kernel-source-%name
Summary: xtables module sources
Group: Development/Kernel
BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description -n kernel-source-%name
XTable addons module sources for Linux kernel.

%prep
%setup
%patch -p1
%autoreconf
%configure --libdir=/%_lib --with-kbuild=no --with-xtlibdir=/%_lib/iptables

%build
%make_build

%install
%makeinstall_std
tar -xf %SOURCE0
mv %name-%version/extensions kernel-source-%name-%version
cp mconfig kernel-source-%name-%version/mconfig
cp kernel-source-%name-%version/Mbuild kernel-source-%name-%version/Makefile
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%name-%version.tar.bz2 kernel-source-%name-%version

%files
%doc README
%_sbindir/*
%attr(0755,root,root) /%_lib/lib*.so*
/%_lib/iptables/*.so*
%_man8dir/*

%files geoip-utils
%_man1dir/*
%_libexecdir/xtables-addons

%files -n kernel-source-%name
%kernel_src/*

%changelog
* Thu Oct 08 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.8-alt1
- new version

* Fri Oct 17 2014 Anton Farygin <rider@altlinux.ru> 2.6-alt1
- new version

* Tue Jun 17 2014 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- new version
- added watch file

* Thu Mar 27 2014 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- New version

* Wed Mar 06 2013 Dmitry V. Levin <ldv@altlinux.org> 1.47.1-alt1
- Updated to v1.47.1-2-gdf9d3c9.
- Built with libxtables.so.10.

* Thu Oct 11 2012 Dmitry V. Levin <ldv@altlinux.org> 1.46-alt1
- Update to v1.46.
- Built with libxtables.so.9.

* Fri May 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.42-alt1
- Fixed build.
- Built with libxtables.so.7.
- Blind update to v1.42-3-g1e8da7c.
- No more ipset-related subpackages, the feature was removed in v1.42~1.

* Mon Oct 10 2011 Anton Farygin <rider@altlinux.ru> 1.39-alt1
- new version

* Sun Mar 06 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.33-alt1
- Update new version

* Sun Jan 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.32-alt1
- Update new version
- Add ipset subpackage and libipset

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 1.30-alt1
- Initial build for Sisyphus, thanls to Sergei Epiphanov for specfile
