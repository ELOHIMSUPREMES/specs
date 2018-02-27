# BEGIN SourceDeps(oneline):
BuildRequires: libgio-devel pkgconfig(cairo) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0)
# END SourceDeps(oneline)
Name:		hitori
Version:	3.14.0.1
Release:	alt1_1
Summary:	Logic puzzle game for GNOME
Summary(de):	Logikpuzzle für GNOME

Group:		Games/Other
# The executable is licensed under GPLv3+, while the user manual is CC-BY-SA.
License:	GPLv3+ and CC-BY-SA
URL:		http://live.gnome.org/Hitori
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.14/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	itstool
BuildRequires:	libgtk+3-devel
BuildRequires:	intltool
Source44: import.info

%description
A small application written to allow one to play the Hitori puzzle game,
which is similar in theme to more popular puzzles such as Sudoku.

It has full support for playing the game (i.e. it checks all three rules are
satisfied). It has undo/redo support, can give hints, and allows for cells
to be tagged with one of two different tags, to aid in solving the puzzle.
It has support for anything from 5A-5 to 10A-10 grids.

%description -l de
Ein kleines Programm zum Spielen des Hitori-Puzzles, das thematisch
populäreren Puzzlespielen wie beispielsweise Sudoku ähnelt.

Das Programm unterstützt die Spielregeln vollständig. Es wird in
jedem Fall überprüft, ob die drei Ausschlussregeln angewendet sind.
Das Zurücknehmen und Wiederholen von Zügen ist ebenso möglich wie das
Kennzeichnen von Feldern mit einer oder mehreren Markierungen, um den Weg zur
Lösung zu erleichtern. Mögliche Spielfeldgrößen reichen von 5x5 bis hin zu
10x10 Feldern. 

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang %{name} --with-gnome

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING-DOCS MAINTAINERS NEWS README
%{_bindir}/%{name}
%{_datadir}/appdata/hitori.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.hitori.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png


%changelog
* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.0.1-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_2
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_2
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_4
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_1
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_3
- converted from Fedora by srpmconvert script

