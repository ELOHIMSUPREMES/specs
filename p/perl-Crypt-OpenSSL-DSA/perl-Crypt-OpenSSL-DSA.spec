%define module Crypt-OpenSSL-DSA

Name: perl-%module
Version: 0.14
Release: alt2.1

Summary: Digital Signature Algorithm using OpenSSL 
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/T/TJ/TJMATHER/Crypt-OpenSSL-DSA-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libssl-devel openssl perl-Digest-SHA1 perl-devel

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm) signature
verification system.

It is a thin XS wrapper to the DSA functions contained in the OpenSSL crypto
library, located at http://www.openssl.org

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- built for perl 5.18

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1.1
- rebuilt with perl 5.12

* Mon Oct 05 2009 Victor Forsyuk <force@altlinux.org> 0.13-alt1
- Initial build.
