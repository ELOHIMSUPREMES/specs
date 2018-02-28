# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname sombok
%define fedora 25
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libsombok
Version:        2.4.0
Release:        alt1_5
Summary:        Unicode Text Segmentation Package

Group:          System/Libraries
License:        GPLv2+ or Artistic clarified
URL:            http://sf.net/projects/linefold/
Source0:        https://github.com/hatukanezumi/sombok/archive/%{oldname}-%{version}.tar.gz

# libthai is available only in Fedora and EL6
%if 0%{?rhel} > 5 || 0%{?fedora}
BuildRequires:  libthai-devel
%endif

BuildRequires:  autoconf-common
BuildRequires:  automake-common
BuildRequires:  libtool-common
Source44: import.info
Provides: sombok = %{version}-%{release}


%description
Sombok library package performs Line Breaking Algorithm described in Unicode
Standards Annex #14 (UAX #14). East_Asian_Width informative properties defined
by Annex #11 (UAX #11) may be concerned to determine breaking positions. This
package also implements "default" Grapheme Cluster segmentation described in
Annex #29 (UAX #29).


%package        devel
Summary:        Development files for %{oldname}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       pkg-config
Provides: sombok-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -q -n %{oldname}-%{oldname}-%{version}


%build
autoreconf -vif
%configure --disable-static
%make_build


%install
# hack
rm -rf doc/html/search
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS ChangeLog ChangeLog.REL1 COPYING NEWS README README.ja_JP
%{_libdir}/libsombok.so.*


%files devel
%{_includedir}/sombok*.h
%{_libdir}/libsombok.so
%{_libdir}/pkgconfig/sombok.pc


%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_3
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_2
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_1
- moved to Sisyphus for perl-Text-vCard

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3
- update to new release by fcimport

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2
- new release

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1
- fc import

