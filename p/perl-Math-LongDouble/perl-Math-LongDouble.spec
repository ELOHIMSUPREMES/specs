%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 0.06
%define module_name Math-LongDouble
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt1.1
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/S/SI/SISYPHUS/Math-LongDouble-%{version}.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

