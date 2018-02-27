Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/pkg-config libgio-devel pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-extensions
%define fedora 21
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name caja-extensions
%define version 1.8.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.8

# Settings used for build from snapshots.
%{!?rel_build:%global commit 298c7255b82986eeba72fff06f59479deae0b9d0}
%{!?rel_build:%global commit_date 20131201}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:           mate-file-manager-extensions
Summary:        Set of extensions for caja file manager
Version:        %{branch}.0
Release:        alt1_1
#Release:        0.4%{?git_rel}%{?dist}
License:        GPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R caja.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%%{oldname}-%%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

Source1:        caja-share-setup-instructions
Source2:        caja-share-smb.conf.example

Patch1:         caja-extensions_use-beesu-command-for-gksu.patch

BuildRequires:  mate-common
%if 0%{?fedora} > 20
BuildRequires:  mate-file-manager-devel
%else
BuildRequires:  mate-file-manager-devel
%endif
BuildRequires:  mate-desktop-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  gtk2-devel
BuildRequires:  libgupnp-devel
Source44: import.info


%description
Extensions for the caja file-browser, open-terminal,
image-converter, sendto and share

%package common
Group: Graphical desktop/MATE
Summary:    Common files for %{oldname}
BuildArch:  noarch
%description common
%{summary}.

%package -n mate-file-manager-image-converter
Group: Graphical desktop/MATE
Summary:    MATE file manager image converter extension
Requires:   %{name}-common = %{version}-%{release}
Requires:   ImageMagick
%description -n mate-file-manager-image-converter
The caja-image-converter extension allows you to
re-size/rotate images from Caja.

%package -n mate-file-manager-open-terminal
Group: Graphical desktop/MATE
Summary:    Mate-file-manager extension for an open terminal shortcut
Requires:   %{name}-common = %{version}-%{release}
%description -n mate-file-manager-open-terminal
The caja-open-terminal extension provides a right-click "Open
Terminal" option for mate-file-manager users who prefer that option.

%package -n mate-file-manager-sendto
Group: Graphical desktop/MATE
Summary:    MATE file manager sendto
Requires:   %{name}-common = %{version}-%{release}
%description -n mate-file-manager-sendto
The caja-sendto extension provides 'send to' functionality
to the MATE Desktop file-manager, Caja.

%package -n mate-file-manager-sendto-devel
Group: Graphical desktop/MATE
Summary:    Development libraries and headers for caja-sendto
Requires:   %{name}-common = %{version}-%{release}
Requires:	mate-file-manager-sendto%{?_isa} = %{version}-%{release}
%description -n mate-file-manager-sendto-devel
Development libraries and headers for caja-sendto

%package -n mate-file-manager-share
Group: Graphical desktop/MATE
Summary:    Easy sharing folder via Samba (CIFS protocol)
Requires:   %{name}-common = %{version}-%{release}
Requires:   samba
%description -n mate-file-manager-share
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%package -n mate-file-manager-beesu
Group: Graphical desktop/MATE
Summary:    MATE file manager beesu
Requires:   %{name}-common = %{version}-%{release}
Requires:   beesu
%description -n mate-file-manager-beesu
Caja beesu extension for open files as superuser


%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}
%patch1 -p1 -b .beesu
cp %{SOURCE1} SETUP

# needed for git snapshots
#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
     --disable-schemas-compile \
     --with-gtk=2.0            \
     --enable-image-converter  \
     --enable-open-terminal    \
     --enable-sendto           \
     --enable-share            \
     --enable-gksu             \
     --disable-static

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

mkdir -p %{buildroot}/%{_sysconfdir}/samba/
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/samba/

# remove needless gsettings convert files
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/caja-sendto-convert
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/caja-open-terminal.convert

%find_lang %{oldname} --with-gnome --all-name


%files common -f %{oldname}.lang
%doc AUTHORS COPYING README SETUP
%dir %{_datadir}/caja-extensions

%files -n mate-file-manager-image-converter
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui

%files -n mate-file-manager-open-terminal
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml

%files -n mate-file-manager-sendto
%{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%{_libdir}/caja-sendto/plugins/libnstpidgin.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja-sendto/plugins/libnstupnp.so
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja-extensions/caja-sendto.ui
%dir %{_datadir}/gtk-doc/html/caja-sendto
%{_datadir}/gtk-doc/html/caja-sendto/*
%{_mandir}/man1/caja-sendto.1*

%files -n mate-file-manager-sendto-devel
%dir %{_includedir}/caja-sendto
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc

%files -n mate-file-manager-share
%config %{_sysconfdir}/samba/caja-share-smb.conf.example
%{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui

%files -n mate-file-manager-beesu
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so


%changelog
* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new fc release

