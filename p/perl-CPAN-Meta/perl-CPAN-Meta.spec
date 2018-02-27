%define dist CPAN-Meta
Name: perl-%dist
Version: 2.132140
Release: alt1

Summary: The distribution metadata for a CPAN dist
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-CPAN-Meta-Requirements perl-Parse-CPAN-Meta perl-Test-Script

%description
Software distributions released to the CPAN include a META.json or,
for older distributions, META.yml, which describes the distribution,
its contents, and the requirements for building and installing the
distribution.  The data structure stored in the META.json file is
described in CPAN::Meta::Spec.

CPAN::Meta provides a simple class to represent this distribution
metadata (or distmeta), along with some helpful methods for
interrogating that data.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CPAN

%changelog
* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.132140-alt1
- automated CPAN update

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.131560-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.120921-alt1
- 2.120351 -> 2.120921

* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.120351-alt1
- New version

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 2.112621-alt1
- initial revision
