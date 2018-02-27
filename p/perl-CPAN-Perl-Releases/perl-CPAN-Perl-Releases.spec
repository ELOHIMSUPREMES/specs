Name: perl-CPAN-Perl-Releases
Version: 1.42
Release: alt1

Summary: Mapping Perl releases on CPAN to the location of the tarballs
Group: Development/Perl
License: perl

Url: %CPAN CPAN-Perl-Releases
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CPAN/Perl/Releases*
%doc Changes LICENSE README

%changelog
* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- 0.72 -> 1.42

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt1
- initial build for ALTLinux

