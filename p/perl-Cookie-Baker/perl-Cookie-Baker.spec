%define module_version 0.05
%define module_name Cookie-Baker
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cookie/Baker/XS.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(Test/Time.pm) perl(URI/Escape.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: Cookie string generator / parser
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Cookie-Baker

Source0: http://cpan.org.ua/authors/id/K/KA/KAZEBURO/%{module_name}-%{module_version}.tar.gz
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
%doc Changes README.md LICENSE
%perl_vendor_privlib/C*

%changelog
* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- moved to Sisyphus as dependency

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

