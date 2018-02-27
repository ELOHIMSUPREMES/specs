# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-mkenums pkgconfig(gio-unix-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
Name:		libindicator
Version:	12.10.1
Release:	alt1_3
Summary:	Shared functions for Ayatana indicators

Group:		System/Libraries
License:	GPLv3
URL:		https://launchpad.net/libindicator
Source0:	https://launchpad.net/libindicator/12.10/12.10.1/+download/%{name}-%{version}.tar.gz

BuildRequires:	chrpath
BuildRequires:	gtk-doc
BuildRequires:	libtool

BuildRequires:	libdbus-glib-devel
BuildRequires:	gtk2-devel
BuildRequires:	libgtk+3-devel
Source44: import.info
Patch33: libindicator-fix-deprecated.patch


%description
A set of symbols and convenience functions that all Ayatana indicators are
likely to use.


%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary:	Shared functions for Ayatana indicators - Tools
Group:		Development/Tools
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains tools used by the %{name} package, the
Ayatana indicators system.


%package gtk3
Summary:	GTK+3 build of %{name}
Group:		System/Libraries

%description gtk3
A set of symbols and convenience functions that all Ayatana indicators
are likely to use. This is the GTK+ 3 build of %{name}, for use
by GTK+ 3 apps.


%package gtk3-devel
Summary:	Development files for %{name}-gtk3
Group:		Development/C

Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.


%package gtk3-tools
Summary:	Shared functions for Ayatana indicators - GTK3 Tools
Group:		Development/Tools

Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk3-tools
This package contains tools used by the %{name}-gtk3 package, the
Ayatana indicators system. This package contains the builds of the
tools for the GTK+3 build of %{name}.


%prep
%setup -q
%patch33 -p2

%build
%global _configure_script ../configure
rm -rf build-gtk2 build-gtk3
mkdir build-gtk2 build-gtk3

pushd build-gtk2
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%configure --with-gtk=2 --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
popd

pushd build-gtk3
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%configure --with-gtk=3 --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
popd


%install
pushd build-gtk2
make install DESTDIR=%{buildroot}
popd

pushd build-gtk3
make install DESTDIR=%{buildroot}
popd


# Ubuntu doesn't package the dummy indicator
rm -f %{buildroot}%{_libdir}/libdummy-indicator*.so

# Remove libtool files
find %{buildroot} -type f -name '*.la' -delete
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done


%files
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libindicator.so.*


%files devel
%dir %{_includedir}/libindicator-0.4/
%dir %{_includedir}/libindicator-0.4/libindicator/
%{_includedir}/libindicator-0.4/libindicator/*.h
%{_libdir}/libindicator.so
%{_libdir}/pkgconfig/indicator-0.4.pc


%files tools
%{_libexecdir}/indicator-loader
%dir %{_datadir}/libindicator/
%{_datadir}/libindicator/80indicator-debugging


%files gtk3
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libindicator3.so.*


%files gtk3-devel
%dir %{_includedir}/libindicator3-0.4/
%dir %{_includedir}/libindicator3-0.4/libindicator/
%{_includedir}/libindicator3-0.4/libindicator/*.h
%{_libdir}/libindicator3.so
%{_libdir}/pkgconfig/indicator3-0.4.pc


%files gtk3-tools
%{_libexecdir}/indicator-loader3

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 12.10.1-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 12.10.1-alt1_2
- update to new release by fcimport

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 12.10.1-alt1_1
- new fc release

* Wed Apr 10 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.94-alt1_4.1
- don't use deprecated gtk_icon_info_free

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.94-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.94-alt1_3
- update to new release by fcimport

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.94-alt1_2
- new version

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.22-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.22-alt1_1
- initial import by fcimport

