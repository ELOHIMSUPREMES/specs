# BEGIN SourceDeps(oneline):
BuildRequires: perl(Pod/Usage.pm) perl(Source/Repository/Matcher/CPAN2ALT.pm) perl(Pod/Text.pm)
# END SourceDeps(oneline)
%define orepo cpan
%define obranch default
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.13
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

BuildRequires: rpm-build-perl

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/%orepo/%obranch/altlinux/sisyphus
#for type in group-strict group-approx;  do
#	install -m755 -d $destdir/$type
#	install -m644 $type/* $destdir/$type/
#done

#for type in binary source ; do
for type in source ; do
	for flag in flags/$type/* ; do
		install -m755 -d $destdir/$flag
		install -m644 $flag/* $destdir/$flag/
	done
done

mkdir -p %buildroot%_bindir
install -m 755 bin/* %buildroot%_bindir/

%files
%_bindir/*
%_datadir/distromap/*

%changelog
* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- db update

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added distromap-filter-translate-altlinux2cpan

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- db update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- db update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- db update

* Tue Jun 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- db update

* Wed Jun 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added cpan distrodb utils

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- db update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- db update

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- db update

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- db update

* Fri Apr 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- db update

* Thu Apr 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- db update
