# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
BuildRequires: gcc-c++
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-ExtUtils-CppGuess
Version:        0.11
Release:        alt1_4
Summary:        Guess C++ compiler and flags
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/ExtUtils-CppGuess/
Source0:        http://www.cpan.org/authors/id/D/DA/DAVIDO/ExtUtils-CppGuess-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(Fatal.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

%prep
%setup -q -n ExtUtils-CppGuess-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/ExtUtils*

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_1
- update to new release by fcimport

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

