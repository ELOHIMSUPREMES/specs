%define dist namespace-clean

Name: perl-namespace-clean
Version: 0.24
Release: alt1

Summary: Keep imports and functions out of your namespace

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source: %dist-%version.tar

BuildRequires: perl-B-Hooks-EndOfScope perl-Package-Stash perl-devel

%description
None.

%prep
%setup -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/namespace/clean.pm

%changelog
* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 0.24-alt1
- 0.024
- spec cleanup

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- initial revision, for MooseX::Types


