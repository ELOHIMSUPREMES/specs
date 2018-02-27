%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dump.pm) perl(File/ShareDir.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Module/Build.pm) perl(Path/Class/Dir.pm) perl(Path/Class/File.pm) perl(Path/FindDev.pm) perl(Path/IsDev.pm) perl(Sub/Exporter.pm) perl(Test/More.pm) perl(YAML/Dumper.pm) perl(YAML/Loader.pm)
# END SourceDeps(oneline)
%define module_version 1.000000
%define module_name File-ShareDir-ProjectDistDir
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.000000
Release: alt1
Summary: Simple set-and-forget using of a '/share' directory in your projects root
Group: Development/Perl
License: perl
URL: https://github.com/kentfredric/File-ShareDir-ProjectDistDir

Source: http://www.cpan.org/authors/id/K/KE/KENTNL/File-ShareDir-ProjectDistDir-%{version}.tar.gz
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
%doc Changes README LICENSE
%perl_vendor_privlib/F*

%changelog
* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1
- initial import by package builder

