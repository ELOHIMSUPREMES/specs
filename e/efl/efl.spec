%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec
%define gst_api_ver 1.0
%def_enable wayland
%def_disable wayland_egl
%def_enable fb
%def_enable multisense
%def_disable tslib
%def_disable egl
%def_disable xcb
%def_enable drm
%def_enable ibus
%def_enable gstreamer1

Name: efl
Version: 1.11.5
Release: alt1

Summary: Enlightenment Foundation Libraries
License: BSD/LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

Source: http://download.enlightenment.org/rel/libs/%name/%name-%version.tar.xz
#Source: %name-%version.tar

%{?_enable_static:BuildPreReq: glibc-devel-static}
BuildRequires: gcc-c++ glibc-kernheaders glib2-devel libcheck-devel lcov doxygen
BuildRequires: libpng-devel libjpeg-devel libopenjpeg-devel libtiff-devel libgif-devel libwebp-devel
BuildRequires: fontconfig-devel libfreetype-devel libfribidi-devel libharfbuzz-devel
BuildRequires: libpulseaudio-devel libsndfile-devel libbullet-devel  zlib-devel
BuildRequires: libluajit-devel libssl-devel libcurl-devel libdbus-devel
BuildRequires: libmount-devel libblkid-devel
BuildRequires: libudev-devel systemd-devel libsystemd-journal-devel libsystemd-daemon-devel
%if_enabled xcb
BuildRequires: libxcb-devel libxcbutil-devel libxcbutil-image-devel libxcb-render-util-devel
BuildRequires: libxcbutil-icccm-devel libxcbutil-keysyms-devel libpixman-devel
%else
BuildRequires: libX11-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXext-devel
BuildRequires: libXfixes-devel libXinerama-devel libXrandr-devel libXrender-devel libXScrnSaver-devel
BuildRequires: libXtst-devel libXcursor-devel libXp-devel libXi-devel
%endif
BuildRequires: libGL-devel
%{?_enable_ibus:BuildRequires: libibus-devel}
%{?_enable_tslib:BuildRequires: libts-devel}
%{?_enable_wayland:BuildRequires: libwayland-client-devel >= 1.3.0 libwayland-cursor-devel libxkbcommon-devel}
%{?_enable_wayland_egl:BuildRequires: libwayland-egl-devel}
%{?_enable_egl:BuildRequires: libEGL-devel libwayland-egl-devel}
%{?_enable_gstreamer1:BuildRequires: gst-plugins%gst_api_ver-devel}

%description
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

There are many components inside EFL. They also build various things
like shared libraries, loadable plug-in modules and also binary
executables.

For more doumentation please see:

http://www.enlightenment.org/p.php?p=docs

%package -n %name-libs
Summary: Enlightenment Foundation Libraries
Group: System/Libraries
Obsoletes: libeina < %version
Provides: libeina = %version-%release
Obsoletes: libeet < %version
Provides: libeet = %version-%release
Obsoletes: libevas < %version
Provides: libevas = %version-%release
Obsoletes: libecore < %version
Provides: libecore = %version-%release
Obsoletes: edje < %version
Provides: edje = %version-%release
Obsoletes: libedje < %version
Provides: libedje = %version-%release
Obsoletes: libeeze < %version
Provides: libeeze = %version-%release
Obsoletes: eeze < %version
Provides: eeze = %version-%release
Obsoletes: libembryo < %version
Provides: libembryo = %version-%release
Obsoletes: libeio < %version
Provides: libeio = %version-%release
Obsoletes: libefreet < %version
Provides: libefreet = %version-%release
Obsoletes: libethumb < %version
Provides: libethumb = %version-%release
Obsoletes: libemotion < %version
Provides: libemotion = %version-%release
Provides: libeo = %version-%release
Provides: libephysics = %version-%release
Provides: libeldbus = %version-%release

%description -n %name-libs
This package contains shared EFL libraries.

%package -n %name-libs-devel
Summary: Enlightenment Foundation Libraries development files
Group: Development/C
Requires: %name-libs = %version-%release
Obsoletes: libeina-devel < %version
Provides: libeina-devel = %version-%release
Obsoletes: libeet-devel < %version
Provides: libeet-devel = %version-%release
Obsoletes: libevas-devel < %version
Provides: libevas-devel = %version-%release
Obsoletes: libecore-devel < %version
Provides: libecore-devel = %version-%release
Obsoletes: libedje-devel < %version
Provides: libedje-devel = %version-%release
Obsoletes: libeeze-devel < %version
Provides: libeeze-devel = %version-%release
Obsoletes: libembryo-devel < %version
Provides: libembryo-devel = %version-%release
Obsoletes: libeio-devel < %version
Provides: libeio-devel = %version-%release
Obsoletes: libefreet-devel < %version
Provides: libefreet-devel = %version-%release
Obsoletes: libethumb-devel < %version
Provides: libethumb-devel = %version-%release
Obsoletes: libemotion-devel < %version
Provides: libemotion-devel = %version-%release
Obsoletes: embryo_cc < %version
Provides: embryo_cc = %version-%release
Provides: libeo-devel = %version-%release
Provides: libephysics-devel = %version-%release
Provides: libeldbus-devel = %version-%release

%description -n %name-libs-devel
This package contains headers, development libraries, test programs and
documentation for EFL.

%prep
%setup
#%%patch -p1
#subst 's/xcb-xprint//
#	/ECORE_XCB_XPRINT/d' configure.ac

%build
%autoreconf
%configure \
	--disable-static \
	--enable-xinput22 \
	--enable-systemd \
	--enable-image-loader-webp \
	--enable-harfbuzz \
	%{subst_enable multisense} \
	%{subst_enable tslib} \
	%{subst_enable wayland} \
	%{subst_enable fb} \
	%{subst_enable egl} \
	%{subst_enable drm} \
	%{subst_enable ibus} \
	%{subst_enable gstreamer1} \
	%{?_enable_xcb:--with-x11=xcb}
# SMP-incompatible build since 1.11
%make
#%make doc

%install
%makeinstall_std
find %buildroot%_libdir -name "*.la" -delete

%find_lang %name

%files -n %name-libs -f %name.lang
%_bindir/ecore_evas_convert
%_bindir/vieet
%_bindir/edje_cc
%_bindir/edje_codegen
%_bindir/edje_decc
%_bindir/edje_external_inspector
%_bindir/edje_inspector
%_bindir/edje_pick
%_bindir/edje_player
%_bindir/edje_recc
%_bindir/edje_watch
%_bindir/eet
%_bindir/eeze_disk_ls
%_bindir/eeze_mount
%_bindir/eeze_scanner
%_bindir/eeze_umount
%_bindir/efreetd
%_bindir/eina-bench-cmp
%_bindir/elua
%_bindir/ethumb
%_bindir/ethumbd
%_bindir/ethumbd_client
%_bindir/evas_cserve2_client
%_bindir/evas_cserve2_usage
%_libdir/*.so.*
%_libdir/ecore/
%_libdir/ecore_evas/
%_libdir/ecore_imf/
%_libdir/ecore_x/
%_libdir/edje/
%_libdir/eeze/
%_libdir/efreet/
%_libdir/emotion/
%_libdir/ethumb/
%_libdir/ethumb_client/
%_libdir/evas/
%_datadir/dbus-1/services/org.enlightenment.Efreet.service
%_datadir/dbus-1/services/org.enlightenment.Ethumb.service
%_datadir/ecore/
%_datadir/ecore_imf/
%_datadir/ecore_x/
%_datadir/edje/
%_datadir/eeze/
%_datadir/efreet/
%_datadir/embryo/
%_datadir/emotion/
%_datadir/eo/
%exclude %_datadir/eo/gdb/eo_gdb.py
%exclude %_datadir/eo/gdb/eo_gdb.py
%_datadir/ethumb/
%_datadir/ethumb_client/
%_datadir/evas/
%_datadir/elua/
%_datadir/mime/packages/edje.xml
%_prefix/lib/systemd/user/efreet.service
%_prefix/lib/systemd/user/ethumb.service
%doc AUTHORS README NEWS COMPLIANCE

%files -n %name-libs-devel
%_bindir/eldbus-codegen
%_bindir/evas_cserve2_debug
%_bindir/evas_cserve2_shm_debug
%_bindir/embryo_cc
%_bindir/eolian_cxx
%_bindir/eolian_gen
%_includedir/*
%_libdir/cmake/*
%_libdir/*.so
%_libdir/pkgconfig/ecore-audio.pc
%_libdir/pkgconfig/ecore-avahi.pc
%_libdir/pkgconfig/ecore-con.pc
%_libdir/pkgconfig/ecore-evas.pc
%_libdir/pkgconfig/ecore-fb.pc
%_libdir/pkgconfig/ecore-file.pc
%_libdir/pkgconfig/ecore-imf-evas.pc
%_libdir/pkgconfig/ecore-imf.pc
%_libdir/pkgconfig/ecore-input-evas.pc
%_libdir/pkgconfig/ecore-input.pc
%_libdir/pkgconfig/ecore-ipc.pc
%_libdir/pkgconfig/ecore-wayland.pc
%_libdir/pkgconfig/ecore-x.pc
%_libdir/pkgconfig/ecore.pc
%_libdir/pkgconfig/edje.pc
%_libdir/pkgconfig/eet.pc
%_libdir/pkgconfig/eeze.pc
%_libdir/pkgconfig/efreet-mime.pc
%_libdir/pkgconfig/efreet-trash.pc
%_libdir/pkgconfig/efreet.pc
%_libdir/pkgconfig/eina.pc
%_libdir/pkgconfig/eio.pc
%_libdir/pkgconfig/eldbus.pc
%_libdir/pkgconfig/embryo.pc
%_libdir/pkgconfig/emotion.pc
%_libdir/pkgconfig/eo.pc
%_libdir/pkgconfig/ephysics.pc
%_libdir/pkgconfig/ethumb.pc
%_libdir/pkgconfig/ethumb_client.pc
%_libdir/pkgconfig/evas-fb.pc
%_libdir/pkgconfig/evas-opengl-x11.pc
%_libdir/pkgconfig/evas-software-buffer.pc
%_libdir/pkgconfig/evas-software-x11.pc
%_libdir/pkgconfig/evas-wayland-shm.pc
%_libdir/pkgconfig/evas.pc
%_libdir/pkgconfig/ecore-audio-cxx.pc
%_libdir/pkgconfig/ecore-cxx.pc
%_libdir/pkgconfig/ecore-drm.pc
%_libdir/pkgconfig/edje-cxx.pc
%_libdir/pkgconfig/eet-cxx.pc
%_libdir/pkgconfig/eina-cxx.pc
%_libdir/pkgconfig/eo-cxx.pc
%_libdir/pkgconfig/eolian-cxx.pc
%_libdir/pkgconfig/eolian.pc
%_libdir/pkgconfig/evas-cxx.pc
%_libdir/pkgconfig/evas-drm.pc
%dir %_datadir/eolian/
%dir %_datadir/eolian/include
%_datadir/eolian/include/*
%_datadir/gdb/
%exclude %_datadir/gdb/auto-load/*/*/libeo.so.*-gdb.py
%exclude %_datadir/eo/gdb/eo_gdb.py


%changelog
* Thu Dec 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.5-alt1
- 1.11.5

* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.4-alt1
- 1.11.4

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.3-alt1
- 1.11.3

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- 1.11.2

* Thu Jul 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.6-alt1
- 1.8.6

* Tue Jan 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Fri Jan 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt2
- enabled IBUS, DRM support
- built against libwebp.so.5

* Sat Dec 21 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Tue Dec 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt2
- 1.8.2 snapshot (3b57d1f)
- obsoletes/provides edje

* Tue Dec 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2
- obsoletes/provides all EFL libraries < 1.8

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- first build for Sisyphus

