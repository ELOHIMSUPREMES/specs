Name: perl-File-Path-Tiny
Version: 0.7
Release: alt1

Summary: recursive versions of mkdir() and rmdir() without as much overhead as File::Path
Group: Development/Perl
License: perl

Url: %CPAN File-Path-Tiny
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/File/Path/Tiny*
%doc Changes README

%changelog
* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1
- automated CPAN update

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.5-alt1
- initial build for ALTLinux

