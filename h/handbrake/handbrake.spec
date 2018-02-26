%define svn svn5010

Name: handbrake
Version: 0.9.9
Release: alt0.%svn
Summary: Multithreaded Video Transcoder
Packager: Motsyo Gennadi <drool@altlinux.ru>
# #Source: http://prdownloads.sourceforge.net/handbrake/HandBrake-%version.tar.bz2
Source0: %name-%version-%svn.tar.bz2

Source101: http://download.handbrake.fr/handbrake/contrib/a52dec-0.7.4.tar.gz
Source102: http://download.handbrake.fr/handbrake/contrib/autoconf-2.69.tar.bz2
Source103: http://download.handbrake.fr/handbrake/contrib/automake-1.12.3.tar.bz2
Source104: http://download.handbrake.fr/handbrake/contrib/faac-1.28.tar.gz
Source105: http://download.handbrake.fr/handbrake/contrib/faad2-2.7.tar.gz
Source106: http://download.handbrake.fr/handbrake/contrib/libav-v0.8-2551-gc83f44d.tar.bz2
Source107: http://download.handbrake.fr/handbrake/contrib/fontconfig-2.8.0.tar.gz
Source108: http://download.handbrake.fr/handbrake/contrib/freetype-2.4.7.tar.bz2
Source109: http://download.handbrake.fr/handbrake/contrib/fribidi-0.19.2.tar.gz
Source110: http://download.handbrake.fr/handbrake/contrib/lame-3.98.tar.gz
Source111: http://download.handbrake.fr/handbrake/contrib/libass-0.10.0-1.tar.gz
Source112: http://download.handbrake.fr/handbrake/contrib/libbluray-0.0.1-pre-213-ga869da8.tar.gz
Source113: http://download.handbrake.fr/handbrake/contrib/libdvdnav-svn1168.tar.gz
Source114: http://download.handbrake.fr/handbrake/contrib/libdvdread-svn1168.tar.gz
Source115: http://download.handbrake.fr/handbrake/contrib/libmkv-0.6.5-0-g82075ae.tar.gz
Source116: http://download.handbrake.fr/handbrake/contrib/libogg-1.3.0.tar.gz
Source117: http://download.handbrake.fr/handbrake/contrib/libsamplerate-0.1.4.tar.gz
Source118: http://download.handbrake.fr/handbrake/contrib/libtheora-1.1.0.tar.bz2
Source119: http://download.handbrake.fr/handbrake/contrib/libtool-2.4.2.tar.bz2
Source120: http://download.handbrake.fr/handbrake/contrib/libvorbis-aotuv_b6.03.tar.bz2
Source121: http://download.handbrake.fr/handbrake/contrib/libxml2-2.7.7.tar.gz
Source122: http://download.handbrake.fr/handbrake/contrib/m4-1.4.16.tar.bz2
Source123: http://download.handbrake.fr/handbrake/contrib/mp4v2-trunk-r355.tar.bz2
Source124: http://download.handbrake.fr/handbrake/contrib/mpeg2dec-0.5.1.tar.gz
Source125: http://download.handbrake.fr/handbrake/contrib/x264-r2200-999b753.tar.gz
Source126: http://download.handbrake.fr/handbrake/contrib/yasm-1.1.0.tar.gz

Source151: handbrake-ffmpeg_fix_missing_return_in_nonvoid_function.patch

Url: http://handbrake.fr/
Group: Video
License: GPLv2

# Automatically added by buildreq on Wed Oct 10 2012 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel gstreamer-devel gtk-update-icon-cache libX11-devel libatk-devel libcairo-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins libgst-plugins1.0 libgtk+2-devel libjavascriptcoregtk2-devel libncurses-devel libogg-devel libpango-devel libsoup-devel libstdc++-devel libtinfo-devel libwayland-client libwayland-server libxml2-devel perl-XML-Parser pkg-config python-base python-modules python-modules-compiler python-modules-email python-modules-encodings shared-mime-info xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel gcc-c++ gst-plugins-devel intltool libalsa-devel libass-devel libavutil-devel libdbus-glib-devel libfribidi-devel libgudev-devel libnotify-devel libsamplerate-devel libtheora-devel libvorbis-devel libwebkitgtk2-devel nasm wget yasm

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
%setup -n %name-%version-%svn

# Copy 3rd party dependencies into expected locations:
%__mkdir download
for f in \
%{S:101} %{S:102} %{S:103} %{S:104} %{S:105} %{S:106} \
%{S:107} %{S:108} %{S:109} %{S:110} %{S:111} %{S:112} \
%{S:113} %{S:114} %{S:115} %{S:116} %{S:117} %{S:118} \
%{S:119} %{S:120} %{S:121} %{S:122} %{S:123} %{S:124} \
%{S:125} %{S:126} \
; do
     %__ln_s "$f" download/
done

# check beforehand that the versions match what the
# build system expects:
missing=$PWD/.missing
%__grep -hE '\.FETCH\.url *=' contrib/*/module.defs \
| %__awk -F' =' '{print $2}' \
| while read url; do
     f=$(echo "$url" | %__sed 's|^.*/||')
     case $f in
    	  bzip2*|libiconv*|pthreads*|zlib*) continue ;;
     esac
     [ -e "$RPM_SOURCE_DIR/$f" ] || echo "$url">>"$missing"
done

if test -e "$missing"; then
     echo "ERROR: missing contrib source archives:" >&2
     cat "$missing" >&2
     exit 1
fi

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

# #%__cp "%{S:151}" contrib/ffmpeg/A99-fix-missing-return-in-nonvoid-function.patch

%__mkdir build
./configure \
     --force \
     --build="$PWD/build" \
     --prefix="%buildroot%prefix" \
     --strip="/bin/true" \
     --optimize=speed \
     --debug=max

GHB_PKGS="dbus-glib-1 glib-2.0 gdk-pixbuf-2.0 gudev-1.0 webkit-1.0 libnotify"
GHB_PKGS="$GHB_PKGS gstreamer-interfaces-0.10 gstreamer-0.10 gstreamer-pbutils-0.10 gstreamer-video-0.10"
pushd build
%__make libhb/project.h
%__make %{?_smp_mflags} \
    GHB_CFLAGS="$(pkg-config --cflags $GHB_PKGS) -I../../libhb" \
    GHB_LIBS="$(pkg-config --libs $GHB_PKGS)"
popd #build

%install
pushd build
%__make install
popd #build

%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"

%__rm "%buildroot%_datadir/icons"/*/*.cache

%files cli
%doc AUTHORS COPYING CREDITS NEWS THANKS
%_bindir/HandBrakeCLI

%files gtk
%doc AUTHORS COPYING CREDITS NEWS THANKS
%_bindir/HandBrakeGUI
%_bindir/ghb
%_desktopdir/ghb.desktop
%_datadir/icons/*/*/apps/hb-icon.png

%changelog
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
