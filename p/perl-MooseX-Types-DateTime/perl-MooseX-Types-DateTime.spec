%define dist MooseX-Types-DateTime
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: DateTime related constraints and coercions for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/I/IL/ILMARI/MooseX-Types-DateTime-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-DateTime perl-Locale-Maketext perl-MooseX-Types perl-Test-Exception perl-Test-use-ok

%description
This module packages several Moose::Util::TypeConstraints with coercions,
designed to work with the DateTime suite of objects.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/MooseX

%changelog
* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- 0.05 -> 0.07

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
