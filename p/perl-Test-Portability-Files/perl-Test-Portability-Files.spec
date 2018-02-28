# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
# We need to patch the test suite if we have an old version of Test::More
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION < 0.88) ? 1 : 0);' 2>/dev/null || echo 0)

Name:           perl-Test-Portability-Files
Version:        0.06
Release:        alt1_6
Summary:        Check file names portability
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Portability-Files/
Source0:        http://www.cpan.org/authors/id/A/AB/ABRAXXA/Test-Portability-Files-%{version}.tar.gz
Patch1:         Test-Portability-Files-0.06-old-Test::More.patch
BuildArch:      noarch
# Build
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This module is used to check the portability across operating systems of
the names of the files present in the distribution of a module. The tests
use the advice given in "Files and Filesystems" in perlport. The author of
a distribution can select which tests to execute.

%prep
%setup -q -n Test-Portability-Files-%{version}

# We need to patch the test suite if we have an old version of Test::More
%if %{old_test_more}
%patch1
%endif

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/Test/

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- update to new release by fcimport

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_20
- Sisyphus build; switch to fc import

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_20
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_19
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_18
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_17
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_16
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_14
- fc import

