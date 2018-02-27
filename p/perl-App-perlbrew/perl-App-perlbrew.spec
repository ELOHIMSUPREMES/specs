Name: perl-App-perlbrew
Version: 0.66
Release: alt1

Summary: Manage perl installations in your $HOME
Group: Development/Perl
License: mit

Url: %CPAN App-perlbrew
Source: %name-%version.tar

Requires: perl-Devel-PatchPerl

BuildArch: noarch
BuildRequires: curl perl-CPAN-Perl-Releases perl-IO-All perl-Capture-Tiny perl-Test-Exception perl-devel perl-Devel-PatchPerl perl-Test-Spec perl-File-Path-Tiny perl-Path-Class perl-Test-Output perl-local-lib perl-Module-Install perl-Module-Install-Repository perl-Test-NoWarnings

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/perlbrew
%perl_vendor_privlib/App/perlbrew*
%doc Changes LICENSE README

%changelog
* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt1
- 0.52 -> 0.66

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt1
- initial build for ALTLinux

