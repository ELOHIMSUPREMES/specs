# 4.1.4.2
%define with_forky yes

Name: LibreOffice4
Version: 4.1
%define urelease 4.2
%define uversion %version.%urelease
%define oopfx lo4
%define lodir %_libdir/%name
%define uname libreoffice4
%define conffile %_sysconfdir/sysconfig/%uname
Release: alt9
Summary: LibreOffice Productivity Suite
License: LGPL
Group: Office
URL: http://www.libreoffice.org

Requires: %name-integrated = %version-%release
Requires: %name-common = %version-%release
Requires: %name-mimetypes = %version-%release
Requires: %name-extensions = %version-%release

Provides: %name-full = %version-%release
Obsoletes: %name-full < %version-%release

%define with_lang ru de fr uk pt-BR es kk
#Requires: java xdg-utils hunspell-en hyphen-en mythes-en
Requires: gst-plugins-bad1.0 gst-plugins-good1.0 gst-plugins-nice1.0 gst-plugins-ugly1.0 gst-plugins-base1.0

Source:		libreoffice-%uversion.tar.xz
Source1:	libreoffice-dictionaries-%uversion.tar.xz
Source2:	libreoffice-help-%uversion.tar.xz
Source3:	libreoffice-translations-%uversion.tar.xz


Source10:	libreoffice-ext_sources.%uversion.tar
Source100:	forky.c

Patch1:	alt-001-MOZILLA_CERTIFICATE_FOLDER.patch
Patch2: libreoffice-4-alt-drop-gnome-open.patch
Patch3: alt-002-tmpdir.patch

# FC patches
Patch201: 0001-do-not-build-LibreOffice_Test.patch
Patch202: 0001-Resolves-rhbz-968892-force-render-full-grapheme-with.patch
Patch203: 0001-Related-rhbz-968892-discard-impossible-languages-for.patch
Patch204: 0002-Related-rhbz-968892-discard-impossible-languages-for.patch
Patch205: 0001-Resolves-fdo-48835-application-menu-for-LibreOffice.patch
Patch206: 0001-Make-charmap.cxx-compile-with-icu-4.4.patch
Patch207: 0001-select-sheet-menu-as-a-right-click-popup-to-the-prev.patch
Patch208: 0001-Resolves-rhbz-1013480-crash-in-EditLineList-operator.patch
Patch209: 0001-Resolves-rhbz-1015281-crash-on-clicking-custom-anima.patch
Patch210: 0001-Resolves-rhbz-996162-apparent-NULL-bullet-font.patch
Patch211: 0001-fdo-70201-sw-eliminate-no-extent-RSID-only-AUTOFMT-h.patch
Patch212: 0001-WaE-Wstrict-overflow-assuming-signed-overflow-does-n.patch
Patch213: 0001-Related-rhbz-1020712-wrong-default-font-shown-in-edi.patch
Patch214: 0001-Related-rhbz-919070-display-1-means-span-all-display.patch
Patch215: 0001-fdo-67725-unoidl-AggregatingCursor-must-wrap-modules.patch
Patch216: 0001-Resolves-rhbz-1021915-force-menubar-menus-to-be-up-d.patch
Patch217: 0001-fdo-70968-Incorrect-rendering-of-Devanagari-short-i-.patch
Patch218: 0001-resolved-fdo-56209-reviving-FilterFormulaParser.patch
Patch219: 0001-update-libmwaw-to-0.2.0.patch
Patch220: 0001-rhbz-1031989-Accept-pt-in-addition-to-deprecated-pt.patch
Patch221: 0001-Related-rhbz-1014990-valgrind-reports-uninitialized-.patch

# Long-term FC patches
Patch300: openoffice.org-2.0.2.rh188467.printingdefaults.patch
Patch301: openoffice.org-3.0.0.ooo88341.sc.verticalboxes.patch
Patch302: openoffice.org-3.1.0.ooo101274.opening-a-directory.patch

# Automatically added by buildreq on Wed Mar 06 2013
# optimized out: ant boost-devel boost-devel-headers boost-interprocess-devel boost-intrusive-devel bzlib-devel cppunit fontconfig fontconfig-devel fonts-ttf-java-1.6.0-sun glib2-devel gstreamer-devel icu-utils java java-devel jpackage-utils junit kde4libs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libcom_err-devel libcurl-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-xlib libgio-devel libgmp-devel libgpg-error libgst-plugins libkrb5-devel libncurses-devel libnspr-devel libpango-devel libpcre-devel libpng-devel libpoppler-devel libpq-devel libqt4-core libqt4-devel libqt4-gui libssl-devel libstdc++-devel libsystemd-daemon libtinfo-devel libunixODBC-devel libwayland-client libwayland-server libwpd9-devel libxml2-devel perl-Compress-Raw-Zlib pkg-config poppler-data python-base tzdata tzdata-java xerces-j2 xml-common xml-commons-jaxp-1.3-apis xml-utils xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel xsltproc xz zlib-devel
BuildRequires: ant-testutil cppunit-devel flex fonts-ttf-liberation gcc-c++ gperf gst-plugins1.0-devel imake junit4 kde4libs-devel libGConf-devel libcups-devel libdb4-devel libdbus-glib-devel libexpat-devel libgtk+2-devel libhunspell-devel libicu-devel libjpeg-devel libldap-devel liblpsolve-devel libmpfr-devel libmysqlclient-devel libmythes-devel libncursesw-devel libneon-devel libnss-devel liborcus-devel libpoppler-cpp-devel libreadline-devel libvigra-devel libwpg-devel libwps-devel libodfgen-devel libcdr-devel libmspub-devel libmwaw-devel libvisio-devel libcmis-devel libxslt-devel perl-Archive-Zip postgresql-devel unzip xorg-cf-files zenity zip

BuildRequires: libbluez-devel libhyphen-devel libclucene-core-devel libgtk+3-devel python3-devel liblcms2-devel libraptor-devel libredland-devel libsane-devel
BuildRequires: xulrunner-devel
BuildRequires: graphite2-devel
BuildRequires: libexttextcat-devel
BuildRequires: tomcat-servlet-3.0-api sac pentaho-libxml flute pentaho-reporting-flow-engine liblayout libloader libformula librepository libserializer libbase apache-commons-codec apache-commons-lang apache-commons-httpclient apache-commons-logging bsh rhino

# 4.1
BuildRequires: libharfbuzz-devel liblangtag-devel

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*

%description
LibreOffice is a productivity suite that is compatible with other major
office suites.

This package provides maximum possible installation of %name along winth
other office packages, except of language packs and GNOME/KDE bindings.

%package common
Summary: Basic installation of %name
Group: Office
AutoReqProv: yes, noshell, nopython
%description common
Common part of %name that does not interfere with other packages

%package standalone
Summary: Renamed binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %version-%release
Conflicts: %name-integrated
Requires: %name-common = %version-%release
%description standalone
Wrapper scripts, icons and desktop files for running renamed version of %name
as lo4write, lo4draw etc.

%package integrated
Summary: Binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %version-%release
Conflicts: %name-standalone
Requires: %name-common = %version-%release
%description integrated
Wrapper scripts, icons and desktop files for running %name

%package gnome
Summary: GNOME Extensions for %name
Group:  Office
Requires: %uname = %version-%release
Requires: %name-common = %version-%release
%description gnome
GNOME extensions for %name

%package kde4
Summary: KDE4 Extensions for %name
Group:  Office
Requires: %uname = %version-%release
Requires: %name-common = %version-%release
%description kde4
KDE4 extensions for %name

%package extensions
Summary: Additional extensions for %name
Group:  Office
Requires: %uname = %version-%release
AutoReqProv: yes, noshell, nopython
%description extensions
Additional extensions for %name.
One can choose either to install this package at once,
or to download and install (possibly newer) extensions manually.

%package mimetypes
Summary: Mimetype keys support for %name
Group: Office
BuildArch: noarch
%description mimetypes
%name is distributed along with some mimetype settings and files.
This package installs them.

# define macro for quick langpack description
%define langpack(l:n:) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %name \
Group:  Office \
Requires: %uname = %version-%release \
%description %{pkgname} \
Provides additional %{langname} translations and resources for %name. \
\
%files %{pkgname} -f %{lang}.lang \
%{nil}

%prep
%ifdef with_forky
echo Using forky
%else
echo Direct build
%endif
%setup -q -n libreoffice-%uversion -a10 -b1 -b2 -b3
%patch1 -p0
%patch2 -p1
%patch3 -p2

# FC (## -- unsuccsessful but seems meaningful)
%patch201 -p1 -b .do-not-build-LibreOffice_Test.patch
#patch202 -p1 -b .rhbz-968892-force-render-full-grapheme-with.patch
#patch203 -p1 -b .rhbz-968892-discard-impossible-languages-for.patch
#patch204 -p1 -b .rhbz-968892-discard-impossible-languages-for.patch
%patch205 -p1 -b .fdo-48835-application-menu-for-LibreOffice.patch
%patch206 -p1 -b .Make-charmap.cxx-compile-with-icu-4.4.patch
%patch207 -p1 -b .select-sheet-menu-as-a-right-click-popup-to-the-prev.patch
%patch208 -p1 -b .rhbz-1013480-crash-in-EditLineList-operator.patch
%patch209 -p1 -b .rhbz-1015281-crash-on-clicking-custom-anima.patch
#patch210 -p1 -b .rhbz-996162-apparent-NULL-bullet-font.patch
#patch211 -p1 -b .fdo-70201-sw-eliminate-no-extent-RSID-only-AUTOFMT-h.patch
#patch212 -p1 -b .WaE-Wstrict-overflow-assuming-signed-overflow-does-n.patch
#patch213 -p1 -b .rhbz-1020712-wrong-default-font-shown-in-edi.patch
%patch214 -p1 -b .rhbz-919070-display-1-means-span-all-display.patch
#patch215 -p1 -b .fdo-67725-unoidl-AggregatingCursor-must-wrap-modules.patch
%patch216 -p1 -b .rhbz-1021915-force-menubar-menus-to-be-up-d.patch
#patch217 -p1 -b .fdo-70968-Incorrect-rendering-of-Devanagari-short-i-.patch
#patch218 -p1 -b .resolved-fdo-56209-reviving-FilterFormulaParser.patch
#patch219 -p1 -b .update-libmwaw-to-0.2.0.patch
#patch220 -p1 -b .rhbz-1031989-Accept-pt-in-addition-to-deprecated-pt.patch
#patch221 -p1 -b .rhbz-1014990-valgrind-reports-uninitialized-.patch

%patch300 -p1
%patch301 -p1
%patch302 -p1

rm -fr %name-tnslations/git-hooks

install -D %SOURCE100 forky.c

# create shell wrappers
for n in office writer impress calc base draw math qstart; do
	oname=%{oopfx}$n
	case "$n" in 
		office) opt=""; oname=libreoffice%version;;
		qstart) opt="--quickstart --nologo --nodefault";;
		*) opt="--$n";;
	esac
	cat > $oname.sh <<@@@
#!/bin/sh
exec %lodir/program/soffice $opt "\$@"
@@@
done

# Now create a config file
grep -r getenv * | sed -n 's/.*getenv *( *"\([^"]*\).*/\1/p' | sort -u | egrep 'STAR_|SAL_|OOO_' > %name.config.ENV

sed -n '/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/p' < desktop/scripts/soffice.sh > libreoffice.config
test -n "libreoffice.config"
sed -i '/# STAR_PROFILE_LOCKING_DISABLED/i\
test -r %conffile && . %conffile ||:
/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/d' desktop/scripts/soffice.sh

%build
# XXX
#sed -i 's/MDDS_CPPFLAGS="-std=gnu++0x"/MDDS_CPPFLAGS=""/
#s/CXXFLAGS -std=gnu++0x/CXXFLAGS/
#' configure.in
# XXX
#sed -i 's/test \([$]enable_mergelibs\)/test "\1"/' configure.in

## --with-system-mozilla, --enable-ext-report-builder, --with-system-mysql, --enable-ext-mysql-connector
./autogen.sh \
        --with-vendor="ALT Linux Team" \
        --disable-gnome-vfs \
        --disable-odk \
        --disable-systray \
        --enable-dbus \
        --enable-evolution2 \
        --enable-gio \
        --with-alloc=system \
        --without-afms \
        --without-fonts \
        --without-myspell-dicts \
        --without-ppds \
        --with-system-libs \
        --without-system-mdds \
	\
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="en-US %with_lang" \
        --with-external-tar=`pwd`/ext_sources \
	\
	--with-parallelism \
	\
	--enable-kde4 \
	\
	--enable-hardlink-deliver \
	\
	--enable-ext-diagram \
	--enable-ext-google-docs \
	--enable-ext-nlpsolver \
	--enable-ext-numbertext \
	--enable-ext-typo \
	--enable-ext-validator \
	--enable-ext-watch-window \
	--enable-ext-wiki-publisher \
	--with-servlet-api-jar=/usr/share/java/tomcat-servlet-api.jar \
	--enable-ext-ct2n \
	--enable-ext-barcode \
  \
	--enable-release-build \
	--with-help \
  \
	--enable-gtk3 \
	--enable-gstreamer \
	--disable-gstreamer-0-10 \
	--disable-fetch-external

# Far TODO --with-branding
# --with-extra-buildid="Tinderbox: Win-x86@6, Branch:master, Date:2012-11-26_00.29.34"
# --with-build-version="Built by Jim"

# Make forky
gcc -g -DHAVE_CONFIG_H -shared -O3 -fomit-frame-pointer -fPIC forky.c -oforky.so -ldl

%make bootstrap

%ifdef with_forky
# TODO prefect forky_max tune
echo Using forky
export forky_divider=16
export forky_max_procs=`awk '/^Max processes/{print int(5*$3/'$forky_divider')}' < /proc/self/limits`
##export forky_max_vsz=`awk '/^CommitLimit/{print int(5*$2/'$forky_divider')}' < /proc/meminfo`
##export forky_max_rss=$(($forky_max_vsz/3))
export forky_max_rss=6000000
export forky_max_vsz=$((3*$forky_max_rss))
export forky_verbose=1
echo "max_procs $forky_max_procs / max_vsz $forky_max_vsz / max_rss $forky_max_rss" | tee $HOME/forky.log
export LD_PRELOAD=`pwd`/forky.so

%make || { tail -100 $HOME/forky.log; head -1 $HOME/forky.log; wc $HOME/forky.log; false; }
test -r $HOME/forky.log && echo "Fork() was `wc -l $HOME/forky.log` times delayed" || :
%else
%make
%endif

%install
%makeinstall DESTDIR=%buildroot INSTALLDIR=%lodir

# Pick up LOO-generated file lists
for l in %with_lang; do
	ll="`echo "$l" | tr '-' '_'`"
	cat %buildroot/gid_*_$ll | sort -u > $l.lang
done

# Create gnome plugin list
(
cd %buildroot
find .%lodir/program/gnome*
find .%lodir/program/*gconf*
find .%lodir/program/*gtk*.so
find .%lodir/share/registry/gnome.xcd
) | sed 's/^[.]//' > files.gnome

# Create kde plugin list
(
cd %buildroot
find .%lodir/program/*kde*
) | sed 's/^[.]//' > files.kde4

# Generate base filelist by removing files from  separated packages
{ cat %buildroot/gid_* | sort -u ; cat *.lang files.gnome files.kde4; } | sort | uniq -u | grep -v '~$' | grep -v '/share/extensions/.' > files.nolang

unset RPM_PYTHON

# Install renamed wrappers
for n in l*4*.sh; do install -m755 -D $n %buildroot%_bindir/${n%%.sh}; done
# Install wrappers
for n in lo4*.sh; do m="lo${n##lo4}"; install -m755 -D $n %buildroot%_bindir/${m%%.sh}; done

# Install renamed icons
for n in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	m=libreoffice%version-`basename "$n"`
	d=`dirname "$n"`
	install -D sysui/desktop/icons/$n %buildroot%_iconsdir/$d/$m
done
# install unrenamed icons
for n in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	d=`dirname "$n"`
	install -D sysui/desktop/icons/$n %buildroot%_iconsdir/$d/$n
done

# TODO icon-themes/

mkdir -p %buildroot%_desktopdir
for n in writer impress calc base draw math qstart; do
	ln -s %lodir/share/xdg/$n.desktop %buildroot%_desktopdir/libreoffice%version-$n.desktop
	ln -s %lodir/share/xdg/$n.desktop %buildroot%_desktopdir/$n.desktop
done

# TODO some other hack with .mime (?)
mkdir -p %buildroot%_datadir/mime-info %buildroot%_datadir/mimelnk/application %buildroot%_datadir/application-registry
install sysui/desktop/mimetypes/*.keys %buildroot%_datadir/mime-info/
install sysui/desktop/mimetypes/*.mime %buildroot%_datadir/mime-info/
install sysui/desktop/mimetypes/*.desktop %buildroot%_datadir/mimelnk/application/
install sysui/desktop/mimetypes/*.applications %buildroot%_datadir/application-registry/

# Config file
install -D libreoffice.config %buildroot%conffile

%files

%files common -f files.nolang
%exclude /gid_Module*
%_bindir/libreoffice%version
%config %conffile
%lodir/share/extensions/package.txt
%lodir/share/extensions/presentation-minimizer
%_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files standalone
%_bindir/lo4*
%exclude %_bindir/libreoffice%version
%_desktopdir/libreoffice%{version}-*
%exclude %_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files integrated
%_bindir/*
%exclude %_bindir/lo4*
%exclude %_bindir/libreoffice%version
%_desktopdir/*
%exclude %_desktopdir/libreoffice%{version}-*
%_iconsdir/*/*/mimetypes/*
%_iconsdir/*/*/apps/*
%exclude %_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files gnome -f files.gnome

%files kde4 -f files.kde4

%files extensions
%lodir/share/extensions/*
%exclude %lodir/share/extensions/package.txt
%exclude %lodir/share/extensions/presentation-minimizer

%files mimetypes
%_datadir/mime-info/*
%_datadir/mimelnk/application/*
%_datadir/application-registry/*

%langpack -l ru -n Russian
%langpack -l de -n German
%langpack -l fr -n French
%langpack -l uk -n Ukrainian
%langpack -l pt-BR -n Brazilian Portuguese
%langpack -l es -n Espanian
%langpack -l kk -n Kazakh

%changelog
* Tue Feb 04 2014 Fr. Br. George <george@altlinux.ru> 4.1-alt9
- Merge -full package into general one
- Buld with help (closes: #29735)
- Require gst1.0 plugins to install (closes: #29782)

* Thu Dec 26 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt8
- Build with --enable-release-build

* Thu Dec 19 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt7
- Version up to officially corporative stable 4.1.4.2
- Disable applied patches

* Mon Nov 25 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt6
- Version up to officially stable 4.1.3.2
- More accurate forky utilization

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt5
- Version up to 4.1.2.3

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt4
- rebuild against libharfbuzz-icu

* Wed Sep 04 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt3
- Version up to 4.1.1.2
- Refresh FC patchset
- Un-hardcode /tmp usage (Closes: 29267)

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1-alt2
- fixed gnome file list
- fixed kde file list
- drop use gnome-open in gnome-open-url.sh
- build with gstreamer-1.0
- build with system libraries (libodfgen,libcdr,libmspub,libmwaw,libvisio,libcmis,libexttextcat)
- build with system jar files
- changed configure options --with-system-* to --with-system-libs

* Tue Jul 30 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt1
- Version up to 4.1.0.4
- Renew FC patchset (previous ones are pushed to upstream)

*  Wed May 15 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt8
- Version up to 4.0.3.3
- Drop some RH patches accepted by upstream

* Wed Apr 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.0-alt7.1
- NMU: rebuilt with new poppler

* Mon Apr 22 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt7
- Closes: 28883
- Drop some internal libraries build

* Thu Apr 18 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt6
- Version up to 4.0.2.2
- Incoprporate useful RH patches

* Thu Mar 21 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt5
- Introduce Kazakh locale
- Fix common binary displacement

* Tue Mar 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt4
- Fix conflicts with LO3
- Introduce "full" package (without langpacks and GNOME/KDE stuff)

* Wed Mar 06 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt3
- Update to 4.0.2.1
- Introduce extra extensions
- Separate %name-standalone and %name-integrated packages
- Introduce %name-mimetype

* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt2
- Separate KDE4 plugins
- Apply Firefox certificates import patch

* Tue Feb 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt1
Initial test build

