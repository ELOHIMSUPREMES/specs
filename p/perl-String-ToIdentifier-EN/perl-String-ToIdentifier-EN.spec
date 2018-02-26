%define dist String-ToIdentifier-EN
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: Convert Strings to English Program Identifiers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Lingua-EN-Inflect-Phrase perl-Pod-Escapes perl-Text-Unidecode perl-devel perl-namespace-clean perl-unicore

%description
This module provides a utility method, "to_identifier" for converting an
arbitrary string into a readable representation using the ASCII subset
of "\w" for use as an identifier in a computer program. The intent is to
make unique identifier names from which the content of the original
string can be easily inferred by a human just by reading the identifier.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/String

%changelog
* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- 0.05 -> 0.08

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
