# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Perl-Destruct-Level
Summary:	Allows you to change perl's internal destruction level
Version:	0.02
Release:	alt4_9
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Perl-Destruct-Level/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RG/RGARCIA/Perl-Destruct-Level-%{version}.tar.gz
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(XSLoader.pm)

# Don't "provide" private Perl libs

Source44: import.info

%description
This module allows you to change perl's internal destruction level. The
default value of the destruct level is 0; it means that perl won't bother
destroying all of its internal data structures and lets the OS do the cleanup
for it at exit.

For perls built with debugging support (-DDEBUGGING), an environment variable
PERL_DESTRUCT_LEVEL allows you to control the destruction level. This module
enables you to modify it on non-debugging perls too.

Note that some embedded environments might extend the meaning of the
destruction level for their own purposes: mod_perl does that, for example.

%prep
%setup -q -n Perl-Destruct-Level-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test

%files
%{perl_vendor_archlib}/auto/Perl/
%{perl_vendor_archlib}/Perl/

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt4_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt4_8
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt4_7
- Sisyphus build

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.02-alt3_7
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_6
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_5
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.02-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- fc import

