%define module_version 0.000060
%define module_name Test2-Suite
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(Importer.pm) perl(List/Util.pm) perl(Scalar/Util.pm) perl(Test2.pm) perl(Unicode/GCString.pm) perl(overload.pm) perl(utf8.pm)
# END SourceDeps(oneline)
%define _without_test 1
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.000060
Release: alt1
Summary: Distribution with a rich set of tools built upon the Test2 framework.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/E/EX/EXODIST/Test2-Suite-%{version}.tar.gz
BuildArch: noarch

%description
Rich set of tools, plugins, bundles, etc built upon the the Test2 manpage testing
library. If you are interested in writing tests, this is the distribution for
you.
%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md README TODO Changes
%perl_vendor_privlib/T*

%changelog
* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.000060-alt1
- automated CPAN update

* Mon Sep 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.000058-alt2
- to Sisyphus

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.000058-alt1
- regenerated from template by package builder

* Sun Aug 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.000055-alt1
- regenerated from template by package builder

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.000054-alt1
- initial import by package builder

