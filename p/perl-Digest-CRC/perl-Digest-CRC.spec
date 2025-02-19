%define _unpackaged_files_terminate_build 1
#
#   - Digest::CRC -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version 0.14 Digest::CRC
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Digest-CRC
%define m_distro Digest-CRC
%define m_name Digest::CRC
%define m_author_id OLIMAUL
%define _enable_test 1

Name: perl-Digest-CRC
Version: 0.21
Release: alt1.2

Summary: Digest::CRC - Generic CRC functions

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Digest-CRC/

Packager: Michael Bochkaryov <misha@altlinux.ru>

Source: http://www.cpan.org/authors/id/O/OL/OLIMAUL/Digest-CRC-%{version}.tar.gz

#BuildArch: noarch
# Automatically added by buildreq on Mon Jun 30 2008
BuildRequires: perl-Module-Build

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains wrapper
functions with the correct parameters for CRC-CCITT, CRC-16 and CRC-32.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/D*
%perl_vendor_autolib/*
%doc README Changes

%changelog
* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1.2
- rebuilt with perl 5.12
- noarch package

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.14-alt1
- first build for ALT Linux Sisyphus

