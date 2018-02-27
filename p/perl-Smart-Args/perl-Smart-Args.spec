%define module_version 0.12
%define module_name Smart-Args
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types/Moose.pm) perl(Mouse.pm) perl(Mouse/Util/TypeConstraints.pm) perl(MouseX/Types.pm) perl(MouseX/Types/Mouse.pm) perl(PadWalker.pm) perl(Params/Validate.pm) perl(Scalar/Util.pm) perl(Test/Builder/Module.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(base.pm) perl(if.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.12
Release: alt2
Summary: argument validation for you
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/Smart-Args

Source0: http://cpan.org.ua/authors/id/T/TO/TOKUHIROM/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Smart::Args is yet another argument validation library.

This module makes your module more readable, and writable =)


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_privlib/S*

%changelog
* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- initial import by package builder

