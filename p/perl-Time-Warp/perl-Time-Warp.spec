# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DynaLoader.pm) perl(Exporter.pm) perl(Test.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-Time-Warp 
Version:    0.51
Release:    alt1.1
# Warp.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Group:      Development/Perl
Summary:    Change the start and speed of Event time 
Source:     http://www.cpan.org/authors/id/S/SZ/SZABGAB/Time-Warp-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Time-Warp

BuildRequires: perl(ExtUtils/MakeMaker.pm)

# don't "provide" private Perl libs
#global _use_internal_dependency_generator 0
#global __deploop() while read FILE; do /usr/lib/rpm/rpmdeps -%{1} ${FILE}; done | /bin/sort -u
#global __find_provides /bin/sh -c "%{__grep} -v '%_docdir' | %{__grep} -v '%{perl_vendor_archlib}/.*\\.so$' | %{__deploop P}"
#global __find_requires /bin/sh -c "%{__grep} -v '%_docdir' | %{__deploop R}"
Source44: import.info

%description
Our external experience unfolds in 3 1/2 dimensions (time has a
dimensionality of 1/2). The Time::Warp module offers developers control
over the measurement of time.

This module is redundant if you're from Gallifrey, and not recommended
for use at high speeds near very massive objects.

%prep
%setup -q -n Time-Warp-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README 
%{perl_vendor_archlib}/*
%exclude %dir %{perl_vendor_archlib}/auto

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt5_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt5_15
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt5_14
- update to new release by fcimport

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 0.5-alt5
- built for perl 5.18

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_14
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_12
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_11
- moved to Sisyphus (Tapper dep)

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.5-alt3_11
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_11
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_9
- fixed provides

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_9
- fc import

