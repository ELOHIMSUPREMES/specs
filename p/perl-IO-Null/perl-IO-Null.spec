# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-IO-Null
Version:        1.01
Release:        alt2_22
Summary:        Class for null filehandles
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/IO-Null/
Source0:        http://www.cpan.org/authors/id/S/SB/SBURKE/IO-Null-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(vars.pm)
Source44: import.info

%description
IO::Null is a class for null filehandles.  Calling a constructor of
this class always succeeds, returning a new null filehandle.  Writing
to any object of this class is always a no-operation, and returns
true.  Reading from any object of this class is always no-operation,
and returns empty-string or empty-list, as appropriate.

%prep
%setup -q -n IO-Null-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendor_privlib}/*

%changelog
* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_21
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_19
- update to new release by fcimport

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_18
- moved to Sysiphus as dependency

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_18
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_17
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_16
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_15
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_14
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_12
- fc import

