%define destname rpm-uscan
%define debian_ver 2.14.4
Name: %destname
Version: 0.14.%debian_ver
Release: alt1

Summary: Utility to check watch files
Source: %name-%version.tar

License: %gpl2plus
Group: Development/Other

BuildArch: noarch

BuildRequires: rpm-build-licenses perl-devel perl-RPM perl(LWP/UserAgent.pm) perl(LWP/Protocol/https.pm)
# for spawn function.
BuildRequires: perl-Dpkg
Requires: perl(LWP/Protocol/https.pm)
Requires: gear-uupdate

%description
- uscan: Automatically scan for and download upstream updates.  Uscan can
  also call a program such as girar-nmu to attempt to update the src.rpm 
  or gear repository.  Whilst uscan could be used to release
  the updated version automatically, it is probably better not to without
  testing it first.

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -Dm755 scripts/uscan.pl %buildroot%_bindir/%destname
sed -i -e 's,###VERSION###,%version-rpm,' %buildroot%_bindir/%destname

install -Dm644 scripts/uscan.1 %buildroot%_man1dir/%destname.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.14.2.14.4-alt1
- bugfix release

* Fri Jun 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.13.2.14.4-alt1
- development release

* Thu Jun 12 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.2.14.4-alt1
- check-dirname-level 2 & 3

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.2.14.4-alt1
- usehttpheaderfilename option

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.2.14.4-alt1
- release

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.2.14.4-alt1
- multiple usability improvements

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.14.4-alt1
- sync with debian uscan 2.14.4
- sync with upstream watch
- updated man page to reflect rpm-uscan changes

* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.13.3-alt1
- sync with debian uscan 2.13.3
- sync with upstream watch

* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.2.11.6-alt1
- more patterns in any-archive

* Tue Apr 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.6-alt1
- sync with debian uscan 2.11.6

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.3-alt1
- sync with debian uscan 2.11.3
- added usehttpheaderfilename option (for cas@)

* Fri Nov 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.1-alt1
- new version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2.11.1-alt1
- new version

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2.11.1-alt1
- new version

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2.11.1-alt1
- new version

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2.11.1-alt1
- any-archive option

* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2.11.1-alt1
- debian uscan, patched to work with rpm and gear.
