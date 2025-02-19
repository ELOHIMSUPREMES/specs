%define _unpackaged_files_terminate_build 1
#
#   - Time-Duration-Parse -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Time::Duration::Parse
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Time-Duration-Parse
%define m_distro Time-Duration-Parse
%define m_name Time-Duration-Parse
%define m_author_id unknown
%define _enable_test 1

Name: perl-Time-Duration-Parse
Version: 0.15
Release: alt1

Summary: Parse string that represents time duration

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/N/NE/NEILB/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Thu Nov 19 2009
BuildRequires: perl-Exporter-Lite perl-Module-Install

%description
Time::Duration::Parse is a module to parse human readable duration
strings like 2 minutes and 3 seconds to seconds.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc Changes LICENSE README
%perl_vendor_privlib/Time/Duration/Parse.pm

%changelog
* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Mon Jul 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- initial build for ALT Linux Sisyphus

