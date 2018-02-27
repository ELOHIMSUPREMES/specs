# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-Geometry-Voronoi
Version:        1.3
Release:        alt3_10
Summary:        Compute Voronoi diagrams from sets of points
License:        (GPL+ or Artistic) and MIT
# Perl module is licensed as Perl, underlaying C code is MIT
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Math-Geometry-Voronoi/
Source0:        http://www.cpan.org/authors/id/S/SA/SAMTREGAR/Math-Geometry-Voronoi-%{version}.tar.gz
Source1:        Math-Geometry-Voronoi-license-mail1.txt
Source2:        Math-Geometry-Voronoi-license-mail2.txt
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(XSLoader.pm)
BuildRequires:  dos2unix

 # Filters (not)shared c libs
Source44: import.info

%description
This module computes Voronoi diagrams from a set of input points.

%prep
%setup -q -n Math-Geometry-Voronoi-%{version}
cp -p %{SOURCE1} license-mail1.txt
cp -p %{SOURCE2} license-mail2.txt
dos2unix *.c
chmod -x *.c *.h

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
# Get the license from the e-mail
tail -22 license-mail1.txt | head -20 | base64 -d | dos2unix > C-LICENSE

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*
rm -rf %{buildroot}%{perl_vendor_archlib}/Math/Geometry/leak-test.pl

%check
make test

%files
%doc Changes C-LICENSE README license-mail*
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Math*

%changelog
* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3_10
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.3-alt2_10
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_9
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_8
- initial fc import

