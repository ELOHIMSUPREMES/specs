%define dist B-Hooks-EndOfScope
Name: perl-%dist
Version: 0.14
Release: alt1

Summary: Execute code after a scope finished compilation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-%{version}.tar.gz

BuildArch: noarch

BuildRequires: perl-Module-Install perl-Sub-Exporter-Progressive perl-Variable-Magic perl-Module-Implementation perl-Module-Runtime

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/B/Hooks/EndOfScope*

%changelog
* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Tue Jun 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.12

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- initial revision, for namespace::clean
