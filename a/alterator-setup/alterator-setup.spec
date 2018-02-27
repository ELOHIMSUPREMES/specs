%define _altdata_dir %_datadir/alterator

Name: alterator-setup
Version: 0.2.1
Release: alt1

Summary: Perform initial setup of an OEM installation
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: alterator >= 4.10-alt6
BuildRequires: rpm-macros-alterator

Requires: libshell
Requires: alterator-l10n >= 2.5-alt1
Requires: alterator-browser-qt >= 2.17.0
Requires: alterator-lookout => 2.4-alt1
Requires: alterator-wizardface
Requires: alterator-notes
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-root
Requires: alterator-users

Requires(post): chkconfig
Requires(preun): chkconfig

%description
%summary

%prep
%setup

%install
%makeinstall

# TODO: alterator-wizardface might take a parameter
mkdir -p %buildroot%_datadir/install2
ln -s ../../..%_sysconfdir/alterator-setup/steps \
	%buildroot%_datadir/install2/installer-steps

cat >> %buildroot%_sysconfdir/alterator-setup/config << EOF
# erase %name and related packages
REMOVE_SELF=1
EOF

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_sbindir/%name
%_alterator_datadir/steps/*
%_alterator_datadir/ui/*
%_alterator_libdir/hooks/*/*
%_alterator_backend3dir/*
%_datadir/alterator-setup/
%_datadir/install2/installer-steps
/lib/systemd/system/setup.*

# the restore is done in postinstall script
# triggered by successful completion of the module
# as it can be reused now (doesn't self destruct)
%post
[ -d /etc/systemd/system ] || exit 0
mv /etc/systemd/system/default.target /etc/systemd/system/default.target.bak ||:
ln -sf /lib/systemd/system/setup.target /etc/systemd/system/default.target

%changelog
* Thu Mar 06 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt1
- Remove more packages during cleanup.

* Tue Jul 16 2013 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- made self destruction optional (sysconfig knob)
- minor spec cleanup

* Fri Jul 12 2013 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- added license step

* Thu Jun 20 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release, thanks sem@

