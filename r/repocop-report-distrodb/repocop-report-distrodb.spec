Name: repocop-report-distrodb
Version: 0.41
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus format
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop > 0.73
Obsoletes: repocop-report-distromap-db < 0.12
Requires: repocop-collector-buildreqs-subst

BuildRequires: perl-devel perldoc
BuildRequires: repocop

Source: %name-%version.tar

%description
Repocop is a repository unit tests platform.
%summary

%prep
%setup
rm -f *.spec

%build

%install
mkdir -p %buildroot/%_bindir
install -m 755 repocop-report-* %buildroot/%_bindir/

%files
#doc README ChangeLog
%_bindir/repocop-report-distrodb
%_bindir/repocop-report-helper-distrodb-preprocess
#%_man1dir/repocop-report-*

%changelog
* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- texlive 2017 support

* Fri Feb 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- php fixes

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- fixed raw pythons

* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- restored sourceurl.raw

* Mon Dec 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- added requires.raw and added raw version 0

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- added sourceurl.raw

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- added exception for libgdiplus

* Wed Jul 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- python fixes

* Sat Jul 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- added base python

* Thu Jul 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- added raw php

* Wed Jul 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- added DependencyAnalyzer python

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- clean plugins
