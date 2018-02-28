%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Errno.pm) perl(Fcntl.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(Scalar/Util.pm) perl(Sys/Hostname.pm) perl-devel perl-podlators perl(MooX/Types/MooseLike/Base.pm)
# END SourceDeps(oneline)
Name:           perl-Email-Sender
Version:        1.300021
Release:        alt1
Summary:        A library for sending email
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Email-Sender/
Source:        http://www.cpan.org/authors/id/R/RJ/RJBS/Email-Sender-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Email/Abstract.pm)
BuildRequires:  perl(Email/Address.pm)
BuildRequires:  perl(Email/Simple.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(JSON.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(Net/SMTP.pm)
BuildRequires:  perl(Net/SMTP/SSL.pm)
BuildRequires:  perl(Pod/Coverage/TrustPod.pm)
BuildRequires:  perl(Sub/Exporter.pm)
BuildRequires:  perl(Sub/Exporter/Util.pm)
BuildRequires:  perl(Sub/Override.pm)
BuildRequires:  perl(Test/MinimumVersion.pm)
BuildRequires:  perl(Test/MockObject.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Throwable/Error.pm)
BuildRequires:  perl(Try/Tiny.pm)
Requires:       perl(Email/Abstract.pm) >= 3
Requires:       perl(Net/SMTP/SSL.pm)
Requires:       perl(Throwable/Error.pm) >= 0.100.090

Patch: Email-Sender-1.300006-alt-fix.patch
Source44: import.info

%description
Email::Sender replaces the old and sometimes problematic Email::Send library,
which did a decent job at handling very simple email sending tasks, but was not
suitable for serious use, for a variety of reasons.

%prep
%setup -q -n Email-Sender-%{version}
#sed -i -e 's,^"220 OK";,1;,' lib/Email/Sender/Simple.pm
%patch -p1
# pod coverage test fails
#rm -f t/release-pod-coverage.t

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.300021-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.300020-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.300016-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.300014-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.300012-alt1
- automated CPAN update

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.300011-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.300010-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.300006-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt2_2
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt2_1
- moved to Sisyphus

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.120001-alt1_1
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.110005-alt1_1
- fc import

