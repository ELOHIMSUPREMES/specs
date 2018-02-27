# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/Liblist.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%filter_from_requires /^perl.XML.SAX.ExpatXS.Preload.pm./d
Name:           perl-XML-SAX-ExpatXS
Version:        1.33
Release:        alt3_8
Summary:        Perl SAX 2 XS extension to Expat parser
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/XML-SAX-ExpatXS/
Source0:        http://www.cpan.org/authors/id/P/PC/PCIMPRICH/XML-SAX-ExpatXS-%{version}.tar.gz
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(XML/SAX/Base.pm)
BuildRequires:  perl(XML/SAX.pm)
BuildRequires:  expat-devel
Requires:       perl(XML/SAX.pm) >= 0.96

 # Filters (not)shared c libs
Source44: import.info

%description
XML::SAX::ExpatXS is a direct XS extension to Expat XML parser. It
implements Perl SAX 2.1 interface. See http://perl-xml.sourceforge.net/perl-
sax/ for Perl SAX API description. Any deviations from the Perl SAX 2.1
specification are considered as bugs.

%prep
%setup -q -n XML-SAX-ExpatXS-%{version}
chmod -x ExpatXS.xs

%build
echo n | %{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%triggerin -- perl-XML-SAX
%{__perl} -MXML::SAX -e \
  'XML::SAX->add_parser(q(XML::SAX::ExpatXS))->save_parsers()' 2>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
 %{__perl} -MXML::SAX -e \
    'XML::SAX->remove_parser(q(XML::SAX::ExpatXS))->save_parsers()' \
    2>/dev/null || :
fi

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/XML*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_8
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed Sep 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt2_7
- rebuild

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_6
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_5
- initial fc import

