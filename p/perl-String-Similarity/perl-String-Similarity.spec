# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DynaLoader.pm) perl(Encode.pm) perl(Exporter.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-String-Similarity
Version:        1.04
Release:        alt3_9
Summary:        Calculates the similarity of two strings
License:        GPLv2+
Group:          Development/Perl
URL:            http://search.cpan.org/dist/String-Similarity/
Source0:        http://www.cpan.org/authors/id/M/ML/MLEHMANN/String-Similarity-%{version}.tar.gz
BuildRequires:  perl(ExtUtils/MakeMaker.pm)


Source44: import.info

%description
The similarity function calculates the similarity index of its two arguments. 
A value of 0 means that the strings are entirely different. A value of 1 
means that the strings are identical. Everything else lies between 0 and 1 
and describes the amount of similarity between the strings.

%prep
%setup -q -n String-Similarity-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/String*

%changelog
* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3_9
- update to new release by fcimport

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3_8
- build for Sisyphus

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_8
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.04-alt2_7
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_7
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_5
- fc import

