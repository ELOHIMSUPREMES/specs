Name: spice-protocol
Version: 0.12.6
Release: alt1
Summary: Spice protocol header files
Group: Development/C
License: BSD
Url: http://www.spice-space.org/

Source: http://www.spice-space.org/download/releases/%name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

%description
Header files describing the spice protocol and the para-virtual graphics card QXL.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc COPYING NEWS
%_includedir/spice-1
%_datadir/pkgconfig/*.pc

%changelog
* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.6-alt1
- 0.12.6

* Mon May 20 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt2
- git snapshot 4f868cc354b617f55a0983fd2b2eafcb223b5772

* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt1
- 0.12.5

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.4-alt1
- 0.12.4

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Thu Nov 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue May 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt2
- upstream/0.8 snapshot with fixes from upstream/master

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sat Nov 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
