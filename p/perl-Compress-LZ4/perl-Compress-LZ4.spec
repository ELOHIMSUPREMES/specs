## SPEC file for Perl module Compress::LZ4

%define real_name Compress-LZ4

Name: perl-Compress-LZ4
Version: 0.22
Release: alt1.1

Summary: Perl interface to the LZ4 (de)compressor

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Compress-LZ4/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

%description
Perl module Compress::LZ4 provides a Perl interface
to the LZ4 (de)compressor.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Compress/LZ4*
%perl_vendor_autolib/Compress/LZ4*

%changelog
* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1
- rebuild with new perl 5.22.0

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.22-alt1
- Initial build for ALT Linux Sisyphus
