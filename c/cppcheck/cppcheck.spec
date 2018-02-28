# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: cppcheck
Version: 1.69
Release: alt1

Summary: A tool for static C/C++ code analysis

License: GPLv3
Group: Development/Tools
Url: http://sourceforge.net/projects/cppcheck/

Source: %name-%version.tar.bz2
Patch1: cppcheck-makefile-docbook_xsl.patch
Patch2: cppcheck-1.67-norebuild.patch
Patch3: cppcheck-1.67-appPath.patch

# Automatically added by buildreq on Wed Nov 26 2014
# optimized out: docbook-dtds fontconfig libcloog-isl4 libgpg-error libqt4-core libqt4-gui libstdc++-devel phonon-devel pkg-config python-base python-modules xml-common
BuildRequires: ImageMagick-tools docbook-style-xsl gcc-c++ gdb libpcre-devel libqt4-devel xsltproc

%description
Static analysis of C/C++ code. Checks for: memory leaks, mismatching
allocation-deallocation, buffer overrun, and many more. The goal is
0%% false positives.

%package gui
Summary: Qt version of %name, %summary
Group: Development/Tools
Requires: %name = %version-%release
%description gui
%summary

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p1

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application

Exec=%name-gui
Icon=%name

Name=CppCheck
Comment=Static analysis of C/C++ code
GenericName=Code analyzer

Categories=Development;Qt;
@@@

for i in 16 24 32 48 64; do
	convert gui/icon.png ${i}.png
done

%build
%define dirs SRCDIR=build CFGDIR=%_datadir/%name/cfg HAVE_RULES=yes INCLUDEPATH="%_includedir/pcre"
%make_build %dirs CPPFLAGS="$(pkg-config --cflags libpcre)"
cd gui
%qmake_qt4 %dirs
lrelease-qt4 gui.pro
%make_build %dirs
cd ..

%make_build man %dirs
%make_build testrunner

# Generate html documentation
for N in man/*.docbook; do
  xsltproc -o ${N%%.docbook}.html \
	/usr/share/xml/docbook/xsl-stylesheets/xhtml/docbook.xsl $N
done

%check
%make_build check

%install
%makeinstall_std %dirs

install -D gui/%name-gui %buildroot%_bindir/%name-gui

install -pD -m 644 %name.1 %buildroot%_man1dir/%name.1

mkdir -p "%buildroot%_datadir/%name/lang"
for N in gui/*.qm; do install -D $N %buildroot%_datadir/%name/lang/`basename $N`; done

install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for i in 64 48 32 24 16; do
	install -D $i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done
install -D gui/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%doc readme.txt man/*.html
%_bindir/%name
%_bindir/%name-htmlreport
%_man1dir/%name.1.*
%_datadir/%name/cfg

%files gui
%doc gui/help/manual.html
%_bindir/%name-gui
%exclude %_datadir/%name/cfg
%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 1.69-alt1
- Autobuild version bump to 1.69

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 1.68-alt1
- Autobuild version bump to 1.68

* Tue Nov 25 2014 Fr. Br. George <george@altlinux.ru> 1.67-alt1
- Autobuild version bump to 1.67
- Package config file
- Build Qt GUI and package separately

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.65-alt1
- Version 1.65

* Mon Nov 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.62-alt1
- Version 1.62

* Tue Jun 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.60.1-alt1
- Version 1.60.1

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.58-alt1
- Version 1.58

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.55-alt1
- Version 1.55

* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 1.50-alt1
- Updated to 1.50

* Fri May 06 2011 Slava Semushin <php-coder@altlinux.ru> 1.48-alt1
- Updated to 1.48
- I not maintain this package any more

* Thu Feb 10 2011 Slava Semushin <php-coder@altlinux.ru> 1.47-alt1
- Updated to 1.47

* Wed Dec 29 2010 Slava Semushin <php-coder@altlinux.ru> 1.46.1-alt1
- Updated to 1.46.1

* Sat Oct 30 2010 Slava Semushin <php-coder@altlinux.ru> 1.45-alt1
- Updated to 1.45

* Fri Jul 16 2010 Slava Semushin <php-coder@altlinux.ru> 1.44-alt1
- Updated to 1.44

* Mon May 10 2010 Slava Semushin <php-coder@altlinux.ru> 1.43-alt1
- Updated to 1.43

* Thu Mar 11 2010 Slava Semushin <php-coder@altlinux.ru> 1.42-alt1
- Updated to 1.42

* Sun Jan 17 2010 Slava Semushin <php-coder@altlinux.ru> 1.40-alt1
- Updated to 1.40

* Sat Dec 12 2009 Slava Semushin <php-coder@altlinux.ru> 1.39-alt1
- Updated to 1.39
- Include manual.html to documentation

* Sat Oct 31 2009 Slava Semushin <php-coder@altlinux.ru> 1.38-alt1
- Updated to 1.38
- Moved "make test" to %%check section

* Wed Sep 23 2009 Slava Semushin <php-coder@altlinux.ru> 1.37-alt1
- Updated to 1.37

* Sun Aug 16 2009 Slava Semushin <php-coder@altlinux.ru> 1.35-alt1
- Updated to 1.35

* Sun Jul 12 2009 Slava Semushin <php-coder@altlinux.ru> 1.34-alt1
- Updated to 1.34

* Wed Jun 10 2009 Slava Semushin <php-coder@altlinux.ru> 1.33-alt1
- Updated to 1.33
- Run test suite during build

* Mon May 11 2009 Slava Semushin <php-coder@altlinux.ru> 1.32-alt1
- Updated to 1.32

* Tue May 05 2009 Slava Semushin <php-coder@altlinux.ru> 1.31-alt1
- Initial build for ALT Linux

