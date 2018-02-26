%add_optflags %optflags_shared
Name:           libhbaapi
Version:        2.2.6
Release:        alt1_1
Summary:        SNIA HBAAPI library
Group:          System/Libraries
License:        SNIA
URL:            http://open-fcoe.org/
# This source was cloned from upstream git (libHBAAPI)
Source:         %{name}-%{version}.tar.bz2
Patch0:         libhbaapi-2.2-9-dl-linking.patch
Patch1:         libhbaapi-2.2-archiver.patch
BuildRequires:  automake libtool
Source44: import.info

%description
The SNIA HBA API library. C-level project to manage
Fibre Channel Host Bus Adapters.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup
%patch0 -p1 -b .ld-linking
%patch1 -p1 -b .archiver

%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING
%config(noreplace) %{_sysconfdir}/hba.conf
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_15
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_14
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_12
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_12
- initial import by fcimport

