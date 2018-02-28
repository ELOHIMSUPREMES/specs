Name: gnubik
Version: 2.4.1
Release: alt1.1

Summary: gnubik -  an interactive, graphic Magic cube program
Summary(ru_RU.UTF-8): gnubik - трёхмерный кубик-рубик
Group: Games/Puzzles
License: GPL

Url: http://www.gnu.org/software/gnubik/

Source0: %name-%version.tar.gz
Source1: %name.desktop
Patch0: gnubik_2.2-7.diff

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: guile18-devel imake libfreeglut-devel libgtkglext-devel xorg-cf-files
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
gnubik - an interactive, graphic Magic cube program.

%prep
%setup
#patch0 -p1

%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%add_optflags "-Wl,--no-as-needed"
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

install -D -m 644 %SOURCE1 %buildroot%_desktopdir/gnubik.desktop

mkdir -p %buildroot%_man6dir/

install -pD -m644 doc/%name.6 %buildroot%_man6dir

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO THANKS
%_bindir/gnubik
%_desktopdir/gnubik.desktop
%_iconsdir/hicolor/*/apps/*
%dir %_datadir/gnubik/
%_datadir/gnubik/
%_infodir/gnubik.*
%_man6dir/gnubik.*

%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1.1
- NMU: added BR: texinfo

* Sat Jun 15 2013 Fr. Br. George <george@altlinux.ru> 2.4.1-alt1
- Autobuild version bump to 2.4.1
- Package icons

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.3-alt1.qa3
- NMU: rebuilt for debuginfo.

* Mon Dec 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.3-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * secondary menu category for gnubik

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for gnubik
  * postclean-05-filetriggers for spec file

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 2.3-alt1
- 2.3

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 2.2-alt4
- apply patch from repocop

* Fri Jun 08 2007 Igor Zubkov <icesik@altlinux.org> 2.2-alt3
- sync with debian gnubik_2.2-7.diff (add desktop file)

* Wed May 03 2006 Igor Zubkov <icesik@altlinux.ru> 2.2-alt2
- fix rebuild with new ld (by -Wl,--no-as-needed)
- buildreq

* Thu Jan 26 2006 Igor Zubkov <icesik@altlinux.ru> 2.2-alt1
- Initial build for Sisyphus
