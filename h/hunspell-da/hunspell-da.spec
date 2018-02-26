Name: hunspell-da
Summary: Danish hunspell dictionaries
Version: 1.7.41
Release: alt1_2
Source: http://da.speling.org/filer/myspell-da-%{version}.tar.bz2
Group: Text tools
URL: http://da.speling.org/
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Danish hunspell dictionaries.

%prep
%setup -q -n myspell-da-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README Copyright contributors COPYING
%{_datadir}/myspell/*

%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.41-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.41-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.40-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.37-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.37-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.37-alt1_1
- import from Fedora by fcimport

