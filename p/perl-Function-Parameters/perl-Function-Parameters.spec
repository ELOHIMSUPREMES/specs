%define module_version 1.0603
%define module_name Function-Parameters
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Dir/Self.pm) perl(ExtUtils/MakeMaker.pm) perl(Moo.pm) perl(Moose.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types.pm) perl(MooseX/Types/Moose.pm) perl(Test/Deep.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(aliased.pm) perl(attributes.pm) perl(constant.pm) perl(overload.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0603
Release: alt1.1
Summary: subroutine definitions with parameter lists
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MA/MAUKE/Function-Parameters-%{version}.tar.gz

%description
This module extends Perl with keywords that let you define functions with
parameter lists. It uses Perl's keyword plugin
API, so it works reliably and doesn't require a source filter.


%prep
%setup -n %module_name-%module_version
sed -i -e "s,^'ok'$,1;," lib/Function/Parameters.pm lib/Function/Parameters/*.pm

# TODO
rm t/unicode*.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/F*
%perl_vendor_autolib/*

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0603-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0603-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0602-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.0503-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0402-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.0401-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.0401-alt1
- regenerated from template by package builder

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.0301-alt1
- initial import by package builder

