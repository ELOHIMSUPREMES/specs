%define _unpackaged_files_terminate_build 1
%define module Test-Differences

Name: perl-%module
Version: 0.66
Release: alt1
Epoch: 1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Test strings and data structures and show differences if not ok
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source0: http://www.cpan.org/authors/id/D/DC/DCANTRELL/Test-Differences-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Diff perl(Capture/Tiny.pm)

%description
Test strings and data structures and show differences if not ok.

%prep
%setup -q -n Test-Differences-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test

%changelog
* Thu Feb 28 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.66-alt1
- automated CPAN update

* Wed Feb 20 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.65-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.64-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.63-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.62-alt1
- automated CPAN update

* Wed Sep 21 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.61-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.500-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.500-alt1
- 0.500

* Fri Jul 27 2007 Victor Forsyuk <force@altlinux.org> 0.47-alt2
- Spec cleanups.

* Thu Aug 25 2005 Alexey Morozov <morozov@altlinux.org> 0.47-alt1
- Initial build for ALT Linux
