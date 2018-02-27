# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: mythes-cs
Summary: Czech thesaurus
%define upstreamid 20070926
Version: 0.%{upstreamid}
Release: alt1_10
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/thes_cs_CZ_v2.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
BuildRequires: perl
License: MIT
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Czech thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_cs_CZ_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc th_cs_CZ_license.txt
%{_datadir}/mythes/*

%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20070926-alt1_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20070926-alt1_9
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20070926-alt1_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20070926-alt1_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20070926-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20070926-alt1_5
- import by fcmass

