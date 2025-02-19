# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
%define fedora 28
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Test_Warnings_enables_optional_test
%else
%bcond_with perl_Test_Warnings_enables_optional_test
%endif

Name:		perl-Test-Warnings
Version:	0.026
Release:	alt1_8
Summary:	Test for warnings and the lack of them
License:	GPL+ or Artistic
Group:		Development/Other
URL:		https://metacpan.org/release/Test-Warnings
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Warnings-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl-devel
BuildRequires:	rpm-build-perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(if.pm)
BuildRequires:	perl(lib.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Tester.pm)
%if %{with perl_Test_Warnings_enables_optional_test}
# Optional Tests
BuildRequires:	perl(CPAN/Meta.pm)
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:	perl(CPAN/Meta/Check.pm)
%endif
BuildRequires:	perl(CPAN/Meta/Prereqs.pm)
BuildRequires:	perl(CPAN/Meta/Requirements.pm)
BuildRequires:	perl(PadWalker.pm)
%endif
# Runtime
Requires:	perl(Carp.pm)
Source44: import.info

%description
If you've ever tried to use Test::NoWarnings to confirm there are no warnings
generated by your tests, combined with the convenience of done_testing to not
have to declare a test count, you'll have discovered that these two features do
not play well together, as the test count will be calculated before the
warnings test is run, resulting in a TAP error (see examples/test_nowarnings.pl
in this distribution for a demonstration).

This module is intended to be used as a drop-in replacement for
Test::NoWarnings: it also adds an extra test, but runs this test before
done_testing calculates the test count, rather than after. It does this by
hooking into done_testing as well as via an END block. You can declare a plan,
or not, and things will still Just Work.

It is actually equivalent to:

    use Test::NoWarnings 1.04 ':early';

as warnings are still printed normally as they occur. You are safe, and
enthusiastically encouraged, to perform a global search-replace of the above
with use Test::Warnings; whether or not your tests have a plan.

%prep
%setup -q -n Test-Warnings-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc --no-dereference LICENCE
%doc Changes CONTRIBUTING README examples/
%{perl_vendor_privlib}/Test/

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1_8
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1_4
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1_2
- update to new release by fcimport

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- automated CPAN update

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1_1
- update to new release by fcimport

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1_1
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_1
- update to new release by fcimport

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_1
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Sat Oct 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt2_1
- bumped release to override the autoimports package

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_1
- update to new release by fcimport

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Wed Sep 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_1
- Sisyphus build

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_2
- update to new release by fcimport

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_1
- fc import

