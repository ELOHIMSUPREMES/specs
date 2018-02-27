Name: xpra
Version: 0.9.6
Release: alt3

Summary: X Persistent Remote Applications

Group: Networking/Remote access
License: GPLv2
Url: http://xpra.org/

Source: http://xpra.org/src/%name-%version.tar

# Automatically added by buildreq on Sat Dec 08 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libXfixes-devel libXi-devel libXrender-devel libatk-devel libavutil-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel pkg-config python-base python-devel python-module-distribute python-module-peak python-module-pygobject-devel python-module-zope python-modules python-modules-compiler python-modules-email python-modules-encodings xorg-compositeproto-devel xorg-damageproto-devel xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXcomposite-devel libXdamage-devel libXrandr-devel libXtst-devel libavcodec-devel libswscale-devel libvpx-devel libx264-devel python-module-Cython python-module-mwlib python-module-paste python-module-pygtk-devel subversion

# Note: we have no linking requires to libwebp.so.x
Requires: libwebp xorg-xvfb setxkbmap

Requires: python-module-pyinotify

%description
Xpra is 'screen for X': it allows you to run X programs,
usually on a remote host, direct their display to your local machine,
and then to disconnect from these programs and reconnect
from the same or another machine, without losing any state.
It gives you remote access to individual applications.
Xpra is "rootless" or "seamless": programs you run under
it show up on your desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt
to changing network bandwidth limits. (see also adaptive JPEG mode)
Xpra is open-source (GPLv2+), multi-platform and multi-language,
with current clients written in Python and Java.

On the machine which will export the application (xterm in this example):
 # xpra start :100 --start-child=xterm

We can then attach to this session from the same machine, with:
 # xpra attach :100

If connecting from a remote machine, you would use something like (or you can also use the GUI):
 # xpra attach ssh:serverhostname:100


%prep
%setup
# Fix error: implicit declaration of function 'avcodec_free_frame'
patch -p1 <patches/old-libav.patch

%__subst "s|pygtk-2.0/pygobject.h|pygtk/pygobject.h|g" wimpiggy/lowlevel/bindings.pyx
%__subst "s|pygtk-2.0/pygtk/pygtk.h|pygtk/pygtk.h|g" wimpiggy/gdk/gdk_atoms.pyx

%build
%python_build

%install
%python_install

%files
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/*
%_bindir/*
%python_sitelibdir/*
%_desktopdir/*
%_iconsdir/*
%_man1dir/*
%_datadir/parti/
%_datadir/wimpiggy/
%_datadir/xpra/

%changelog
* Wed Feb 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.6-alt3
- Rebuilt for libwebp5.

* Thu Sep 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.6-alt2
- rebuilt with recent libx264

* Thu Jul 11 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version 0.9.6 (with rpmrb script)
- rebuild with new libwebp, apply patch to build with old libav

* Sat Dec 08 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- initial build for Sisyphus

