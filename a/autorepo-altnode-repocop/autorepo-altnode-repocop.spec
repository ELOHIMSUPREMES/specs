%filter_from_requires /^repocop-unittest-build-logs/d

#BuildRequires: 
Name: autorepo-altnode-repocop
Version: 0.13
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop scripts for an automated packaging node
Group: Development/Other
License: GPL2+
#Url: 
Source: %name-%version.tar

BuildRequires: repocop
Requires: repocop > 0.65

%description
%summary

%prep
%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT%_bindir
install -m 755 repocop-* $RPM_BUILD_ROOT%_bindir

%files
%doc daily.conf.*
%doc crontab
%_bindir/*

%changelog
* Tue Jul 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- more daily.conf

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- html support

* Fri Jul 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- release

* Thu Jul 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt6
- bugfix release

* Wed Jul 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt5
- fixed dependencies

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt4
- more altnode tags

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3
- support for html report

* Mon Jul 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- added altnode support

* Mon Jul 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added extra statistics reports

* Fri May 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- support for archive task on autorepo nodes

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- new distrodb format

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- distrodb-extra support

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- enabled build logs again

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- dropped optional dependency on repocop-unittest-build-logs

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- prometheus2 support

* Fri Jul 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- export of watch files

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- repocop 0.59 distrotest support

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- repocop 0.58 support

* Fri Jul 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- support for repocop-report-prometeus2-sqlite

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
