%add_optflags %optflags_shared
Name:           libXcm
Version:        0.5.1
Release:        alt1_4
Summary:        X Color Management Library

Group:          System/Libraries
License:        MIT
URL:            http://www.oyranos.org
Source0:        http://downloads.sourceforge.net/oyranos/libXcm-%{version}.tar.bz2

BuildRequires: xorg-util-macros
BuildRequires: autoconf automake libtool
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libXfixes-devel
BuildRequires:  libXmu-devel
BuildRequires: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-evieproto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-pmproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcbproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86rushproto-devel xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel
BuildRequires:  xorg-xtrans-devel
Source44: import.info


%description
The libXcm library is a reference implementation of the net-color spec.
It allows to attach color regions to X windows to communicate with color
servers.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
autoreconf -v --install --force
CFLAGS="$RPM_OPT_FLAGS -fPIC"

%configure --disable-static --enable-shared
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files devel
%doc docs/*.txt
%dir %{_includedir}/X11/Xcm
%{_includedir}/X11/Xcm/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/xcm.pc
%{_mandir}/man3/*.3.*


%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_4
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_2
- update to new release by fcimport

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_3
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_1
- initial import by fcimport

