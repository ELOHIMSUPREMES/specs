%define _unpackaged_files_terminate_build 1
%define dist DateTime-Locale
Name: perl-%dist
Version: 1.02
Release: alt1

Summary: Localization support for DateTime.pm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz

BuildArch: noarch

# avoid rpmdb bloat
%add_findreq_skiplist */DateTime/Locale/[a-qs-z]*.pm
%add_findprov_skiplist */DateTime/Locale/[a-qs-z]*.pm

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-List-MoreUtils perl-Module-Build perl-Params-Validate perl-Test-Output perl(Dist/CheckConflicts.pm) perl(Test/Fatal.pm) perl(Test/Requires.pm) perl(Test/Warnings.pm)

%description
DateTime::Locale is primarily a factory for the various locale
subclasses.  It also provides some functions for getting information
on available locales.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/DateTime

%changelog
* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3
- restored Provides: perl(DateTime/Locale/root.pm) for MouseX-Types-DateTime

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt2
- rebuilt as plain src.rpm

* Tue Mar 30 2010 Alexey Tourbin <at@altlinux.ru> 0.45-alt1
- 0.44 -> 0.45

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.43 -> 0.44

* Thu Jul 02 2009 Alexey Tourbin <at@altlinux.ru> 0.43-alt1
- 0.42 -> 0.43

* Wed Nov 05 2008 Alexey Tourbin <at@altlinux.ru> 0.42-alt1
- 0.41 -> 0.42

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 0.41-alt1
- 0.4001 -> 0.41

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- 0.35 -> 0.4001

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- 0.34 -> 0.35

* Sun Apr 08 2007 Alexey Tourbin <at@altlinux.ru> 0.34-alt1
- 0.22 -> 0.34

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- initial revision
