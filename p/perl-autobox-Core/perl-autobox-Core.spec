## SPEC file for Perl module autobox::Core

%define real_name autobox-Core

Name: perl-autobox-Core
Version: 1.29
Release: alt1

Summary: Perl module with core functions to autoboxed scalars, arrays and hashes

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/autobox-Core/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-Scope-Guard
BuildRequires: perl-autobox perl-devel

%description
Perl module autobox promotes Perl's primitive types (literals
(strings and numbers), scalars, arrays and hashes) into
first-class objects. However, autobox does not provide any
methods for these new classes.

autobox::Core provides a set of methods for these new classes.
It includes almost everything in perlfunc, some things from
Scalar::Util and List::Util, and some Perl 5 versions of
methods taken from Perl 6.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/autobox/Core*

%changelog
* Wed Sep 23 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.29-alt1
- New version

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.28-alt1
- Initial build for ALT Linux Sisyphus
