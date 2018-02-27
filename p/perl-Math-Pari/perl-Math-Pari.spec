%define _unpackaged_files_terminate_build 1
%define dist Math-Pari
Name: perl-%dist
Version: 2.010808
Release: alt1
Serial: 1

Summary: Perl interface to PARI
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/I/IL/ILYAZ/modules/Math-Pari-%{version}.zip
Source1: http://pari.math.u-bordeaux.fr/pub/pari/unix/OLD/pari-2.3.5.tar.gz

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-devel unzip

%description
This package is a Perl interface to famous library PARI for
numerical/scientific/number-theoretic calculations.  It allows use of
most PARI functions as Perl functions, and (almost) seamless merging
of PARI and Perl data. In what follows we suppose prior knowledge of
what PARI is (see <ftp://megrez.math.u-bordeaux.fr/pub/pari>, or
Math::libPARI).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build pari_tgz=%SOURCE1

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Math
%perl_vendor_autolib/Math

%changelog
* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.010808-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 2.01080607-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.01080605-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 2.01080605-alt3
- rebuilt for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 2.01080605-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.01080605-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.01080604-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.01080604-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.010709-alt2
- fix directory ownership violation

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.010709-alt1
- new version (2.010709)
- fix build

* Mon Jun 05 2006 Vitaly Lipatov <lav@altlinux.ru> 2.010706-alt1
- new version (2.010706)

* Sun Dec 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.010702-alt1
- new version; TODO: what about linking with system libpari?
- add textrel=relaxed :(

* Thu Oct 06 2005 Vitaly Lipatov <lav@altlinux.ru> 2.010604-alt1
- new version

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.010603-alt1
- first build for ALT Linux Sisyphus
