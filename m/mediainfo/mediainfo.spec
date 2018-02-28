Name: mediainfo
Version: 0.7.95
Release: alt1

Group: File tools
Summary: MediaInfo supplies information about a video or audio file
License: LGPL
Url: http://mediainfo.sourceforge.net

Source: https://mediaarea.net/download/source/%name/%version/%{name}_%{version}.tar.xz

BuildRequires(pre): rpm-macros-kde-common-devel

BuildRequires: gcc-c++
BuildRequires: dos2unix
BuildRequires: zlib-devel
BuildRequires: libpango-devel
BuildRequires: libzen-devel >= 0.4.35
BuildRequires: libmediainfo-devel >= %version
BuildRequires: libwxGTK-devel
BuildRequires: sgml-common

%package gui
Group: File tools
Summary: MediaInfo supplies information about a video or audio file

%package gui-KDE3
Group: File tools
Summary: KDE3 related MediaInfo files
BuildArch: noarch
Requires: %name-gui = %version-%release
Requires: kdebase-konqueror < 4.0

%package gui-KDE4
Group: File tools
Summary: KDE4 related MediaInfo files
BuildArch: noarch
Requires: %name-gui = %version-%release
Requires: kde4libs

%description
MediaInfo supplies technical and tag information about a video or audio file

What information can I get from MediaInfo?
General: title, author, director, album, track number, date, duration...
Video: codec, aspect, fps, bitrate...
Audio: codec, sample rate, channels, language, bitrate...
Text: language of subtitle
Chapters: number of chapters, list of chapters

What format (container) does MediaInfo support?
Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
       MPEG-4, DVD (VOB)...
(Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF...
Subtitles: SRT, SSA, ASS, SAMI...

This package includes the command line interface

%description gui
MediaInfo supplies technical and tag information about a video or audio file

What information can I get from MediaInfo?
General: title, author, director, album, track number, date, duration...
Video: codec, aspect, fps, bitrate...
Audio: codec, sample rate, channels, language, bitrate...
Text: language of subtitle
Chapters: number of chapters, list of chapters

What format (container) does MediaInfo support?
Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
       MPEG-4, DVD (VOB)...
(Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF...
Subtitles: SRT, SSA, ASS, SAMI...

This package contains the graphical user interface.

To combine with KDE install KDE-related package

%description gui-KDE3
This package contains KDE3 related MediaInfo files for konqueror

%description gui-KDE4
This package contains KDE4 related MediaInfo files for konqueror

%prep
%setup -q -T -b 0 -n MediaInfo

%build
pushd Project/GNU/CLI
%autoreconf
%configure --disable-staticlibs --with-dll
%make
popd
pushd Project/GNU/GUI
%autoreconf
%configure --disable-staticlibs --with-dll
%make
popd

%install
pushd Project/GNU/CLI
%makeinstall_std
popd
pushd Project/GNU/GUI
%makeinstall_std
popd
# Add here commands to install the package
cp Release/ReadMe_CLI_Linux.txt .
cp Release/ReadMe_GUI_Linux.txt .

install -m 644 Source/Resource/Image/MediaInfo.png %buildroot%_pixmapsdir/mediainfo.png
install -dm 755 %buildroot%_liconsdir
install -m 644 Source/Resource/Image/MediaInfo.png %buildroot%_liconsdir/mediainfo.png

install -dm 755 %buildroot%_K3apps/konqueror/servicemenus/
grep -v '^Encoding=' Project/GNU/GUI/mediainfo-gui.kde3.desktop >%buildroot%_K3apps/konqueror/servicemenus/mediainfo-gui.desktop
install -dm 755 %buildroot%_K4srv/ServiceMenus/
grep -v '^Encoding=' Project/GNU/GUI/mediainfo-gui.kde4.desktop >%buildroot%_K4srv/ServiceMenus/mediainfo-gui.desktop

%files
%doc ReadMe_CLI_Linux.txt
%_bindir/%name

%files gui
%doc ReadMe_GUI_Linux.txt
%_bindir/%name-gui
%_desktopdir/%name-gui.desktop
%_datadir/appdata/%name-gui.appdata.xml
%_datadir/apps/konqueror/servicemenus/%name-gui.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_pixmapsdir/%name.xpm
%_pixmapsdir/%name.png

%files gui-KDE3
%_K3apps/konqueror/servicemenus/%name-gui.desktop

%files gui-KDE4
%_K4srv/ServiceMenus/%name-gui.desktop

%changelog
* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.95-alt1
- 0.7.95

* Tue Apr 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.94-alt1
- 0.7.94

* Tue Aug 25 2015 Motsyo Gennadi <drool@altlinux.ru> 0.7.76-alt1
- 0.7.76

* Wed Oct 01 2014 Motsyo Gennadi <drool@altlinux.ru> 0.7.70-alt1
- 0.7.70

* Sat Feb 18 2012 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.53-alt1
- New version

* Sun Dec 04 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt2
- Fix build spec

* Sun Dec 04 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt1
- New version

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.47-alt1
- New version

* Mon Mar 07 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt2
- Update spec with noarch and K3/K4 macros

* Sun Mar 06 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt1
- New version

* Mon Feb 28 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.41-alt1
- New version

* Mon Oct 18 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.35-alt1
- New version

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt1
- New version

* Wed Feb 17 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.27-alt2
- Rebuild with libwxGTK
- Fix .destop files due to repocop info

* Wed Feb 10 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.27-alt1
- New version

* Mon Nov 23 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.25-alt1
- New version
- create KDE3 and KDE4 subpackages from mediainfo-gui

* Thu Nov 12 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.24-alt1
- initial build
