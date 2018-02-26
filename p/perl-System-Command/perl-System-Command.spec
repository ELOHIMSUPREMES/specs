Name: perl-System-Command
Version: 1.07
Release: alt1

Summary: System::Command - Object for running system commands
License: Perl
Group: Development/Perl

Url: %CPAN System-Command
# Cloned from git://github.com/book/System-Command.git
Source: %name-%version.tar

BuildRequires: perl-devel perl-Module-Build
BuildArch: noarch

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/System/Command*
%doc Changes README 

%changelog
* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- 1.0.4 -> 1.0.7

* Fri Jun 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1
- New version 1.0.4

* Thu Jun 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1
- initial build
