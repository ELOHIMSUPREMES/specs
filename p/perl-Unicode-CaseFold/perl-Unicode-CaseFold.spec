%define module_version 1.00
%define module_name Unicode-CaseFold
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Benchmark.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Unicode/UCD.pm) perl(XSLoader.pm) perl(charnames.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.00
Release: alt2.1
Summary: Unicode case-folding for case-insensitive lookups.
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/Unicode-CaseFold

Source0: http://cpan.org.ua/authors/id/A/AR/ARODLAND/%{module_name}-%{module_version}.tar.gz

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes TODO
%perl_vendor_archlib/U*
%perl_vendor_autolib/*

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2.1
- rebuild with new perl 5.20.1

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- moved to Sysiphus as perl-Text-Ngram dependency

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

