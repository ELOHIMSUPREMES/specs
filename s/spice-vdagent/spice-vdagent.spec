%define _localstatedir /var

Name: spice-vdagent
Version: 0.12.1
Release: alt1
Summary: Agent for Spice guests
Group: Networking/Remote access
License: GPLv3+
Url: http://spice-space.org/

Source: http://spice-space.org/download/releases/%name-%version.tar
Source2: spice-vdagentd.init-alt
Patch: %name-%version-%release.patch

BuildRequires: spice-protocol libXrandr-devel >= 1.3 libXfixes-devel libXinerama-devel libX11-devel
BuildRequires: libpciaccess-devel >= 0.10
BuildRequires: desktop-file-utils
BuildRequires: libsystemd-login-devel >= 42 systemd-devel

%description
Spice agent for Linux guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput. This will only work if the active X-session is running a
  spice-vdagent process so that its resolution can be determined.
* Automatic adjustment of the X-session resolution to the client resolution
* Support of copy and paste (text and images) between the active X-session
  and the client

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--with-session-info=systemd \
	--with-init-script=systemd+redhat

%make_build

%install
%makeinstall_std
install -m 0755 %SOURCE2 %buildroot%_initdir/spice-vdagentd

%post
%post_service spice-vdagentd

%preun
%preun_service spice-vdagentd

%files
%doc COPYING ChangeLog README TODO
/lib/udev/rules.d/*.rules
/lib/tmpfiles.d/spice-vdagentd.conf
%config(noreplace) %_sysconfdir/modules-load.d/spice-vdagentd.conf
%config(noreplace) %_sysconfdir/rsyslog.d/spice-vdagentd.conf
%_initddir/spice-vdagentd
%_unitdir/*
%_bindir/spice-vdagent
%_sbindir/spice-vdagentd
%_var/run/spice-vdagentd
%_sysconfdir/xdg/autostart/spice-vdagent.desktop
%_datadir/gdm/autostart/LoginWindow/spice-vdagent.desktop

%changelog
* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Tue Apr 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Mon Mar 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
