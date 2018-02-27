Name: qucs
Version: 0.0.16
Release: alt3
Summary: Circuit simulator
License: GPL
Group: Education
Url: http://qucs.sourceforge.net/

Source0: http://ovh.dl.sourceforge.net/sourceforge/qucs/%name-%version.tar.gz
Source1: %name.desktop
Source2: qucs-tango-icons.tar.bz2
Source3: qucs-icons.tar.bz2
Patch: qucs-0.0.16-qucsdigi.patch

# Automatically added by buildreq on Wed Mar 06 2013
# optimized out: fontconfig gnu-config libICE-devel libSM-devel libX11-devel libstdc++-devel xorg-xproto-devel
BuildRequires: flex gcc-c++ gperf imake libqt3-devel xorg-cf-files

%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.

%prep
%setup
tar -xjf %SOURCE2 -C qucs
sed -i '\@<tr1/complex>@d' qucs-core/configure
%patch -p1

%build
#autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_iconsdir
tar -xjf %SOURCE3 -C %buildroot%_iconsdir

for l in $(find %buildroot%_datadir/%name/lang -name \*.qm); do
    echo -n $l | sed 's,.*_\(.*\)\.qm,%%lang\(\1\) ,' >> %name.lang
    echo $l | sed "s,%buildroot,," >> %name.lang
done

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/*
%dir %_datadir/%name
%dir %_datadir/%name/lang
%_datadir/%name/bitmaps
%_datadir/%name/library
%_datadir/%name/tline
%_datadir/%name/octave
%dir %_datadir/%name/docs
%_datadir/%name/docs/en
%lang(de) %_datadir/%name/docs/de
%lang(es) %_datadir/%name/docs/es
%lang(fr) %_datadir/%name/docs/fr
%lang(ru) %_datadir/%name/docs/ru
%lang(uk) %_datadir/%name/docs/uk
%lang(cs) %_datadir/%name/docs/cs
%lang(pt) %_datadir/%name/docs/pt
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png
%_man1dir/*

%changelog
* Wed May 29 2013 Fr. Br. George <george@altlinux.ru> 0.0.16-alt3
- QnD fix qucsdigi (Closes: 28560)

* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 0.0.16-alt2
- Fix build on i586

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 0.0.16-alt1
- Autobuild version bump to 0.0.16
- Switch to gcc3.4 to avoid C++ error messages

* Thu Jul 01 2010 Fr. Br. George <george@altlinux.ru> 0.0.15-alt1.1
- Rebuild for Sisyphus

* Sun May 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.0.15-alt1
- 0.0.15

* Wed Jan 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.13-alt1
- 0.0.13

* Tue Jun 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.12-alt1
- 0.0.12

* Wed Jun 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.11-alt1
- initial build
