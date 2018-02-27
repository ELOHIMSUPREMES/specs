%define _altdata_dir %_datadir/alterator

Name: alterator-snort
Version: 0.3.3
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for snort administration
Packager: Mikhail Efremov <sem@altlinux.org>
Source: %name-%version.tar

Requires: alterator >= 4.10-alt8 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4
Requires: alterator-service-functions
Requires: snort barnyard2-mysql snort-rules
Requires: oinkmaster wget
Requires: alterator-l10n >= 2.8-alt4
Requires: fail2ban >= 0.8.13

BuildPreReq: alterator >= 4.10-alt8
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for snort administration.

%prep
%setup -q

%build
%make_build

%install
%makeinstall
mkdir -p %buildroot/%_sysconfdir/cron.d/
touch %buildroot/%_sysconfdir/cron.d/%name
touch %buildroot/%_sysconfdir/cron.d/%name-notifications
mkdir -p %buildroot/%_sysconfdir/sysconfig/
touch %buildroot/%_sysconfdir/sysconfig/%name
mkdir -p %buildroot/%_datadir/alterator-snort/
install -m644 tools/base_conf.php %buildroot/%_datadir/alterator-snort/

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*
%_libexecdir/%name/
%ghost %_sysconfdir/cron.d/%name
%ghost %_sysconfdir/cron.d/%name-notifications
%_sysconfdir/sysconfig/%name
%_datadir/alterator-snort
%_datadir/alterator-snort/base_conf.php

%changelog
* Tue Jul 22 2014 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Use alterator-service-functions.
- reset-snort-db.sh: Fix password setup.

* Wed Jul 16 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt2
- Require snort.

* Mon Jun 30 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.2-alt1
- Grant UPDATE,DELETE for all database

* Fri Jun 27 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.1-alt2
- Add Req: fail2ban

* Wed Jun 25 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.1-alt1
- Mod reset-snort-db.sh

* Wed Jun 25 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.0-alt1
- Add notifications page
- Add ban and banned page
- Add base page
- Add configuration page
- Mod rules page

* Wed May 28 2014 Timur Aitov <timonbl4@altlinux.org> 0.2.5-alt1
- Fix download rules by oinkcode

* Wed May 28 2014 Timur Aitov <timonbl4@altlinux.org> 0.2.4-alt2
- Remove Req: MySQL-server, MySQL-client

* Mon Feb 18 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.4-alt1
- Get password for mysql from barnyard config

* Fri Jan 25 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.3-alt3
- Add barnyard2-mysql requires (instead snort-mysql)

* Thu Dec 23 2010 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt2
- Add wget requires (for oinkmaster).

* Wed Dec 22 2010 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Use user 'snort' for access to mysql database.

* Fri Dec 11 2009 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- require alterator-l10n.
- change desktop entry category.

* Thu Nov 05 2009 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- use timestamp in UTC.
- disable 'auto_update' checkbox if no url selected.

* Tue Nov 03 2009 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- package cron file as ghost.

* Mon Nov 02 2009 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- added 'Custom URL' field.
- use '-U' option for oinkmaster.
- added cron settings.

* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- enable mysqld service when snort started.
- reset-snort-db.sh: added 'host=localhost' to output plugin
  configuration.

* Thu Oct 22 2009 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- UI improved.
- fix typo.
- reset-snort-db.sh: fix return code.

* Tue Oct 20 2009 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- script reset-snort-db.sh is added.
- fix enabled/disabled state displaying.
- fix snortd restart.
- skip 'on' value in details list.

* Mon Oct 19 2009 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- initial release



