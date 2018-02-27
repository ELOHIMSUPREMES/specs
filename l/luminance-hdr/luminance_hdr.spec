%define _name luminance
Name: %_name-hdr
Version: 2.3.1
Release: alt2

Summary: A graphical tool for creating and processing HDR images
Group: Graphics
License: GPLv2+
Url: http://qtpfsgui.sourceforge.net/

Source: http://sourceforge.net/projects/qtpfsgui/files/%name-%version.tar.bz2
Source1: luminance-hdr_lang_ru.qm

Obsoletes: qtpfsgui
Provides: qtpfsgui = %version-%release

BuildRequires: cmake gcc-c++ boost-devel libgomp-devel libqt4-devel phonon-devel
BuildRequires: openexr-devel libexiv2-devel libfftw3-devel liblcms2-devel
BuildRequires: libraw-devel-static libjpeg-devel libtiff-devel libgsl-devel

%description
Luminance HDR is a graphical user interface application that aims to
provide a workflow for HDR imaging.

%prep
%setup -n %name-%version
# new russian translation
#cp %SOURCE1 i18n/lang_ru.qm
#rm -f i18n/lang_ru.ts

%build
%cmake
pushd BUILD
%make_build

%install
pushd BUILD
%makeinstall_std
popd
%find_lang --with-qt --output=%name.lang lang qt

%files -f %name.lang
%_bindir/*
%dir %_datadir/%name
%dir %_datadir/%name/i18n
%_datadir/%name/help/
%_datadir/applications/*
%_datadir/icons/hicolor/*/*/*
%doc AUTHORS Changelog README TODO BUGS

%changelog
* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt2
- rebuilt against libraw.so.10

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1
- built against libexiv2.so.13

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt2
- rebuilt against libexiv2.so.12

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sun Jan 22 2012 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt2
- rebuilt against libexiv2.so.11

* Sun Aug 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Wed Apr 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Sun Oct 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Mon Jun 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- rebuild against libexiv2-0.20
- updated russian translation
- obsoletes and provides qtpfsgui

* Mon May 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- first build for Sisyphus

