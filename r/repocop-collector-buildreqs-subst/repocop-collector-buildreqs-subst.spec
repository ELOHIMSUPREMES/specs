%define collectorname buildreqs-subst

Name: repocop-collector-%collectorname
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %collectorname collector for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop >= 0.60 perl-DBI perl-DBD-SQLite
BuildRequires: perl-DBI

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/
install -m 755 %collectorname.test $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/test
install -m 644 %collectorname.sql $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/init.sql.2
#install -m 644 %collectorname.purge.sql $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/purge.sql
install -m 644 %collectorname.filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/filepattern

%files
#doc README ChangeLog
%_datadir/repocop/pkgcollectors/%collectorname

%changelog
* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
