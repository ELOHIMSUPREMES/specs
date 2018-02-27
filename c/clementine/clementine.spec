%def_with vkontakte

Name: clementine
Version: 1.2.3
Release: alt3
Summary: A music player and library organiser

Group: Sound
License: %lgpl3only
Url: http://code.google.com/p/clementine-player
Packager: Pavel Maleev <rolland@altlinux.org>

Source0: %name-%version.tar.gz
Source1: clementine_48.png
Patch: %name-1.2.3-alt-desktop.patch
Patch1: %name-1.2.0-chromaprint-avcodec.patch
Patch2: clementine-0.6-alt-install-icons.patch
Patch3: %name-1.2.2-alt-unistd.patch
%if_with vkontakte
# Vkontakte support. Patches are taken from Rosa
# https://abf.io/current/clementine.git
Source2: %name-vk-files.tar.bz2
Patch4: %name-1.2.2-rosa-vkontakte-advanced.patch
Patch5: %name-1.2.0-rosa-vkontakte-tags.patch
Patch6: %name-1.2.0-rosa-ru-vkontakte.patch
%endif

BuildRequires(pre): rpm-build-licenses
BuildRequires: boost-devel-headers cmake gcc-c++ gstreamer-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libgio-devel libglew-devel libgpod-devel liblastfm-devel libmtp-devel libqt4-opengl libqt4-sql libqt4-webkit libqt4-xmlpatterns libtag-devel libxkbfile-devel python-module-sip qt4-designer subversion

BuildRequires: kde-common-devel libqt4-sql-sqlite gst-plugins-gio libqca2-devel protobuf-compiler
# Enable Google Drive support
BuildRequires: libgoogle-sparsehash
%if_with vkontakte
# Enable VK support
BuildRequires: libvreen-devel
%endif
BuildPreReq: libfftw3-devel libavcodec-devel libavformat-devel libpcre-devel
BuildPreReq: libprotobuf-devel qjson-devel gst-plugins-devel libcdio-devel

# Clementine crashes without it
Requires: gst-plugins-base

%description
Clementine is a modern music player and library organiser.
It is largely a port of Amarok 1.4, with some features rewritten to take
advantage of Qt4.

%add_python_req_skip clementine

%prep
%setup
%patch -p2
%patch1 -p2
%patch2 -p1
%patch3 -p2

%if_with vkontakte
tar -xf %{SOURCE2}
%patch4 -p1 -b .vkontakte~
%patch5 -p1 -b .vkontakte~
%patch6 -p1 -b .vkontakte~
%endif

%build
%K4build -DSTATIC_SQLITE=on -DBUILD_WERROR=off

%install
%K4install

%files
%doc Changelog
%_bindir/clementine
%_bindir/clementine-tagreader
%_desktopdir/clementine.desktop
%_iconsdir/hicolor/*/apps/application-x-clementine.*
%_datadir/kde4/services/*
%_datadir/clementine

%changelog
* Thu Feb 12 2015 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt3
- add gst-plugins-base to requires - clementine crashes without it

* Mon Jul 7 2014 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt2
- add vkontakte support (closes: #29522)

* Mon May 19 2014 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt1
- Version 1.2.3

* Mon Feb 24 2014 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- Version 1.2.2

* Fri Dec 13 2013 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Wed Oct 17 2013 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Wed Oct 16 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1-alt4
- Fixed build with new libav.

* Wed Apr 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt3
- rebuilt against libimobiledevice.so.4

* Sat Jan 12 2013 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt2
- Enable Google Drive support

* Fri Dec 28 2012 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2.qa2
- Removed -Werror compiler flag
- Fixed build with new glib2

* Mon May 30 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt2.qa1
- Rebuild for GNOME 3

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt2
- Fix patch name

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- New version 0.7.1

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1.svn2877.qa1
- Fix build in Sisyphus (remove nvidia_glx requires)

* Sat Feb 26 2011 Pavel Maleev <rolland@altlinux.org> 0.6-alt1.svn2877
- new version (svn2877)

* Sun Nov 21 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2253
- new version (svn2253)

* Mon Oct 25 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2205
- new version (svn2205)

* Sun Oct 3 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2086
- new version (svn2086)

* Tue Sep 21 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2034
- new version (svn2034)

* Mon Aug 9 2010 Pavel Maleev <rolland@altlinux.org> 0.4-alt1.svn1664
- new version (svn1664)

* Thu Jul 15 2010 Pavel Maleev <rolland@altlinux.org> 0.4-alt1.svn1480
- new version (svn1480)

* Tue Jun 29 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn1386
- new version (svn1093)

* Wed Jun 09 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn1093
- new version (svn1093)

* Sat May 22 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn952
- new version (svn952)

* Tue Apr 13 2010 Pavel Maleev <rolland@altlinux.org> 0.2-alt1.svn673
- new version (svn673)

* Tue Apr 06 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1.svn586
- new version (svn586)

* Wed Mar 24 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1.svn479
- new version (svn479)

* Sun Mar 14 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1.svn370
- new version (svn370)
- fix previous changelog entry (changelog author)

* Sun Mar 01 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1.svn285
- initial build for ALT Linux Sisyphus (svn285)
