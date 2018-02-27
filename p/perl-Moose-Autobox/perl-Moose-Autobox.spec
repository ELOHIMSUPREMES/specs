## SPEC file for Perl module Moose::Autobox

%define real_name Moose-Autobox

Name: perl-Moose-Autobox
Version: 0.15
Release: alt1

Summary: Autoboxed wrappers for Native Perl datatypes

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Moose-Autobox/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Oct 06 2013
# optimized out: perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Scope-Guard perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Sub-Uplevel perl-Try-Tiny perl-devel perl-parent
BuildRequires: perl-Moose perl-Pod-Escapes perl-Syntax-Keyword-Junction perl-Test-Exception perl-autobox

%description
Perl module Moose::Autobox provides an implementation of SCALAR,
ARRAY, HASH & CODE for use with autobox. It does this using a
hierarchy of roles in a manner similar to what Perl 6 might do.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Moose/Autobox*

%changelog
* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.13-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- Initial build for ALT Linux Sisyphus
