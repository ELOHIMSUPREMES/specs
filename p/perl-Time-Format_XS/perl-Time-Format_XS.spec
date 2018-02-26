%define dist Time-Format_XS
Name: perl-%dist
Version: 1.03
Release: alt2

Summary: Companion module for Time::Format, to speed up time formatting
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-DateTime perl-devel

%description
This is a companion module to Time::Format.  It contains a version
of the time_format function written in C, so it is much faster.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/Time
%perl_vendor_archlib/Time

%changelog
* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1.1
- rebuilt with perl 5.12

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt1
- New version 1.03

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt0
- Initial build
