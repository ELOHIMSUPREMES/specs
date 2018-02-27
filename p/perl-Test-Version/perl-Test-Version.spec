# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

Name:		perl-Test-Version
Version:	2.01
Release:	alt1
Summary:	Check to see that versions in modules are sane
License:	Artistic 2.0
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Test-Version/
Source:	http://www.cpan.org/authors/id/P/PL/PLICEASE/Test-Version-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(File/Find/Rule/Perl.pm)
BuildRequires:	perl(Module/Metadata.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(version.pm)
BuildRequires:	perl(warnings.pm)
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(CPAN/Meta.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(IO/Handle.pm)
BuildRequires:	perl(IPC/Open3.pm)
BuildRequires:	perl(Test/Exception.pm)
BuildRequires:	perl(Test/Tester.pm)
# ===================================================================
# Author/Release test requirements
#
# Don't run these tests or include their requirements if we're
# bootstrapping, as many of these modules require each other for
# their author/release tests.
# ===================================================================
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(English.pm)
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Test/CPAN/Changes.pm)
BuildRequires:	perl(Test/CPAN/Meta/JSON.pm)
BuildRequires:	perl(Test/DistManifest.pm)
BuildRequires:	perl(Test/EOL.pm)
BuildRequires:	perl(Test/MinimumVersion.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Perl/Critic.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(Test/Portability/Files.pm)
BuildRequires:	perl(Test/Vars.pm)
%endif
Source44: import.info
# ===================================================================
# Runtime requirements
# ===================================================================

%description
This module's goal is to be a one stop shop for checking to see that your
versions across your dist are sane.

%prep
%setup -q -n Test-Version-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test
%if 0%{!?perl_bootstrap:1}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%doc LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendor_privlib}/Test/

%changelog
* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.004001-alt1_1
- update to new release by fcimport

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.004001-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.002004-alt1_4
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.002004-alt1_3
- update to new release by fcimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.002004-alt1_1
- update to new release by fcimport

* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.002004-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.002003-alt2_1
- Sisyphus build

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.002003-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_11
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_10
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_8
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_3
- fc import

