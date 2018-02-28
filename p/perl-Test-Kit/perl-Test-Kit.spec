%define _unpackaged_files_terminate_build 1
%define module_version 2.14
%define module_name Test-Kit
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Import/Into.pm) perl(Module/Runtime.pm) perl(Scalar/Util.pm) perl(Sub/Delete.pm) perl(Test/Aggregate.pm) perl(Test/Aggregate/Nested.pm) perl(Test/Builder.pm) perl(Test/CPAN/Changes.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/NoWarnings.pm) perl(Test/Output.pm) perl(Test/Pod.pm) perl(Test/Warn.pm) perl(parent.pm) perl(Hook/LexWrap.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.14
Release: alt1
Summary: Build custom test packages with only the features you want.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/K/KA/KAORU/Test-Kit-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/T*

%changelog
* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- automated CPAN update

* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.12-alt2
- moved to Sisyphus as dependency

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.101-alt1
- initial import by package builder

