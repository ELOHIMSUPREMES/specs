# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-mn
Summary: Mongolian hunspell dictionaries
%define upstreamid 20080709
Version: 0.%{upstreamid}
Release: alt2_10
Source: http://extensions.services.openoffice.org/files/1408/0/dict-mn_0.06-5.oxt
Group: Text tools
URL: http://mnspell.openmn.org
License: GPLv2 and LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Mongolian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mn

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mn_MN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_mn_MN.txt
%{_datadir}/myspell/*

%changelog
* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_7
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_5
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080709-alt1_3
- import from Fedora by fcimport

