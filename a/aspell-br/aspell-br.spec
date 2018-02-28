# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define lang br
%define langrelease 2
Summary: Breton dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 0.50
Release: alt2_21
License: GPLv2
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Patch0: aspell-br-0.50-conf.patch
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: Breton

%prep
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}
%patch0 -b .conf -p1

%build
./configure 
%make_build

%install
make install DESTDIR="$RPM_BUILD_ROOT"

%files
%doc COPYING Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_21
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_16
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_15
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_14
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_13
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_12
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_12
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import

