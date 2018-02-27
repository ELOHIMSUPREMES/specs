%add_optflags %optflags_shared
%define oldname lwp
Name:           liblwp
Version:        2.6
Release:        alt1_7
Summary:        C library for user-mode threading
Group:          System/Libraries
License:        LGPLv2
URL:            http://www.coda.cs.cmu.edu/
Source0:        ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{oldname}-%{version}.tar.gz
Source1:        ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{oldname}-%{version}.tar.gz.asc
Patch0:         lwp-2.6-no-longjmp_chk.patch
Source44: import.info
Provides: lwp = %{version}-%{release}

%description
The LWP user-space threads library. The LWP threads library is used by the Coda
distributed file-system, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package        devel
Summary:        Development files for %{oldname}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides: lwp-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -b .nolongjmpchk

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
./src/testlwp 2

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{oldname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{oldname}.pc

%changelog
* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_7
- initial fc import

