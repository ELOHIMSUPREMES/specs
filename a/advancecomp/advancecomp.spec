Group: Emulators
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/col /usr/bin/groff /usr/bin/gzip /usr/bin/valgrind /usr/bin/wine bzlib-devel gcc-c++
# END SourceDeps(oneline)
Name:           advancecomp
Version:        1.19
Release:        alt1_2
Summary:        Recompression utilities for .PNG, .MNG and .ZIP files
License:        GPLv3
URL:            http://advancemame.sourceforge.net/
Source0:        http://downloads.sf.net/advancemame/advancecomp-%{version}.tar.gz
BuildRequires:  tofrodos
BuildRequires:  zlib-devel
Source44: import.info

%description
AdvanceCOMP is a set of recompression utilities for .PNG, .MNG and .ZIP files.
The main features are :
* Recompress ZIP, PNG and MNG files using the Deflate 7-Zip implementation.
* Recompress MNG files using Delta and Move optimization.

This package contains:
* advzip - Recompression and test utility for zip files
* advpng - Recompression utility for png files
* advmng - Recompression utility for mng files
* advdef - Recompression utility for deflate streams in .png, .mng and .gz 
files

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
make check

%files
%doc AUTHORS COPYING HISTORY README
%doc doc/{advdef*,authors,history,readme}.{txt,html}
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_2
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_1
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_19
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_18
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_17
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_16
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_14
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_13
- initial release by fcimport

