%define _unpackaged_files_terminate_build 1
%define module_version 3.0204
%define module_name Cpanel-JSON-XS
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Carp.pm) perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Pod/Text.pm) perl(Pod/Usage.pm) perl(Test.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(common/sense.pm) perl(overload.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3.0204
Release: alt1
Summary: JSON::XS for Cpanel, fast and correct serialising, also for 5.6.2
Group: Development/Perl
License: perl
URL: http://software.schmorp.de/pkg/JSON-XS.html

Source: http://www.cpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-%{version}.tar.gz

%description
This module converts Perl data structures to JSON and vice versa. Its.primary goal is to be *correct* and its secondary goal is to be
*fast*. To reach the latter goal it was written in C.

As this is the n-th-something JSON module on CPAN, what was the reason
to write yet another JSON module? While it seems there are many JSON
modules, none of them correctly handle all corner cases, and in most cases
their maintainers are unresponsive, gone missing, or not listening to bug
reports for other reasons.

See below for the Cpanel fork.

See MAPPING, below, on how Cpanel::JSON::XS maps perl values to JSON
values and vice versa.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes COPYING README
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 3.0204-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.0115-alt1.1
- rebuild with new perl 5.22.0

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 3.0115-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 3.0114-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.0113-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.0106-alt1.1
- rebuild with new perl 5.20.1

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 3.0106-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 3.0104-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 3.0103-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.3404-alt1
- automated CPAN update

* Sat Nov 16 2013 Igor Vlasenko <viy@altlinux.ru> 2.3403-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.3401-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.3401-alt1
- initial import by package builder

