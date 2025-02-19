Name: v4l-utils
Version: 1.16.6
Release: alt1

Summary: Collection of video4linux support libraries and utilities
License: GPLv2+
Group: Video
Url: http://linuxtv.org

Source: %name-%version-%release.tar
BuildRequires: gcc-c++ libalsa-devel libelf-devel libGLU-devel libjpeg-devel
BuildRequires: libudev-devel qt5-base-devel

%package -n ir-keytable
Summary: IR keytable management tool
Group: System/Kernel and hardware
Conflicts: v4l-utils < 0.8.2-alt1

%package -n libv4l
Summary: video4linux support libraries
Group: System/Libraries
License: LGPLv2+

%package -n libv4l-devel
Summary: Development files for libv4l
Group: Development/C
Requires: libv4l = %version-%release
License: LGPLv2+

%package -n qv4l2
Summary: A test bench application for video4linux devices
Group: Video

%package -n qvidcap
Summary: A video capture viewer
Group: Video

%description
Linux V4L2 and DVB API utilities.

%description -n ir-keytable
ir-keytable  is a tool that lists the Remote Controller devices, allows
to get/set IR keycode/scancode tables, test events generated by IR, and
to adjust other Remote Controller options.

%description -n libv4l
libv4l is a collection of libraries which adds a thin abstraction layer on
top of video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices without
having to write separate code for different devices in the same class. libv4l
consists of 3 different libraries: libv4lconvert, libv4l1 and libv4l2.

libv4lconvert offers functions to convert from any (known) pixelformat
to V4l2_PIX_FMT_BGR24 or V4l2_PIX_FMT_YUV420.

libv4l1 offers the (deprecated) v4l1 API on top of v4l2 devices, independent
of the drivers for those devices supporting v4l1 compatibility (which many
v4l2 drivers do not).

libv4l2 offers the v4l2 API on top of v4l2 devices, while adding for the
application transparent libv4lconvert conversion where necessary.

%description -n libv4l-devel
The libv4l-devel package contains libraries and header files for
developing applications that use libv4l.

%description -n qv4l2
The qv4l2 tool is used to test video4linux capture devices, either
video, vbi or radio. This application can also serve as a generic
video/TV viewer application.

%description -n qvidcap
The qvidcap tool is used to test video4linux capture devices, either
using a video device, a file, or over network. This application can
also serve as a generic video/TV viewer application.

%prep
%setup

%build
[ -x bootstrap.sh ] && ./bootstrap.sh
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog COPYING README

%_sbindir/*
%_bindir/*
%exclude %_bindir/ir-keytable
%exclude %_bindir/qv4l2
%ifnarch armh
%exclude %_bindir/qvidcap
%endif
%_man1dir/cec-compliance.1*
%_man1dir/cec-ctl.1.*
%_man1dir/cec-follower.1*
%_man1dir/ir-ctl.1*
%_man1dir/dvb-fe-tool.1*
%_man1dir/dvb-format-convert.1*
%_man1dir/dvbv5-scan.1*
%_man1dir/dvbv5-zap.1*
%_man1dir/v4l2-compliance.1*
%_man1dir/v4l2-ctl.1*

%files -n ir-keytable
%config(noreplace) %_sysconfdir/rc_maps.cfg
/lib/udev/rules.d/70-infrared.rules
/lib/udev/rc_keymaps
%_bindir/ir-keytable
%_man1dir/ir-keytable.1*

%files -n libv4l
%doc COPYING.libv4l ChangeLog README.libv4l TODO
%_libdir/libv4l*.so.*
%_libdir/libdvbv5.so.*
%_libdir/libv4l

%files -n libv4l-devel
%doc README.lib-multi-threading
%_includedir/libv4l*.h
%_includedir/libdvbv5
%_libdir/libv4l*.so
%_libdir/libdvbv5.so
%_pkgconfigdir/*.pc

%files -n qv4l2
%_bindir/qv4l2
%_desktopdir/qv4l2.desktop
%_iconsdir/hicolor/*/*/qv4l2.*
%_man1dir/qv4l2.1*

%ifnarch armh
%files -n qvidcap
%_bindir/qvidcap
%_desktopdir/qvidcap.desktop
%_iconsdir/hicolor/*/*/qvidcap.*
%_man1dir/qvidcap.1*
%endif

%changelog
* Tue May 21 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.6-alt1
- 1.16.6 released

* Tue Jan 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.2-alt2
- fixed build on arm

* Tue Jan 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.2-alt1
- 1.16.2 released

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Fri Jul 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.5-alt1
- 1.12.5 released

* Thu May 04 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.3-alt1
- 1.12.3 released

* Wed Apr 13 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.6.0-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Sun Feb 15 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Mon Sep 16 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Wed May 01 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.5-alt1
- 0.9.5 released

* Tue Oct 02 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.8-alt2
- fix build with gcc-4.7

* Tue Jun 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.8-alt1
- 0.8.8 released

* Sun Feb 19 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.6-alt1
- 0.8.6 released

* Thu Aug 18 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.5-alt1
- 0.8.5 released

* Sat Feb 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt1
- 0.8.3 released

* Tue Feb 08 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.2-alt1
- 0.8.2 released

* Fri Nov 05 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Wed May 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.0-alt1
- 0.8.0 released

* Tue Apr 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- new version 0.6.4 (with rpmrb script)

* Sun Mar 21 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version (0.6.1) import in git

* Fri Jul 31 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.6.0-alt2
- Dummy changelog entry to make girar (or whatever) happier.

* Wed Jul 29 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 release (with brain force) 

* Thu Nov 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.5.6-alt1
- new version 0.5.6 (with hands only)
- prettified some macro.

* Sat Oct 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

* Sat Oct 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Aug 15 2008 bphilips@suse.de
- Initial SuSE package
