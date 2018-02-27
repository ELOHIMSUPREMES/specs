%define _unpackaged_files_terminate_build 1
%define module_version 3.23
%define module_name Math-MPFR
# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel libmpfr-devel perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(Math/Decimal64.pm) perl(Math/GMP.pm) perl(Math/GMPf.pm) perl(Math/GMPq.pm) perl(Math/GMPz.pm) perl(Math/LongDouble.pm) perl(Math/Trig.pm) perl(overload.pm) perl(subs.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3.23
Release: alt1
Summary: perl interface to the MPFR (floating point) library..
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/S/SI/SISYPHUS/Math-MPFR-%{version}.tar.gz

%description
A bigfloat module utilising the MPFR library. Basically.
   this module simply wraps the 'mpfr' floating point functions
   provided by that library.
   Operator overloading is also available.
   The following documentation heavily plagiarises the mpfr
   documentation.
   See also the Math::MPFR test suite for some examples of usage.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.23-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 3.22-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.21-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.21-alt1
- regenerated from template by package builder

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 3.18-alt1
- initial import by package builder

