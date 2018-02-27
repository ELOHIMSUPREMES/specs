# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Safe-Isa
Version:        1.000005
Release:        alt1_1
Summary:        Call isa, can, does and DOES safely on things that may not be objects
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Safe-Isa/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Safe-Isa-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
Source44: import.info
# Runtime

%description
How many times have you found yourself writing:

  if ($obj->isa('Something')) {

and then shortly afterwards cursing and changing it to:

  if (Scalar::Util::blessed($obj) and $obj->isa('Something')) {

Right. That's why this module exists.

%prep
%setup -q -n Safe-Isa-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Safe/

%changelog
* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.000005-alt1_1
- update to new release by fcimport

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.000005-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.000004-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1_2
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1_2
- update to new release by fcimport

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1_1
- new version

