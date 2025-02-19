%define _unpackaged_files_terminate_build 1

Name: xfce4-calculator-plugin
Version: 0.7.0
Release: alt1

Summary: A calculator plugin for the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-calculator-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel

Requires: xfce4-panel >= 4.12

%description
Simple command line based calculator for the Xfce panel

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Feb 25 2019 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Mon Jan 14 2019 Mikhail Efremov <sem@altlinux.org> 0.6.90-alt1
- Enable debug (minimum level).
- Update url.
- Drop obsoleted path.
- Updated to 0.6.90.

* Tue Jun 21 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Enabled tests.
- Updated to 0.6.0.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Initial build.

