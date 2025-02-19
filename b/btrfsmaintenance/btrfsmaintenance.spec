Name: btrfsmaintenance
Version: 0.4.2
Release: alt3
Summary: Scripts for btrfs periodic maintenance tasks
License: GPLv2
Group: System/Base
Url: https://github.com/kdave/btrfsmaintenance
Source0: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires: pkgconfig(systemd)
# https://bugzilla.altlinux.org/35388
BuildRequires: rpm-macros-fedora-compat
Requires: btrfs-progs

%description
Scripts for btrfs maintenance tasks like periodic scrub, balance, trim or defrag
on selected mountpoints or directories. Hints for periodic snapshot tuning (eg.
for snapper).

%prep
%setup
%patch -p1

%build
%install
# scripts
install -m 755 -d %buildroot%_datadir/%name/
install -m 755 btrfs-defrag.sh %buildroot%_datadir/%name/
install -m 755 btrfs-balance.sh %buildroot%_datadir/%name/
install -m 755 btrfs-scrub.sh %buildroot%_datadir/%name/
install -m 755 btrfs-trim.sh %buildroot%_datadir/%name/
install -m 755 btrfsmaintenance-refresh-cron.sh %buildroot%_datadir/%name/
install -m 644 btrfsmaintenance-functions %buildroot%_datadir/%name/

# systemd services and timers
install -m 755 -d %buildroot%_unitdir/
install -m 755 -d %buildroot%_presetdir/
install -m 644 -D btrfsmaintenance-refresh.service %buildroot%_unitdir/
install -m 644 -D btrfsmaintenance-refresh.path %buildroot%_unitdir/
install -m 644 -D btrfs-balance.service %buildroot%_unitdir/
install -m 644 -D btrfs-defrag.service %buildroot%_unitdir/
install -m 644 -D btrfs-scrub.service %buildroot%_unitdir/
install -m 644 -D btrfs-trim.service %buildroot%_unitdir/
install -m 644 -D btrfs-balance.timer %buildroot%_unitdir/
install -m 644 -D btrfs-defrag.timer %buildroot%_unitdir/
install -m 644 -D btrfs-scrub.timer %buildroot%_unitdir/
install -m 644 -D btrfs-trim.timer %buildroot%_unitdir/
install -m 644 -D 80-btrfsmaintenance.preset %buildroot%_presetdir/

# config
install -m 644 -D sysconfig.btrfsmaintenance %buildroot%_sysconfdir/sysconfig/%name

%post
# According to 80-btrfmaintenance.preset,
# needed systemd units will be enabled automatically on package installation
%systemd_post btrfsmaintenance-refresh.service btrfsmaintenance-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer

%preun
%systemd_preun btrfsmaintenance-refresh.service btrfsmaintenance-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer

%files
%doc COPYING README.md
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_datadir/%name
%_datadir/%name/*
%_unitdir/btrfsmaintenance-refresh.path
%_unitdir/btrfsmaintenance-refresh.service
%_unitdir/btrfs-balance.service
%_unitdir/btrfs-defrag.service
%_unitdir/btrfs-scrub.service
%_unitdir/btrfs-trim.service
%_unitdir/btrfs-balance.timer
%_unitdir/btrfs-defrag.timer
%_unitdir/btrfs-scrub.timer
%_unitdir/btrfs-trim.timer
%_presetdir/80-btrfsmaintenance.preset

%changelog

* Fri May 31 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 0.4.2-alt3
- Fix %%post and %%preun scripts:
  - not only systemd *.service units, but also *.timer and *.path should be
    processed by systemctl set-default
- Add systemd preset to autoenable needed systemd units (humans will not
  understand which ones must be enabled manually as there are too many of them)
- Adjusted default config /etc/sysconfig/btrfsmaintenance:
  - Process all btrfs mount points by default, not only /
  - Disable scrub by default;
    it is not really needed on desktops and causes very high Load Average
- These changes are in sync with
  https://gitlab.com/nixtux-packaging/btrfsmaintenance

* Sat Jan 12 2019 Vera Blagoveschenskaya <vercha@altlinux.org> 0.4.2-alt1
- Initial build for ALT
