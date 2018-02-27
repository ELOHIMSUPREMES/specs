Name: perl-strictures
Version: 1.004004
Release: alt1

Summary: strictures - turn on strict and make all warnings fatal
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/p5sagit/strictures.git
Url: %CPAN strictures
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel
BuildArch: noarch

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/strictures*
%doc Changes

%changelog
* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.004004-alt1
- 1.004002 -> 1.004004

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.004002-alt1
- 1.002002 -> 1.004002

* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.002002-alt1
- initial build
