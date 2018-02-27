# -*- rpm-spec -*-
# $Id: avr-libc,v 1.33 2005/06/03 10:59:46 grigory Exp $

%define cross_arch avr

Summary: AVR libc
Name: avr-libc
Version: 1.8.0
Release: alt5
Serial: 1
License: GPL, LGPL, BSD, Public Domain
Group: Development/Other
URL: http://savannah.gnu.org/projects/avr-libc

Source0: http://savannah.gnu.org/download/avr-libc/avr-libc-%version.tar.gz
Source1: avr8-headers-6.2.0.142.zip
Patch0: 1.8.0.fix.patch

# Automatically added by buildreq on Fri Feb 01 2013
# optimized out: avr-binutils avr-gcc fontconfig fonts-ttf-gnu-freefont-mono fonts-ttf-gnu-freefont-sans fonts-ttf-gnu-freefont-serif fonts-type1-urw ghostscript-classic ghostscript-common netpbm ruby texlive-extra-utils
BuildRequires: azenis-fonts-ttf cups-filters doxygen ruby-stdlibs transfig
BuildRequires: fonts-otf-oldstandard fonts-otf-stix fonts-ttf-armenian fonts-ttf-baekmuk-batang fonts-ttf-baekmuk-dotum
BuildRequires: fonts-ttf-baekmuk-gulim fonts-ttf-baekmuk-hline fonts-ttf-bengali fonts-ttf-chinese-big5
BuildRequires: fonts-ttf-chinese-gb2312 fonts-ttf-church fonts-ttf-dejavu fonts-ttf-dejavu-lgc fonts-ttf-devanagari
BuildRequires: fonts-ttf-freefont fonts-ttf-georgian fonts-ttf-gost fonts-ttf-gw fonts-ttf-java-1.6.0-sun fonts-ttf-junicode
BuildRequires: fonts-ttf-kannada fonts-ttf-latex-xft fonts-ttf-liberation fonts-ttf-malayalam fonts-ttf-ms fonts-ttf-oldstandard
BuildRequires: fonts-ttf-reduce fonts-ttf-sazanami-gothic fonts-ttf-sazanami-mincho fonts-ttf-sil-gentium fonts-ttf-syriac
BuildRequires: fonts-ttf-tamil fonts-ttf-tempora fonts-ttf-urdu fonts-ttf-vera fonts-ttf-xorg fonts-ttf-znamen
BuildRequires: fonts-type1-cm-super-pfb fonts-type1-dmtr40in fonts-type1-phonetic fonts-type1-xorg unzip

BuildRequires: avr-binutils >= 2:2.23.1-alt1
BuildRequires: avr-gcc >= 4.7.2-alt3
BuildRequires: avr-gcc-c++ >= 4.7.2-alt3

Requires: avr-binutils >= 2:2.23.1-alt1
Requires: avr-gcc >= 4.7.2-alt3
Requires: avr-gcc-c++ >= 4.7.2-alt3

%define libavrdir %_libdir/%cross_arch
%define includeavrdir %_includedir/%cross_arch

%description
Avr-libc is a C library for developing applications for Atmel AVR microcontrollers.

%package doc
Summary: Documentation for avr-libc
Group: Development/Other
BuildArch: noarch

%description doc
Documentation for avr-libc in html, postscript and pdf formats.


%prep
%setup -q -n libc/avr-libc
# patch0 -p1
unzip %SOURCE1
for i in avr/io*.h; do
	mv --verbose --force $i include/avr/
done

%build
./bootstrap
./configure \
	--host=avr \
	--build=$(./config.guess) \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--includedir=%includeavrdir \
	--mandir=%_mandir \
	--infodir=%_infodir \
	--enable-doc --disable-versioned-doc --disable-pdf-doc
#	--exec-prefix=%libavrdir \

%make_build

%install
%make_build \
	prefix=%buildroot%_prefix \
	exec_prefix=%buildroot%_libdir \
	mandir=%buildroot%_mandir \
	infodir=%buildroot%_infodir \
	libdir=%buildroot%_libdir \
	includedir=%buildroot%includeavrdir \
	install

# Move lib and include files from /usr/avr -> /usr/lib/avr
%__mkdir_p %buildroot%_libdir
%__mv %buildroot%_prefix/avr %buildroot%_libdir/

%files
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README
%doc doc/CHANGES.old doc/ChangeLog doc/INSTALL doc/TODO
%libavrdir/include/*
%libavrdir/lib/*

%files doc
%_bindir/*
%_datadir/doc/avr-libc/*

%changelog
* Fri Mar 14 2014 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt5
- update Atmel headers to last version

* Wed Oct 16 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt4
- must be rebuilded with new avr-gcc

* Mon Oct 14 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt3
- last version from Atmel
- build with new avr-binutils and avr-gcc

* Fri Feb 01 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt2
- rebuild with new avr-binutils and avr-gcc

* Fri Feb 01 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt1
- new version released

* Thu Mar 17 2011 Grigory Milev <week@altlinux.ru> 1:1.7.1-alt2
- rebuilded with avr-gcc-4.5.1-alt3

* Thu Mar 10 2011 Grigory Milev <week@altlinux.ru> 1:1.7.1-alt1
- new version released

* Thu Jan 13 2011 Grigory Milev <week@altlinux.ru> 1:1.7.0-alt2
- rebuild by new binutils and gcc

* Wed Nov 03 2010 Grigory Milev <week@altlinux.ru> 1:1.7.0-alt1
- new version released

* Sun Nov 29 2009 Grigory Milev <week@altlinux.ru> 1:1.6.7-alt1
- new version released
- remove .pdf from manual package

* Tue Jun 23 2009 Grigory Milev <week@altlinux.ru> 1:1.6.6-alt1
- new version released (see ChangeLog inside package)

* Mon Dec 29 2008 Grigory Milev <week@altlinux.ru> 1:1.6.4-alt1
- new version released

* Mon May 19 2008 Grigory Milev <week@altlinux.ru> 1:1.6.2-alt1
- new version released
- fixed build requires (LaTex utf8.def)

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 1:1.6.1-alt1
- new version released

* Wed Oct  4 2006 Grigory Milev <week@altlinux.ru> 1:1.4.4-alt1
- new version released
- fixating spec
- move avr-man to doc package
- clean up spec

* Mon Sep 19 2005 Grigory Milev <week@altlinux.ru> 1:1.2.5-alt1
- new version released

* Fri Jun 03 2005 Grigory Milev <week@altlinux.ru> 1:1.2.3-alt1
- new version released
- do not compile documents, get it from precompiled (due some bugs)

* Fri Jan 21 2005 Grigory Milev <week@altlinux.ru> 1:1.2.0-alt1
- new version released

* Fri May 28 2004 Grigory Milev <week@altlinux.ru> 1:1.0.4-alt1
- new version released

* Tue Apr 13 2004 Grigory Milev <week@altlinux.ru> 1:1.0.3-alt1
- new version released

* Wed Oct  8 2003 Grigory Milev <week@altlinux.ru> 1:1.0-alt1
- first release
- build user-manual

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 20030805-alt1
- new cvs snapshot released

* Thu Jun 19 2003 Grigory Milev <week@altlinux.ru> 20030512-alt1
- new cvs snapshot released

* Tue Apr 22 2003 Grigory Milev <week@altlinux.ru> 20030414-alt1
- new snapshot version

* Mon Feb 10 2003 Grigory Milev <week@altlinux.ru> 20030203-alt2
- new cvs version (snapshot)

* Tue Nov  5 2002 Grigory Milev <week@altlinux.ru> 20021028-alt1.cvs
- new version (snapshot)

* Fri Oct 25 2002 Grigory Milev <week@altlinux.ru> 20020203-alt1
- Initial build for ALT Linux

* Fri May 03 2002 Theodore Roth <troth@verinet.com>
- Added patch to fix timer.h for mega128.

* Mon Apr 29 2002 Theodore Roth <troth@verinet.com>
- Added patch to fix headers.
- Fix strncasecmp_P macro in pgmspace.h.

* Wed Mar 27 2002 Theodore Roth <troth@verinet.com>
- Updated avr-gcc dependency to 3.0.4-2.
- Fixed up %files section to work with rh-7.1.

* Mon Mar 17 2002 Theodore Roth <troth@verinet.com>
- Initial spec file.


