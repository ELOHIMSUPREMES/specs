%define dist Date-Calc-XS
%def_without bootstrap
Name: perl-%dist
Version: 6.3
Release: alt4

Summary: XS wrapper and C library plug-in for Date::Calc
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: perl-devel perl-Carp-Clan perl-Bit-Vector

%if_with bootstrap
# bootstrap: disable build dependency on Date::Calc
%def_disable test
%else
BuildRequires: perl-Date-Calc
%endif

%description
This package provides all sorts of date calculations based on the Gregorian
calendar (the one used in all western countries today).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	CHANGES.txt CREDITS.txt README.txt
%dir	%perl_vendor_archlib/Date
%dir	%perl_vendor_archlib/Date/Calc
	%perl_vendor_archlib/Date/Calc/XS.pm
%doc	%perl_vendor_archlib/Date/Calc/XS.pod
%dir	%perl_vendor_autolib/Date
%dir	%perl_vendor_autolib/Date/Calc
%dir	%perl_vendor_autolib/Date/Calc/XS
	%perl_vendor_autolib/Date/Calc/XS/XS.so

%changelog
* Thu Sep 05 2013 Vladimir Lettiev <crux@altlinux.ru> 6.3-alt4
- re-enabled build dependency on perl-Date-Calc

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 6.3-alt3
- built for perl 5.18
- disabled build dependency on perl-Date-Calc, for bootstrap

* Sun Sep 09 2012 Vladimir Lettiev <crux@altlinux.ru> 6.3-alt2
- re-enabled build dependency on perl-Date-Calc

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 6.3-alt1
- 6.2 -> 6.3
- built for perl-5.16
- disabled build dependency on perl-Date-Calc, for bootstrap

* Thu Nov 10 2011 Alexey Tourbin <at@altlinux.ru> 6.2-alt3
- re-enabled build dependency on perl-Date-Calc

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 6.2-alt2
- rebuilt for perl-5.14

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 6.2-alt1.1
- rebuilt for perl-5.12
- disabled build dependency on perl-Date-Calc, for bootstrap

* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 6.2-alt1
- initial revision
