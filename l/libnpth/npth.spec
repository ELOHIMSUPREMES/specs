Group: System/Libraries
%add_optflags %optflags_shared
%define oldname npth
Name:           libnpth
Version:        1.2
Release:        alt1_2
Summary:        The New GNU Portable Threads library
# software uses dual licensing (or both in parallel)
License:        LGPLv3+ or GPLv2+ or (LGPLv3+ and GPLv2+)
URL:            http://git.gnupg.org/cgi-bin/gitweb.cgi?p=npth.git
Source:         ftp://ftp.gnupg.org/gcrypt/npth/npth-%{version}.tar.bz2
#Source1:        ftp://ftp.gnupg.org/gcrypt/npth/npth-%{version}.tar.bz2.sig
# Manual page is re-used and changed pth-config.1 from pth-devel package
Source2:        npth-config.1
Source44: import.info
Provides: npth = %{version}-%{release}

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package        devel
Group: Development/C
Summary:        Development files for %{oldname}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides: npth-devel = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q

%build
%configure --disable-static
%make_build

%install
%makeinstall_std INSTALL='install -p'

mkdir -p %{buildroot}%{_mandir}/man1/
install -pm0644 %{S:2} %{buildroot}%{_mandir}/man1/

find %{buildroot} -name '*.la' -delete -print

%check
make check

%files
%doc COPYING COPYING.LESSER
%{_libdir}/*.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/*/*
%{_datadir}/aclocal/*

%changelog
* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_6
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_5
- initial fc import

