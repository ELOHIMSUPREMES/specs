%define dist Devel-Declare
Name: perl-%dist
Version: 0.006016
Release: alt1

Summary: Adding keywords to perl, in perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/Devel-Declare-%{version}.tar.gz

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-B-Hooks-EndOfScope perl-B-Hooks-OP-Check perl-ExtUtils-Depends perl-Pod-Escapes perl-Sub-Name perl-Test-Warn perl(Test/Requires.pm)

%description
Devel::Declare can install subroutines called declarators which locally
take over Perl's parser, allowing the creation of new syntax.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.006016-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.006015-alt1
- automated CPAN update

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.006014-alt2
- built for perl 5.18

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.006014-alt1
- automated CPAN update

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.006011-alt1
- 0.006008 -> 0.006011
- built for perl-5.16

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.006008-alt1
- initial revision
