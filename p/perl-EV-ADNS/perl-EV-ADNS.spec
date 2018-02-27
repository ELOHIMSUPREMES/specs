## SPEC file for Perl module EV::ADNS

%define real_name EV-ADNS

Name: perl-EV-ADNS
Version: 2.2
Release: alt1

Summary: Perl module for lightweight asynchronous DNS queries using EV and libadns

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/HTML-Tidy/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

Patch0: %real_name-2.2-alt-gcc_warnings_fix.patch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri Feb 21 2014
# optimized out: libcloog-isl4 perl-common-sense
BuildRequires: libadns-devel perl-EV

%description
Perl module EV::ADNS provides a simple interface to libadns
(asynchronous dns) that integrates well and automatically
into the EV event loop.

%prep
%setup -q -n %real_name-%version

%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%exclude /.perl.req
%perl_vendor_autolib/EV/ADNS*
%perl_vendor_archlib/EV/ADNS*


%changelog
* Fri Feb 21 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.2-alt1
- Initial build for ALT Linux Sisyphus
