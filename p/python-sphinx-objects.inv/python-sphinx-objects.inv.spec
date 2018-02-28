%define inversion 2
%define pyversion 3.6
%define reldate 20160808

Name: python-sphinx-objects.inv
Version: %inversion.%pyversion.%reldate
Release: alt1
Summary: Sphinx inventory version %inversion
License: BSD
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>
Url: https://docs.python.org/dev/objects.inv
Source: %url
BuildArch: noarch

%description
This package contains periodically updated Sphinx inventory version %inversion
for Python %pyversion.

%install
mkdir -p %buildroot%_datadir/python-sphinx
install -pDm644 %SOURCE0 %buildroot%_datadir/python-sphinx/objects.inv

%files
%_datadir/python-sphinx/

%changelog
* Tue Aug 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160808-alt1
- repocop cronbuild 20160809. At your service.

* Sat Aug 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160806-alt1
- repocop cronbuild 20160806. At your service.

* Sat Jul 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160730-alt1
- repocop cronbuild 20160730. At your service.

* Sat Jul 16 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160716-alt1
- repocop cronbuild 20160716. At your service.

* Wed Jul 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160712-alt1
- repocop cronbuild 20160713. At your service.

* Sat Jul 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160708-alt1
- repocop cronbuild 20160709. At your service.

* Mon Jul 04 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160703-alt1
- repocop cronbuild 20160704. At your service.

* Sat Jun 25 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160624-alt1
- repocop cronbuild 20160625. At your service.

* Thu Jun 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160622-alt1
- repocop cronbuild 20160623. At your service.

* Wed Jun 22 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160621-alt1
- repocop cronbuild 20160622. At your service.

* Sun Jun 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160618-alt1
- repocop cronbuild 20160619. At your service.

* Sat Jun 18 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160617-alt1
- repocop cronbuild 20160618. At your service.

* Wed Jun 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160614-alt1
- repocop cronbuild 20160615. At your service.

* Sun Jun 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160612-alt1
- repocop cronbuild 20160612. At your service.

* Fri Jun 10 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160610-alt1
- repocop cronbuild 20160610. At your service.

* Thu Jun 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160608-alt1
- repocop cronbuild 20160609. At your service.

* Mon Jun 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160605-alt1
- repocop cronbuild 20160606. At your service.

* Sat Jun 04 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160604-alt1
- repocop cronbuild 20160604. At your service.

* Fri Jun 03 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160603-alt1
- repocop cronbuild 20160603. At your service.

* Thu Jun 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160601-alt1
- repocop cronbuild 20160602. At your service.

* Sat May 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160527-alt1
- repocop cronbuild 20160528. At your service.

* Wed May 25 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160524-alt1
- repocop cronbuild 20160525. At your service.

* Fri May 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160519-alt1
- repocop cronbuild 20160520. At your service.

* Sun May 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160515-alt1
- repocop cronbuild 20160515. At your service.

* Wed May 11 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160510-alt1
- repocop cronbuild 20160511. At your service.

* Mon May 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160508-alt1
- repocop cronbuild 20160509. At your service.

* Sun May 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160507-alt1
- repocop cronbuild 20160508. At your service.

* Sat Apr 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160429-alt1
- repocop cronbuild 20160430. At your service.

* Sat Apr 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160423-alt1
- repocop cronbuild 20160423. At your service.

* Tue Apr 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160416-alt1
- repocop cronbuild 20160419. At your service.

* Wed Apr 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160413-alt1
- repocop cronbuild 20160413. At your service.

* Tue Apr 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160411-alt1
- repocop cronbuild 20160412. At your service.

* Sat Apr 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160408-alt1
- repocop cronbuild 20160409. At your service.

* Tue Apr 05 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160404-alt1
- repocop cronbuild 20160405. At your service.

* Sat Apr 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160402-alt1
- repocop cronbuild 20160402. At your service.

* Fri Apr 01 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160401-alt1
- repocop cronbuild 20160401. At your service.

* Mon Mar 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160327-alt1
- repocop cronbuild 20160328. At your service.

* Thu Mar 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160323-alt1
- repocop cronbuild 20160324. At your service.

* Tue Mar 22 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160322-alt1
- repocop cronbuild 20160322. At your service.

* Mon Mar 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160321-alt1
- repocop cronbuild 20160321. At your service.

* Sun Mar 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160319-alt1
- repocop cronbuild 20160320. At your service.

* Sat Mar 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160318-alt1
- repocop cronbuild 20160319. At your service.

* Mon Mar 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160314-alt1
- repocop cronbuild 20160314. At your service.

* Sat Mar 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160311-alt1
- repocop cronbuild 20160312. At your service.

* Tue Mar 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160307-alt1
- repocop cronbuild 20160308. At your service.

* Fri Feb 26 2016 Dmitry V. Levin <ldv@altlinux.org> 2.3.6.20160226-alt1
- Initial revision.
