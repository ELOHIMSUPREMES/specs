# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize libICE-devel libgio-devel pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-3.0) pkgconfig(gtksourceview-3.0) pkgconfig(libxml-2.0) pkgconfig(pygtk-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname pluma
%define fedora 23
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name pluma
%define version 1.12.2
%add_python_req_skip pluma
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

# Settings used for build from snapshots.
%{!?rel_build:%global commit c1ca209172a8b3a0751ac0a1e2dbec33c1894290}
%{!?rel_build:%global commit_date 20140712}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Summary:  Text editor for the MATE desktop
Name:     mate-text-editor
Version:  %{branch}.2
%if 0%{?rel_build}
Release:  alt1_1
%else
Release:  alt1_1
%endif
License:  GPLv2+ and LGPLv2+
Group:    Editors
URL:      http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R pluma.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: desktop-file-utils
BuildRequires: libenchant-devel
BuildRequires: libsoup-devel
BuildRequires: gtk2-devel
BuildRequires: libgtksourceview-devel
BuildRequires: iso-codes-devel
BuildRequires: libSM-devel
BuildRequires: mate-common
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-pygtksourceview-devel
BuildRequires: python-devel
BuildRequires: rarian-compat
BuildRequires: yelp-tools
BuildRequires: mate-desktop-devel

Requires: %{name}-data = %{version}
Requires: pygtk2
Requires: python-module-pygobject
Requires: python-module-pygtksourceview
# needed to get a gsettings schema, #959607
Requires: libmate-desktop
# needed to get a gsettings schema, #959607
Requires: mate-file-manager-schemas
# the run-command plugin uses zenity
Requires: zenity

%if 0%{?fedora} && 0%{?fedora} > 19
%endif
Source44: import.info

%description
mate-text-editor is a small, but powerful text editor designed specifically for
the MATE desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

mate-text-editor is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.

%package data
Summary:   Data files for pluma
Group:     Editors
BuildArch: noarch
Requires:  mate-text-editor = %{version}

%description data
This package contains shared data needed for pluma.

%package devel
Summary:   Support for developing plugins for the mate-text-editor text editor
Group:     Development/C
Requires:  mate-text-editor = %{version}
%if 0%{?fedora} && 0%{?fedora} > 19
Provides:  mate-text-editor-devel%{?_isa} = %{version}-%{release}
Provides:  mate-text-editor-devel = %{version}-%{release}
Obsoletes: mate-text-editor-devel < %{version}-%{release}
%endif

%description devel
Development files for mate-text-editor

%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}

%if 0%{?rel_build}
# for releases
#NOCONFIGURE=1 ./autogen.sh
%else
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif

# Fix debug permissions with messy hack 
find ./*/* -type f -exec chmod 644 {} \;
find ./*/*/* -type f -exec chmod 644 {} \;


%build
%configure \
        --disable-static          \
        --enable-gtk-doc-html     \
        --enable-gvfs-metadata    \
        --enable-python           \
        --disable-schemas-compile \
        --with-gtk=2.0

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop

# clean up all the static libs for plugins
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/pluma.convert

%find_lang %{oldname} --with-gnome --all-name


%post data
/bin/touch --no-create %{_datadir}/pluma/icons &> /dev/null || :

%postun data
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/pluma/icons &> /dev/null

fi

%files
%{_bindir}/pluma
%{_libdir}/pluma/
%{_libexecdir}/pluma/
%{_datadir}/applications/pluma.desktop
%{_datadir}/appdata/pluma.appdata.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml

%files data -f %{oldname}.lang
%doc README COPYING AUTHORS
%{_datadir}/pluma/
%{_mandir}/man1/pluma.1.*

%files devel
%{_includedir}/pluma/
%{_libdir}/pkgconfig/pluma.pc
%{_datadir}/gtk-doc/html/pluma/


%changelog
* Tue Apr 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.2-alt1_1
- new fc release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2_1
- built with gtk 2

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_5
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
dropped obsolete mate-conf BR:

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- added mate-desktop-1.5.0-alt-settings.patch - font settings

