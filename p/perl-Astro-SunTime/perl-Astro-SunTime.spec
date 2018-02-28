%define _unpackaged_files_terminate_build 1
%define m_distro Astro-SunTime
Name: perl-%m_distro
Version: 0.05
Release: alt1
Summary: Astro::SunTime provides a function interface to calculate sun rise/set times.
Group: Development/Perl
License: Artistic/GPL
Url: http://search.cpan.org/dist/Astro-SunTime/
Source0: http://www.cpan.org/authors/id/R/RO/ROBF/Astro-SunTime-%{version}.tar.gz
Packager: Alex Negulescu <alecs@altlinux.org>
BuildRequires: perl-Time-modules perl-devel

%description
Astro::SunTime provides a function interface to calculate sun rise/set times.

%prep
%setup -q -n Astro-SunTime-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%clean
%__rm -rf %buildroot

%files
%_datadir/perl5/Astro/*
%dir %perl_vendor_autolib/Astro/SunTime
%doc Changes MANIFEST README

%changelog
* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.01-alt1.1
- redundant buildreq dropped

* Thu Jan 13 2011 Alex Negulescu <alecs@altlinux.org> 0.01-alt1
- initial build

