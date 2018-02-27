%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gmic
Version: 1.5.7.2
Release: alt1

Summary: GREYC's Magic Image Converter
License: CeCILL v.2.0
Group: Graphics
Url: http://gmic.sourceforge.net/


Source: http://downloads.sourceforge.net/gmic/gmic_%version.tar.gz
Patch1: gmic-1.4.8.1-bashcompletion.patch
Patch2: gmic-1.5.7.2-alt-makefile.patch

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ imake libGraphicsMagick-c++-devel libImageMagick-devel libXext-devel libXrandr-devel
BuildRequires: libavformat-devel libfftw3-devel libgimp-devel libjpeg-devel libopencv-devel libpng-devel
BuildRequires: libswscale-devel libtiff-devel openexr-devel xorg-cf-files zlib-devel
# for zart
BuildRequires: libqt4-devel

%description
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

%package -n lib%name
Summary: GREYC's Magic Image Converter Library
Group: System/Libraries

%description -n lib%name
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

This package provides shared G'MIC library.

%package -n lib%name-devel
Summary: GREYC's Magic Image Converter Library (development package)
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

This package provides development files for GREYC's Magic Image Converter Library.

%package zart
Summary: GREYC's image processing language demo
Group: Graphics
Requires: lib%name = %version-%release

%description zart
ZArt is a computer program whose purpose is to demonstrate the possibilities of
the G'MIC image processing language by offering the choice of several
manipulations on a video stream acquired from a webcam. In other words, ZArt is
a GUI for G'MIC real-time manipulations on the output of a webcam.

%package -n gimp-plugin-gmic
Summary: Image denoising and interpolation plugin for GIMP
Group: Graphics
Requires: gimp

%description -n gimp-plugin-gmic
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

%prep
%setup -n gmic-%version
%patch1 -p1
%patch2 -p1
subst 's|\$(USR)/lib/|$(USR)/%_lib/|' src/Makefile

%build
pushd src
%make_build
popd

%install
pushd src
%makeinstall_std
popd

%find_lang --with-man %name

%files -f %name.lang
%config /etc/bash_completion.d/*
%_bindir/%name
%_man1dir/%name.1.*
%doc README COPYING

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/gmic.h
%_libdir/lib%name.so

%files zart
%_bindir/zart
%_datadir/zart/
%doc zart/README

%files -n gimp-plugin-gmic
%gimpplugindir/plug-ins/*

%changelog
* Sat Nov 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.7.2-alt1
- 1.5.7.2

* Mon Jan 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.3.0-alt1
- 1.5.3.0 (ALT #28117)

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.8-alt1.1
- Rebuilt with libopencv2.4

* Sun Jan 08 2012 Victor Forsiuk <force@altlinux.org> 1.5.0.8-alt1
- 1.5.0.8

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.7-alt1
- 1.5.0.7

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.6-alt1
- 1.5.0.6

* Wed Aug 31 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.1-alt1
- 1.5.0.1

* Sun Aug 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.0-alt1.1
- Rebuilt with OpenCV 2.3.1

* Sun Jul 10 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.0-alt1
- 1.5.0.0

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.5-alt1
- 1.4.9.5

* Tue May 10 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.2-alt1
- 1.4.9.2

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.0-alt1
- 1.4.9.0

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 1.4.8.2-alt1
- 1.4.8.2

* Mon Feb 21 2011 Victor Forsiuk <force@altlinux.org> 1.4.8.1-alt1
- 1.4.8.1
- Package bash completion file.

* Tue Feb 01 2011 Victor Forsiuk <force@altlinux.org> 1.4.7.4-alt1
- 1.4.7.4

* Wed Dec 01 2010 Victor Forsiuk <force@altlinux.org> 1.4.5.2-alt1
- 1.4.5.2
- Patched to build with libopencv2 (patch by real@).

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.4.1.0-alt1.1
- NMU: rebuild with new ImageMagick

* Thu Sep 09 2010 Victor Forsiuk <force@altlinux.org> 1.4.1.0-alt1
- 1.4.1.0

* Wed Jul 14 2010 Anton Farygin <rider@altlinux.ru> 1.3.4.0-alt1.1
- NMU: rebuild with new ImageMagick

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 1.3.4.0-alt1
- 1.3.4.0

* Mon Feb 22 2010 Victor Forsiuk <force@altlinux.org> 1.3.3.6-alt1
- 1.3.3.6

* Thu Nov 26 2009 Victor Forsyuk <force@altlinux.org> 1.3.3.0-alt1
- 1.3.3.0

* Wed Aug 26 2009 Victor Forsyuk <force@altlinux.org> 1.3.2.4-alt1
- 1.3.2.4

* Mon Jun 15 2009 Victor Forsyuk <force@altlinux.org> 1.3.2.0-alt1
- 1.3.2.0

* Thu Mar 19 2009 Victor Forsyuk <force@altlinux.org> 1.3.1.1-alt1
- 1.3.1.1

* Wed Mar 11 2009 Victor Forsyuk <force@altlinux.org> 1.3.0.4-alt1
- 1.3.0.4

* Tue Feb 17 2009 Victor Forsyuk <force@altlinux.org> 1.3.0.3-alt1
- Initial build.
