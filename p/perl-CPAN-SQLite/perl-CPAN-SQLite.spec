# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    CPAN-SQLite
%define upstream_version 0.211

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Maintain and search a minimal CPAN database
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(CPAN/DistnameInfo.pm)
BuildRequires: perl(CPAN/HandleConfig.pm)
BuildRequires: perl(CPAN/Index.pm)
BuildRequires: perl(CPAN/Version.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Compress/Zlib.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Copy.pm)
BuildRequires: perl(File/HomeDir.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(FindBin.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IO/Zlib.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(LWP/Simple.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Test/CheckDeps.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/UseAllModules.pm)
BuildRequires: perl(base.pm)
BuildRequires: perl(lib.pm)
BuildRequires: perl(parent.pm)
BuildArch:  noarch
Source44: import.info

%description
This package is used for setting up, maintaining, and searching a CPAN
database consisting of the information stored in the three main CPAN
indices: _$CPAN/modules/03modlist.data.gz_,
_$CPAN/modules/02packages.details.txt.gz_, and
_$CPAN/authors/01mailrc.txt.gz_. It should be considered at an alpha stage
of development.

One begins by creating the object as

  my $obj = CPAN::SQLite->new(%%args);

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%{make}

%check
[ %version != 0.211 ] && make test

%install
%makeinstall_std

%files
%doc Changes INSTALL LICENSE META.json META.yml  README
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendor_privlib}/*

%changelog
* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.211-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.204-alt1_3
- update by mgaimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.203-alt1_2
- moved to Sisyphus

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.203-alt1_1
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.202-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.202-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.202-alt1_1
- converted for ALT Linux by srpmconvert tools

