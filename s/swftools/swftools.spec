Name: swftools
Version: 0.9.2
Release: alt1

Summary: A collection of SWF manipulation and generation utilities
License: GPL
Group: Graphics

Url: http://www.swftools.org
Source: %url/%name-%version.tar.gz
Patch0: swftools-0.9.2_nopdf.patch
Patch1: swftools-0.9.2_general.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Jul 29 2009 (-bi)
BuildRequires: gcc-c++ libfreetype-devel libgif-devel libjpeg-devel liblame-devel

BuildPreReq: zlib-devel

Summary(ru_RU.KOI8-R): ����� �������� ��� ������ � ������� ������� SWF

%description
SWF Tools is a collection of SWF manipulation and generation utilities

Included are:

 PDF2SWF A PDF to SWF Converter. Generates one frame per page. Enables
 you to have fully formatted text, including tables, formulas etc.
 inside your Flash Movie. Uses the xpdf PDF parser from Derek B.
 Noonburg and the tt2pt1 font converter developed by the TTF2PT1 Project
 and its contributors.

 SWFCombine A tool for inserting SWFs into Wrapper SWFs. (Templates)
 E.g. for including the pdf2swf SWFs in some sort of Browsing-SWF.

 SWFStrings Scans SWFs for text data.

 SWFDump Prints out various informations about SWFs.

 JPEG2SWF Takes one or more JPEG pictures and generates a SWF slideshow.

 PNG2SWF Like JPEG2SWF, only for PNGs.

 WAV2SWF Converts WAV audio files to SWFs with MP3 Streams, using the
 L.A.M.E. MP3 encoder.

 AVI2SWF Converts AVI animation files to SWF. Still Alpha, but some
 examples can already be found at %url/examples.html.

 SWFExtract Allows to extract Movieclips, Sounds, Images etc. from SWF
 files.

 RFXSWF Library A fully featured library which can be used for
 standalone SWF generation. Includes support for Bitmaps, Buttons,
 Shapes, Text, Fonts, Sound etc.

 SWFTools has been reported to work on Solaris, Linux, FreeBSD and OSX.

%description -l ru_RU.KOI8-R
SWF Tools -- ��� ����� �������� ��� ������ � ������� ������� SWF.

� ����� ��������:

PDF2SWF --- ��������������� PDF � SWF. �������� �� ��������
1 �������� = 1 ����. ��������� ��������� � ���� SWF
����������������� �����, �������, ������� � �.�. ������������
������ PDF �� xpdf � ��������������� ������� tt2pt1.

SWFCombine --- ��� ���������� ��� ������� ������ SWF � Wrapper SWFs.
��������, ����� ��������� "�������������" SWF ����� pdf2swf.

SWFStrings ��������� ����� SWF �� ������� ���������� � ��� ������.

SWFDump ������� ��������� ���������� � ����� SWFs.

JPEG2SWF ������� �������� � ������� SWF �� ���������� ������ JPEG.

PNG2SWF ������ �� �� �����, ��� � JPEG2SWF, ������ � ������� PNG.

WAV2SWF ��������������� �������� ����� � ������� WAV � ����� SWF � MP3
��� ������ ����������� L.A.M.E.

AVI2SWF ��������������� ����� � ������� AVI � SWF. ��� ���������
��������� � ��������� ������ ����������, ������ ����������
������� ��� ����� ����� �� ������ %url/examples.html.

SWFExtract ��������� ��������� �����������, �����, ����������� �
������ ������ �� ������ SWF.

RFXSWF --- ��� ����������, ��� ������ ������� ����� ���������
����� � ������� SFX � �������������� �����������, ������,
�������������� ����������, ������, �������, ������ � �.�.

SWFTools ���� �������� � ���������� ��������� �� Solaris, Linux,
FreeBSD � MacOS X.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%configure --disable-static
%make_build

%install
%makeinstall
cd %buildroot%_datadir/%name/swfs
# FIXME: that was patched before; need to bother upstream some day:
# http://mail.nongnu.org/mailman/listinfo/swftools-common
[ -L default_loader.swf ] && ln -sf tessel_loader.swf default_loader.swf
[ -L default_viewer.swf ] && ln -sf simple_viewer.swf default_viewer.swf

%files
%_bindir/*
%_datadir/%name
%_man1dir/*
%doc AUTHORS ChangeLog doc/*

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- 0.9.2
- dropped a patch
- applied gentoo patches

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.1
- Fixed build

* Wed Jul 29 2009 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0 (closes: #20860)
  + fixed build with gcc-4.4
- buildreq
- dropped ancient unused patch from the package
- NB: I don't use this package, it needs proper maintainer

* Mon Sep 17 2007 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1
- 0.8.1
- picked up an orphan
- replaced makefile patch with the same overrides in %%install
- buildreq
- NB: built without avifile support as that's orphaned too;
  anyone who really cares can step forward to fix it
  (C++ templates knowledge seems required)

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.2-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Nov 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sat Feb 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.4-alt2
- rebuild with new t1lib (5.0.0)

* Mon Jul 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.4-alt1
- 0.4.4
- summary, description by avp.

* Thu Jan 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.3-alt1
- new version.

* Wed Sep 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt1
- 0.4.2 

* Tue Jun 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- First build for Sisyphus.
