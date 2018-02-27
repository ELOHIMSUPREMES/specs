%define _hooksdir %_sysconfdir/hooks/hostname.d

Name: alterator-ldap-groups
Version: 0.6.4
Release: alt1

Source: %name-%version.tar

Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: Alterator module for LDAP groups administration
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Requires: alterator >= 2.9 ldap-user-tools >= 0.8.3 alterator-auth >= 0.9-alt3
Requires: alterator-sh-functions >= 0.11-alt2
Requires: shadow-groups >= 4.0.4.1-alt9
Requires: alterator-l10n >= 2.7-alt6

Conflicts: alterator-fbi < 0.16-alt2
Obsoletes: alterator-ldap-groups-school-server < %version
Provides:  alterator-ldap-groups-school-server = %version-%release

BuildPreReq: alterator >= 3.2-alt3 
BuildRequires: alterator-l10n alterator-fbi

%description
Alterator module for LDAP groups administration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%config(noreplace) %_sysconfdir/alterator/ldap-groups
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*
%_datadir/alterator/type/*
%_hooksdir/91-ldap-groups

%changelog
* Mon Jun 10 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1
- No wrap checkbox text
- Localization support for system group combobox

* Thu Jun 06 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.3-alt1
- Add mapping to system UNIX and Samba group

* Fri May 31 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt3
- Fix button look by use standard definition

* Tue Apr 23 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt2
- Disable show of group flags (default, local)
- Don't distribute button in source selection

* Thu Nov 01 2012 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt1
- Support empty lines and comments beginning from # in group-init-list
- Add groups 'users' and 'admins' for NT domain

* Thu Oct 25 2012 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- Move init script from firsttime.d to hostname.d hooks directory.
  Please, run /etc/hooks/hostname.d/91-ldap-groups manually
  to create initial groups for existing domain (ALT #24494)
- Obsoletes alterator-ldap-groups-school-server package
- Hide registered workstations groups (with trailing $)
- Support School Server specific default groups. If they are
  unnecessary, just remove it manually

* Wed Dec 15 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt2
- Released as  0.6-alt2 for test

* Wed Nov 24 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt1
- Manage local and LDAP groups.

* Fri Apr 02 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.5-alt1
- Redesigned membership.
- Fixed bug with space in group name.

* Mon Oct 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- fix typo in desktop file

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- show message on successful update

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- redesign email and member edition
- use workflow 'none'

* Wed Sep 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- move hook into firsttime.d
- improve html ui (closes: #21566)
- use constraints for e-mail (closes: #21400)

* Wed Sep 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add initial group list (closes: #21222)

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt5.1
- added requires alterator-l10n and alterator-fbi
- fixed group_del

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt5
- improved ui management
- added multiple group deletion

* Thu May 14 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt4.1
- fixed #19971
- fixed #19954

* Thu May 07 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt4
- fixed #19932: multiple select of users

* Mon May 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt3
- fixed #19880 (ldap groups with space in name)

* Thu Apr 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2
- rewrote error handling

* Mon Apr 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt1
- initial build
