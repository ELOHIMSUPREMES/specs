Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install libgio-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-export-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
BuildRequires: mate-common
%define _libexecdir %_prefix/libexec
Name:		mate-calc
Version:	1.8.0
Release:	alt1_4
Summary:	MATE Desktop calculator
License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
Source44: import.info



%description
mate-calc is a powerful graphical calculator with financial, logical and scientific modes.
It uses a multiple precision package to do its arithmetic to give a high degree of accuracy.

%prep
%setup -q -n %{name}-%{version}


%build
%configure --disable-schemas-compile \
           --with-gtk=2.0

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}


desktop-file-install									\
	--delete-original								\
	--dir=%{buildroot}%{_datadir}/applications					\
%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-calc
%{_bindir}/mate-calc-cmd
%{_bindir}/mate-calculator
%{_datadir}/applications/mate-calc.desktop
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_datadir}/mate-calc
%{_datadir}/help/*/mate-calc


%changelog
* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_4
- new version

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_3
- new fc release

* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- converted for ALT Linux by srpmconvert tools

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2
- build fixed

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

