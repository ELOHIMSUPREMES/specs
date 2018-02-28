Name: xfce4-pulseaudio-plugin
Version: 0.2.4
Release: alt2

Summary: A pulseaudio plugin for the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-pulseaudio-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libpulseaudio-devel libnotify-devel

Requires: xfce4-panel >= 4.11

%define _unpackaged_files_terminate_build 1

%description
A panel plugin for controlling PulseAudio mixer.

%prep
%setup
%patch -p1
# Don't use git tag in version.
%xfce4_drop_gitvtag pulseaudio_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/*/*.*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Wed Mar 15 2017 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt2
- Fix menu translation.
- Use _unpackaged_files_terminate_build.
- Added translations from upstream git.

* Tue Oct 27 2015 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Thu May 14 2015 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Add libnotify-devel to BR.
- Updated to 0.2.3.

* Fri Mar 27 2015 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Thu Mar 19 2015 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Patches from upstream git:
  + Remove grab-broken.
  + Disconnect events and cleanup.
  + Removed grab_notify to avoid crashes.
- Initial build (closes: #30822).

