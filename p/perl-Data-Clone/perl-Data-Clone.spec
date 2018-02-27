# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(CPAN.pm) perl(Clone.pm) perl(Config.pm) perl(Devel/Peek.pm) perl(Errno.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Parse/CPAN/Meta.pm) perl(Storable.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(if.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Data-Clone
Version:        0.004
Release:        alt1_3
Summary:        Polymorphic data cloning
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Data-Clone/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/Data-Clone-%{version}.tar.gz
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/PPPort.pm)
BuildRequires:  perl(ExtUtils/ParseXS.pm)
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/AuthorTests.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/LeakTrace.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Requires.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(Tie/Array.pm)
BuildRequires:  perl(Tie/Hash.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(XSLoader.pm)
Requires:       perl(Exporter.pm)


Source44: import.info

%description
Data::Clone does data cloning, i.e. copies things recursively. This is
smart so that it works with not only non-blessed references, but also
with blessed references (i.e. objects). When clone() finds an object, it
calls a clone method of the object if the object has a clone, otherwise
it makes a surface copy of the object. That is, this module does
polymorphic data cloning.

%prep
%setup -q -n Data-Clone-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Data*

%changelog
* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_2
- update to new release by fcimport

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.003-alt2_7
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_6
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_5
- update to new release by fcimport

* Thu Dec 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_4
- initial release

