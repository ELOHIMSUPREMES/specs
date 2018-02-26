%define module_name Module-ExtractUse

Name: perl-%module_name
Version: 0.28
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Find out what Perl modules are used
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/authors/id/D/DO/DOMM/Module-ExtractUse-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 16 2009
BuildRequires: perl-Module-Build perl-Parse-RecDescent perl-Pod-Strip perl-Test-Deep perl-Test-NoWarnings perl-Test-Pod perl-Test-Pod-Coverage perl-UNIVERSAL-require

%description
Module::ExtractUse is basically a Parse::RecDescent grammar to parse Perl code.
It tries very hard to find all modules (whether pragmas, Core, or from CPAN)
used by the parsed code.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/

%changelog
* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 0.23-alt1
- Initial build.
