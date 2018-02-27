# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(FindBin.pm) perl(Math/BigInt.pm) perl(Math/BigRat.pm) perl(Math/Complex.pm) perl(Math/Symbolic.pm) perl(Math/Symbolic/Derivative.pm) perl(Test.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 1.006
%define module_name Math-Polynomial
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.006
Release: alt1
Summary: Perl class for polynomials in one variable
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MH/MHASCH/Math-Polynomial-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/M*

%changelog
* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.006-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.005-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1
- initial import by package builder

