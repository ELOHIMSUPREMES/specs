%define _unpackaged_files_terminate_build 1
%define dist Capture-Tiny
Name: perl-Capture-Tiny
Version: 0.25
Release: alt1

Summary: Capture::Tiny - Capture STDOUT and STDERR from Perl, XS or external programs
Group: Development/Perl
License: Apache 2.0

Url: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Build perl-Test-Differences

%description
%summary

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Capture/Tiny*
%doc Changes Todo LICENSE README 

%changelog
* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- 0.18 -> 0.20
- built as plain srpm

* Thu May 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt1
- New version 0.18

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- New version 0.17

* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- New version 0.13

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- New version 0.10

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- New version 0.09

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- New version 0.08

* Sun Jan 31 2010 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- initial build
