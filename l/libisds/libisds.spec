# BEGIN SourceDeps(oneline):
BuildRequires: libexpat-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libisds
Version:        0.7
Release:        alt1_4
Summary:        Library for accessing the Czech Data Boxes
Group:          System/Libraries
License:        LGPLv3
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
BuildRequires:  libxml2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpgme-devel
BuildRequires:  expat-devel >= 2.0.0
# Run-time:
BuildRequires:  gnupg2
# Tests:
BuildRequires:  libgnutls-devel >= 2.12.0
# Update config.sub to support aarch64, bug #925782
BuildRequires:  autoconf automake gettext-devel libtool
Requires:       gnupg2
Source44: import.info

%description
This is a library for accessing ISDS (InformaA.nA. systA.m datovA.ch schrA.nek /
Data Box Information System) SOAPa..services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
# Update config.sub to support aarch64, bug #925782
autoreconf -i -f

%build
%configure --disable-static \
    --enable-test \
    --with-libcurl \
    --enable-curlreauthorizationbug
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
mv doc specification
rm -rf client/.deps

%files -f %{name}.lang
%doc README AUTHORS NEWS TODO COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/isds.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%doc client specification

%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt3_3
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- initial import by fcimport

