%define _unpackaged_files_terminate_build 1

%define _libexecdir %prefix/libexec

Summary: SELinux policy core utilities
Name: policycoreutils
Epoch:   1
Version: 2.9
Release: alt2
License: GPLv2
Group: System/Base
Url: https://github.com/SELinuxProject/selinux

Source0: %name-%version.tar

Source1: restorecond.init
Source2: sandbox.init
Source3: system-config-selinux.pam
Source6: system-config-selinux.console
Source8: selinux-polgengui.console
Source9: mcstrans.init

Source13: selinux-python-%version.tar
Source14: selinux-gui-%version.tar
Source15: selinux-sandbox-%version.tar
Source16: selinux-dbus-%version.tar
Source17: semodule-utils-%version.tar
Source18: restorecond-%version.tar
Source19: mcstrans-%version.tar

Patch1: %name-%version-policycoreutils-alt.patch
Patch2: %name-%version-python-alt.patch
Patch6: %name-%version-restorecond-alt.patch
Patch7: %name-%version-mcstrans-alt.patch

%define mcstrans_ver 0.3.3
Requires: python3-module-semanage python3-module-audit

BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-python3
BuildRequires: libaudit-devel libcap-devel libpam-devel
BuildRequires: libselinux-devel libsemanage-devel libsepol-devel libsepol-devel-static
BuildRequires: desktop-file-utils
BuildRequires: glib2-devel libdbus-glib-devel
BuildRequires: libcap-ng-devel libpcre-devel libcgroup-devel
BuildRequires: python3-devel

%add_python3_path %_datadir/system-config-selinux

%description
policycoreutils contains the policy core utilities that are required
for basic operation of a SELinux system.  These utilities include
load_policy to load policies, setfiles to label filesystems, newrole
to switch roles, and run_init to run /etc/init.d scripts in the proper
context.

%package newrole
Summary: The newrole application for RBAC/MLS
Group: System/Base
Requires: %name = %EVR

%description newrole
RBAC/MLS policy machines require newrole as a way of changing the role
or level of a logged in user.

%package sandbox
Summary: SELinux sandbox utilities
Group: System/Base
Requires: %name = %EVR

%description sandbox
This package contains the sandbox which allow you to run an applications
within a tightly confined SELinux domain.

%package sandbox-x
Summary: SELinux sandbox utilities for X applications
Group: System/Base
Requires: %name-sandbox = %EVR
Requires: xorg-xephyr
Requires: matchbox-window-manager
Requires: xmodmap
BuildArch: noarch

%description sandbox-x
This package contains the scripts to create graphical sandboxes.

%package restorecond
Summary: SELinux restorecond utilities
Group:   System/Base
Obsoletes: mcstrans <= 0.3.1
Provides: mcstrans = %mcstrans_ver

%description restorecond
This package contains the restorecond service.

%package mcstransd
Summary: SELinux Translation Daemon
Group: System/Base

%description mcstransd
mcstrans provides an translation daemon to translate SELinux categories
from internal representations to user defined representation.

%package devel
Requires: %name = %EVR
Summary: SELinux policy core policy devel utilities
Group: System/Base

%description devel
The policycoreutils-devel package contains the management tools use to
develop policy in an SELinux environment.

%package gui
Summary: SELinux configuration GUI
Group: System/Base
Requires: policycoreutils = %EVR
Requires: selinux-policy

%description gui
system-config-selinux is a utility for managing the SELinux environment.

%package -n python3-module-policycoreutils
Summary: SELinux policy core python utilities
Group:   Development/Python3
Requires: %name = %EVR

%description -n python3-module-policycoreutils
The policycoreutils-python package contains the management tools use to manage
an SELinux environment.

%prep
%setup -c -n selinux
%setup -q -T -D -a 13 -n selinux
%setup -q -T -D -a 14 -n selinux
%setup -q -T -D -a 15 -n selinux
%setup -q -T -D -a 16 -n selinux
%setup -q -T -D -a 17 -n selinux
%setup -q -T -D -a 18 -n selinux
%setup -q -T -D -a 19 -n selinux

pushd %name-%version
%patch1 -p1
popd

pushd selinux-python-%version
%patch2 -p1
popd

pushd restorecond-%version
%patch6 -p1
popd

pushd mcstrans-%version
%patch7 -p1
popd

%build
%make_build -C policycoreutils-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" all
%make_build -C selinux-python-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" all
%make_build -C selinux-gui-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" all
%make_build -C selinux-sandbox-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" all
%make_build -C selinux-dbus-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" all
%make_build -C semodule-utils-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" all
%make_build -C restorecond-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" all
%make_build -C mcstrans-%version LIBDIR=%_libdir CFLAGS="%optflags $(pkg-config --cflags-only-I libpcre)" LIBSEPOLA="%_libdir/libsepol.a"

%install
%makeinstall_std -C policycoreutils-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro"
%makeinstall_std -C selinux-python-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro"
%makeinstall_std -C selinux-gui-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro"
%makeinstall_std -C selinux-sandbox-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro"
%makeinstall_std -C selinux-dbus-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro"
%makeinstall_std -C semodule-utils-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro"
%makeinstall_std -C restorecond-%version LSPP_PRIV=y LIBDIR="%_libdir" LIBEXECDIR="%_libexecdir" LIBSEPOLA="%_libdir/libsepol.a" CFLAGS="%optflags %optflags_shared" LDFLAGS="-pie -Wl,-z,relro" SYSTEMDDIR="/lib/systemd"
%makeinstall_std -C mcstrans-%version LIBDIR=%_libdir CFLAGS="%optflags $(pkg-config --cflags-only-I libpcre)" LIBSEPOLA="%_libdir/libsepol.a" SYSTEMDDIR="/lib/systemd"

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mkdir -pv %buildroot%python3_sitelibdir
mv  %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
rm -rf %buildroot%_prefix/lib/python3*
%endif

chmod -x %buildroot%python3_sitelibdir/seobject.py

install -d -m 0755 %buildroot%_localstatedir/selinux
install -D -m 0644 %SOURCE3 %buildroot%_sysconfdir/pam.d/system-config-selinux
install -D -m 0644 %SOURCE3 %buildroot%_sysconfdir/pam.d/selinux-polgengui
install -D -m 0644 %SOURCE6 %buildroot%_sysconfdir/security/console.apps/system-config-selinux
install -D -m 0644 %SOURCE8 %buildroot%_sysconfdir/security/console.apps/selinux-polgengui

# sysvinit
install -D -m 0755 %SOURCE1 %buildroot%_initddir/restorecond
install -D -m 0755 %SOURCE2 %buildroot%_initddir/sandbox
install -D -m 0755 %SOURCE9 %buildroot%_initddir/mcstrans

for f in system-config-selinux selinux-polgengui; do
	ln -sf consolehelper %buildroot%_bindir/$f
done

install -d -m 0755 %buildroot{%_datadir/mcstrans,%_sysconfdir/selinux/mls/setrans.d}
cp -r mcstrans-%version/share/* %buildroot%_datadir/mcstrans/

# TODO: compatibility for policy packages. remove later
ln -sv $(relative %_sbindir/fixfiles /sbin/fixfiles) %buildroot/sbin/fixfiles

%find_lang --with-man --all-name %name

egrep 'newrole\.1' %name.lang > %name-newrole.lang
egrep 'sandbox\.5|sandbox\.8|seunshare\.8' %name.lang > %name-sandbox.lang
egrep 'restorecond\.8' %name.lang > %name-restorecond.lang
egrep 'mcs\.8|mcstransd\.8|setrans\.conf\.8' %name.lang > %name-mcstransd.lang
egrep 'sepolgen\.8|sepolicy-booleans\.8|sepolicy-generate\.8|sepolicy-interface\.8|sepolicy-network\.8|sepolicy\.8|sepolicy-communicate\.8|sepolicy-manpage\.8|sepolicy-transition\.8|semodule_expand\.8|semodule_link\.8|semodule_unpackage\.8' %name.lang > %name-devel.lang
egrep 'system-config-selinux\.8|selinux-polgengui\.8|sepolicy-gui\.8' %name.lang > %name-gui.lang

# Now remove all matched lines from original lang file
grep -Fvx -f %name-newrole.lang -f %name-sandbox.lang -f %name-restorecond.lang -f %name-mcstransd.lang -f %name-devel.lang -f %name-gui.lang %name.lang > %name-common.lang


%triggerin -- selinux-policy
[ -f %_datadir/selinux/devel/include/build.conf ] && sepolgen-ifgen ||:

%post restorecond
%post_service restorecond

%preun restorecond
%preun_service restorecond

%post mcstransd
%post_service mcstrans

%preun mcstransd
%preun_service mcstrans

#
# stanv@ note:
# Fedora spec file has additional sub-packages: -python, -python3. 
# Put it contents here, to main policycoreutils package
#
%files -f %name-common.lang
/sbin/restorecon
/sbin/restorecon_xattr
/sbin/fixfiles
/sbin/setfiles
%_sbindir/fixfiles
%_sbindir/load_policy
%_sbindir/genhomedircon
%_sbindir/setsebool
%_sbindir/semodule
%_sbindir/sestatus
%_bindir/secon
%_libexecdir/selinux/hll/
%config(noreplace) %_sysconfdir/sestatus.conf

#
# Fedora python sub-package
#
%_sbindir/semanage
%_bindir/chcat
%_bindir/audit2allow
%_bindir/audit2why
%_bindir/semodule_package

#
# Policy Kit config, send_destination="org.selinux"
#
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.selinux.conf
%dir /var/lib/selinux

#
# Fedora doesn't pack them.
# run_init isn't required for systemd
%_sbindir/run_init
%_sbindir/open_init_pty
%config(noreplace) %_sysconfdir/pam.d/run_init

%_datadir/bash-completion/completions/semanage
%_datadir/bash-completion/completions/setsebool

%_man5dir/selinux_config.*
%_man5dir/sestatus.conf*
%_man8dir/fixfiles.*
%_man8dir/load_policy.*
%_man8dir/restorecon.*
%_man8dir/restorecon_xattr.*
%_man8dir/semodule.*
%_man8dir/sestatus.*
%_man8dir/setsebool.*
%_man8dir/setfiles.*
%_man1dir/audit2allow.*
%_man1dir/audit2why.*
%_man8dir/chcat.*
%_man8dir/semanage.*
%_man8dir/semanage-*.*
%_man8dir/semodule_package.*
%_man1dir/secon.*
%_man8dir/genhomedircon.*
# Remove ?
%_man8dir/open_init_pty.*
%_man8dir/run_init.*


%files newrole -f %name-newrole.lang
%config(noreplace) %_sysconfdir/pam.d/newrole
%attr(4511,root,root) %_bindir/newrole
%_man1dir/newrole.*

#
# stanv@:
# sandbox - useless for selinux-policy-altlinux.
# Leave it for ref-policy.
#
%files sandbox -f %name-sandbox.lang
%_bindir/sandbox
%_sbindir/seunshare
%_initddir/sandbox
%config(noreplace) %_sysconfdir/sysconfig/sandbox
%_man5dir/sandbox.*
%_man8dir/sandbox.*
%_man8dir/seunshare.*


%files sandbox-x
%_datadir/sandbox


%files restorecond -f %name-restorecond.lang
%_unitdir/restorecond.service
%_datadir/dbus-1/services/org.selinux.Restorecond.service
%_sbindir/restorecond
%_initddir/restorecond
%config(noreplace) %_sysconfdir/selinux/restorecond*
%_man8dir/restorecond.*

%files mcstransd -f %name-mcstransd.lang
/sbin/mcstransd
%_initrddir/mcstrans
%_unitdir/mcstrans.service
%dir %_sysconfdir/selinux/mls/setrans.d
%_man8dir/mcs.*
%_man8dir/mcstransd.*
%_man8dir/setrans.conf.*
%_datadir/mcstrans

%files devel -f %name-devel.lang
%_bindir/sepolgen
%_bindir/sepolgen-ifgen
%_bindir/sepolgen-ifgen-attr-helper
%_bindir/sepolicy
%_bindir/semodule_expand
%_bindir/semodule_link
%_bindir/semodule_unpackage

%_datadir/bash-completion/completions/sepolicy

%_localstatedir/sepolgen/perm_map

%_man8dir/sepolgen.*
%_man8dir/sepolicy-booleans.*
%_man8dir/sepolicy-generate.*
%_man8dir/sepolicy-interface.*
%_man8dir/sepolicy-network.*
%_man8dir/sepolicy.*
%_man8dir/sepolicy-communicate.*
%_man8dir/sepolicy-manpage.*
%_man8dir/sepolicy-transition.*
%_man8dir/semodule_expand.*
%_man8dir/semodule_link.*
%_man8dir/semodule_unpackage.*


%files gui -f %name-gui.lang
%_bindir/system-config-selinux
%_bindir/selinux-polgengui

%_iconsdir/hicolor/*/apps/system-config-selinux.png
%_pixmapsdir/system-config-selinux.png
%_iconsdir/hicolor/*/apps/sepolicy.png
%_pixmapsdir/sepolicy.png

%dir %_datadir/system-config-selinux
%_datadir/system-config-selinux/*.py*
%_datadir/system-config-selinux/__pycache__
%_datadir/system-config-selinux/*png
%_datadir/system-config-selinux/*.ui

%_datadir/system-config-selinux/selinux-polgengui.desktop
%_datadir/system-config-selinux/sepolicy.desktop
%_datadir/system-config-selinux/system-config-selinux.desktop

%_xdgconfigdir/autostart/restorecond.desktop

%config(noreplace) %_sysconfdir/pam.d/system-config-selinux
%config(noreplace) %_sysconfdir/pam.d/selinux-polgengui
%config(noreplace) %_sysconfdir/security/console.apps/system-config-selinux
%config(noreplace) %_sysconfdir/security/console.apps/selinux-polgengui

%_datadir/polkit-1/actions/org.selinux.policy
%_datadir/polkit-1/actions/org.selinux.config.policy
%_datadir/dbus-1/system-services/org.selinux.service

%_man8dir/system-config-selinux.*
%_man8dir/selinux-polgengui.*
%_man8dir/sepolicy-gui.*

%files -n python3-module-policycoreutils
%python3_sitelibdir/sepolicy
%python3_sitelibdir/sepolgen
%python3_sitelibdir/sepolicy-*.egg-info
%python3_sitelibdir/seobject.py
%python3_sitelibdir/__pycache__/*

%changelog
* Tue Apr 30 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt2
- Updated man pages translation by Olesya Gerasimenko.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt1
- Updated to upstream version 2.9.
- Disabled support for python-2.

* Tue Dec 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt2
- Added man pages translation by Olesya Gerasimenko.

* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt1
- Updated to upstream version 2.8.

* Mon Jun 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.7-alt3
- Obsoleted package python-module-sepolgen (Closes: #34981).

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.7-alt2
- Fixed build dependencies.

* Mon Feb 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.7-alt1
- Updated to upstream version 2.7.

* Tue Nov 01 2016 Anton Farygin <rider@altlinux.ru> 1:2.5-alt1
- new version

* Thu Sep 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:2.3-alt1
- downgraded due regression (closes: #32254)

* Mon Jul 18 2016 Sergey V Turchin <zerg@altlinux.org> 2.4-alt2
- move _libexecdir/selinux/hll to main package

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- new version

* Thu Feb 05 2015 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- new version

* Thu Apr 24 2014 Andriy Stepanov <stanv@altlinux.ru> 2.2.5-alt4
- Add devel package, adjust spec according to Fedora spec

* Wed Apr 23 2014 Andriy Stepanov <stanv@altlinux.ru> 2.2.5-alt3
- Add BuildRequires to python-module-pygnome

* Fri Feb 07 2014 Andriy Stepanov <stanv@altlinux.ru> 2.2.5-alt2
- Go away from python gnome module dependency

* Tue Jan 21 2014 Andriy Stepanov <stanv@altlinux.ru> 2.2.5-alt1
- new version

* Tue Nov 19 2013 Anton Farygin <rider@altlinux.ru> 2.2.3-alt1
- New version

* Thu Jul 11 2013 Timur Aitov <timonbl4@altlinux.org> 2.1.14-alt4
- fix mcstrans.service

* Wed Jul 10 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.14-alt3
- Rebuild with new setools

* Thu Jul 04 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.14-alt2
- Add newrole capabilities

* Wed Jun 26 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.14-alt1
- New Version

* Tue Apr 30 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.13-alt9
- newrole: CAP_SETPCAP, capng_lock()

* Mon Apr 29 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.13-alt8
- Update gears tags

* Mon Apr 29 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.13-alt7
- newrole: patch from policycoreutils-2.1.14-37.fc20.src.rpm

* Mon Apr 22 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.13-alt6
- newrole: add CAP_AUDIT_WRITE to list fo drop_capabilities()

* Wed Apr 17 2013 Timur Aitov <timonbl4@altlinux.org> 2.1.13-alt5
- mcstransd: convert sensitivity and categoryset separately

* Wed Apr 03 2013 Led <led@altlinux.ru> 2.1.13-alt4
- newrole: add CAP_SETGID to list fo drop_capabilities() (ALT#28784)

* Fri Nov 30 2012 Led <led@altlinux.ru> 2.1.13-alt3
- fix restorecond.service (by amike@) (ALT#28073)
- some fixes for mcstrans.service (thanx amike@)

* Sun Nov 25 2012 Led <led@altlinux.ru> 2.1.13-alt2
- added restorecond.service for systemd (ALT#28074)
- added mcstrans.service for systemd (ALT#28073)

* Mon Sep 24 2012 Led <led@altlinux.ru> 2.1.13-alt1
- 2.1.13
- fixed License

* Fri Feb 24 2012 Mikhail Efremov <sem@altlinux.org> 2.0.85-alt3
- newrole: Grant CAP_SETGID for pam_tcb.
- newrole: Fix drop_capabilities().

* Mon Feb 20 2012 Mikhail Efremov <sem@altlinux.org> 2.0.85-alt2
- Fix requires.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.85-alt1.1
- Rebuild with Python-2.7

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.85-alt1
- Add policycoreutils-alt-autorelabel-fix-path.patch.
- Update gui and po patches from FC.
- spec cleanup.
- add mcstransd subpackage.
- Move /etc/pam.d/newrole into newrole subpackage.
- Move restorecond into its own subpackage.
- made gui subpackage noarch.
- to own /usr/share/sandbox.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.83-alt4
- rewrite system-config-selinux.pam.
- enable build gui subpackage.
- move polgen.py back to gui subpackage.

* Fri Oct 15 2010 Mikhail Efremov <sem@altlinux.org> 2.0.83-alt3
- restorecond init script: add condstop.
- restorecond init script: fix status.
- Drop Russian man pages.
- Package sandbox-x subpackage as noarch.

* Thu Sep 16 2010 Mikhail Efremov <sem@altlinux.org> 2.0.83-alt2
- fixfiles: set context for root filesystem /dev/* files.

* Wed Sep 15 2010 Mikhail Efremov <sem@altlinux.org> 2.0.83-alt1
- update policycoreutils-po.patch from FC.
- update policycoreutils-gui.patch from FC.
- slightly spec cleanup.
- add sandbox and sandbox-x subpackages.
- Remove redundant information from description.
- Fix Url.
- Move sepolgen to separate package.
- fixfiles: /.autorelabel -> /etc/selinux/.autorelabel.

* Thu Jul 01 2010 Mikhail Efremov <sem@altlinux.org> 2.0.81-alt4
- slightly spec cleanup.
- rebuild with libaudit-2.0.4

* Tue Jun 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.81-alt3
- build without gui

* Thu Jun 10 2010 Mikhail Efremov <sem@altlinux.org> 2.0.81-alt2
- package sepolgen
- update policycoreutils-gui.patch from FC
- update translations from FC

* Wed Jun 09 2010 Mikhail Efremov <sem@altlinux.org> 2.0.81-alt1
- new version

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.79-alt1
- restorecond.init: use {start,stop}_daemon
- new version

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.62-alt1
- new version

* Wed Jan 14 2009 Anton Farygin <rider@altlinux.ru> 2.0.61-alt1
- first build for Sisyphus, based on specfile from fedora

* Wed Dec 10 2008 Dan Walsh <dwalsh@redhat.com> 2.0.60-5
- Fix Japanese translations

* Sat Dec 6 2008 Dan Walsh <dwalsh@redhat.com> 2.0.60-4
- Change md5 to hashlib.md5 in sepolgen

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.60-3
- Rebuild for Python 2.6

* Tue Dec 2 2008 Dan Walsh <dwalsh@redhat.com> 2.0.60-2
- Fix error checking in restorecond, for inotify_add_watch

* Mon Dec 1 2008 Dan Walsh <dwalsh@redhat.com> 2.0.60-1
- Update to upstream
	* semanage: use semanage_mls_enabled() from Stephen Smalley.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.59-2
- Rebuild for Python 2.6

* Tue Nov 11 2008 Dan Walsh <dwalsh@redhat.com> 2.0.59-1
- Update to upstream
	* fcontext add checked local records twice, fix from Dan Walsh.

* Mon Nov 10 2008 Dan Walsh <dwalsh@redhat.com> 2.0.58-1
- Update to upstream
	* Allow local file context entries to override policy entries in
	semanage from Dan Walsh.
	* Newrole error message corrections from Dan Walsh.
	* Add exception to audit2why call in audit2allow from Dan Walsh.

* Fri Nov 7 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-12
- add compression

* Tue Nov 04 2008 Jesse Keating <jkeating@redhat.com> - 2.0.57-11
- Move the usermode-gtk requires to the -gui subpackage.

* Thu Oct 30 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-10
- Fix traceback in audit2why

* Wed Oct 29 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-9
- Make GUI use translations

* Wed Oct 29 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-8
- Fix typo in man page

* Mon Oct 28 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-7
- Handle selinux disabled correctly
- Handle manipulation of fcontext file correctly

* Mon Oct 27 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-6
- Add usermode-gtk requires

* Tue Oct 23 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-5
- Allow addition of local modifications of fcontext policy.

* Mon Oct 20 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-4
- Fix system-config-selinux booleanspage throwing and exception
- Update po files

* Fri Oct 17 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-3
- Fix text in newrole
- Fix revertbutton on booleans page in system-config-selinux

* Wed Oct 1 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-2
- Change semodule calls for libsemanage

* Wed Oct 1 2008 Dan Walsh <dwalsh@redhat.com> 2.0.57-1
- Update to upstream
	* Update po files from Dan Walsh.

* Fri Sep 12 2008 Dan Walsh <dwalsh@redhat.com> 2.0.56-1
- Fix semanage help display
- Update to upstream
	* fixfiles will now remove all files in /tmp and will check for
	  unlabeled_t in /tmp and /var/tmp from Dan Walsh.
	* add glob support to restorecond from Dan Walsh.
	* allow semanage to handle multi-line commands in a single transaction
	  from Dan Walsh.

* Thu Sep 11 2008 Dan Walsh <dwalsh@redhat.com> 2.0.55-8
- Only call gen_requires once in sepolgen

* Tue Sep 9 2008 Dan Walsh <dwalsh@redhat.com> 2.0.55-7
- Change Requires line to gnome-python2-gnome
- Fix spelling mistakes
- Require libselinux-utils

* Mon Sep 8 2008 Dan Walsh <dwalsh@redhat.com> 2.0.55-5
- Add node support to semanage

* Mon Sep 8 2008 Dan Walsh <dwalsh@redhat.com> 2.0.55-4
- Fix fixfiles to correct unlabeled_t files and remove .? files

* Wed Sep 3 2008 Dan Walsh <dwalsh@redhat.com> 2.0.55-2
- Add glob support to restorecond so it can check every file in the homedir

* Thu Aug 28 2008 Dan Walsh <dwalsh@redhat.com> 2.0.55-1
- Update to upstream
	* Merged semanage node support from Christian Kuester.

* Fri Aug 15 2008 Dan Walsh <dwalsh@redhat.com> 2.0.54-7
- Add require libsemanage-python

* Mon Aug 11 2008 Dan Walsh <dwalsh@redhat.com> 2.0.54-6
- Add missing html_util.py file

* Thu Aug 7 2008 Dan Walsh <dwalsh@redhat.com> 2.0.54-5
- Fixes for multiple transactions

* Wed Aug 6 2008 Dan Walsh <dwalsh@redhat.com> 2.0.54-2
- Allow multiple transactions in one semanage command

* Tue Aug 5 2008 Dan Walsh <dwalsh@redhat.com> 2.0.54-1
- Update to upstream
	* Add support for boolean files and group support for seusers from Dan Walsh.
	* Ensure that setfiles -p output is newline terminated from Russell Coker.

* Fri Aug 1 2008 Dan Walsh <dwalsh@redhat.com> 2.0.53-3
- Allow semanage user to add group lists %%groupname

* Tue Jul 29 2008 Dan Walsh <dwalsh@redhat.com> 2.0.53-2
- Fix help

* Tue Jul 29 2008 Dan Walsh <dwalsh@redhat.com> 2.0.53-1
- Update to upstream
	* Change setfiles to validate all file_contexts files when using -c from Stephen Smalley.

* Tue Jul 29 2008 Dan Walsh <dwalsh@redhat.com> 2.0.52-6
- Fix boolean handling
- Upgrade to latest sepolgen
- Update po patch

* Wed Jul 9 2008 Dan Walsh <dwalsh@redhat.com> 2.0.52-5
- Additial cleanup of boolean handling for semanage

* Tue Jul 8 2008 Dan Walsh <dwalsh@redhat.com> 2.0.52-4
- Handle ranges of ports in gui

* Tue Jul 8 2008 Dan Walsh <dwalsh@redhat.com> 2.0.52-3
- Fix indent problems in seobject

* Wed Jul 2 2008 Dan Walsh <dwalsh@redhat.com> 2.0.52-2
- Add lockdown wizard
- Allow semanage booleans to take an input file an process lots of booleans at once.

* Wed Jul 2 2008 Dan Walsh <dwalsh@redhat.com> 2.0.52-1
- Default prefix to "user"

* Tue Jul 1 2008 Dan Walsh <dwalsh@redhat.com> 2.0.50-2
- Remove semodule use within semanage
- Fix launching of polgengui from toolbar

* Mon Jun 30 2008 Dan Walsh <dwalsh@redhat.com> 2.0.50-1
- Update to upstream
	* Fix audit2allow generation of role-type rules from Karl MacMillan.

* Tue Jun 24 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-10
- Fix spelling of enforcement

* Mon Jun 23 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-8
- Fix sepolgen/audit2allow handling of roles

* Mon Jun 16 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-7
- Fix sepolgen-ifgen processing

* Thu Jun 12 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-6
- Add deleteall to semanage permissive, cleanup error handling

* Thu Jun 12 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-5
- Complete removal of rhpl requirement

* Wed Jun 11 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-4
- Add semanage permissive *

* Fri May 16 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-3
- Fix fixfiles to cleanup /tmp and /var/tmp

* Fri May 16 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-2
- Fix listing of types in gui

* Mon May 12 2008 Dan Walsh <dwalsh@redhat.com> 2.0.49-1
- Update to upstream
	* Remove security_check_context calls for prefix validation from semanage.
	* Change setfiles and restorecon to not relabel if the file already has the correct context value even if -F/force is specified.

* Mon May 12 2008 Dan Walsh <dwalsh@redhat.com> 2.0.47-3
- Remove /usr/share/locale/sr@Latn/LC_MESSAGES/policycoreutils.mo

* Wed May 7 2008 Dan Walsh <dwalsh@redhat.com> 2.0.47-2
- Add 	rm -rf /tmp/gconfd-* /tmp/pulse-* /tmp/orbit-* to fixfiles restore
- So that mislabeled files will get removed on full relabel

* Wed May 7 2008 Dan Walsh <dwalsh@redhat.com> 2.0.47-1
- Make restorecond not start by default
- Fix polgengui to allow defining of confined roles.
- Add patches from Lubomir Rintel <lkundrak@v3.sk>
  * Add necessary runtime dependencies on setools-console for -gui
  * separate stderr when run seinfo commands
- Update to upstream
  * Update semanage man page for booleans from Dan Walsh.
  * Add further error checking to seobject.py for setting booleans.

* Fri Apr 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.0.46-5
- Uninvasive (ie no string or widget changes) HIG approximations
  in selinux-polgenui

* Fri Apr 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.0.46-4
- Move s-c-selinux to the right menu

* Sun Apr 6 2008 Dan Walsh <dwalsh@redhat.com> 2.0.46-3
- Fix boolean descriptions
- Fix semanage man page

* Wed Mar 19 2008 Dan Walsh <dwalsh@redhat.com> 2.0.46-2
- Don't use prefix in gui

* Tue Mar 18 2008 Dan Walsh <dwalsh@redhat.com> 2.0.46-1
- Update to upstream
	* Update audit2allow to report dontaudit cases from Dan Walsh.
	* Fix semanage port to use --proto from Caleb Case.

* Fri Feb 22 2008 Dan Walsh <dwalsh@redhat.com> 2.0.44-1
- Update to upstream
	* Fix for segfault when conf file parse error occurs.

* Wed Feb 13 2008 Dan Walsh <dwalsh@redhat.com> 2.0.43-2
- Don't show tabs on polgengui

* Wed Feb 13 2008 Dan Walsh <dwalsh@redhat.com> 2.0.43-1
- Update to upstream
	* Merged fix fixfiles option processing from Vaclav Ovsik.
- Added existing users, staff and user_t users to polgengui

* Fri Feb 8 2008 Dan Walsh <dwalsh@redhat.com> 2.0.42-3
- Add messages for audit2allow DONTAUDIT

* Tue Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 2.0.42-2
- Add ability to transition to roles via polgengui

* Sat Feb 2 2008 Dan Walsh <dwalsh@redhat.com> 2.0.42-1
- Update to upstream
	* Make semodule_expand use sepol_set_expand_consume_base to reduce
	  peak memory usage.

* Tue Jan 29 2008 Dan Walsh <dwalsh@redhat.com> 2.0.41-1
- Update to upstream
	* Merged audit2why fix and semanage boolean --on/--off/-1/-0 support from Dan Walsh.
	* Merged a second fixfiles -C fix from Marshall Miller.

* Thu Jan 24 2008 Dan Walsh <dwalsh@redhat.com> 2.0.39-1
- Don't initialize audit2allow for audit2why call.  Use default
- Update to upstream
	* Merged fixfiles -C fix from Marshall Miller.

* Thu Jan 24 2008 Dan Walsh <dwalsh@redhat.com> 2.0.38-1
- Update to upstream
  * Merged audit2allow cleanups and boolean descriptions from Dan Walsh.
  * Merged setfiles -0 support by Benny Amorsen via Dan Walsh.
  * Merged fixfiles fixes and support for ext4 and gfs2 from Dan Walsh.

* Wed Jan 23 2008 Dan Walsh <dwalsh@redhat.com> 2.0.37-1
- Update to upstream
  * Merged replacement for audit2why from Dan Walsh.

* Wed Jan 23 2008 Dan Walsh <dwalsh@redhat.com> 2.0.36-2
- Cleanup fixfiles -f message in man page

* Wed Jan 23 2008 Dan Walsh <dwalsh@redhat.com> 2.0.36-1
- Update to upstream
	* Merged update to chcat, fixfiles, and semanage scripts from Dan Walsh.
	* Merged sepolgen fixes from Dan Walsh.

* Tue Jan 22 2008 Dan Walsh <dwalsh@redhat.com> 2.0.35-5
- handle files with spaces on upgrades

* Tue Jan 22 2008 Dan Walsh <dwalsh@redhat.com> 2.0.35-4
- Add support in fixfiles for ext4 ext4dev and gfs2

* Mon Jan 21 2008 Dan Walsh <dwalsh@redhat.com> 2.0.35-3
- Allow files with spaces to be used by setfiles

* Tue Jan 15 2008 Dan Walsh <dwalsh@redhat.com> 2.0.35-2
- Add descriptions of booleans to audit2allow

* Fri Jan 11 2008 Dan Walsh <dwalsh@redhat.com> 2.0.35-1
- Update to upstream
	* Merged support for non-interactive newrole command invocation from Tim Reed.

* Thu Jan 8 2008 Dan Walsh <dwalsh@redhat.com> 2.0.34-8
- Change to use selinux bindings to audit2why

* Tue Jan 8 2008 Dan Walsh <dwalsh@redhat.com> 2.0.34-7
- Fix fixfiles to handle no args

* Mon Dec 31 2007 Dan Walsh <dwalsh@redhat.com> 2.0.34-5
- Fix roles output when creating a module

* Mon Dec 31 2007 Dan Walsh <dwalsh@redhat.com> 2.0.34-4
- Handle files with spaces in fixfiles

* Fri Dec 21 2007 Dan Walsh <dwalsh@redhat.com> 2.0.34-3
- Catch SELINUX_ERR with audit2allow and generate policy

* Thu Dec 20 2007 Dan Walsh <dwalsh@redhat.com> 2.0.34-2
- Make sepolgen set error exit code when partial failure
- audit2why now checks booleans for avc diagnosis

* Wed Dec 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.34-1
- Update to upstream
	* Update Makefile to not build restorecond if
	  /usr/include/sys/inotify.h is not present

* Wed Dec 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.33-4
- Fix sepolgen to be able to parse Fedora 9 policy
      Handle ifelse statements
      Handle refpolicywarn inside of define
      Add init.if and inetd.if into parse
      Add parse_file to syntax error message

* Fri Dec 14 2007 Dan Walsh <dwalsh@redhat.com> 2.0.33-3
- Add scroll bar to fcontext gui page

* Tue Dec 11 2007 Dan Walsh <dwalsh@redhat.com> 2.0.33-2
- Add Russion Man pages

* Mon Dec 10 2007 Dan Walsh <dwalsh@redhat.com> 2.0.33-1
- Upgrade from NSA
	* Drop verbose output on fixfiles -C from Dan Walsh.
	* Fix argument handling in fixfiles from Dan Walsh.
	* Enhance boolean support in semanage, including using the .xml description when available, from Dan Walsh.
- Fix handling of final screen in polgengui

* Sun Dec 2 2007 Dan Walsh <dwalsh@redhat.com> 2.0.32-2
- Fix handling of disable selinux button in gui

* Mon Nov 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.32-1
- Upgrade from NSA
	* load_policy initial load option from Chad Sellers.

* Mon Nov 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-20
- Don't show error on missing policy.xml

* Mon Nov 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-19
- GUI Enhancements
  - Fix cgi generation
  - Use more patterns

* Mon Nov 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-18
- Remove codec hacking, which seems to be fixed in python

* Fri Nov 16 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-17
- Fix typo
- Change to upstream minimal privledge interfaces

* Fri Nov 16 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-16
- Fix fixfiles argument parsing

* Thu Nov 15 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-15
- Fix File Labeling add

* Thu Nov 8 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-14
- Fix semanage to handle state where policy.xml is not installed

* Mon Nov 5 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-13
- Remove -v from restorecon in fixfiles

* Mon Nov 5 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-12
- Fix filter and search capabilities, add wait cursor

* Fri Nov 2 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-11
- Translate booleans via policy.xml
- Allow booleans to be set via semanage

* Thu Nov 1 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-10
- Require use of selinux-policy-devel

* Wed Oct 31 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-9
- Validate semanage fcontext input
- Fix template names for log files in gui

* Fri Oct 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-8
- Fix template to generate correct content

* Fri Oct 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-7
- Fix consolekit link to selinux-polgengui

* Thu Oct 18 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-6
- Fix the generation templates

* Tue Oct 16 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-5
- Fix enable/disable audit messages

* Mon Oct 15 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-4
- Add booleans page

* Mon Oct 15 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-3
- Lots of updates to gui

* Mon Oct 15 2007 Dan Walsh <dwalsh@redhat.com> 2.0.31-1
- Remove no.po
- Update to upstream
	* Fix semodule option handling from Dan Walsh.
	* Add deleteall support for ports and fcontexts in semanage from Dan Walsh.

* Thu Oct 11 2007 Dan Walsh <dwalsh@redhat.com> 2.0.29-2
- Fix semodule parameter checking

* Sun Oct 7 2007 Dan Walsh <dwalsh@redhat.com> 2.0.29-1
- Update to upstream
	* Add genhomedircon script to invoke semodule -Bn from Dan Walsh.
- Add deleteall for ports and fcontext

* Fri Oct 5 2007 Dan Walsh <dwalsh@redhat.com> 2.0.28-1
- Update to upstream
	* Update semodule man page for -D from Dan Walsh.
	* Add boolean, locallist, deleteall, and store support to semanage from Dan Walsh.

* Tue Oct 2 2007 Dan Walsh <dwalsh@redhat.com> 2.0.27-7
- Add genhomedircon script to rebuild file_context for shadow-utils

* Tue Oct 2 2007 Dan Walsh <dwalsh@redhat.com> 2.0.27-6
- Update translations

* Tue Oct 2 2007 Dan Walsh <dwalsh@redhat.com> 2.0.27-5
- Additional checkboxes for application policy

* Fri Sep 28 2007 Dan Walsh <dwalsh@redhat.com> 2.0.27-4
- Allow policy writer to select user types to transition to there users

* Thu Sep 27 2007 Dan Walsh <dwalsh@redhat.com> 2.0.27-3
- Fix bug in building policy with polgengui
- Creating ports correctly

* Wed Sep 26 2007 Dan Walsh <dwalsh@redhat.com> 2.0.27-1
- Update to upstream
	* Improve semodule reporting of system errors from Stephen Smalley.

* Mon Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 2.0.26-3
- Show local changes with semanage

* Mon Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 2.0.26-2
- Fixed spelling mistakes in booleans defs
- Update po

* Tue Sep 18 2007 Dan Walsh <dwalsh@redhat.com> 2.0.26-1
- Update to upstream
  * Fix setfiles selabel option flag setting for 64-bit from Stephen Smalley.

* Tue Sep 18 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-15
- Fix wording in policy generation tool

* Fri Sep 14 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-14
- Fix calls to _admin interfaces

* Tue Sep 13 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-13
- Upgrade version of sepolgen from NSA
	* Expand the sepolgen parser to parse all current refpolicy modules from Karl MacMillan.
	* Suppress generation of rules for non-denials from Karl MacMillan (take 3).

* Tue Sep 11 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-12
- Remove bogus import libxml2

* Mon Sep 10 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-11
- Lots of fixes for polgengui

* Thu Sep 6 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-10
- Change Requires /bin/rpm to rpm

* Wed Sep 5 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-9
- Bump libsemanage version for disable dontaudit
- New gui features for creating admin users

* Fri Aug 31 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-8
- Fix generated code for admin policy

* Fri Aug 31 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-7
- Lots of fixes for role templates

* Tue Aug 28 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-6
- Add more role_templates

* Tue Aug 28 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-5
- Update genpolgui to add creation of user domains

* Mon Aug 27 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-4
- Fix location of sepolgen-ifgen

* Sat Aug 25 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-3
- Add selinux-polgengui to desktop

* Fri Aug 24 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-2
- Cleanup spec

* Thu Aug 23 2007 Dan Walsh <dwalsh@redhat.com> 2.0.25-1
- Update semodule man page
	* Fix genhomedircon searching for USER from Todd Miller
	* Install run_init with mode 0755 from Dan Walsh.
	* Fix chcat from Dan Walsh.
	* Fix fixfiles pattern expansion and error reporting from Dan Walsh.
	* Optimize genhomedircon to compile regexes once from Dan Walsh.
	* Fix semanage gettext call from Dan Walsh.

* Thu Aug 23 2007 Dan Walsh <dwalsh@redhat.com> 2.0.23-2
- Update semodule man page

* Mon Aug 20 2007 Dan Walsh <dwalsh@redhat.com> 2.0.23-1
- Update to match NSA
  	* Disable dontaudits via semodule -D

* Wed Aug 1 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-13
- Speed up genhomedircon by an order of magnitude by compiling regex
- Allow semanage fcontext -a -t <<none>> /path to work

* Fri Jul 27 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-11
- Fixfiles update required to match new regex

* Fri Jul 27 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-10
- Update booleans translations

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 2.0.22-9
- rebuild for toolchain bug

* Tue Jul 24 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-8
- Add requires libselinux-python

* Mon Jul 23 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-7
- Fix fixfiles to report incorrect rpm
- Patch provided by Tony Nelson

* Fri Jul 20 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-6
- Clean up spec file

* Thu Jul 11 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-5
- Require newer libselinux version

* Fri Jul 7 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-4
- Fix checking for conflicting directory specification in genhomedircon

* Mon Jun 25 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-3
- Fix spelling mistakes in GUI

* Fri Jun 22 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-2
- Fix else path in chcat

* Thu Jun 21 2007 Dan Walsh <dwalsh@redhat.com> 2.0.22-1
- Update to match NSA
	* Rebase setfiles to use new labeling interface.

* Wed Jun 13 2007 Dan Walsh <dwalsh@redhat.com> 2.0.21-2
- Add filter to all system-config-selinux lists

* Wed Jun 13 2007 Dan Walsh <dwalsh@redhat.com> 2.0.21-1
- Update to match NSA
	* Fixed setsebool (falling through to error path on success).

* Mon Jun 11 2007 Dan Walsh <dwalsh@redhat.com> 2.0.20-1
- Update to match NSA
	* Merged genhomedircon fixes from Dan Walsh.
	* Merged setfiles -c usage fix from Dan Walsh.
	* Merged restorecon fix from Yuichi Nakamura.
	* Dropped -lsepol where no longer needed.

* Mon Jun 11 2007 Dan Walsh <dwalsh@redhat.com> 2.0.19-5
- Fix translations code,  Add more filters to gui

* Mon Jun 4 2007 Dan Walsh <dwalsh@redhat.com> 2.0.19-4
- Fix setfiles -c to make it work

* Mon Jun 4 2007 Dan Walsh <dwalsh@redhat.com> 2.0.19-3
- Fix french translation to not crash system-config-selinux

* Fri Jun 1 2007 Dan Walsh <dwalsh@redhat.com> 2.0.19-2
- Fix genhomedircon to work in stage2 builds of anaconda

* Fri May 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.19-1
- Update to match NSA

* Thu May 17 2007 Dan Walsh <dwalsh@redhat.com> 2.0.16-2
- Fixes for polgentool templates file

* Tue May 4 2007 Dan Walsh <dwalsh@redhat.com> 2.0.16-1
- Updated version of policycoreutils
	* Merged support for modifying the prefix via semanage from Dan Walsh.
- Fixed genhomedircon to find homedirs correctly.

* Tue May 1 2007 Dan Walsh <dwalsh@redhat.com> 2.0.15-1
- Updated version of policycoreutils
	* Merged po file updates from Dan Walsh.
- Fix semanage to be able to modify prefix in user record

* Mon Apr 30 2007 Dan Walsh <dwalsh@redhat.com> 2.0.14-2
- Fix title on system-config-selinux

* Wed Apr 25 2007 Dan Walsh <dwalsh@redhat.com> 2.0.14-1
- Updated version of policycoreutils
	* Build fix for setsebool.

* Wed Apr 25 2007 Dan Walsh <dwalsh@redhat.com> 2.0.13-1
- Updated version of policycoreutils
	* Merged setsebool patch to only use libsemanage for persistent boolean changes from Stephen Smalley.
	* Merged genhomedircon patch to use the __default__ setting from Dan Walsh.
	* Dropped -b option from load_policy in preparation for always preserving booleans across reloads in the kernel.

* Tue Apr 24 2007 Dan Walsh <dwalsh@redhat.com> 2.0.10-2
- Fixes for polgengui

* Tue Apr 24 2007 Dan Walsh <dwalsh@redhat.com> 2.0.10-1
- Updated version of policycoreutils
	* Merged chcat, fixfiles, genhomedircon, restorecond, and restorecon patches from Dan Walsh.

* Fri Apr 20 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-10
- Fix genhomedircon to handle non user_u for the default user

* Wed Apr 18 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-9
- More cleanups for gui

* Wed Apr 18 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-8
- Fix size and use_tmp problem on gui

* Wed Apr 18 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-7
- Fix restorecon crash

* Wed Apr 18 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-6
- Change polgengui to a druid

* Tue Apr 16 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-5
- Fully path script.py

* Mon Apr 16 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-4
- Add -l flag to restorecon to not traverse file systems

* Sat Apr 14 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-3
- Fixes for policygengui

* Fri Apr 13 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-2
- Add polgengui

* Thu Apr 12 2007 Dan Walsh <dwalsh@redhat.com> 2.0.9-1
- Updated version of sepolgen
	* Merged seobject setransRecords patch to return the first alias from Xavier Toth.

* Wed Apr 11 2007 Dan Walsh <dwalsh@redhat.com> 2.0.8-1
- Updated version of sepolgen
	* Merged updates to sepolgen-ifgen from Karl MacMillan.
	* Merged updates to sepolgen parser and tools from Karl MacMillan.
	  This includes improved debugging support, handling of interface
	  calls with list parameters, support for role transition rules,
	  updated range transition rule support, and looser matching.

* Mon Apr 9 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-11
- Don't generate invalid context with genhomedircon

* Mon Apr 9 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-10
- Add filter to booleans page

* Tue Apr 3 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-9
- Fix polgen.py to not generate udp rules on tcp input

* Fri Mar 30 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-8
- system-config-selinux should be able to run on a disabled system,
- at least enough to get it enabled.

* Thu Mar 29 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-7
- Many fixes to polgengui

* Fri Mar 23 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-6
- Updated version of sepolgen
	* Merged patch to discard self from types when generating requires from Karl MacMillan.

* Fri Mar 23 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-5
- Change location of audit2allow and sepol-ifgen to sbin
- Updated version of sepolgen
	* Merged patch to move the sepolgen runtime data from /usr/share to /var/lib to facilitate a read-only /usr from Karl MacMillan.

* Mon Mar 19 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-4
- Add polgen gui
- Many fixes to system-config-selinux

* Mon Mar 12 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-3
- service restorecond status needs to set exit value correctly

* Mon Mar 12 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-2
- Fix gui

* Thu Mar 1 2007 Dan Walsh <dwalsh@redhat.com> 2.0.7-1
- Update to upstream
	* Merged restorecond init script LSB compliance patch from Steve Grubb.
  -sepolgen
	* Merged better matching for refpolicy style from Karl MacMillan
	* Merged support for extracting interface paramaters from interface calls from Karl MacMillan
	* Merged support for parsing USER_AVC audit messages from Karl MacMillan.

* Tue Feb 27 2007 Dan Walsh <dwalsh@redhat.com> 2.0.6-3
- Update to upstream
  -sepolgen
	* Merged support for enabling parser debugging from Karl MacMillan.
- Add sgrupp cleanup of restorcon init script

* Mon Feb 26 2007 Dan Walsh <dwalsh@redhat.com> 2.0.6-2
- Add Bill Nottinham patch to run restorcond condrestart in postun

* Fri Feb 23 2007 Dan Walsh <dwalsh@redhat.com> 2.0.6-1
- Update to upstream
  - policycoreutils
	* Merged newrole O_NONBLOCK fix from Linda Knippers.
	* Merged sepolgen and audit2allow patches to leave generated files
	  in the current directory from Karl MacMillan.
	* Merged restorecond memory leak fix from Steve Grubb.
  -sepolgen
	* Merged patch to leave generated files (e.g. local.te) in current directory from Karl MacMillan.
	* Merged patch to make run-tests.py use unittest.main from Karl MacMillan.
	* Merged patch to update PLY from Karl MacMillan.
	* Merged patch to update the sepolgen parser to handle the latest reference policy from Karl MacMillan.

* Thu Feb 22 2007 Dan Walsh <dwalsh@redhat.com> 2.0.3-2
- Do not fail on sepolgen-ifgen

* Thu Feb 22 2007 Dan Walsh <dwalsh@redhat.com> 2.0.3-1
- Update to upstream
	* Merged translations update from Dan Walsh.
	* Merged chcat fixes from Dan Walsh.
	* Merged man page fixes from Dan Walsh.
	* Merged seobject prefix validity checking from Dan Walsh.
	* Merged Makefile and refparser.py patch from Dan Walsh.
	  Fixes PYTHONLIBDIR definition and error handling on interface files.

* Tue Feb 20 2007 Dan Walsh <dwalsh@redhat.com> 2.0.2-3
- Updated newrole NONBlOCK patch

* Tue Feb 20 2007 Dan Walsh <dwalsh@redhat.com> 2.0.2-2
- Remove Requires: %%{name}-plugins

* Tue Feb 20 2007 Dan Walsh <dwalsh@redhat.com> 2.0.2-1
- Update to upstream
	* Merged seobject exception handler fix from Caleb Case.
	* Merged setfiles memory leak patch from Todd Miller.

* Thu Feb 15 2007 Dan Walsh <dwalsh@redhat.com> 2.0.1-2
- Cleanup man pages syntax
- Add sepolgen

* Mon Feb 12 2007 Dan Walsh <dwalsh@redhat.com> 2.0.1-1
- Update to upstream
	* Merged small fix to correct include of errcodes.h in semodule_deps from Dan Walsh.

* Wed Feb 7 2007 Dan Walsh <dwalsh@redhat.com> 2.0.0-1
- Update to upstream
	* Merged new audit2allow from Karl MacMillan.
	  This audit2allow depends on the new sepolgen python module.
	  Note that you must run the sepolgen-ifgen tool to generate
	  the data needed by audit2allow to generate refpolicy.
	* Fixed newrole non-pam build.
- Fix Changelog and spelling error in man page

* Thu Feb 1 2007 Dan Walsh <dwalsh@redhat.com> 1.34.1-4
- Fix audit2allow on missing translations

* Wed Jan 24 2007 Dan Walsh <dwalsh@redhat.com> 1.34.1-3
- More chcat fixes

* Wed Jan 24 2007 Dan Walsh <dwalsh@redhat.com> 1.34.1-2
- Change chcat to exec semodule so file context is maintained

* Wed Jan 24 2007 Dan Walsh <dwalsh@redhat.com> 1.34.1-1
- Fix system-config-selinux ports view
- Update to upstream
	* Fixed newrole non-pam build.
	* Updated version for stable branch.

* Wed Jan 17 2007 Dan Walsh <dwalsh@redhat.com> 1.33.15-1
- Update to upstream
	* Merged unicode-to-string fix for seobject audit from Dan Walsh.
	* Merged man page updates to make "apropos selinux" work from Dan Walsh.
* Tue Jan 16 2007 Dan Walsh <dwalsh@redhat.com> 1.33.14-1
	* Merged newrole man page patch from Michael Thompson.
	* Merged patch to fix python unicode problem from Dan Walsh.

* Tue Jan 16 2007 Dan Walsh <dwalsh@redhat.com> 1.33.12-3
- Fix handling of audit messages for useradd change
Resolves: #222159

* Fri Jan 12 2007 Dan Walsh <dwalsh@redhat.com> 1.33.12-2
- Update man pages by adding SELinux to header to fix apropos database
Resolves: #217881

* Tue Jan 9 2007 Dan Walsh <dwalsh@redhat.com> 1.33.12-1
- Want to update to match api
- Update to upstream
	* Merged newrole securetty check from Dan Walsh.
	* Merged semodule patch to generalize list support from Karl MacMillan.
Resolves: #200110

* Tue Jan 9 2007 Dan Walsh <dwalsh@redhat.com> 1.33.11-1
- Update to upstream
	* Merged fixfiles and seobject fixes from Dan Walsh.
	* Merged semodule support for list of modules after -i from Karl MacMillan.

* Tue Jan 9 2007 Dan Walsh <dwalsh@redhat.com> 1.33.10-1
- Update to upstream
	* Merged patch to correctly handle a failure during semanage handle
	  creation from Karl MacMillan.
	* Merged patch to fix seobject role modification from Dan Walsh.

* Fri Jan 5 2007 Dan Walsh <dwalsh@redhat.com> 1.33.8-2
- Stop newrole -l from working on non secure ttys
Resolves: #200110

* Thu Jan 4 2007 Dan Walsh <dwalsh@redhat.com> 1.33.8-1
- Update to upstream
	* Merged patches from Dan Walsh to:
	  - omit the optional name from audit2allow
	  - use the installed python version in the Makefiles
	  - re-open the tty with O_RDWR in newrole

* Wed Jan 3 2007 Dan Walsh <dwalsh@redhat.com> 1.33.7-1
- Update to upstream
	* Patch from Dan Walsh to correctly suppress warnings in load_policy.

* Tue Jan 2 2007 Dan Walsh <dwalsh@redhat.com> 1.33.6-9
- Fix fixfiles script to use tty command correctly.  If this command fails, it
should set the LOGFILE to /dev/null
Resolves: #220879

* Wed Dec 20 2006 Dan Walsh <dwalsh@redhat.com> 1.33.6-8
- Remove hard coding of python2.4 from Makefiles

* Tue Dec 19 2006 Dan Walsh <dwalsh@redhat.com> 1.33.6-7
- add exists switch to semanage to tell it not to check for existance of Linux user
Resolves: #219421

* Mon Dec 18 2006 Dan Walsh <dwalsh@redhat.com> 1.33.6-6
- Fix audit2allow generating reference policy
- Fix semanage to manage user roles properly
Resolves: #220071

* Fri Dec 8 2006 Dan Walsh <dwalsh@redhat.com> 1.33.6-5
- Update po files
- Fix newrole to open stdout and stderr rdrw so more will work on MLS machines
Resolves: #216920

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.33.6-4
- rebuild for python 2.5

* Wed Dec 6 2006 Dan Walsh <dwalsh@redhat.com> 1.33.6-3
- Update po files
Resolves: #216920

* Fri Dec 1 2006 Dan Walsh <dwalsh@redhat.com> 1.33.6-2
- Update po files
Resolves: #216920

* Wed Nov 29 2006 Dan Walsh <dwalsh@redhat.com> 1.33.6-1
- Update to upstream
	* Patch from Dan Walsh to add an pam_acct_msg call to run_init
	* Patch from Dan Walsh to fix error code returns in newrole
	* Patch from Dan Walsh to remove verbose flag from semanage man page
	* Patch from Dan Walsh to make audit2allow use refpolicy Makefile
	  in /usr/share/selinux/<SELINUXTYPE>

* Wed Nov 29 2006 Dan Walsh <dwalsh@redhat.com> 1.33.5-4
- Fixing the Makefile line again to build with LSPP support
Resolves: #208838

* Wed Nov 29 2006 Dan Walsh <dwalsh@redhat.com> 1.33.5-3
- Don't report errors on restorecond when file system does not support XATTRS
Resolves: #217694

* Tue Nov 28 2006 Dan Walsh <dwalsh@redhat.com> 1.33.5-2
- Fix -q qualifier on load_policy
Resolves: #214827

* Tue Nov 28 2006 Dan Walsh <dwalsh@redhat.com> 1.33.5-1
- Merge to upstream
- Fix makefile line
Resolves: #208838

* Fri Nov 24 2006 Dan Walsh <dwalsh@redhat.com> 1.33.4-2
- Additional po changes
- Added all booleans definitions

* Wed Nov 22 2006 Dan Walsh <dwalsh@redhat.com> 1.33.4-1
- Upstream accepted my patches
	* Merged setsebool patch from Karl MacMillan.
	  This fixes a bug reported by Yuichi Nakamura with
	  always setting booleans persistently on an unmanaged system.

* Mon Nov 20 2006 Dan Walsh <dwalsh@redhat.com> 1.33.2-2
- Fixes for the gui

* Mon Nov 20 2006 Dan Walsh <dwalsh@redhat.com> 1.33.2-1
- Upstream accepted my patches

* Fri Nov 17 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-9
- Add Amy Grifis Patch to preserve newrole exit status

* Thu Nov 16 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-8
- Fix display of gui

* Thu Nov 16 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-7
- Add patch by Jose Plans to make run_init use pam_acct_mgmt

* Wed Nov 15 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-6
- More fixes to gui

* Wed Nov 15 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-5
- Fix audit2allow to generate referene policy

* Wed Nov 15 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-4
- Add group sort for portsPage.py
- Add enable/disableaudit to modules page

* Wed Nov 15 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-3
- Add glade file

* Tue Nov 14 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-2
- Fix Module handling in system-config-selinux

* Tue Nov 14 2006 Dan Walsh <dwalsh@redhat.com> 1.33.1-1
- Update to upstream
	* Merged newrole patch set from Michael Thompson.
- Add policycoreutils-gui

* Thu Nov 9 2006 Dan Walsh <dwalsh@redhat.com> 1.32-3
- No longer requires rhpl

* Fri Nov 6 2006 Dan Walsh <dwalsh@redhat.com> 1.32-2
- Fix genhomedircon man page

* Fri Oct 9 2006 Dan Walsh <dwalsh@redhat.com> 1.32-1
- Add newrole audit patch from sgrubb
- Update to upstream
	* Merged audit2allow -l fix from Yuichi Nakamura.
	* Merged restorecon -i and -o - support from Karl MacMillan.
	* Merged semanage/seobject fix from Dan Walsh.
	* Merged fixfiles -R and verify changes from Dan Walsh.

* Fri Oct 6 2006 Dan Walsh <dwalsh@redhat.com> 1.30.30-2
- Separate out newrole into its own package

* Fri Sep 29 2006 Dan Walsh <dwalsh@redhat.com> 1.30.30-1
- Update to upstream
	* Merged newrole auditing of failures due to user actions from
	  Michael Thompson.

* Tue Sep 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.29-6
- Pass -i qualifier to restorecon  for fixfiles -R
- Update translations

* Tue Sep 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.29-5
- Remove recursion from fixfiles -R calls
- Fix semanage to verify prefix

* Tue Sep 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.29-4
- More translations
- Compile with -pie

* Mon Sep 18 2006 Dan Walsh <dwalsh@redhat.com> 1.30.29-3
- Add translations
- Fix audit2allow -l

* Thu Sep 14 2006 Dan Walsh <dwalsh@redhat.com> 1.30.29-2
- Rebuild

* Thu Sep 14 2006 Dan Walsh <dwalsh@redhat.com> 1.30.29-1
- Update to upstream
- Change -o to take "-" for stdout

* Wed Sep 13 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-9
- Add -h support for genhomedircon

* Wed Sep 13 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-8
- Fix fixfiles handling of -o

* Mon Sep 11 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-7
- Make restorecon return the number of changes files if you use the -n flag

* Fri Sep 8 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-6
- Change setfiles and restorecon to use stderr except for -o flag
- Also -o flag will now output files

* Thu Sep 7 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-5
- Put back Erich's change

* Wed Sep 6 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-4
- Remove recursive switch when using rpm

* Wed Sep 6 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-3
- Fix fixfiles to handle multiple rpm and make -o work

* Fri Sep 1 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-2
- Apply patch

* Fri Sep 1 2006 Dan Walsh <dwalsh@redhat.com> 1.30.28-1
- Security fixes to run python in a more locked down manner
- More Translations
- Update to upstream
	* Merged fix for restorecon // handling from Erich Schubert.
	* Merged translations update and fixfiles fix from Dan Walsh.

* Thu Aug 31 2006 Dan Walsh <dwalsh@redhat.com> 1.30.27-5
- Change scripts to use /usr/sbin/python

* Thu Aug 31 2006 Dan Walsh <dwalsh@redhat.com> 1.30.27-4
- Add -i qualified to restorecon to tell it to ignore files that do not exist
- Fixfiles also modified for this change

* Thu Aug 31 2006 Dan Walsh <dwalsh@redhat.com> 1.30.27-3
- Ignore sigpipe

* Thu Aug 31 2006 Dan Walsh <dwalsh@redhat.com> 1.30.27-2
- Fix init script and add translations

* Thu Aug 24 2006 Dan Walsh <dwalsh@redhat.com> 1.30.27-1
- Update to upstream
	* Merged fix for restorecon symlink handling from Erich Schubert.

* Sat Aug 12 2006 Dan Walsh <dwalsh@redhat.com> 1.30.26-1
- Update to upstream
	* Merged semanage local file contexts patch from Chris PeBenito.
- Fix fixfiles log creation
- More translations

* Thu Aug 3 2006 Dan Walsh <dwalsh@redhat.com> 1.30.25-1
- Update to upstream
	* Merged patch from Dan Walsh with:
	  * audit2allow: process MAC_POLICY_LOAD events
	  * newrole:  run shell with - prefix to start a login shell
	  * po:  po file updates
	  * restorecond:  bail if SELinux not enabled
	  * fixfiles: omit -q
	  * genhomedircon:  fix exit code if non-root
	  * semodule_deps:  install man page
	* Merged secon Makefile fix from Joshua Brindle.
	* Merged netfilter contexts support patch from Chris PeBenito.

* Wed Aug 2 2006 Dan Walsh <dwalsh@redhat.com> 1.30.22-3
- Fix audit2allow to handle reload of policy

* Wed Aug 2 2006 Dan Walsh <dwalsh@redhat.com> 1.30.22-2
- Stop restorecond init script when selinux is not enabled

* Tue Aug 1 2006 Dan Walsh <dwalsh@redhat.com> 1.30.22-1
- Update to upstream
	* Merged restorecond size_t fix from Joshua Brindle.
	* Merged secon keycreate patch from Michael LeMay.
	* Merged restorecond fixes from Dan Walsh.
	  Merged updated po files from Dan Walsh.
	* Merged python gettext patch from Stephen Bennett.
	* Merged semodule_deps from Karl MacMillan.

* Thu Jul 27 2006 Dan Walsh <dwalsh@redhat.com> 1.30.17-7
- Change newrole to exec a login shell to prevent suspend.

* Fri Jul 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.17-6
- Report error when selinux not enabled in restorecond

* Tue Jul 18 2006 Dan Walsh <dwalsh@redhat.com> 1.30.17-5
- Fix handling of restorecond

* Mon Jul 17 2006 Dan Walsh <dwalsh@redhat.com> 1.30.17-4
- Fix creation of restorecond pidfile

* Mon Jul 17 2006 Dan Walsh <dwalsh@redhat.com> 1.30.17-3
- Update translations
- Update to new GCC

* Mon Jul 10 2006 Dan Walsh <dwalsh@redhat.com> 1.30.17-2
- Add verbose flag to restorecond and update translations

* Tue Jul 4 2006 Dan Walsh <dwalsh@redhat.com> 1.30.17-1
- Update to upstream
	* Lindent.
	* Merged patch from Dan Walsh with:
	  * -p option (progress) for setfiles and restorecon.
	  * disable context translation for setfiles and restorecon.
	  * on/off values for setsebool.
	* Merged setfiles and semodule_link fixes from Joshua Brindle.

* Thu Jun 22 2006 Dan Walsh <dwalsh@redhat.com> 1.30.14-5
- Add progress indicator on fixfiles/setfiles/restorecon

* Wed Jun 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.14-4
- Don't use translations with matchpathcon

* Tue Jun 20 2006 Dan Walsh <dwalsh@redhat.com> 1.30.14-3
- Prompt for selinux-policy-devel package in audit2allow

* Mon Jun 19 2006 Dan Walsh <dwalsh@redhat.com> 1.30.14-2
- Allow setsebool to use on/off
- Update translations

* Fri Jun 16 2006 Dan Walsh <dwalsh@redhat.com> 1.30.14-1
- Update to upstream
	* Merged fix for setsebool error path from Serge Hallyn.
	* Merged patch from Dan Walsh with:
	*    Updated po files.
	*    Fixes for genhomedircon and seobject.
	*    Audit message for mass relabel by setfiles.

* Tue Jun 13 2006 James Antill <jantill@redhat.com> 1.30.12-5
- Update audit mass relabel to only compile in when audit is installed.

* Mon Jun 12 2006 Dan Walsh <dwalsh@redhat.com> 1.30.12-4
- Update to required versions
- Update translation

* Wed Jun 7 2006 Dan Walsh <dwalsh@redhat.com> 1.30.12-3
- Fix shell selection

* Mon Jun 5 2006 Dan Walsh <dwalsh@redhat.com> 1.30.12-2
- Add BuildRequires for gettext

* Mon Jun 5 2006 Dan Walsh <dwalsh@redhat.com> 1.30.12-1
	* Updated fixfiles script for new setfiles location in /sbin.

* Tue May 30 2006 Dan Walsh <dwalsh@redhat.com> 1.30.11-1
- Update to upstream
	* Merged more translations from Dan Walsh.
	* Merged patch to relocate setfiles to /sbin for early relabel
	  when /usr might not be mounted from Dan Walsh.
	* Merged semanage/seobject patch to preserve fcontext ordering in list.
	* Merged secon patch from James Antill.

* Fri May 26 2006 Dan Walsh <dwalsh@redhat.com> 1.30.10-4
- Fix seobject.py to not sort the file_context file.
- move setfiles to /sbin

* Wed May 24 2006 James Antill <jantill@redhat.com> 1.30.10-3
- secon man page and getopt fixes.
- Enable mass relabel audit, even though it doesn't work.

* Wed May 24 2006 James Antill <jantill@redhat.com> 1.30.10-2
- secon fixes for --self-exec etc.
- secon change from level => sensitivity, add clearance.
- Add mass relabel AUDIT patch, but disable it until kernel problem solved.

* Tue May 24 2006 Dan Walsh <dwalsh@redhat.com> 1.30.10-1
- Update to upstream
	* Merged patch with updates to audit2allow, secon, genhomedircon,
	  and semanage from Dan Walsh.

* Sat May 20 2006 Dan Walsh <dwalsh@redhat.com> 1.30.9-4
- Fix exception in genhomedircon

* Mon May 15 2006 James Antill <jantill@redhat.com> 1.30.9-3
- Add rhpl dependancy

* Mon May 15 2006 James Antill <jantill@redhat.com> 1.30.9-2
- Add secon man page and prompt options.

* Mon May 15 2006 Dan Walsh <dwalsh@redhat.com> 1.30.9-1
- Update to upstream
	* Fixed audit2allow and po Makefiles for DESTDIR= builds.
	* Merged .po file patch from Dan Walsh.
	* Merged bug fix for genhomedircon.

* Wed May 10 2006 Dan Walsh <dwalsh@redhat.com> 1.30.8-2
- Fix exception on bad file_context

* Mon May 8 2006 Dan Walsh <dwalsh@redhat.com> 1.30.8-1
- Update to upstream
	* Merged fix warnings patch from Karl MacMillan.
	* Merged patch from Dan Walsh.
	  This includes audit2allow changes for analysis plugins,
	  internationalization support for several additional programs
	  and added po files, some fixes for semanage, and several cleanups.
	  It also adds a new secon utility.

* Sun May 7 2006 Dan Walsh <dwalsh@redhat.com> 1.30.6-5
- Fix genhomedircon to catch duplicate homedir problem

* Thu May 4 2006 Dan Walsh <dwalsh@redhat.com> 1.30.6-4
- Add secon program
- Add translations

* Thu Apr 20 2006 Dan Walsh <dwalsh@redhat.com> 1.30.6-3
- Fix check for "msg"

* Mon Apr 17 2006 Dan Walsh <dwalsh@redhat.com> 1.30.6-2
- Ship avc.py

* Fri Apr 14 2006 Dan Walsh <dwalsh@redhat.com> 1.30.6-1
- Add /etc/samba/secrets.tdb to restorecond.conf
- Update from upstream
	* Merged semanage prefix support from Russell Coker.
	* Added a test to setfiles to check that the spec file is
	  a regular file.

* Thu Apr 06 2006 Karsten Hopp <karsten@redhat.de> 1.30.4-4
- added some missing buildrequires
- added Requires: initscripts for /sbin/service

* Thu Apr 06 2006 Karsten Hopp <karsten@redhat.de> 1.30.4-3
- use absolute path /sbin/service

* Wed Apr 5 2006 Dan Walsh <dwalsh@redhat.com> 1.30.4-2
- Fix audit2allow to not require ausearch.
- Fix man page
- Add libflashplayer to restorecond.conf

* Wed Mar 29 2006 Dan Walsh <dwalsh@redhat.com> 1.30.4-1
- Update from upstream
	* Merged audit2allow fixes for refpolicy from Dan Walsh.
	* Merged fixfiles patch from Dan Walsh.
	* Merged restorecond daemon from Dan Walsh.
	* Merged semanage non-MLS fixes from Chris PeBenito.
	* Merged semanage and semodule man page examples from Thomas Bleher.

* Tue Mar 28 2006 Dan Walsh <dwalsh@redhat.com> 1.30.1-4
- Clean up reference policy generation in audit2allow

* Tue Mar 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.1-3
- Add IN_MOVED_TO to catch renames

* Tue Mar 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.1-2
- make restorecond only ignore non directories with lnk > 1

* Tue Mar 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30.1-1
- Make audit2allow translate dontaudit as well as allow rules
- Update from upstream
	* Merged semanage labeling prefix patch from Ivan Gyurdiev.

* Tue Mar 21 2006 Dan Walsh <dwalsh@redhat.com> 1.30-5
- Fix audit2allow to retrieve dontaudit rules

* Mon Mar 20 2006 Dan Walsh <dwalsh@redhat.com> 1.30-4
- Open file descriptor to make sure file does not change from underneath.

* Fri Mar 17 2006 Dan Walsh <dwalsh@redhat.com> 1.30-3
- Fixes for restorecond attack via symlinks
- Fixes for fixfiles

* Fri Mar 17 2006 Dan Walsh <dwalsh@redhat.com> 1.30-2
- Restorecon has to handle suspend/resume

* Fri Mar 17 2006 Dan Walsh <dwalsh@redhat.com> 1.30-1
- Update to upstream

* Fri Mar 10 2006 Dan Walsh <dwalsh@redhat.com> 1.29.27-1
- Add restorecond

* Fri Mar 10 2006 Dan Walsh <dwalsh@redhat.com> 1.29.26-6
- Remove prereq

* Mon Mar 6 2006 Dan Walsh <dwalsh@redhat.com> 1.29.26-5
- Fix audit2allow to generate all rules

* Fri Mar 3 2006 Dan Walsh <dwalsh@redhat.com> 1.29.26-4
- Minor fixes to chcat and semanage

* Sat Feb 24 2006 Dan Walsh <dwalsh@redhat.com> 1.29.26-3
- Add missing setsebool man page

* Thu Feb 23 2006 Dan Walsh <dwalsh@redhat.com> 1.29.26-2
- Change audit2allow to use devel instead of refpolicy

* Mon Feb 20 2006 Dan Walsh <dwalsh@redhat.com> 1.29.26-1
- Update from upstream
	* Merged semanage bug fix patch from Ivan Gyurdiev.
	* Merged improve bindings patch from Ivan Gyurdiev.
	* Merged semanage usage patch from Ivan Gyurdiev.
	* Merged use PyList patch from Ivan Gyurdiev.

* Mon Feb 13 2006 Dan Walsh <dwalsh@redhat.com> 1.29.23-1
- Update from upstream
	* Merged newrole -V/--version support from Glauber de Oliveira Costa.
	* Merged genhomedircon prefix patch from Dan Walsh.
	* Merged optionals in base patch from Joshua Brindle.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.29.20-2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Dan Walsh <dwalsh@redhat.com> 1.29.20-2
- Fix auditing to semanage
- Change genhomedircon to use new prefix interface in libselinux

* Tue Feb 07 2006 Dan Walsh <dwalsh@redhat.com> 1.29.20-1
- Update from upstream
	* Merged seuser/user_extra support patch to semodule_package
	  from Joshua Brindle.
	* Merged getopt type fix for semodule_link/expand and sestatus
	  from Chris PeBenito.
- Fix genhomedircon output

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.29.18-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 3 2006 Dan Walsh <dwalsh@redhat.com> 1.29.18-2
- Add auditing to semanage

* Thu Feb 2 2006 Dan Walsh <dwalsh@redhat.com> 1.29.18-1
- Update from upstream
	* Merged clone record on set_con patch from Ivan Gyurdiev.

* Mon Jan 30 2006 Dan Walsh <dwalsh@redhat.com> 1.29.17-1
- Update from upstream
	* Merged genhomedircon fix from Dan Walsh.
	* Merged seusers.system patch from Ivan Gyurdiev.
	* Merged improve port/fcontext API patch from Ivan Gyurdiev.
	* Merged genhomedircon patch from Dan Walsh.

* Fri Jan 27 2006 Dan Walsh <dwalsh@redhat.com> 1.29.15-1
- Update from upstream
	* Merged newrole audit patch from Steve Grubb.
	* Merged seuser -> seuser local rename patch from Ivan Gyurdiev.
	* Merged semanage and semodule access check patches from Joshua Brindle.
* Wed Jan 25 2006 Dan Walsh <dwalsh@redhat.com> 1.29.12-1
- Add a default of /export/home

* Wed Jan 25 2006 Dan Walsh <dwalsh@redhat.com> 1.29.11-3
- Cleanup of the patch

* Wed Jan 25 2006 Dan Walsh <dwalsh@redhat.com> 1.29.11-2
- Correct handling of symbolic links in restorecon

* Wed Jan 25 2006 Dan Walsh <dwalsh@redhat.com> 1.29.11-1
- Added translation support to semanage
- Update from upstream
	* Modified newrole and run_init to use the loginuid when
	  supported to obtain the Linux user identity to re-authenticate,
	  and to fall back to real uid.  Dropped the use of the SELinux
	  user identity, as Linux users are now mapped to SELinux users
	  via seusers and the SELinux user identity space is separate.
	* Merged semanage bug fixes from Ivan Gyurdiev.
	* Merged semanage fixes from Russell Coker.
	* Merged chcat.8 and genhomedircon patches from Dan Walsh.

* Thu Jan 19 2006 Dan Walsh <dwalsh@redhat.com> 1.29.9-2
- Fix genhomedircon to work on MLS policy

* Thu Jan 19 2006 Dan Walsh <dwalsh@redhat.com> 1.29.9-1
- Update to match NSA
	* Merged chcat, semanage, and setsebool patches from Dan Walsh.

* Thu Jan 19 2006 Dan Walsh <dwalsh@redhat.com> 1.29.8-4
- Fixes for "add"-"modify" error messages
- Fixes for chcat

* Wed Jan 18 2006 Dan Walsh <dwalsh@redhat.com> 1.29.8-3
- Add management of translation file to semaange and seobject

* Wed Jan 18 2006 Dan Walsh <dwalsh@redhat.com> 1.29.8-2
- Fix chcat -l -L to work while not root

* Wed Jan 18 2006 Dan Walsh <dwalsh@redhat.com> 1.29.8-1
- Update to match NSA
	* Merged semanage fixes from Ivan Gyurdiev.
	* Merged semanage fixes from Russell Coker.
	* Merged chcat, genhomedircon, and semanage diffs from Dan Walsh.

* Tue Jan 14 2006 Dan Walsh <dwalsh@redhat.com> 1.29.7-4
- Update chcat to manage user categories also

* Sat Jan 14 2006 Dan Walsh <dwalsh@redhat.com> 1.29.7-3
- Add check for root for semanage, genhomedircon

* Sat Jan 14 2006 Dan Walsh <dwalsh@redhat.com> 1.29.7-2
- Add ivans patch

* Fri Jan 13 2006 Dan Walsh <dwalsh@redhat.com> 1.29.7-1
- Update to match NSA
	* Merged newrole cleanup patch from Steve Grubb.
	* Merged setfiles/restorecon performance patch from Russell Coker.
	* Merged genhomedircon and semanage patches from Dan Walsh.
	* Merged remove add_local/set_local patch from Ivan Gyurdiev.

* Tue Jan 10 2006 Dan Walsh <dwalsh@redhat.com> 1.29.5-3
- Fixes for mls policy

* Tue Jan 10 2006 Dan Walsh <dwalsh@redhat.com> 1.29.5-2
- Update semanage and split out seobject
- Fix labeleing of home_root

* Thu Jan 5 2006 Dan Walsh <dwalsh@redhat.com> 1.29.5-1
- Update to match NSA
	* Added filename to semodule error reporting.

* Thu Jan 5 2006 Dan Walsh <dwalsh@redhat.com> 1.29.4-1
- Update to match NSA
	* Merged genhomedircon and semanage patch from Dan Walsh.
	* Changed semodule error reporting to include argv[0].

* Wed Jan 4 2006 Dan Walsh <dwalsh@redhat.com> 1.29.3-1
- Update to match NSA
	* Merged semanage getpwnam bug fix from Serge Hallyn (IBM).
	* Merged patch series from Ivan Gyurdiev.
	  This includes patches to:
	  - cleanup setsebool
	  - update setsebool to apply active booleans through libsemanage
	  - update semodule to use the new semanage_set_rebuild() interface
	  - fix various bugs in semanage
	* Merged patch from Dan Walsh (Red Hat).
	  This includes fixes for restorecon, chcat, fixfiles, genhomedircon,
	  and semanage.

* Mon Jan 2 2006 Dan Walsh <dwalsh@redhat.com> 1.29.2-10
- Fix restorecon to not say it is changing user section when -vv is specified

* Tue Dec 27 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-9
- Fixes for semanage, patch from Ivan and added a test script

* Sat Dec 24 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-8
- Fix getpwnam call

* Fri Dec 23 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-7
- Anaconda fixes

* Thu Dec 22 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-6
- Turn off try catch block to debug anaconda failure

* Tue Dec 20 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-5
- More fixes for chcat

* Tue Dec 20 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-4
- Add try catch for files that may not exists

* Mon Dec 19 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-3
- Remove commands from genhomedircon for installer

* Wed Dec 14 2005 Dan Walsh <dwalsh@redhat.com> 1.29.2-1
- Fix genhomedircon to work in installer
- Update to match NSA
	* Merged patch for chcat script from Dan Walsh.

* Fri Dec 9 2005 Dan Walsh <dwalsh@redhat.com> 1.29.1-2
- More fixes to chcat

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec 8 2005 Dan Walsh <dwalsh@redhat.com> 1.29.1-1
- Update to match NSA
	* Merged fix for audit2allow long option list from Dan Walsh.
	* Merged -r option for restorecon (alias for -R) from Dan Walsh.
	* Merged chcat script and man page from Dan Walsh.

* Wed Dec 7 2005 Dan Walsh <dwalsh@redhat.com> 1.28-1
- Update to match NSA
- Add gfs support

* Wed Dec 7 2005 Dan Walsh <dwalsh@redhat.com> 1.27.37-1
- Update to match NSA
- Add chcat to policycoreutils, adding +/- syntax
`
* Tue Dec 6 2005 Dan Walsh <dwalsh@redhat.com> 1.27.36-2
- Require new version of libsemanage

* Mon Dec 5 2005 Dan Walsh <dwalsh@redhat.com> 1.27.36-1
- Update to match NSA
	* Changed genhomedircon to warn on use of ROLE in homedir_template
	  if using managed policy, as libsemanage does not yet support it.

* Sun Dec 4 2005 Dan Walsh <dwalsh@redhat.com> 1.27.35-1
- Update to match NSA
	* Merged genhomedircon bug fix from Dan Walsh.
	* Revised semodule* man pages to refer to checkmodule and
	  to include example sections.

* Thu Dec 1 2005 Dan Walsh <dwalsh@redhat.com> 1.27.33-1
- Update to match NSA
	* Merged audit2allow --tefile and --fcfile support from Dan Walsh.
	* Merged genhomedircon fix from Dan Walsh.
	* Merged semodule* man pages from Dan Walsh, and edited them.
	* Changed setfiles to set the MATCHPATHCON_VALIDATE flag to
	  retain validation/canonicalization of contexts during init.

* Wed Nov 30 2005 Dan Walsh <dwalsh@redhat.com> 1.27.31-1
- Update to match NSA
	* Changed genhomedircon to always use user_r for the role in the
	  managed case since user_get_defrole is broken.
- Add te file capabilities to audit2allow
- Add man pages for semodule

* Tue Nov 29 2005 Dan Walsh <dwalsh@redhat.com> 1.27.30-1
- Update to match NSA
	* Merged sestatus, audit2allow, and semanage patch from Dan Walsh.
	* Fixed semodule -v option.

* Mon Nov 28 2005 Dan Walsh <dwalsh@redhat.com> 1.27.29-1
- Update to match NSA
	* Merged audit2allow python script from Dan Walsh.
	  (old script moved to audit2allow.perl, will be removed later).
	* Merged genhomedircon fixes from Dan Walsh.
	* Merged semodule quieting patch from Dan Walsh
	  (inverts default, use -v to restore original behavior).

* Thu Nov 17 2005 Dan Walsh <dwalsh@redhat.com> 1.27.28-3
- Audit2allow
	* Add more error checking
	* Add gen policy package
	* Add gen requires

* Wed Nov 16 2005 Dan Walsh <dwalsh@redhat.com> 1.27.28-2
- Update to match NSA
	* Merged genhomedircon rewrite from Dan Walsh.
- Rewrite audit2allow to python

* Mon Nov 14 2005 Dan Walsh <dwalsh@redhat.com> 1.27.27-5
- Fix genhomedircon to work with non libsemanage systems

* Fri Nov 11 2005 Dan Walsh <dwalsh@redhat.com> 1.27.27-3
- Patch genhomedircon to use libsemanage.py stuff

* Wed Nov 9 2005 Dan Walsh <dwalsh@redhat.com> 1.27.27-1
- Update to match NSA
	* Merged setsebool cleanup patch from Ivan Gyurdiev.

* Wed Nov 9 2005 Dan Walsh <dwalsh@redhat.com> 1.27.26-4
- Fix genhomedircon to use seusers file, temporary fix until swigified semanage

* Tue Nov 8 2005 Dan Walsh <dwalsh@redhat.com> 1.27.26-1
	* Added -B (--build) option to semodule to force a rebuild.
	* Reverted setsebool patch to call semanage_set_reload_bools().
	* Changed setsebool to disable policy reload and to call
	  security_set_boolean_list to update the runtime booleans.
	* Changed setfiles -c to use new flag to set_matchpathcon_flags()
	  to disable context translation by matchpathcon_init().

* Tue Nov 8 2005 Dan Walsh <dwalsh@redhat.com> 1.27.23-1
- Update to match NSA
	* Changed setfiles for the context canonicalization support.
	* Changed setsebool to call semanage_is_managed() interface
	  and fall back to security_set_boolean_list() if policy is
	  not managed.
	* Merged setsebool memory leak fix from Ivan Gyurdiev.
	* Merged setsebool patch to call semanage_set_reload_bools()
	  interface from Ivan Gyurdiev.

* Mon Nov 7 2005 Dan Walsh <dwalsh@redhat.com> 1.27.20-1
- Update to match NSA
	* Merged setsebool patch from Ivan Gyurdiev.
	  This moves setsebool from libselinux/utils to policycoreutils,
	  and rewrites it to use libsemanage for permanent boolean changes.

* Tue Oct 25 2005 Dan Walsh <dwalsh@redhat.com> 1.27.19-2
- Rebuild to use latest libselinux, libsemanage, and libsepol

* Tue Oct 25 2005 Dan Walsh <dwalsh@redhat.com> 1.27.19-1
- Update to match NSA
	* Merged semodule support for reload, noreload, and store options
	  from Joshua Brindle.
	* Merged semodule_package rewrite from Joshua Brindle.

* Thu Oct 20 2005 Dan Walsh <dwalsh@redhat.com> 1.27.18-1
- Update to match NSA
	* Cleaned up usage and error messages and releasing of memory by
   	  semodule_* utilities.
	* Corrected error reporting by semodule.
	* Updated semodule_expand for change to sepol interface.
	* Merged fixes for make DESTDIR= builds from Joshua Brindle.

* Tue Oct 18 2005 Dan Walsh <dwalsh@redhat.com> 1.27.14-1
- Update to match NSA
	* Updated semodule_package for sepol interface changes.

* Tue Oct 18 2005 Dan Walsh <dwalsh@redhat.com> 1.27.13-1
- Update to match NSA
	* Updated semodule_expand/link for sepol interface changes.

* Sat Oct 15 2005 Dan Walsh <dwalsh@redhat.com> 1.27.12-1
- Update to match NSA
	* Merged non-PAM Makefile support for newrole and run_init from Timothy Wood.

* Fri Oct 14 2005 Dan Walsh <dwalsh@redhat.com> 1.27.11-1
- Update to match NSA
	* Updated semodule_expand to use get interfaces for hidden sepol_module_package type.
	* Merged newrole and run_init pam config patches from Dan Walsh (Red Hat).
	* Merged fixfiles patch from Dan Walsh (Red Hat).
	* Updated semodule for removal of semanage_strerror.

* Thu Oct 13 2005 Dan Walsh <dwalsh@redhat.com> 1.27.7-2
- Fix run_init.pamd and spec file

* Wed Oct 12 2005 Dan Walsh <dwalsh@redhat.com> 1.27.7-1
- Update to match NSA
	* Updated semodule_link and semodule_expand to use shared libsepol.
	Fixed audit2why to call policydb_init prior to policydb_read (still
	uses the static libsepol).

* Mon Oct 10 2005 Dan Walsh <dwalsh@redhat.com> 1.27.6-1
- Update to match NSA
	* Updated for changes to libsepol.
	Changed semodule and semodule_package to use the shared libsepol.
	Disabled build of semodule_link and semodule_expand for now.
	Updated audit2why for relocated policydb internal headers,
	still needs to be converted to a shared lib interface.

* Fri Oct 6 2005 Dan Walsh <dwalsh@redhat.com> 1.27.5-3
- Update newrole pam file to remove pam-stack
- Update run_init pam file to remove pam-stack

* Thu Oct 6 2005 Dan Walsh <dwalsh@redhat.com> 1.27.5-1
- Update to match NSA
	* Fixed warnings in load_policy.
	* Rewrote load_policy to use the new selinux_mkload_policy()
	interface provided by libselinux.

* Wed Oct 5 2005 Dan Walsh <dwalsh@redhat.com> 1.27.3-2
- Rebuild with newer libararies

* Wed Sep 28 2005 Dan Walsh <dwalsh@redhat.com> 1.27.3-1
- Update to match NSA
	* Merged patch to update semodule to the new libsemanage API
	and improve the user interface from Karl MacMillan (Tresys).
	* Modified semodule for the create/connect API split.

* Wed Sep 28 2005 Dan Walsh <dwalsh@redhat.com> 1.27.2-2
- More fixes to stop find from following nfs paths

* Wed Sep 21 2005 Dan Walsh <dwalsh@redhat.com> 1.27.2-1
- Update to match NSA
	* Merged run_init open_init_pty bug fix from Manoj Srivastava
	  (unblock SIGCHLD).  Bug reported by Erich Schubert.

* Tue Sep 20 2005 Dan Walsh <dwalsh@redhat.com> 1.27.1-1
- Update to match NSA
	* Merged error shadowing bug fix for restorecon from Dan Walsh.
	* Merged setfiles usage/man page update for -r option from Dan Walsh.
	* Merged fixfiles -C patch to ignore :s0 addition on update
	  to a MCS/MLS policy from Dan Walsh.

* Thu Sep 15 2005 Dan Walsh <dwalsh@redhat.com> 1.26-3
- Add chcat script for use with chcon.

* Tue Sep 13 2005 Dan Walsh <dwalsh@redhat.com> 1.26-2
- Fix restorecon to exit with error code

* Mon Sep 12 2005 Dan Walsh <dwalsh@redhat.com> 1.26-1
	* Updated version for release.

* Tue Sep 6 2005 Dan Walsh <dwalsh@redhat.com> 1.25.9-2
- Add prereq for mount command

* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 1.25.9-1
- Update to match NSA
	* Changed setfiles -c to translate the context to raw format
	prior to calling libsepol.

* Fri Aug 26 2005 Dan Walsh <dwalsh@redhat.com> 1.25.7-3
- Use new version of libsemange and require it for install

* Fri Aug 26 2005 Dan Walsh <dwalsh@redhat.com> 1.25.7-2
- Ignore s0 in file context

* Thu Aug 25 2005 Dan Walsh <dwalsh@redhat.com> 1.25.7-1
- Update to match NSA
	* Merged patch for fixfiles -C from Dan Walsh.

* Tue Aug 23 2005 Dan Walsh <dwalsh@redhat.com> 1.25.6-1
- Update to match NSA
	* Merged fixes for semodule_link and sestatus from Serge Hallyn (IBM).
	  Bugs found by Coverity.

* Mon Aug 22 2005 Dan Walsh <dwalsh@redhat.com> 1.25.5-3
- Fix fixfiles to call sort -u followed by sort -d.

* Wed Aug 17 2005 Dan Walsh <dwalsh@redhat.com> 1.25.5-2
- Change fixfiles to ignore /home directory on updates

* Fri Aug 5 2005 Dan Walsh <dwalsh@redhat.com> 1.25.5-1
- Update to match NSA
	* Merged patch to move module read/write code from libsemanage
	  to libsepol from Jason Tang (Tresys).

* Thu Jul 28 2005 Dan Walsh <dwalsh@redhat.com> 1.25.4-1
- Update to match NSA
	* Changed semodule* to link with libsemanage.

* Wed Jul 27 2005 Dan Walsh <dwalsh@redhat.com> 1.25.3-1
- Update to match NSA
	* Merged restorecon patch from Ivan Gyurdiev.

* Mon Jul 18 2005 Dan Walsh <dwalsh@redhat.com> 1.25.2-1
- Update to match NSA
	* Merged load_policy, newrole, and genhomedircon patches from Red Hat.

* Thu Jul 7 2005 Dan Walsh <dwalsh@redhat.com> 1.25.1-1
- Update to match NSA
	* Merged loadable module support from Tresys Technology.

* Wed Jun 29 2005 Dan Walsh <dwalsh@redhat.com> 1.24-1
- Update to match NSA
	* Updated version for release.

* Tue Jun 14 2005 Dan Walsh <dwalsh@redhat.com> 1.23.11-4
- Fix Ivan's patch for user role changes

* Sat May 28 2005 Dan Walsh <dwalsh@redhat.com> 1.23.11-3
- Add Ivan's patch for user role changes in genhomedircon

* Thu May 26 2005 Dan Walsh <dwalsh@redhat.com> 1.23.11-2
- Fix warning message on reload of booleans

* Fri May 20 2005 Dan Walsh <dwalsh@redhat.com> 1.23.11-1
- Update to match NSA
	* Merged fixfiles and newrole patch from Dan Walsh.
	* Merged audit2why man page from Dan Walsh.

* Thu May 19 2005 Dan Walsh <dwalsh@redhat.com> 1.23.10-2
- Add call to pam_acct_mgmt in newrole.

* Tue May 17 2005 Dan Walsh <dwalsh@redhat.com> 1.23.10-1
- Update to match NSA
	* Extended audit2why to incorporate booleans and local user
	  settings when analyzing audit messages.

* Mon May 16 2005 Dan Walsh <dwalsh@redhat.com> 1.23.9-1
- Update to match NSA
	* Updated audit2why for sepol_ prefixes on Flask types to
	  avoid namespace collision with libselinux, and to
	  include <selinux/selinux.h> now.

* Fri May 13 2005 Dan Walsh <dwalsh@redhat.com> 1.23.8-1
- Fix fixfiles to accept -f
- Update to match NSA
	* Added audit2why utility.

* Fri Apr 29 2005 Dan Walsh <dwalsh@redhat.com> 1.23.7-1
- Change -f flag in fixfiles to remove stuff from /tmp
- Change -F flag to pass -F flag  to restorecon/fixfiles.  (IE Force relabel).

* Thu Apr 14 2005 Dan Walsh <dwalsh@redhat.com> 1.23.6-1
- Update to match NSA
	* Fixed signed/unsigned pointer bug in load_policy.
	* Reverted context validation patch for genhomedircon.

* Wed Apr 13 2005 Dan Walsh <dwalsh@redhat.com> 1.23.5-1
- Update to match NSA
	* Reverted load_policy is_selinux_enabled patch from Dan Walsh.
	  Otherwise, an initial policy load cannot be performed using
	  load_policy, e.g. for anaconda.

* Mon Apr 11 2005 Dan Walsh <dwalsh@redhat.com> 1.23.4-3
- remove is_selinux_enabled check from load_policy  (Bad idea)

* Mon Apr 11 2005 Dan Walsh <dwalsh@redhat.com> 1.23.4-1
- Update to version from NSA
	* Merged load_policy is_selinux_enabled patch from Dan Walsh.
	* Merged restorecon verbose output patch from Dan Walsh.
	* Merged setfiles altroot patch from Chris PeBenito.

* Thu Apr 7 2005 Dan Walsh <dwalsh@redhat.com> 1.23.3-2
- Don't run load_policy on a non SELinux kernel.

* Wed Apr 6 2005 Dan Walsh <dwalsh@redhat.com> 1.23.3-1
- Update to version from NSA
        * Merged context validation patch for genhomedircon from Eric Paris.
- Fix verbose output of restorecon

* Thu Mar 17 2005 Dan Walsh <dwalsh@redhat.com> 1.23.2-1
- Update to version from NSA
	* Changed setfiles -c to call set_matchpathcon_flags(3) to
	  turn off processing of .homedirs and .local.

* Tue Mar 15 2005 Dan Walsh <dwalsh@redhat.com> 1.23.1-1
- Update to released version from NSA
	* Merged rewrite of genhomedircon by Eric Paris.
	* Changed fixfiles to relabel jfs since it now supports security xattrs
	  (as of 2.6.11).  Removed reiserfs until 2.6.12 is released with
	  fixed support for reiserfs and selinux.

* Thu Mar 10 2005 Dan Walsh <dwalsh@redhat.com> 1.22-2
- Update to released version from NSA
- Patch genhomedircon to handle passwd in different places.

* Wed Mar 9 2005 Dan Walsh <dwalsh@redhat.com> 1.21.22-2
- Fix genhomedircon to not put bad userad error in file_contexts.homedir

* Tue Mar 8 2005 Dan Walsh <dwalsh@redhat.com> 1.21.22-1
- Cleanup error reporting

* Tue Mar 1 2005 Dan Walsh <dwalsh@redhat.com> 1.21.21-1
	* Merged load_policy and genhomedircon patch from Dan Walsh.

* Mon Feb 28 2005 Dan Walsh <dwalsh@redhat.com> 1.21.20-3
- Fix genhomedircon to add extr "\n"

* Fri Feb 24 2005 Dan Walsh <dwalsh@redhat.com> 1.21.20-2
- Fix genhomedircon to handle blank users

* Fri Feb 24 2005 Dan Walsh <dwalsh@redhat.com> 1.21.20-1
- Update to latest from NSA
- Add call to libsepol

* Thu Feb 23 2005 Dan Walsh <dwalsh@redhat.com> 1.21.19-4
- Fix genhomedircon to handle root
- Fix fixfiles to better handle file system types

* Wed Feb 23 2005 Dan Walsh <dwalsh@redhat.com> 1.21.19-2
- Fix genhomedircon to handle spaces in SELINUXPOLICYTYPE

* Tue Feb 22 2005 Dan Walsh <dwalsh@redhat.com> 1.21.19-1
- Update to latest from NSA
        * Merged several fixes from Ulrich Drepper.

* Mon Feb 21 2005 Dan Walsh <dwalsh@redhat.com> 1.21.18-2
- Apply Uli patch
	* The Makefiles should use the -Wall option even if compiled in beehive
	* Add -W, too
	* use -Werror when used outside of beehive.  This could also be used unconditionally
	* setfiles/setfiles.c: fix resulting warning
	* restorecon/restorecon.c: Likewise
	* run_init/open_init_pty.c: argc hasn't been checked, the program would crash if
called without parameters.  ignore the return value of nice properly.
	* run_init: don't link with -ldl lutil
	* load_policy: that's the bad bug.  pointer to unsigned int is passed, size_t is
written to.  fails on 64-bit archs
	* sestatus: signed vs unsigned problem
	* newrole: don't link with -ldl

* Sat Feb 19 2005 Dan Walsh <dwalsh@redhat.com> 1.21.18-1
- Update to latest from NSA
	* Changed load_policy to fall back to the original policy upon
	  an error from sepol_genusers().

* Thu Feb 17 2005 Dan Walsh <dwalsh@redhat.com> 1.21.17-2
- Only restorecon on ext[23], reiser and xfs

* Thu Feb 17 2005 Dan Walsh <dwalsh@redhat.com> 1.21.17-1
- Update to latest from NSA
	* Merged new genhomedircon script from Dan Walsh.
	* Changed load_policy to call sepol_genusers().

* Thu Feb 17 2005 Dan Walsh <dwalsh@redhat.com> 1.21.15-9
- Remove Red Hat rhpl usage
- Add back in original syntax
- Update man page to match new syntax

* Fri Feb 11 2005 Dan Walsh <dwalsh@redhat.com> 1.21.15-8
- Fix genhomedircon regular expression
- Fix exclude in restorecon

* Thu Feb 10 2005 Dan Walsh <dwalsh@redhat.com> 1.21.15-5
- Trap failure on write
- Rewrite genhomedircon to generate file_context.homedirs
- several passes

* Thu Feb 10 2005 Dan Walsh <dwalsh@redhat.com> 1.21.15-1
- Update from NSA
	* Changed relabel Makefile target to use restorecon.

* Wed Feb 9 2005 Dan Walsh <dwalsh@redhat.com> 1.21.14-1
- Update from NSA
	* Merged restorecon patch from Dan Walsh.

* Tue Feb 8 2005 Dan Walsh <dwalsh@redhat.com> 1.21.13-1
- Update from NSA
	* Merged further change to fixfiles -C from Dan Walsh.
	* Merged updated fixfiles script from Dan Walsh.
- Fix error handling of restorecon

* Mon Feb 7 2005 Dan Walsh <dwalsh@redhat.com> 1.21.12-2
- Fix sestatus for longer booleans

* Wed Feb 2 2005 Dan Walsh <dwalsh@redhat.com> 1.21.12-1
- More cleanup of fixfiles sed patch
	* Merged further patches for restorecon/setfiles -e and fixfiles -C.

* Wed Feb 2 2005 Dan Walsh <dwalsh@redhat.com> 1.21.10-2
- More cleanup of fixfiles sed patch

* Mon Jan 31 2005 Dan Walsh <dwalsh@redhat.com> 1.21.10-1
- More cleanup of fixfiles sed patch
- Upgrade to latest from NSA
	* Merged patch for open_init_pty from Manoj Srivastava.

* Fri Jan 28 2005 Dan Walsh <dwalsh@redhat.com> 1.21.9-1
- More cleanup of sed patch
- Upgrade to latest from NSA
	* Merged updated fixfiles script from Dan Walsh.
	* Merged updated man page for fixfiles from Dan Walsh and re-added unzipped.
	* Reverted fixfiles patch for file_contexts.local;
	  obsoleted by setfiles rewrite.
	* Merged error handling patch for restorecon from Dan Walsh.
	* Merged semi raw mode for open_init_pty helper from Manoj Srivastava.
	* Rewrote setfiles to use matchpathcon and the new interfaces
	  exported by libselinux (>= 1.21.5).

* Fri Jan 28 2005 Dan Walsh <dwalsh@redhat.com> 1.21.7-3
- Fix fixfiles patch
- Upgrade to latest from NSA
	* Prevent overflow of spec array in setfiles.
- Add diff comparason between file_contexts to fixfiles
- Allow restorecon to give an warning on file not found instead of exiting

* Thu Jan 27 2005 Dan Walsh <dwalsh@redhat.com> 1.21.5-1
- Upgrade to latest from NSA
	* Merged newrole -l support from Darrel Goeddel (TCS).
- Fix genhomedircon STARTING_UID

* Wed Jan 26 2005 Dan Walsh <dwalsh@redhat.com> 1.21.4-1
- Upgrade to latest from NSA
	* Merged fixfiles patch for file_contexts.local from Dan Walsh.

* Fri Jan 20 2005 Dan Walsh <dwalsh@redhat.com> 1.21.3-2
- Temp file needs to be created in /etc/selinux/POLICYTYPE/contexts/files/ directory.

* Fri Jan 20 2005 Dan Walsh <dwalsh@redhat.com> 1.21.3-1
- Upgrade to latest from NSA
	* Fixed restorecon to not treat errors from is_context_customizable()
	  as a customizable context.
	* Merged setfiles/restorecon patch to not reset user field unless
	  -F option is specified from Dan Walsh.
	* Merged open_init_pty helper for run_init from Manoj Srivastava.
	* Merged audit2allow and genhomedircon man pages from Manoj Srivastava.

* Fri Jan 20 2005 Dan Walsh <dwalsh@redhat.com> 1.21.1-3
- Don't change user componant if it is all that changed unless forced.
- Change fixfiles to concatinate file_context.local for setfiles

* Thu Jan 20 2005 Dan Walsh <dwalsh@redhat.com> 1.21.1-1
- Update to latest from NSA

* Mon Jan 10 2005 Dan Walsh <dwalsh@redhat.com> 1.20.1-2
- Fix restorecon segfault

* Mon Jan 3 2005 Dan Walsh <dwalsh@redhat.com> 1.20.1-1
- Update to latest from NSA
	* Merged fixfiles rewrite from Dan Walsh.
	* Merged restorecon patch from Dan Walsh.

* Mon Jan 3 2005 Dan Walsh <dwalsh@redhat.com> 1.19.3-1
- Update to latest from NSA
	* Merged fixfiles and restorecon patches from Dan Walsh.
	* Don't display change if only user part changed.

* Mon Jan 3 2005 Dan Walsh <dwalsh@redhat.com> 1.19.2-4
- Fix fixfiles handling of rpm
- Fix restorecon to not warn on symlinks unless -v -v
- Fix output of verbose to show old context as well as new context

* Mon Dec 29 2004 Dan Walsh <dwalsh@redhat.com> 1.19.2-1
- Update to latest from NSA
	* Changed restorecon to ignore ENOENT errors from matchpathcon.
	* Merged nonls patch from Chris PeBenito.

* Mon Dec 20 2004 Dan Walsh <dwalsh@redhat.com> 1.19.1-1
- Update to latest from NSA
	* Removed fixfiles.cron.
	* Merged run_init.8 patch from Dan Walsh.

* Thu Nov 18 2004 Dan Walsh <dwalsh@redhat.com> 1.18.1-3
- Fix run_init.8 to refer to correct location of initrc_context

* Wed Nov 3 2004 Dan Walsh <dwalsh@redhat.com> 1.18.1-1
- Upgrade to latest from NSA

* Wed Oct 27 2004 Steve Grubb <sgrubb@redhat.com> 1.17.7-3
- Add code to sestatus to output the current policy from config file

* Fri Oct 22 2004 Dan Walsh <dwalsh@redhat.com> 1.17.7-2
- Patch audit2allow to return self and no brackets if only one rule

* Fri Oct 22 2004 Dan Walsh <dwalsh@redhat.com> 1.17.7-1
- Update to latest from NSA
- Eliminate fixfiles.cron

* Tue Oct 12 2004 Dan Walsh <dwalsh@redhat.com> 1.17.6-2
- Only run fixfiles.cron once a week, and eliminate null message

* Fri Oct 1 2004 Dan Walsh <dwalsh@redhat.com> 1.17.6-1
- Update with NSA
	* Added -l option to setfiles to log changes via syslog.
	* Merged -e option to setfiles to exclude directories.
	* Merged -R option to restorecon for recursive descent.
* Fri Oct 1 2004 Dan Walsh <dwalsh@redhat.com> 1.17.5-6
- Add -e (exclude directory) switch to setfiles
- Add syslog to setfiles

* Fri Sep 24 2004 Dan Walsh <dwalsh@redhat.com> 1.17.5-5
- Add -R (recursive) switch to restorecon.

* Thu Sep 23 2004 Dan Walsh <dwalsh@redhat.com> 1.17.5-4
- Change to only display to terminal if tty is specified

* Tue Sep 21 2004 Dan Walsh <dwalsh@redhat.com> 1.17.5-3
- Only display to stdout if logfile not specified

* Mon Sep 9 2004 Dan Walsh <dwalsh@redhat.com> 1.17.5-2
- Add Steve Grubb patch to cleanup log files.

* Mon Aug 30 2004 Dan Walsh <dwalsh@redhat.com> 1.17.5-1
- Add optargs
- Update to match NSA

* Wed Aug 24 2004 Dan Walsh <dwalsh@redhat.com> 1.17.4-1
- Add fix to get cdrom info from /proc/media in fixfiles.

* Wed Aug 24 2004 Dan Walsh <dwalsh@redhat.com> 1.17.3-4
- Add Steve Grub patches for
	* Fix fixfiles.cron MAILTO
	* Several problems in sestatus

* Wed Aug 24 2004 Dan Walsh <dwalsh@redhat.com> 1.17.3-3
- Add -q (quiet) qualifier to load_policy to not report warnings

* Tue Aug 24 2004 Dan Walsh <dwalsh@redhat.com> 1.17.3-2
- Add requires for libsepol >= 1.1.1

* Tue Aug 24 2004 Dan Walsh <dwalsh@redhat.com> 1.17.3-1
- Update to latest from upstream

* Mon Aug 23 2004 Dan Walsh <dwalsh@redhat.com> 1.17.2-1
- Update to latest from upstream
- Includes Colin patch for verifying file_contexts

* Sun Aug 22 2004 Dan Walsh <dwalsh@redhat.com> 1.17.1-1
- Update to latest from upstream

* Mon Aug 16 2004 Dan Walsh <dwalsh@redhat.com> 1.15.7-1
- Update to latest from upstream

* Thu Aug 12 2004 Dan Walsh <dwalsh@redhat.com> 1.15.6-1
- Add Man page for load_policy

* Tue Aug 10 2004 Dan Walsh <dwalsh@redhat.com> 1.15.5-1
-  new version from NSA uses libsepol

* Mon Aug 2 2004 Dan Walsh <dwalsh@redhat.com> 1.15.3-2
- Fix genhomedircon join command

* Thu Jul 29 2004 Dan Walsh <dwalsh@redhat.com> 1.15.3-1
- Latest from NSA

* Mon Jul 26 2004 Dan Walsh <dwalsh@redhat.com> 1.15.2-4
- Change fixfiles to not change when running a check

* Tue Jul 20 2004 Dan Walsh <dwalsh@redhat.com> 1.15.2-3
- Fix restorecon getopt call to stop hang on IBM Arches

* Mon Jul 19 2004 Dan Walsh <dwalsh@redhat.com> 1.15.2-2
- Only mail files less than 100 lines from fixfiles.cron
- Add Russell's fix for genhomedircon

* Fri Jul 16 2004 Dan Walsh <dwalsh@redhat.com> 1.15.2-1
- Latest from NSA

* Thu Jul 8 2004 Dan Walsh <dwalsh@redhat.com> 1.15.1-2
- Add ro warnings

* Thu Jul 8 2004 Dan Walsh <dwalsh@redhat.com> 1.15.1-1
- Latest from NSA
- Fix fixfiles.cron to delete outfile

* Tue Jul 6 2004 Dan Walsh <dwalsh@redhat.com> 1.14.1-2
- Fix fixfiles.cron to not run on non SELinux boxes
- Fix several problems in fixfiles and fixfiles.cron

* Wed Jun 30 2004 Dan Walsh <dwalsh@redhat.com> 1.14.1-1
- Update from NSA
- Add cron capability to fixfiles

* Fri Jun 25 2004 Dan Walsh <dwalsh@redhat.com> 1.13.4-1
- Update from NSA

* Thu Jun 24 2004 Dan Walsh <dwalsh@redhat.com> 1.13.3-2
- Fix fixfiles to handle no rpm file on relabel

* Wed Jun 23 2004 Dan Walsh <dwalsh@redhat.com> 1.13.3-1
- Update latest from NSA
- Add -o option to setfiles to save output of any files with incorrect context.

* Tue Jun 22 2004 Dan Walsh <dwalsh@redhat.com> 1.13.2-2
- Add rpm support to fixfiles
- Update restorecon to add file input support

* Fri Jun 18 2004 Dan Walsh <dwalsh@redhat.com> 1.13.2-1
- Update with NSA Latest

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jun 12 2004 Dan Walsh <dwalsh@redhat.com> 1.13.1-2
- Fix run_init to use policy formats

* Wed Jun 2 2004 Dan Walsh <dwalsh@redhat.com> 1.13.1-1
- Update from NSA

* Tue May 25 2004 Dan Walsh <dwalsh@redhat.com> 1.13-3
- Change location of file_context file

* Tue May 25 2004 Dan Walsh <dwalsh@redhat.com> 1.13-2
- Change to use /etc/sysconfig/selinux to determine location of policy files

* Fri May 21 2004 Dan Walsh <dwalsh@redhat.com> 1.13-1
- Update to latest from NSA
- Change fixfiles to prompt before deleteing /tmp files

* Tue May 18 2004 Dan Walsh <dwalsh@redhat.com> 1.12-2
- have restorecon ingnore <<none>>
- Hand matchpathcon the file status

* Thu May 14 2004 Dan Walsh <dwalsh@redhat.com> 1.12-1
- Update to match NSA

* Mon May 10 2004 Dan Walsh <dwalsh@redhat.com> 1.11-4
- Move location of log file to /var/tmp

* Mon May 10 2004 Dan Walsh <dwalsh@redhat.com> 1.11-3
- Better grep command for bind

* Fri May 7 2004 Dan Walsh <dwalsh@redhat.com> 1.11-2
- Eliminate bind and context mounts

* Wed May 5 2004 Dan Walsh <dwalsh@redhat.com> 1.11-1
- update to match NSA

* Wed Apr 28 2004 Dan Walsh <dwalsh@redhat.com> 1.10-4
- Log fixfiles to the /tmp directory

* Wed Apr 21 2004 Colin Walters <walters@redhat.com> 1.10-3
- Add patch to fall back to authenticating via uid if
  the current user's SELinux user identity is the default
  identity
- Add BuildRequires pam-devel

* Mon Apr 12 2004 Dan Walsh <dwalsh@redhat.com> 1.10-2
- Add man page, thanks to Richard Halley

* Thu Apr 8 2004 Dan Walsh <dwalsh@redhat.com> 1.10-1
- Upgrade to latest from NSA

* Fri Apr 2 2004 Dan Walsh <dwalsh@redhat.com> 1.9.2-1
- Update with latest from gentoo and NSA

* Thu Apr 1 2004 Dan Walsh <dwalsh@redhat.com> 1.9.1-1
- Check return codes in sestatus.c

* Mon Mar 29 2004 Dan Walsh <dwalsh@redhat.com> 1.9-19
- Fix sestatus to not double free
- Fix sestatus.conf to be unix format

* Mon Mar 29 2004 Dan Walsh <dwalsh@redhat.com> 1.9-18
- Warn on setfiles failure to relabel.

* Mon Mar 29 2004 Dan Walsh <dwalsh@redhat.com> 1.9-17
- Updated version of sestatus

* Mon Mar 29 2004 Dan Walsh <dwalsh@redhat.com> 1.9-16
- Fix fixfiles to checklabel properly

* Fri Mar 26 2004 Dan Walsh <dwalsh@redhat.com> 1.9-15
- add sestatus

* Thu Mar 25 2004 Dan Walsh <dwalsh@redhat.com> 1.9-14
- Change free call to freecon
- Cleanup

* Tue Mar 23 2004 Dan Walsh <dwalsh@redhat.com> 1.9-12
- Remove setfiles-assoc patch
- Fix restorecon to not crash on missing dir

* Thu Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-11
- Eliminate trailing / in restorecon

* Thu Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-10
- Add Verbosity check

* Thu Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-9
- Change restorecon to not follow symlinks.  It is too difficult and confusing
- to figure out the file context for the file pointed to by a symlink.

* Wed Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-8
- Fix restorecon
* Wed Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-7
- Read restorecon patch

* Wed Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-6
- Change genhomedircon to take POLICYSOURCEDIR from command line

* Wed Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-5
- Add checkselinux
- move fixfiles and restorecon to /sbin

* Wed Mar 17 2004 Dan Walsh <dwalsh@redhat.com> 1.9-4
- Restore patch of genhomedircon

* Mon Mar 15 2004 Dan Walsh <dwalsh@redhat.com> 1.9-3
- Add setfiles-assoc patch to try to freeup memory use

* Mon Mar 15 2004 Dan Walsh <dwalsh@redhat.com> 1.9-2
- Add fixlabels

* Mon Mar 15 2004 Dan Walsh <dwalsh@redhat.com> 1.9-1
- Update to latest from NSA

* Wed Mar 10 2004 Dan Walsh <dwalsh@redhat.com> 1.6-8
- Increase the size of buffer accepted by setfiles to BUFSIZ.

* Tue Mar 9 2004 Dan Walsh <dwalsh@redhat.com> 1.6-7
- genhomedircon should complete even if it can't read /etc/default/useradd

* Tue Mar 9 2004 Dan Walsh <dwalsh@redhat.com> 1.6-6
- fix restorecon to relabel unlabled files.

* Fri Mar 5 2004 Dan Walsh <dwalsh@redhat.com> 1.6-5
- Add genhomedircon from tresys
- Fixed patch for restorecon

* Thu Feb 26 2004 Dan Walsh <dwalsh@redhat.com> 1.6-4
- exit out when selinux is not enabled

* Thu Feb 26 2004 Dan Walsh <dwalsh@redhat.com> 1.6-3
- Fix minor bugs in restorecon

* Thu Feb 26 2004 Dan Walsh <dwalsh@redhat.com> 1.6-2
- Add restorecon c program

* Tue Feb 24 2004 Dan Walsh <dwalsh@redhat.com> 1.6-1
- Update to latest tarball from NSA

* Thu Feb 19 2004 Dan Walsh <dwalsh@redhat.com> 1.4-9
- Add sort patch

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004 Dan Walsh <dwalsh@redhat.com> 1.4-7
- remove mods to run_init since init scripts don't require it anymore

* Wed Jan 28 2004 Dan Walsh <dwalsh@redhat.com> 1.4-6
- fix genhomedircon not to return and error

* Wed Jan 28 2004 Dan Walsh <dwalsh@redhat.com> 1.4-5
- add setfiles quiet patch

* Tue Jan 27 2004 Dan Walsh <dwalsh@redhat.com> 1.4-4
- add checkcon to verify context match file_context

* Wed Jan 7 2004 Dan Walsh <dwalsh@redhat.com> 1.4-3
- fix command parsing restorecon

* Tue Jan 6 2004 Dan Walsh <dwalsh@redhat.com> 1.4-2
- Add restorecon

* Sat Dec 6 2003 Dan Walsh <dwalsh@redhat.com> 1.4-1
- Update to latest NSA 1.4

* Tue Nov 25 2003 Dan Walsh <dwalsh@redhat.com> 1.2-9
- Change run_init.console to run as run_init_t

* Tue Oct 14 2003 Dan Walsh <dwalsh@redhat.com> 1.2-8
- Remove dietcc since load_policy is not in mkinitrd
- Change to use CONSOLEHELPER flag

* Tue Oct 14 2003 Dan Walsh <dwalsh@redhat.com> 1.2-7
- Don't authenticate run_init when used with consolehelper

* Wed Oct 01 2003 Dan Walsh <dwalsh@redhat.com> 1.2-6
- Add run_init consolehelper link

* Wed Sep 24 2003 Dan Walsh <dwalsh@redhat.com> 1.2-5
- Add russell spead up patch to deal with file path stems

* Fri Sep 12 2003 Dan Walsh <dwalsh@redhat.com> 1.2-4
- Build load_policy with diet gcc in order to save space on initrd

* Fri Sep 12 2003 Dan Walsh <dwalsh@redhat.com> 1.2-3
- Update with NSA latest

* Thu Aug 7 2003 Dan Walsh <dwalsh@redhat.com> 1.2-1
- remove i18n
- Temp remove gtk support

* Thu Aug 7 2003 Dan Walsh <dwalsh@redhat.com> 1.1-4
- Remove wnck requirement

* Thu Aug 7 2003 Dan Walsh <dwalsh@redhat.com> 1.1-3
- Add gtk support to run_init

* Tue Aug 5 2003 Dan Walsh <dwalsh@redhat.com> 1.1-2
- Add internationalization

* Mon Jun 2 2003 Dan Walsh <dwalsh@redhat.com> 1.0-1
- Initial version

