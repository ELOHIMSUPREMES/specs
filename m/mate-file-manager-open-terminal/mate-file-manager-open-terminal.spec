Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/pkg-config libgio-devel pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:		mate-file-manager-open-terminal
Version:	1.6.0
Release:	alt1_3
Summary:	Mate-file-manager extension for an open terminal shortcut

License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:	mate-common
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
Source44: import.info


%description
The mate-file-manager-open-terminal extension provides a right-click "Open
Terminal" option for mate-file-manager users who prefer that option.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
    --disable-static  \
    --disable-schemas-compile

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_libdir}/caja/extensions-2.0/*.la

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/caja-open-terminal.convert

%find_lang caja-open-terminal


%files -f caja-open-terminal.lang
%doc AUTHORS ChangeLog README COPYING
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml


%changelog
* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Fri Dec 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- 20120622 mate snapshot

