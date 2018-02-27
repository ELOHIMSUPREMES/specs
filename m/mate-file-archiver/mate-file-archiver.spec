Group: Archiving/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums libgio-devel pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname mate-file-archiver
Name:           mate-file-archiver
Version:        1.6.0
Release:        alt1_2
Summary:        MATE Desktop file archiver
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

# upstream patch to fix
# https://github.com/mate-desktop/mate-file-archiver/issues/19
# will be removed with next release
Patch0:         mate-file-archiver_missing_gsettings_schema.patch

BuildRequires:  mate-common
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  mate-file-manager-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  libSM-devel
BuildRequires:  rarian-compat
BuildRequires:  librarian-devel

Provides: engrampa

# bugzilla.redhat.com/908137
# dropped mate-file-manager-archiver subpkg sometime after 1.5.1-1 release
Obsoletes: mate-file-manager-archiver < 1.5.1-5
Patch33: file-roller-2.28.2-alt-7z.patch
Source44: import.info

%description
Mate File Archiver is an application for creating and viewing archives files,
such as tar or zip files.


%prep
%setup -n %{name}-%{version} -q
%patch0 -p1 -b .gsettings_schema
NOCONFIGURE=1 ./autogen.sh
%patch33 -p0


%build
%configure                 \
   --disable-scrollkeeper  \
   --disable-static        \
   --with-gtk=2.0          \
   --enable-caja-actions

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/engrampa.desktop

find %{buildroot} -name "*.la" -exec rm -f {} ';'

# remove needless gsettings convert file to avoid slow session start
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/engrampa.convert

%find_lang engrampa

%files -f engrampa.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/engrampa
%{_libexecdir}/engrampa
%{_datadir}/engrampa
%{_datadir}/mate/help/engrampa
%{_datadir}/applications/engrampa.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml
%{_libdir}/caja/extensions-2.0/libcaja-engrampa.so
%{_datadir}/omf/engrampa


%changelog
* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_6
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_4
- new fc release

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_3
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

