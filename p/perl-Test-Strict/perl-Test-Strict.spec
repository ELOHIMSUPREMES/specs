%define m_distro Test-Strict
Name: perl-Test-Strict
Version: 0.32
Release: alt1
Summary: Check syntax, presence of use strict; and test coverage

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~pdenis/Test-Strict/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Test-Pod-Coverage perl-Test-Pod perl-CGI perl-devel perl-Devel-Cover perl-Storable perl-B-Debug perl(IO/Scalar.pm)

%description
%summary

%prep
%setup -q -n %m_distro-%version
# fix test 04
mkdir cover_db

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Strict*
%doc Changes README 

%changelog
* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- added perl-B-Debug to buildreq to fix build

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build
