# ISBC package is disabled because the module is not packaged
%def_disable isbc

Name: pkcs11-profiles
Version: 0.1.5
Release: alt2

Summary: Set of scripts and profiles for PAM PKCS11 configuration
License: GPLv3+
Group: System/Configuration/Other

Conflicts: pam_pkcs11 < 0.6.9-alt30

Source0: %name-%version.tar

%description
%summary

%package common
Summary: Control scripts for profile-based PAM PKCS11 configuration
License: GPLv3+
Group: System/Configuration/Other
BuildArch: noarch

%description common
Control scripts for profile-based PAM PKCS11 configuration.

%ifnarch aarch64
%package rutokenecp
Summary: RuToken ECP PAM PKCS11 module configuration
License: GPLv3+
Group: System/Configuration/Other
Requires: %name-common = %version-%release
Requires: pam_pkcs11 >= 0.6.9-alt9
Requires: librtpkcs11ecp >= 1.5.3.0-alt4

%description rutokenecp
RuToken ECP PAM PKCS11 module configuration
%endif

%package isbc
Summary: ESMART PAM PKCS11 module configuration
License: GPLv3+
Group: System/Configuration/Other
Requires: %name-common = %version-%release
Requires: pam_pkcs11 >= 0.6.9-alt9
Requires: pam_pkcs11-isbc
Requires: isbc-pkcs11

%description isbc
ESMART PAM PKCS11 module configuration

%package p11-kit-proxy
Summary: PKCS#11 Kit Proxy module configuration
License: GPLv3+
Group: System/Configuration/Other
Requires: %name-common = %version-%release
Requires: pam_pkcs11 >= 0.6.9-alt17
Requires: libp11-kit >= 0.23.8-alt2

%description p11-kit-proxy
PKCS#11 Kit Proxy module configuration

%package zastava
Summary: "Zastava" PAM PKCS#11 profile and configuration files
License: GPLv3+
Group: System/Configuration/Other
Requires: %name-common = %version-%release
Requires: pam_pkcs11 >= 0.6.9-alt18
Requires: %name-messages-zastava = %version-%release
BuildArch: noarch

%description zastava
Contains profile and configuration files used for "Zastava" installation

%package messages-zastava
Summary: "Zastava" PAM PKCS#11 message set
License: GPLv3+
Group: System/Configuration/Other
Requires: %name-common = %version-%release
Requires: pam_pkcs11 >= 0.6.9-alt18
BuildArch: noarch

%description messages-zastava
Contains prompts and other messages of "Zastava" PAM PKCS#11 set

%prep
%setup

%build
%autoreconf
%configure syslibdir=/%_lib
%make_build syslibdir=/%_lib

%install
%makeinstall_std 

%define confdir %_sysconfdir/security/pam_pkcs11

%files common
%_controldir/*
%dir %confdir/profiles
%config(noreplace) %confdir/profiles/opensc
%dir %confdir/modules.avail
%config(noreplace) %confdir/modules.avail/aladdin
%dir %confdir/mapping.profiles
%config(noreplace) %confdir/mapping.profiles/cert
%config(noreplace) %confdir/mapping.profiles/cn
%config(noreplace) %confdir/mapping.profiles/mail
%config(noreplace) %confdir/mapping.profiles/snils
%config(noreplace) %confdir/mapping.profiles/snils_scrambled
%config(noreplace) %confdir/mapping.profiles/subject
%dir %confdir/message.profiles
%config(noreplace) %confdir/message.profiles/default
%dir %confdir/param-set.d
%config(noreplace) %confdir/param-set.d/default

%ifnarch aarch64
%files rutokenecp
%config(noreplace) %confdir/modules.avail/rutokenecp
%config(noreplace) %confdir/profiles/rutokenecp
%endif

%files p11-kit-proxy
%config(noreplace) %confdir/modules.avail/p11_kit_proxy
%config(noreplace) %confdir/profiles/p11_kit_proxy

%if_enabled isbc
%files isbc
%config(noreplace) %confdir/modules.avail/isbc
%config(noreplace) %confdir/profiles/isbc
%endif

%files zastava
%config(noreplace) %confdir/param-set.d/zastava
%config(noreplace) %confdir/zastava_*

%files messages-zastava
%config(noreplace) %confdir/message.profiles/zastava

%changelog
* Wed Aug 22 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.5-alt2
- Skip "rutokenecp" profile for the "aarch64" arch.

* Mon Aug 13 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.5-alt1
- Added Russian translations for "prompt_so_pin_change_err" and
  "prompt_so_pin_change_err_locked" ("Zastava" profile).

* Mon Aug 06 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.4-alt2
- Increase the default PIN expiration timeout in "Zastava" profile
  up to 6 months.

* Mon Dec 04 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.4-alt1
- Fix: Substitute @syslibdir@ in the profiles.
- Fixed processing of multi-section profiles.
- Fix: Move the ISBC lowlevel module description to "isbc" profiles.
- Set the lowlevel module in the ISBC profile.
- Allow the module profiles to define additional (lowlevel, etc)
  values.

* Fri Dec 01 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt3
- Disable building of "isbc" package until the module is packaged.

* Mon Nov 27 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt2
- Extract noarch stuff in noarch packages.

* Mon Nov 27 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt1
- Added new "param-set" facility.
- Support "NONE" value in profiles (to delete the existing values).
- Move scripts and base profiles from pam_pkcs11 package.
- Fix: Handle values with ";" properly.

* Thu Nov 23 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Added "zastava" package (depends on "%name-messages-zastava").
- Packaged all "Zastava" parameters related to pam_pkcs11.

* Mon Oct 23 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Added "zastava" message set.
- Added ISBC (ESMART) profile.
- Added message profiles.

* Wed Sep 06 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt5
- Add 'p11-kit-proxy' subpackage with 'p11_kit_proxy' profile and module.
- Rely on librtpkcs11ecp >= 1.5.3.0-alt4 for pcsc-lite-ccid.
- Fixed the description of the RuTokenECP module.

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt4
- Require pcsc-lite-ccid for RuTokenECP.

* Thu Aug 10 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Remove the word "profile" from its description.

* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Fix: Exclude the mapping settings from the profiles.

* Fri Jun 09 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build.
