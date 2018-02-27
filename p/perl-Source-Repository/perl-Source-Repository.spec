%define module Source-Repository

Name: perl-%module
Version: 0.27
Release: alt2
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl-RPM perl-DistroMap perl-String-ShellQuote perl-RPM-Source-Convert perl-Source-Package perl-RPM-Source-BundleImport
Requires: perl-RPM-Source-Editor > 0.829
Conflicts: perl-RPM-Source-Convert < 0.48

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
#doc README
%_bindir/*mass
%perl_vendor_privlib/Source*

%changelog
* Thu Nov 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2
- bugfix release

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- development release

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- development release

* Mon Nov 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- development release

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- new version

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- development release

* Thu May 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- bugfix release

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- development release

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- development release

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- development release

* Wed Apr 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- development release

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- development release

* Thu Apr 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- development release

* Sun Mar 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- development release

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- bugfix release

* Fri Sep 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- new version 

* Thu Sep 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- development release

* Fri Aug 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- development release

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- new API; development release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt4
- PLD support

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3
- development release

* Tue Jul 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- development release

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- development release

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt5
- misc fixes

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt4
- python3 copycat support

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3
- bugfix release

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- bugfix release

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- development release

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3
- bugfix release

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- bugfix release

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- development release

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- configurable matcher

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- bugfix relase

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- more strategies

* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt4
- added verbosity

* Tue Apr 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3
- bugfix release

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- support for rawhide nested folders

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- bugfix release

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3
- maintainance release

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- bugfix

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- new version

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3
- bugfix

* Wed Dec 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- bugfix

* Wed Dec 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfixes

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- more options

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
