BuildRequires: libgmp-devel
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(Math/GMP.pm) perl(overload.pm) perl(subs.pm)
# END SourceDeps(oneline)
#BuildRequires: perl(Math/GMPq.pm) perl(Math/GMPz.pm) perl(Math/MPFR.pm)
%define module_version 0.39
%define module_name Math-GMPf
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.39
Release: alt1.1
Summary: perl interface to the GMP library's floating point (mpf) functions..
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/S/SI/SISYPHUS/Math-GMPf-%{version}.tar.gz

%description
A bigfloat module utilising the Gnu MP (GMP) library..
   Basically this module simply wraps all of the 'mpf'
   floating point functions provided by that library.
   The documentation below extensively plagiarises the
   GMP documentation at http://gmplib.org .
   See the Math::GMPf test suite for some examples
   of usage.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1.1
- rebuild with new perl 5.20.1

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.36-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- initial import by package builder

