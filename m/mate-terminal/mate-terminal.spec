Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtk-builder-convert libICE-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(vte-2.90) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary:        Terminal emulator for MATE
Name:           mate-terminal
Version:        1.6.1
Release:        alt1_11
License:        GPLv3+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

#Default to black bg white fg, unlimited scrollback, turn off use theme default
Patch0:        mate-terminal_better_defaults.patch

BuildRequires: libdconf-devel
BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: libSM-devel
BuildRequires: mate-doc-utils
BuildRequires: mate-common
BuildRequires: rarian-compat
BuildRequires: librarian-devel
BuildRequires: libvte-devel

Requires:      libmate-desktop
Requires:      gsettings-desktop-schemas
Source44: import.info
Provides: xvt

%description
Mate-terminal is a terminal emulator for MATE. It supports translucent
backgrounds, opening multiple terminals in a single window (tabs) and
clickable URLs.

%prep
%setup -q
%patch0 -p1
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static                \
           --with-gtk=2.0                  \
           --disable-scrollkeeper          \
           --disable-schemas-compile       

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install
%find_lang %{name}

desktop-file-install							\
	--delete-original						\
	--dir=%{buildroot}%{_datadir}/applications			\
%{buildroot}%{_datadir}/applications/mate-terminal.desktop
# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt    %_bindir/%name  48
EOF


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog
%{_mandir}/man1/*
%{_bindir}/mate-terminal
%{_datadir}/mate-terminal
%{_datadir}/mate/help/mate-terminal
%{_datadir}/omf/mate-terminal
%{_datadir}/applications/mate-terminal.desktop
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%_altdir/%name

%changelog
* Sat Aug 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_11
- new fc release

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Thu Apr 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_4
- added xvt provides (closes: 28160)

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_4
- added xvt alternative

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_4
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

