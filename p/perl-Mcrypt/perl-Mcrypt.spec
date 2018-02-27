Name: perl-Mcrypt
Version: 2.5.7.0
Release: alt2

Summary: Mcrypt - Perl extension for the Mcrypt cryptography library
Group: Development/Perl
License: Perl

Url: %CPAN Mcrypt
Source: %name-%version.tar

BuildRequires: libmcrypt-devel perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Mcrypt*
%perl_vendor_autolib/Mcrypt*
%doc ChangeLog README 

%changelog
* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 2.5.7.0-alt2
- built for perl 5.18

* Thu Sep 20 2012 Vladimir Lettiev <crux@altlinux.ru> 2.5.7.0-alt1
- initial build
