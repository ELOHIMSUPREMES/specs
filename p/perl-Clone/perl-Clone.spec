%define dist Clone
Name: perl-%dist
Version: 0.34
Release: alt2

Summary: Recursively copy Perl datatypes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GA/GARU/Clone-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types,
including tied variables and objects.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Clone*
%perl_vendor_autolib/Clone*

%changelog
* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.31-alt4
- rebuilt for perl-5.16

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 0.31-alt3
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.31-alt2
- rebuilt as plain src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.31-alt1.1
- rebuilt for perl-5.12

* Tue Mar 10 2009 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.28 -> 0.31

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- 0.27 -> 0.28

* Thu Jul 26 2007 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- 0.22 -> 0.27
- Clone.pm: replaced DynaLoader with XSLoader, removed AutoLoader

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.20 -> 0.22

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- 0.18 -> 0.20

* Tue Sep 06 2005 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- initial revision (for PPI) (also for Class::DBI)
