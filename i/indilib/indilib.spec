%define shortname indi


Name: indilib
Version: 0.9.8
Release: alt1

%add_verify_elf_skiplist %_libdir/libindidriver.so.%version
%add_verify_elf_skiplist %_libdir/libindimain.so.%version
%add_verify_elf_skiplist %_libdir/libAlignmentDriver.so

Group: Development/C
Summary: Library to control astronomical devices
Url: http://indi.sourceforge.net/
License: LGPLv2+

Provides: %shortname = %version-%release
Conflicts: kde4edu-kstars < 4.1.60
Conflicts: kdeedu-kstars <= 3.5.10-alt2

Source: http://nchc.dl.sourceforge.net/sourceforge/indi/lib%{shortname}_%version.tar.gz

# Automatically added by buildreq on Wed Oct 05 2011 (-bi)
# optimized out: cmake-modules elfutils libstdc++-devel pkg-config zlib-devel
#BuildRequires: boost-devel-headers cmake gcc-c++ libcfitsio-devel libnova-devel libusb-compat-devel zlib-devel-static
BuildRequires: boost-devel cmake gcc-c++ libcfitsio-devel libnova-devel libusb-compat-devel zlib-devel
BuildRequires: libusb-devel libjpeg-devel libgsl-devel
BuildRequires: kde-common-devel

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%package -n libsbigudrv
Summary: Librar file for INDI
Group: Development/C
%description -n libsbigudrv
  INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).
  This package contains library files of indilib.

%package -n lib%shortname
Group: System/Libraries
Summary: Library to control astronomical devices
%description -n lib%shortname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%package -n lib%shortname-devel
Summary: INDI devellopment files
Group: Development/C
Requires: lib%shortname = %version-%release
Provides: %shortname-devel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release
%description -n lib%shortname-devel
  INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).
  This package contains files need to build applications using indilib.

%prep
%setup -q -n lib%{shortname}_%version

%build
%Kbuild \
    -DUDEVRULES_INSTALL_DIR=%_udevrulesdir \
    #

%install
%Kinstall

mkdir -p %buildroot/%_libdir/%shortname/MathPlugins/
mv %buildroot/%_datadir/%shortname/MathPlugins/*.so %buildroot/%_libdir/%shortname/MathPlugins/
for f in %buildroot/%_libdir/%shortname/MathPlugins/*.so
do
    fname=`basename $f`
    ln -s `relative %buildroot/%_libdir/%shortname/MathPlugins/$fname %buildroot/%_datadir/%shortname/MathPlugins/$fname` %buildroot/%_datadir/%shortname/MathPlugins/$fname
done

%files
%doc ChangeLog README
%_bindir/*
%_libdir/%shortname/
%_datadir/%shortname/
%_udevrulesdir/*.rules

%files -n lib%shortname
%doc ChangeLog README
%_libdir/lib*.so.*

#%files -n libsbigudrv
#%_libdir/libsbigudrv.so.*

%files -n lib%shortname-devel
%doc ChangeLog TODO README
#%doc src/examples
%_libdir/*.so
%_libdir/*.a
%_includedir/libindi
%_pkgconfigdir/libindi.pc

%changelog
* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.8-alt1
- new version

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt0.M70P.1
- built for M70P

* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt1
- new version

* Fri Jul 27 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1.M60P.1
- new version

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt2
- rebuilt whith new libnova

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- new version

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2.M60P.1
- built for M60P

* Wed Oct 19 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt3
- rebuilt whith new libnova

* Wed Oct 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1.M60P.1
- built for M60P

* Wed Oct 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2
- fix build requires

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt0.M60P.1
- built for M60P

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt3
- rebuilt

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt2
- rebuilt

* Fri Aug 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 0.6-alt4
- rebuilt with new libnova

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt3
- remove ExclusiveArch from specfile

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt2
- fix conflicts

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- initial specfile

