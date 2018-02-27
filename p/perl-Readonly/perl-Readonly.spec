%define dist Readonly

Name: perl-%dist
Version: 1.03
Release: alt4

Summary: Readonly - facility for creating read-only scalars, arrays, hashes
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/modules/by-module/Readonly/%dist-%version.tar.gz

BuildArch: noarch

#Requires: perl-Readonly-XS

BuildRequires: perl-devel

%description
This is a facility for creating non-modifiable variables. This is useful
for configuration files, headers, etc. It can also be useful as a
development and debugging tool, for catching updates to variables that
should not be changed.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
# Come home, baby!
mv %buildroot%perl_vendor_privlib/benchmark.pl .

%files
%doc README benchmark.pl
%perl_vendor_privlib/Readonly.pm

%changelog
* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt4
- built for perl 5.18
- bootstrap: disabled dependency on perl-Readonly-XS

* Sun Sep 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt3
- enabled dependency on perl-Readonly-XS

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2
- rebuilt for perl-5.16
- bootstrap: disabled dependency on perl-Readonly-XS

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt1.2
- rebuilt for perl-5.14
- enabled dependency on perl-Readonly-XS

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1.1
- rebuilt with perl 5.12

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 1.03-alt1
- Initial build.
