Name: 	  pcs
Version:  0.9.160
Release:  alt1
Epoch:    1

Summary:  Pacemaker/Corosync configuration system
License:  GPLv2
Group:    Other
Url: 	  https://github.com/ClusterLabs/pcs

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch
BuildArch: noarch

BuildRequires: rpm-build-python rpm-build-ruby ruby python-devel corosync python-module-setuptools fontconfig fonts-ttf-liberation
Requires: pacemaker

%filter_from_requires /^ruby(\(auth\|bootstrap\|cfgsync\|cluster\|cluster_entity\|config\|corosyncconf\|fenceagent\|pcs\|pcsd\|pcsd_file\|permissions\|remote\|resource\|session\|settings\|ssl\|wizard\|pcsd_test_utils\|test_auth\|test_cfgsync\|test_cluster\|test_cluster_entity\|test_config\|test_corosyncconf\|test_pcs\|test_permissions\|test_session\|pcsd_action_command\|pcsd_exchange_format\|pcsd_remove_file\))/d

%description
Pacemaker/Corosync configuration system with remote access

%package pcsd
Summary:  Pacemaker/Corosync cli and gui for configuration system
Requires: pcs
Group: Other
BuildArch: noarch
Requires: corosync
Requires: openssl
Requires: ruby-rack-handler-webrick < 2.0.0

%description pcsd
Pacemaker/Corosync gui/cli configuration system and daemon

%package pcsd-tests
Summary: tests for Pacemaker/Corosync cli and gui
Requires: pcs-pcsd
Group: Other
BuildArch: noarch

%description pcsd-tests
Tests for Pacemaker/Corosync gui/cli configuration system and daemon

%prep
%setup
%patch -p1

%install
%makeinstall_std
mkdir -p %buildroot/%_logdir/pcsd
make install_pcsd DESTDIR=%buildroot BUILD_GEMS=false PCSD_PARENT_DIR=%ruby_sitelibdir
mkdir -p %buildroot/%_initdir
mv %buildroot/%_sysconfdir/init.d/pcsd %buildroot/%_initdir
install -Dm 0644 pcsd/pcsd.logrotate %buildroot%_logrotatedir/pcsd.logrotate
mkdir -p %buildroot/var/lib/pcsd
mkdir -p %buildroot/lib/systemd/system
install -Dm 0644 pcsd/pcsd.service %buildroot/lib/systemd/system

mkdir -p %buildroot/usr/sbin/
mv  pcsd/pcsd.service-runner %buildroot/usr/sbin/pcsd
chmod 750 %buildroot/usr/sbin/pcsd

# Remove unnecessary stuff
rm -rf %buildroot/%ruby_sitelibdir/pcsd/*{.service,.logrotate,debian,orig}*

%post pcsd
%post_service pcsd


%preun pcsd
%preun_service pcsd

%files
%doc CHANGELOG.md COPYING README.md
%_sbindir/pcs
%python_sitelibdir_noarch/*
%_man8dir/*.*
%_sysconfdir/bash_completion.d/pcs

%files pcsd
%exclude %ruby_sitelibdir/pcsd/test/*
%ruby_sitelibdir/pcsd/*
%_initdir/pcsd
%_sysconfdir/logrotate.d/pcsd
%_sysconfdir/pam.d/pcsd
%_sysconfdir/sysconfig/pcsd
%dir %_logdir/pcsd
%dir /var/lib/pcsd
%_logrotatedir/pcsd.logrotate
/lib/systemd/system/pcsd.service
/usr/sbin/pcsd

%files pcsd-tests
%ruby_sitelibdir/pcsd/test/*

%changelog
* Sun Oct 15 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.160-alt1
- New version

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt3
- Completely remove requirement rack as gem
- pcs-pcsd requires openssl

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt2
- Comment out rack as gem load to prevent daemon fail

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jul 14 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt1
- New version

* Thu Jun 29 2017 Denis Medvedev <nbr@altlinux.org> 1:0.9.158-alt3
- Added systemd unit (ALT #33590).

* Fri Jun 23 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.158-alt2
- Fix pathes to pcsd and pacemaker data (ALT #33580)

* Tue Jun 20 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.158-alt1
- New version
- Build from upstream tag
- Use initscript and daemon executable from upstream (ALT #33562)
- pcs-pcsd requires ruby-rack-handler-webrick (ALT #33561)

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.99.156-alt5
- pcs-pcsd requires corosync and ruby-rack-handler-webrick
- fix initscript

* Wed Jun 14 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt4
- Packaged pcsd (ALT #33522) (thanks cas@)

* Wed Apr 05 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt3
- changed default placement of pacemaker files

* Tue Apr 04 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt2
- added dependency to pacemaker

* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt1
- Initial release
