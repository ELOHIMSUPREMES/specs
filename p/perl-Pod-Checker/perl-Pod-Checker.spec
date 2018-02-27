# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(FileHandle.pm) perl(Pod/Simple.pm) perl(Pod/Simple/Methody.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 1.71
%define module_name Pod-Checker
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.71
Release: alt1
Summary: Pod::Checker verifies POD documentation contents for compliance with the POD format specifications
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MA/MAREKR/Pod-Checker-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_privlib/P*
%_bindir/*
%_man1dir/*

%changelog
* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1
- automated CPAN update

* Sun Oct 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1
- Sisyphus build

