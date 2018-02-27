%define module	JSON-RPC-Common

Name: perl-JSON-RPC-Common
Version: 0.10
Release: alt2

Summary: Transport agnostic JSON RPC helper objects

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/JSON-RPC-Common

Source0: %module-%version.tar
Patch0: %name-0.10-test.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Tue Oct 08 2013
# optimized out: perl-B-Hooks-EndOfScope perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Encode perl-Eval-Closure perl-IPC-Run3 perl-JSON-XS perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Probe-Perl perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Sub-Uplevel perl-Try-Tiny perl-URI perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean
BuildRequires: perl-HTTP-Message perl-JSON perl-MooseX-Types perl-Test-Exception perl-Test-Script perl-Variable-Magic

%description
Perl module provides abstractions for JSON-RPC 1.0, 1.1 (both
variations) and 2.0 (formerly 1.2) Procedure Call and Procedure
Return objects (formerly known as request and result), along
with error objects. It also provides marshalling objects to
convert the model objects into JSON text and HTTP
requests/responses.

This module does not concern itself with the transport layer
at all, so the JSON-RPC 1.1 and the alternative specification,
which are very different on that level are implemented with
the same class.

%prep
%setup -q -n %module-%version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc MANIFEST Changes
%perl_vendor_privlib/JSON*


%changelog
* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt2
- Fix build with Perl 5.18

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.08-alt1
- Initial build for ALT Linux
