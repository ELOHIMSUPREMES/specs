%define _unpackaged_files_terminate_build 1
%define oversion 1.0

Name:		sway
Version:	1.0
Release:	alt1

Summary:	i3wm drop-in replacement for Wayland

Url:		http://swaywm.org/
License:	MIT
Group:		Graphical desktop/Other

# https://github.com/swaywm/sway
# git://git.altlinux.org/gears/s/sway.git
Source0:	%name-%version-%release.tar
Source2:	startsway

Patch00:	sway-config.patch

BuildPreReq: libwlc-devel >= 0.0.10
BuildPreReq: libdbus-devel

BuildRequires: asciidoc-a2x
BuildRequires: libcap-devel
BuildRequires: libevdev-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libjson-c-devel
BuildRequires: libpam-devel
BuildRequires: libpango-devel
BuildRequires: libpcre-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwlc0-devel
BuildRequires: libwlroots-devel
BuildRequires: meson
BuildRequires: time

Requires:	/etc/tcb
Requires:	%name-data
Requires(post):	/sbin/setcap

%package	data
Summary:	i3wm drop-in replacement for Wayland - data files
Group:		Graphical desktop/Other
BuildArch:	noarch

%define common_descr \
Sway is a drop-in replacement for the i3 window manager, but for Wayland \
instead of X11. It works with your existing i3 configuration and \
supports most of i3's features, and a few extras.

%description
%common_descr

%description data
%common_descr

This package contains data files.

%prep
%setup -n %name-%version-%release
%patch00 -p1

sed -i -e "s/'json-c', version: '>=0.13'/'json-c', version: '>=0.12'/" meson.build

%build
%meson \
	-Dsway-version="%oversion" \
	-Dwerror=false \
	#
%meson_build

%install
%meson_install
install -pm0755 -D %SOURCE2 %buildroot%_bindir/

rm -rf -- \
	%buildroot/%_datadir/bash-completion \
	%buildroot/%_datadir/fish \
	%buildroot/%_datadir/zsh \
	#

%post
/sbin/setcap cap_sys_ptrace,cap_sys_tty_config=eip %_bindir/%name

%files
%doc LICENSE
%doc README.md
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/security.d
%config(noreplace) %_sysconfdir/%name/config
%config(noreplace) %_sysconfdir/%name/security.d/00-defaults
%_bindir/sway
%_bindir/startsway
%_bindir/swaybar
%_bindir/swaybg
%_bindir/swaymsg
%_bindir/swaynag
#%%_man1dir/*
#%%_man5dir/*
#%%_man7dir/*
%_datadir/wayland-sessions/sway.desktop

%files data
%dir %_datadir/backgrounds/%name
%_datadir/backgrounds/%name/*

%changelog
* Sun Mar 24 2019 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- New version (1.0)

* Thu Jan 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.beta.2.0.75.g4a3ada30.1
- Updated to 1.0-beta.2-75-g4a3ada30.

* Mon Apr 16 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.15.2-alt1
- 0.15.2
- added startsway script

* Mon Jul 31 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.14.0-alt1
- 0.14.0
- fixed capabilities setting

* Wed May 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.13.0-alt1
- 0.13.0

* Sat Apr 08 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12.2-alt1
- 0.12.2
- set CAP_SYS_TTY_CONFIG to sway binary

* Wed Mar 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12-alt2
- added swaylock.
- fixed post requires type.
- removed control file.

* Sat Mar 11 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12-alt1
- 0.12
- fixed: set CAP_SYS_PTRACE to sway binary
- upstream changes:
 + %%_sysconfdir/%%name/security config is no longer used by sway
 + added security configs dir: %%_sysconfdir/%%name/security.d

* Tue Feb 28 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.11-alt1
- 0.11
- fixed: system configs are noreplace now

* Sat Oct 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.10-alt1
- 0.10

* Thu Sep 22 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9-alt1
- Initial build
