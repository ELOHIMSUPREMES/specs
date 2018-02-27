# BEGIN SourceDeps(oneline):
BuildRequires: librest-gir-devel pkgconfig(gio-2.0)
# END SourceDeps(oneline)
%define fedora 19
# -*- rpm-spec -*-

%global with_gir 0

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%global with_gir 1
%endif

Summary: A GObject library for interacting with oVirt REST API
Name: libgovirt
Version: 0.0.3
Release: alt1_2%{?extra_release}
License: LGPLv2+
Group: Development/C
Source: http://people.freedesktop.org/~teuf/govirt/%{name}-%{version}.tar.xz
URL: http://people.freedesktop.org/~teuf/govirt/
BuildRequires: glib2-devel
BuildRequires: librest-devel >= 0.7.90
%if %{with_gir}
BuildRequires: gobject-introspection-devel
%endif
Source44: import.info

%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package devel
Summary: Libraries, includes, etc. to compile with the libgovirt library
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

Libraries, includes, etc. to compile with the libgovirt library

%prep
%setup -q

%build
%if %{with_gir}
%global gir_arg --enable-introspection=yes
%else
%global gir_arg --enable-introspection=no
%endif

%configure %{gir_arg}
%__make %{?_smp_mflags} V=1

%install
%__make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%files
%doc AUTHORS COPYING MAINTAINERS README
%{_libdir}/%{name}.so.1*
%if %{with_gir}
%{_libdir}/girepository-1.0/GoVirt-1.0.typelib
%endif

%files devel
%{_libdir}/%{name}.so
%dir %{_includedir}/govirt-1.0/
%dir %{_includedir}/govirt-1.0/govirt/
%{_includedir}/govirt-1.0/govirt/*.h
%{_libdir}/pkgconfig/govirt-1.0.pc
%if %{with_gir}
%{_datadir}/gir-1.0/GoVirt-1.0.gir
%endif

%changelog
* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_2
- initial fc import

