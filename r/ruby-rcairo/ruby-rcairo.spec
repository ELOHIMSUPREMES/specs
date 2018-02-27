# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname rcairo

Name: ruby-%pkgname
Version: 1.10.0
Release: alt4.2

Summary: ruby bindings for cairo
Group: Development/Ruby
License: GPLv2/Ruby
Url: http://cairographics.org/rcairo
Obsoletes: rcairo < 1.7.0
Provides: rcairo = %version-%release

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildPreReq: rpm-build-ruby
# Automatically added by buildreq on Thu May 17 2012 (-bi)
# optimized out: elfutils fontconfig libEGL-devel libGL-devel libX11-devel libruby-devel libwayland-client libwayland-server pkg-config python-base rpm-build-ruby ruby ruby-stdlibs xorg-xproto-devel
BuildRequires: libcairo-devel ruby-pkg-config libruby-devel

# buildreq misses a lot this time
BuildRequires: glib2-devel libpixman-devel xorg-glproto-devel xorg-dri2proto-devel libXau-devel libXdmcp-devel libXext-devel libXdamage-devel libXxf86vm-devel
BuildRequires: pkgconfig(expat)

%description
Ruby bindings for cairo // cairo extension for Ruby.

%package devel
Summary: Development files for %name
Group: Development/Ruby
Requires: %name = %version-%release
PreReq: libruby-devel
Obsoletes: rcairo-devel < 1.7.0
Provides: rcairo-devel = %version-%release
# due to #include <cairo.h>
Requires: libcairo-devel

%description devel
Ruby bindings for cairo // cairo extension for Ruby.

This package contains development files.

%prep
%setup -n %pkgname-%version
%patch -p1

%build
export RUBYOPT=-rvendor-specific
%ruby_configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README.rdoc
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files devel
%doc samples
%_includedir/*

%changelog
* Mon Oct 07 2013 Led <led@altlinux.ru> 1.10.0-alt4.2
- fixed BuildRequires

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.10.0-alt4.1
- Rebuilt with ruby-1.9.3-alt1
- updated BuildRequires

* Thu May 17 2012 Michael Shigorin <mike@altlinux.org> 1.10.0-alt4
- fixed FTBFS by updating BR:

* Sat May 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.10.0-alt3
- ruby-rcairo-devel: Added libcairo-devel to requirements.
- Updated build dependencies.
- Rebuilt with libcairo-1.10.2-alt7.

* Tue May 03 2011 Timur Aitov <timonbl4@altlinux.org> 1.10.0-alt2
- Repair build

* Sun Jan 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1.10.0-alt1
- [1.10.0]

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 1.8.1-alt1
- [1.8.1]

* Sat May 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.8.0-alt3
- Rebuild with new ruby

* Fri Dec 12 2008 Kirill A. Shutemov <kas@altlinux.org> 1.8.0-alt2
- Update BuildRequires

* Fri Oct 03 2008 Sir Raorn <raorn@altlinux.ru> 1.8.0-alt1
- [1.8.0]

* Tue Sep 02 2008 Sir Raorn <raorn@altlinux.ru> 1.7.0-alt1
- [1.7.0]
- Package renamed to ruby-rcairo

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 1.5.1-alt1
- [1.5.1]

* Thu Jan 25 2007 Sir Raorn <raorn@altlinux.ru> 1.2.0-alt1
- Built for Sisyphus

