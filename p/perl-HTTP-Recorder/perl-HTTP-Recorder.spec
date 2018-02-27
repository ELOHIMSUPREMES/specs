%define dist HTTP-Recorder
Name: perl-%dist
Version: 0.07
Release: alt1

Summary: record interaction with websites
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SE/SEMUELF/HTTP-Recorder-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 22 2011
BuildRequires: perl-HTTP-Request-Params perl-Test-Pod perl-libwww

%description
This is a browser-independent recorder for recording interactions with
web sites.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/HTTP*

%changelog
* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2
- updated build dependencies

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
