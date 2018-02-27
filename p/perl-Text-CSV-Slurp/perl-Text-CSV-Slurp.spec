# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Text-CSV-Slurp
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_4

Summary:    Convert CSV into an array of hashes, or an array of hashes into CSV
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(Test/Most.pm)
BuildRequires: perl(Text/CSV.pm)
BuildArch:  noarch
Source44: import.info

%description
Convert CSV into an array of hashes, or an array of hashes into CSV.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml  README
%perl_vendor_privlib/*

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_3
- update by mgaimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_2
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- mageia import by cas@ requiest

