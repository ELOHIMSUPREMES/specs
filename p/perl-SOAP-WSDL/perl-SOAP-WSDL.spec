%define module SOAP-WSDL

Name: perl-%module
Version: 2.00.10
Release: alt3

Packager: Victor Forsyuk <force@altlinux.org>

Summary: SOAP-WSDL provides a SOAP client with WSDL support
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/SOAP/%module-%version.tar.gz
Patch1: SOAP-WSDL-2.00.05-fixmodulepath.patch

# Patches from debian
# https://rt.cpan.org/Public/Bug/Display.html?id=74257
Patch2: SOAP-WSDL-2.00.10-debian-load_with_class_load.patch
Patch3: SOAP-WSDL-2.00.10-debian-lvalue_modification_5.18.patch
Patch4: SOAP-WSDL-2.00.10-debian-prefix_from_namespace.patch
Patch5: SOAP-WSDL-2.00.10-debian-use_test_xml.patch


BuildArch: noarch

# Automatically added by buildreq on Fri Aug 01 2008 (-bi)
BuildRequires: apache2-mod_perl libnss-mdns perl-Class-Std-Fast perl-IO-stringy perl-Log-Agent perl-Module-Build perl-SOAP-Lite perl-Template perl-Term-ReadKey perl-Test-Pod perl-TimeDate perl-Class-Load

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
SOAP-WSDL provides a SOAP client with WSDL support.

%prep
%setup -n %module-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%_man1dir/*
%perl_vendor_privlib/SOAP/*

%changelog
* Tue Feb 11 2014 Vladimir Lettiev <crux@altlinux.ru> 2.00.10-alt3
- fixed build with perl-5.18 (patches from Debian)

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 2.00.10-alt2
- fixed build with perl-5.16

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 2.00.10-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 2.00.10-alt1
- 2.00.10

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 2.00.06-alt1
- 2.00.06

* Tue Aug 05 2008 Victor Forsyuk <force@altlinux.org> 2.00.05-alt1
- Initial build.
