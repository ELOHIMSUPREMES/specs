Name: xfce4-whiskermenu-plugin
Version: 1.0.0
Release: alt2.git20130710

Summary: Alternate Xfce menu
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://gottcode.org/xfce4-whiskermenu-plugin/
Packager: XFCE Team <xfce@packages.altlinux.org>

# git://github.com/gottcode/xfce4-whiskermenu-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools gcc-c++ rpm-macros-cmake cmake
BuildRequires: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel
BuildRequires: libgarcon-devel libexo-devel
BuildRequires: libpixman-devel libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: libharfbuzz-devel libpng-devel

Requires: xfce4-panel >= 4.8

%description
Whisker Menu is an alternate application launcher for Xfce. When you
open it you are shown a list of applications you have marked as
favorites. You can browse through all of your installed applications by
clicking on the category buttons on the side. Top level catagories make
browsing fast, and simple to switch between. Additionally, Whisker Menu
keeps a list of the last ten applications that you've launched from it.

%prep
%setup
%patch -p1

%build
%cmake -DLIB_INSTALL_DIR=%_libdir
%cmake_build

%install
%cmakeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Wed Jul 10 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2.git20130710
- xfce4-popup-whiskermenu.in: Fix variables.
- Upstream git snapshot (master branch).

* Mon Jul 01 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2.git20130630
- Upstream git snapshot (master branch).

* Fri Jun 21 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Add Hebrew translation from upstream git.
- Initial build.

