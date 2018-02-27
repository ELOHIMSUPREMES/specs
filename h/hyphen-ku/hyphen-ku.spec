# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-ku
Summary: Kurdish hyphenation rules
Version: 1.71.2
Release: alt1_7
Source: http://extensions.services.openoffice.org/e-files/2445/12/kitandin.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/project/kitandin
License: LGPLv2+
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Kurdish hyphenation rules.

%prep
%setup -q -c -n hyphen-ku

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ku.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_ku_TR.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen
ku_TR_aliases="ku_SY"
for lang in $ku_TR_aliases; do
        ln -s hyph_ku_TR.dic hyph_$lang.dic
done
popd

%files
%doc README_ku.txt
%{_datadir}/hyphen/*

%changelog
* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.71.2-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.71.2-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.71.2-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.71.2-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.71.2-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.71.2-alt1_2
- import by fcmass

