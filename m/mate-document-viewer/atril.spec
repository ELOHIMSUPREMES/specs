Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize gcc-c++ libICE-devel libgio-devel pkgconfig(cairo) pkgconfig(cairo-pdf) pkgconfig(cairo-ps) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(sm) pkgconfig(x11) t1lib-devel zlib-devel intltool
# END SourceDeps(oneline)
BuildRequires: pkgconfig(libxml-2.0)
## important!!! # https://bugzilla.altlinux.org/show_bug.cgi?id=28634
Requires: mate-desktop
%define _libexecdir %_prefix/libexec
%define oldname atril
%define fedora 25
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name atril
%define version 1.19.4
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.19

# Settings used for build from snapshots.
%{!?rel_build:%global commit 5bba3723566489763aafaad3669c77f60a23d2e0}
%{!?rel_build:%global commit_date 20140122}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:          mate-document-viewer
Version:       %{branch}.4
%if 0%{?rel_build}
Release:       alt2_1
%else
Release:       alt2_1
%endif
Summary:       Document viewer
License:       GPLv2+ and LGPLv2+ and MIT
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R caja.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  libpoppler-gir-devel libpoppler-glib-devel
BuildRequires:  libXt-devel
BuildRequires:  libsecret-devel libsecret-gir-devel
BuildRequires:  libglade-devel
BuildRequires:  libtiff-devel libtiffxx-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libspectre-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  libcairo-gobject-devel
BuildRequires:  yelp-tools

# for the xps back-end
BuildRequires:  libgxps-devel libgxps-gir-devel
# for the caja properties page
BuildRequires:  mate-file-manager-devel
# for the dvi back-end
%if 0%{?fedora} >= 24
BuildRequires:  libkpathsea-devel
%else
BuildRequires:  libkpathsea-devel
%endif
# for the djvu back-end
BuildRequires:  libdjvu-devel
# for epub back-end
%if 0%{?fedora}
BuildRequires:  libwebkit2gtk-devel libwebkit2gtk-gir-devel
%endif
%if 0%{?rhel}
BuildRequires:  libwebkitgtk3-devel
%endif

Requires:       mate-document-viewer-libs = %{version}-%{release}
#  fix (#974791)
Requires:       libmate-desktop
Requires:       mathjax
Source44: import.info
Patch33: mate-document-viewer-1.4.0-alt-link.patch
Patch34: evince-2.32.0-alt.patch

%description
Mate-document-viewer is simple document viewer.
It can display and print Portable Document Format (PDF),
PostScript (PS), Encapsulated PostScript (EPS), DVI, DJVU, epub and XPS files.
When supported by the document format, mate-document-viewer
allows searching for text, copying text to the clipboard,
hypertext navigation, table-of-contents bookmarks and editing of forms.


%package -n mate-document-viewer-libs
Group: System/Libraries
Summary: Libraries for the mate-document-viewer

%description -n mate-document-viewer-libs
This package contains shared libraries needed for mate-document-viewer.


%package devel
Group: Development/C
Summary: Support for developing back-ends for the mate-document-viewer
Requires: mate-document-viewer-libs = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
mate-document-viewer back-ends development.

%package dvi
Summary: Atril backend for dvi files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description dvi
This package contains a backend to let atril display dvi files.

%package djvu
Summary: Atril backend for djvu files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description djvu
This package contains a backend to let atril display djvu files.

%package pixbuf
Summary: Atril backend for graphics files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description pixbuf
This package contains a backend to let atril display graphics files.

%package xps
Summary: Atril backend for xps files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description xps
This package contains a backend to let atril display xps files.

%package caja
Group: Graphical desktop/MATE
Summary: Mate-document-viewer extension for caja
Requires: %{name} = %{version}-%{release}
Requires: mate-file-manager

%description caja
This package contains the mate-document-viewer extension for the
caja file manager.
It adds an additional tab called "Document" to the file properties dialog.

%package thumbnailer
Group: Publishing
Summary: Atril thumbnailer extension for caja
Requires: %{name} = %{version}-%{release}
Requires: mate-file-manager
BuildArch: noarch

%description thumbnailer
This package contains the atril extension for the
caja file manager.


%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}
%patch33 -p0
%patch34 -p1

%build
%autoreconf
%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-introspection \
        --enable-comics \
        --enable-dvi=yes \
        --enable-djvu=yes \
        --enable-t1lib=no \
        --enable-pixbuf \
        --enable-xps \
        --enable-epub

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build V=1


%install
%{makeinstall_std}

%find_lang %{oldname} --with-gnome --all-name

find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'


%check
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/atril.desktop


%post
/bin/touch --no-create %{_datadir}%{oldname}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ]; then

  /bin/touch --no-create %{_datadir}%{oldname}/icons/hicolor &>/dev/null



fi

%files -f %{oldname}.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/*
%dir %{_datadir}/atril
%{_datadir}/atril/*
%{_datadir}/applications/atril.desktop
%{_datadir}/icons/hicolor/*/apps/atril.*
%{_libexecdir}/atrild
%{_datadir}/dbus-1/services/org.mate.atril.Daemon.service
%{_datadir}/glib-2.0/schemas/org.mate.Atril.gschema.xml
%{_datadir}/appdata/atril.appdata.xml
%{_mandir}/man1/atril-*.1.*
%{_mandir}/man1/atril.1.*

%files -n mate-document-viewer-libs
%{_libdir}/libatrilview.so.*
%{_libdir}/libatrildocument.so.*
%{_libdir}/atril/3/backends/
%{_libdir}/girepository-1.0/AtrilDocument-1.5.0.typelib
%{_libdir}/girepository-1.0/AtrilView-1.5.0.typelib

%exclude %{_libdir}/atril/3/backends/libdvidocument.so*
%exclude %{_libdir}/atril/3/backends/dvidocument.atril-backend
%exclude %{_libdir}/atril/3/backends/libdjvudocument.so
%exclude %{_libdir}/atril/3/backends/djvudocument.atril-backend
%exclude %{_libdir}/atril/3/backends/libxpsdocument.so*
%exclude %{_libdir}/atril/3/backends/xpsdocument.atril-backend
%exclude %{_libdir}/atril/3/backends/libpixbufdocument.so*
%exclude %{_libdir}/atril/3/backends/pixbufdocument.atril-backend

%files dvi
%{_libdir}/atril/3/backends/libdvidocument.so*
%{_libdir}/atril/3/backends/dvidocument.atril-backend

%files djvu
%{_libdir}/atril/3/backends/libdjvudocument.so
%{_libdir}/atril/3/backends/djvudocument.atril-backend

%files xps
%{_libdir}/atril/3/backends/libxpsdocument.so*
%{_libdir}/atril/3/backends/xpsdocument.atril-backend

%files pixbuf
%{_libdir}/atril/3/backends/libpixbufdocument.so*
%{_libdir}/atril/3/backends/pixbufdocument.atril-backend

%files caja
%{_libdir}/caja/extensions-2.0/libatril-properties-page.so
%{_datadir}/caja/extensions/libatril-properties-page.caja-extension

%files thumbnailer
%{_datadir}/thumbnailers/atril.thumbnailer

%files devel
%dir %{_includedir}/atril/
%{_includedir}/atril/1.5.0/
%{_libdir}/libatrilview.so
%{_libdir}/libatrildocument.so
%{_libdir}/pkgconfig/atril-view-1.5.0.pc
%{_libdir}/pkgconfig/atril-document-1.5.0.pc
%{_datadir}/gir-1.0/AtrilDocument-1.5.0.gir
%{_datadir}/gir-1.0/AtrilView-1.5.0.gir
%{_datadir}/gtk-doc/html/libatrildocument-1.5.0/
%{_datadir}/gtk-doc/html/libatrilview-1.5.0/
%{_datadir}/gtk-doc/html/atril/


%changelog
* Sat Feb 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.19.4-alt2_1
- NMU: rebuild with texlive 2016

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.4-alt1_1
- new fc release

* Wed Sep 13 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.3-alt1_1
- new fc release

* Thu Sep 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.1-alt1_1
- new fc release

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_1
- update to 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.2-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Tue Mar 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_0
- added patch1

* Sun Mar 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new version

* Sun Aug 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_0
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.0-alt1_0.qa1
- NMU: rebuilt with libarchive.so.13.

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_0
- new version

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3_0
- added Req: mate-desktop (closes: 28634)

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
dropped obsolete mate-conf BR:

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- fixed build

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

