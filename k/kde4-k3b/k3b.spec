
%define sover 6
%define libk3blib libk3blib%sover
%define libk3bdevice libk3bdevice%sover

%define req_std_burning cdrkit cdrdao dvd+rw-tools
%define req_std_kde kde4libs >= %{get_version kde4libs}
%define req_std_common alterator-control
%define req_multimedia sox-play libsox-fmt-pulseaudio transcode vcdimager >= 0.7 normalize lame flac mpc

%define req_mini %req_std_burning %req_std_kde %req_std_common
%define req_all %req_mini %req_multimedia

%define rname k3b
Name: kde4-%rname
Version: 2.0.3
Release: alt5

Group: Archiving/Cd burning
Summary: The CD Kreator (Complete set)
Summary(ru_RU.UTF-8): Программа записи CD (Полный набор)
URL: http://www.k3b.org/
License: GPLv2

Provides: k3b = %version-%release
Requires: %req_all
#Requires: %name-mini = %version-%release
Conflicts: k3b-mini < 1.0.5-alt7

Source0: %rname-%version.tar
# ALT
Patch101: k3b-1.92-alt-check-cdrecord-ver.patch
Patch102: k3b-2.0.2-alt-k3bsetup.patch
Patch103: k3b-2.0.3-libav10.patch
Patch104: alt-fix-build.patch

# Automatically added by buildreq on Wed Nov 12 2014 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libavcodec-devel libavutil-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libflac-devel libfreetype-devel libgpg-error libogg-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-svg libqt4-webkit libqt4-xml libsoprano-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs shared-mime-info xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4base-runtime-core libXxf86misc-devel libavdevice-devel libavformat-devel libdvdread-devel libflac++-devel libicu50 libkcddb4-devel liblame-devel libmad-devel libmpcdec-devel libmusicbrainz-devel libmusicbrainz3-devel libpostproc-devel libqt3-devel libsamplerate-devel libsndfile-devel libswscale-devel libtag-devel libvorbis-devel python-module-google qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++
BuildRequires: libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel
BuildRequires: libdvdread-devel libflac++-devel libkcddb4-devel liblame-devel libmad-devel libmpcdec-devel
BuildRequires: libmusicbrainz-devel libsamplerate-devel libsndfile-devel libtag-devel libvorbis-devel

%description
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains all requiremnts and libraries necessary for full 
program functionality.
%description -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет cодержит зависимости и библиотеки, необходимые для 
полнофункциональной работы программы.


%package mini
Summary: The CD Creator
Summary(ru_RU.UTF-8): Программа записи CD
License: GPL
Group: Archiving/Cd burning
Requires: %req_mini
%description mini
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording.
Install 'k3b' package to get all of the program's features.
%description mini -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков.
Для полнофункцмональной работы Вы можете установить пакет 'k3b'.


%package devel
Summary: The CD Kreator (Development package.)
Summary(ru_RU.UTF-8): Программа записи CD (Пакет разработчика.)
License: GPL
Group: Development/KDE and QT
%description devel
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains k3b development files and libraries.
%description devel -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет содержит файлы и библиотеки, необходимые разработчику 
модулей k3b.

%package -n %libk3blib
Summary: KDE 4 library
Group: System/Libraries
%description -n %libk3blib
KDE 4 library.

%package -n %libk3bdevice
Summary: KDE 4 library
Group: System/Libraries
%description -n %libk3bdevice
KDE 4 library.

%prep
%setup -q -n %rname-%version
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1

%build
%K4cmake \
    -DK3B_BUILD_K3BSETUP:BOOL=ON \
    -DK3B_ENABLE_HAL_SUPPORT=OFF
%K4make


%install
%K4install

%K4find_lang --with-kde %rname
%K4find_lang --append --output=%rname.lang libk3b
%K4find_lang --append --output=%rname.lang libk3bdevice
%K4find_lang --append --output=%rname.lang kio_videodvd


%files -f %rname.lang
%doc README FAQ PERMISSIONS ChangeLog
%_K4bindir/*
%_K4lib/*.so*
%_K4xdg_apps/%rname.desktop
%_K4apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%_K4apps/solid/actions/k3b_*.desktop
%_K4apps/%rname
%_K4xdg_mime/x-k3b.xml
%_K4srv/*.*
%_K4srv/ServiceMenus/*.desktop
%_K4srvtyp/%{rname}*
#%_K4snd/%{rname}*
%_K4iconsdir/hicolor/*/apps/*.*

%files -n %libk3blib
%_K4libdir/libk3blib.so.%sover
%_K4libdir/libk3blib.so.%sover.*

%files -n %libk3bdevice
%_K4libdir/libk3bdevice.so.%sover
%_K4libdir/libk3bdevice.so.%sover.*

%files devel
%_K4link/*.so
%_K4includedir/*.h

%changelog
* Fri May 13 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt5
- provide k3b

* Wed Nov 25 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt4
- update requires

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt3
- fix FTBFS

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt2
- rebuild with new libav

* Wed Nov 12 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt1
- new version

* Tue May 27 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt8
- built with new libav

* Tue Oct 01 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt7
- sync patches with Debian to fix compile with new libav

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt6
- fix requires

* Fri May 04 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt4.M60P.1
- build for M60P

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt5
- fix compile with libav

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt4
- fix build requires

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt3
- move to standart place

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt2
- disable hal support

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Fri Sep 10 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1.M51.1
- built for M51

* Fri Sep 10 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt2
- add fix against crash in settings

* Tue Aug 17 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt0.M51.1
- built for M51

* Tue Aug 17 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt2.M51.1
- built for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt3
- 2.0-RC4 (1.93.0)

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt1.M51.1
- built for M51

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt2
- fix crash when cdrecord and wodim not found; thanks wrar@alt (ALT#23619)

* Fri May 28 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.3.M51.1
- built for M51

* Thu May 27 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.4
- 2.0-RC3 (1.92.0)

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.2.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.3
- 2.0-RC2 (1.91.0)

* Sat Feb 27 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.1.M51.1
- built for M51

* Sat Feb 27 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.2
- allow to start alterator-control from k3b

* Sat Feb 27 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.0.M51.1
- built for M51

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.1
- 2.0-beta1 (1.70)

* Sat Dec 05 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.12.M51.1
- built for M51

* Fri Nov 27 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.13
- 1.69.0alpha4

* Mon Oct 19 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.12
- 1.68.0alpha3

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.11
- update to svn r1034264 (ALT #21099, #21623)

* Mon Sep 21 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.10
- rebuilt with new libdvdread

* Fri Sep 04 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.9
- fix cdrkit detection when hidden under symlink

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.8
- don't require cdrtools

* Tue Aug 25 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.7
- update to svn r1009369

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.5.M50.1
- built for M50

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.6
- update to svn r1004480

* Thu Jul 02 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.4.M50.1
- built for M50

* Thu Jul 02 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.5
- fix to write dvd images

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.3.M50.1
- build for M50

* Wed Jun 24 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.4
- fix to use growisofs for DVDs by default

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.3
- 1.66.0 alpha2

* Fri Apr 24 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.1.M50.1
- built for M50

* Thu Apr 23 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.2
- 1.65.0 alpha1

* Thu Apr 16 2009 Sergey V Turchin <zerg@altlinux.org> 1.95-alt0.0.M50.1
- built for M50

* Thu Apr 16 2009 Sergey V Turchin <zerg at altlinux dot org> 1.95-alt0.1
- svn r948770
