# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Cwd.pm) perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(MIME/Base64.pm) perl(XSLoader.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Crypt-Eksblowfish
Version:        0.009
Release:        alt4_9
Summary:        Eksblowfish block cipher
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Crypt-Eksblowfish/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Crypt-Eksblowfish-%{version}.tar.gz
BuildRequires:  perl(Class/Mix.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)


Source44: import.info

%description
An object of this type encapsulates a keyed instance of the Eksblowfish
block cipher, ready to encrypt and decrypt.

%prep
%setup -q -n Crypt-Eksblowfish-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Crypt*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_9
- update to new release by fcimport

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_8
- moved to Sisyphus as dependency

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.009-alt3_8
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_7
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_6
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.009-alt2_5
- rebuild with new perl

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_5
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_3
- fc import

