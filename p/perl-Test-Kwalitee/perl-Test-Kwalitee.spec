# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(if.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-Kwalitee
Version:	1.17
Release:	alt1_1
Summary:	Test the Kwalitee of a distribution before you release it
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://metacpan.org/module/Test::Kwalitee
Source0:	http://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Kwalitee-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	perl(Module/Build/Tiny.pm)
# Module
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(Dist/CheckConflicts.pm)
BuildRequires:	perl(Module/CPANTS/Analyse.pm)
BuildRequires:	perl(namespace/clean.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(CPAN/Meta.pm)
BuildRequires:	perl(CPAN/Meta/Requirements.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(lib.pm)
BuildRequires:	perl(List/Util.pm)
BuildRequires:	perl(Test/Deep.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Tester.pm)
BuildRequires:	perl(Test/Warnings.pm)
# Runtime
Requires:	perl(Dist/CheckConflicts.pm) >= 0.02
Source44: import.info

%description
Kwalitee is an automatically-measurable gauge of how good your software
is. That's very different from quality, which a computer really can't
measure in a general sense (if you can, you've solved a hard problem in
computer science).

%prep
%setup -q -n Test-Kwalitee-%{version}
sed -i -e 's,use Module::Build::Tiny 0.030,use Module::Build::Tiny,' Build.PL

%build
perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
chmod -c 755 %{buildroot}%{_bindir}/kwalitee-metrics

%check
./Build test

%files
%doc Changes CONTRIBUTING LICENSE README
%{_bindir}/kwalitee-metrics
%{perl_vendor_privlib}/Test/
%{_mandir}/man1/kwalitee-metrics.1*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_1
- Sisyphus build

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_1
- update to new release by fcimport

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1
- update to new release by fcimport

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_1
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_15
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_14
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_12
- fc import

