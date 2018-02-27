# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(YAML/Syck.pm) perl(parent.pm)
%define upstream_name    Tapper-TAP-Harness
%define upstream_version 4.1.1

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_3

Summary:    Tapper - Tapper specific TAP handling
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Directory/Scratch.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(IO/String.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(TAP/DOM.pm)
BuildRequires: perl(TAP/Parser.pm)
BuildRequires: perl(TAP/Parser/Aggregator.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Tiny.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
This package provides a Tapper-specific TAP handling.

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
%doc META.json META.yml Changes LICENSE README
%perl_vendor_privlib/*




%changelog
* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

