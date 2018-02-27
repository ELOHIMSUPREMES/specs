%define svn svn5891

Name: handbrake
Version: 0.9.9
Release: alt1.%svn
Summary: Multithreaded Video Transcoder
Packager: Motsyo Gennadi <drool@altlinux.ru>
# #Source: http://prdownloads.sourceforge.net/handbrake/HandBrake-%version.tar.bz2
Source0: %name-%svn.tar.bz2

Source101: http://download.handbrake.fr/handbrake/contrib/a52dec-0.7.4.tar.gz
# #Source102: http://download.handbrake.fr/handbrake/contrib/faac-1.28.tar.gz
Source102: http://download.handbrake.fr/handbrake/contrib/fdk-aac-v0.1.1-6-gbae4553.tar.bz2
Source103: http://download.handbrake.fr/handbrake/contrib/faad2-2.7.tar.gz
Source104: http://download.handbrake.fr/handbrake/contrib/libav-v9.6.tar.bz2
Source105: http://download.handbrake.fr/handbrake/contrib/fontconfig-2.8.0.tar.gz
Source106: http://download.handbrake.fr/handbrake/contrib/freetype-2.4.7.tar.bz2
Source107: http://download.handbrake.fr/handbrake/contrib/lame-3.98.tar.gz
Source108: http://download.handbrake.fr/handbrake/contrib/libbluray-0.2.3.tar.bz2
Source109: http://download.handbrake.fr/handbrake/contrib/libdvdnav-svn1168.tar.gz
Source110: http://download.handbrake.fr/handbrake/contrib/libdvdread-svn1168.tar.gz
Source111: http://download.handbrake.fr/handbrake/contrib/libmkv-0.6.5-0-g82075ae.tar.gz
Source112: http://download.handbrake.fr/handbrake/contrib/libtool-2.4.2.tar.bz2
Source113: http://download.handbrake.fr/handbrake/contrib/libxml2-2.7.7.tar.gz
Source114: http://download.handbrake.fr/handbrake/contrib/m4-1.4.16.tar.bz2
Source115: http://download.handbrake.fr/handbrake/contrib/mp4v2-trunk-r355.tar.bz2
Source116: http://download.handbrake.fr/handbrake/contrib/mpeg2dec-0.5.1.tar.gz
Source117: http://download.handbrake.fr/handbrake/contrib/x264-r2377-1ca7bb9.tar.gz
Source118: http://download.handbrake.fr/handbrake/contrib/yasm-1.2.0.tar.gz

Source151: handbrake-ffmpeg_fix_missing_return_in_nonvoid_function.patch
Source152: handbrake-svn5042-fix_libbluray_implicit_declaration_of_function_strdup.patch

Patch200: handbrake-svn5891-fdk_aac-autoreconf.patch

Url: http://handbrake.fr/
Group: Video
License: GPLv2+

# Automatically added by buildreq on Sun Nov 04 2012 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel gstreamer-devel gtk-update-icon-cache libX11-devel libatk-devel libcairo-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins libgtk+2-devel libncurses-devel libogg-devel libpango-devel libsoup-devel libstdc++-devel libtinfo-devel libxml2-devel perl-XML-Parser pkg-config python-base python-modules python-modules-compiler python-modules-encodings shared-mime-info xorg-xproto-devel
BuildRequires: bzlib-devel gcc-c++ gst-plugins-devel intltool libalsa-devel libass-devel libdbus-glib-devel libfribidi-devel libgudev-devel libnotify-devel libsamplerate-devel libtheora-devel libvorbis-devel libwebkitgtk2-devel subversion wget zlib-devel

%description
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

%package cli
Summary: Multithreaded Video Transcoder
Group: Video

%description cli
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a command-line interface for Handbrake.

%package gtk
Summary: Multithreaded Video Transcoder
Group: Video
Requires: %name-cli = %version-%release

%description gtk
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a GTK+ graphical user interface for Handbrake.

%prep
# #%setup -n HandBrake-%version
%setup -n %name-svn
%patch200 -p1

# Copy 3rd party dependencies into expected locations:
%__mkdir download
for f in \
%{S:101} %{S:102} %{S:103} %{S:104} %{S:105} %{S:106} \
%{S:107} %{S:108} %{S:109} %{S:110} %{S:111} %{S:112} \
%{S:113} %{S:114} %{S:115} %{S:116} %{S:117} %{S:118} \
; do
     %__ln_s "$f" download/
done

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

# #%__cp "%{S:151}" contrib/ffmpeg/A99-fix-missing-return-in-nonvoid-function.patch
%__cp "%{S:152}" contrib/libbluray/A99-fix_libbluray_implicit_declaration_of_function_strdup.patch

./configure --prefix="%buildroot%prefix" --force
pushd build
%make_build
popd build

%install
pushd build
%__make install
popd #build

%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"

%__rm "%buildroot%_datadir/icons"/*/*.cache

%find_lang --with-gnome ghb

%files cli
%doc AUTHORS COPYING CREDITS NEWS THANKS
%_bindir/HandBrakeCLI

%files gtk -f ghb.lang
%doc AUTHORS COPYING CREDITS NEWS THANKS
%_bindir/HandBrakeGUI
%_bindir/ghb
%_desktopdir/ghb.desktop
%_datadir/icons/*/*/apps/hb-icon.png

%changelog
* Sat Nov 09 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5891
- build svn5891

* Thu Sep 19 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5787
- build svn5787

* Wed Sep 04 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5767
- build svn5767

* Mon Sep 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5764
- build svn5764

* Tue Aug 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5693
- build svn5693

* Tue Aug 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5690
- build svn5690

* Fri Jun 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5577
- build svn5577

* Sun May 19 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5478
- 0.9.9 released
- build svn5433

* Wed May 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5433
- build svn5433

* Mon Apr 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5369
- build svn5369

* Thu Mar 07 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5307
- build svn5307

* Mon Feb 11 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5245
- build svn5245

* Wed Jan 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5127
- build svn5127

* Wed Nov 28 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5086
- build svn5086

* Fri Nov 16 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5065
- build svn5065
- cleanup BuildRequres

* Sat Nov 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5042
- build svn5042
- cleanup spec
- cleanup BuildRequres

* Wed Oct 17 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt0.svn5017
- build svn5017

* Wed Oct 10 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt0.svn5010
- build svn5010

* Tue Jun 05 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.3
- fir build for Sisyphus (thank azol@ for help)

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.2
- test fix for sisyphus

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.1
- test fix for sisyphus

* Fri Jun 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1
- initial build for ALT Linux from OpenSUSE package
