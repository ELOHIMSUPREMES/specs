%define m_distro Test-Script
Name: perl-Test-Script
Version: 1.10
Release: alt1
Summary: Test::Script - Basic cross-platform tests for scripts

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/Test-Script/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-IPC-Run3 perl-Probe-Perl perl(Test/Tester.pm)

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Script*
%doc Changes README 

%changelog
* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- initial build
