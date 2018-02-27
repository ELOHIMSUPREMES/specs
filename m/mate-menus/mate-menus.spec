Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/glib-gettextize pkgconfig(gio-2.0) pkgconfig(glib-2.0)
# END SourceDeps(oneline)
Requires: altlinux-freedesktop-menu-mate
%define _libexecdir %_prefix/libexec
Name:           mate-menus
Version:        1.6.0
Release:        alt1_5
Summary:        Displays menus for MATE Desktop
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
Source1: 		mate-preferences-categories.menu

# patch in upstream
# https://github.com/mate-desktop/mate-menus/commit/e5734e2b6017c36fca8ab2403ed6cabfa7ef0d23
Patch0:         mate-menus_preferences-menu.patch

BuildRequires:  gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  python-devel

Requires:		libmate-menus = %{version}-%{release}

# we don't want to provide private python extension libs
%{echo 


}
Source44: import.info
%add_findprov_skiplist %{python_sitelibdir}/.*\.so$
Patch33: gnome-menus-2.14-alt-add-config-dir.patch
Patch34: gnome-menus-alt-applications-menu-no-legacy-kde.patch

%description
Displays menus for MATE Desktop

%package -n libmate-menus
Group: System/Libraries
Summary: Shared libraries for mate-menus
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n libmate-menus
Shared libraries for mate-menus

%package preferences-category-menu
Group: System/Libraries
Summary: Categories for the preferences menu
Requires:	libmate-menus = %{version}-%{release}

%description preferences-category-menu
Categories for the preferences menu

%package devel
Group: Development/C
Summary: Development files for mate-menus
Requires:	libmate-menus = %{version}-%{release}

%description devel
Development files for mate-menus

%prep
%setup -q
%patch0 -p1 -b .preferences

# fedora specific
# fix for usage of multimedia-menus package
sed -i -e '/<!-- End Other -->/ a\  <MergeFile>applications-merged/multimedia-categories.menu</MergeFile>' layout/mate-applications.menu

NOCONFIGURE=1 ./autogen.sh
%patch33 -p0
%patch34 -p1


%build
%configure \
 --disable-static \
 --enable-python \
 --enable-introspection=yes

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/menus
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
#%config %{_sysconfdir}/xdg/menus/mate-applications.menu
#%config %{_sysconfdir}/xdg/menus/mate-settings.menu
%{_datadir}/mate-menus
%{_datadir}/mate/desktop-directories

%files -n libmate-menus
%{_libdir}/girepository-1.0/MateMenu-2.0.typelib
%{_libdir}/libmate-menu.so.2
%{_libdir}/libmate-menu.so.2.4.9
%{python_sitelibdir}/matemenu.so

%files devel
%{_datadir}/gir-1.0/MateMenu-2.0.gir
%{_libdir}/libmate-menu.so
%{_includedir}/mate-menus
%{_libdir}/pkgconfig/libmate-menu.pc


%changelog
* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_5
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_4
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_2
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
- dropped hack with 586 provides

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

