# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-az
Summary: Azerbaijani hunspell dictionaries
%define upstreamid 20040827
Version: 0.%{upstreamid}
Release: alt2_10
Group: Text tools
Source: ftp://ftp.gnu.org/gnu/aspell/dict/az/aspell6-az-0.02-0.tar.bz2
URL: http://borel.slu.edu/crubadan/apps.html
License: GPLv2+
BuildArch: noarch
BuildRequires: aspell libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Azerbaijani hunspell dictionaries.

%prep
%setup -q -n aspell6-az-0.02-0

%build
export LANG=az_AZ.utf8
preunzip az.cwl
wordlist2hunspell az.wl az_AZ
for i in Copyright doc/Crawler.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc COPYING Copyright README doc/Crawler.txt
%{_datadir}/myspell/*

%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040827-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040827-alt2_9
- update to new release by fcimport

* Wed Nov 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040827-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040827-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040827-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040827-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040827-alt1_5
- import from Fedora by fcimport

