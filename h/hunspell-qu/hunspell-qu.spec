# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-qu
Summary: Quechua Ecuador hunspell dictionaries
Version: 0.9
Release: alt2_5
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/2121/8/qu_EC-0.9.oxt
URL: http://extensions.services.openoffice.org/project/KichwaSpellchecker
License: AGPLv3
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Quechua Ecuador hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p qu_EC.aff qu_EC.dic $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc CURRENTVERSION.txt LICENSE.txt README.txt REVISION.txt   
%{_datadir}/myspell/*

%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_1
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1
- import from Fedora by fcimport

