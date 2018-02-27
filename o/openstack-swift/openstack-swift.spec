
Name: openstack-swift
Version: 2.2.2
Release: alt1
Summary: OpenStack Object Storage (Swift)

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/swift
Source: %name-%version.tar

Source2: %name-account.service
Source21: %name-account@.service
Source22: account-server.conf
Source23: %name-account-replicator.service
Source24: %name-account-replicator@.service
Source25: %name-account-auditor.service
Source26: %name-account-auditor@.service
Source27: %name-account-reaper.service
Source28: %name-account-reaper@.service
Source120: %name-account.init
Source123: %name-account-replicator.init
Source125: %name-account-auditor.init
Source127: %name-account-reaper.init
Source4: %name-container.service
Source41: %name-container@.service
Source42: container-server.conf
Source43: %name-container-replicator.service
Source44: %name-container-replicator@.service
Source45: %name-container-auditor.service
Source46: %name-container-auditor@.service
Source47: %name-container-updater.service
Source48: %name-container-updater@.service
Source49: %name-container-reconciler.service
Source140: %name-container.init
Source143: %name-container-replicator.init
Source145: %name-container-auditor.init
Source147: %name-container-updater.init
Source149: %name-container-reconciler.init
Source5: %name-object.service
Source51: %name-object@.service
Source52: object-server.conf
Source53: %name-object-replicator.service
Source54: %name-object-replicator@.service
Source55: %name-object-auditor.service
Source56: %name-object-auditor@.service
Source57: %name-object-updater.service
Source58: %name-object-updater@.service
Source59: %name-object-expirer.service
Source150: %name-object.init
Source153: %name-object-replicator.init
Source155: %name-object-auditor.init
Source157: %name-object-updater.init
Source159: %name-object-expirer.init

# Is it possible to supply an instance-style expirer unit for single-node?
Source6: %name-proxy.service
Source61: proxy-server.conf
Source62: object-expirer.conf
Source64: container-reconciler.conf
Source160: %name-proxy.init
Source20: %name.tmpfs
Source7: swift.conf

#
# patches_base=1.13.1
#
Patch0001: 0001-remove-runtime-requirement-on-pbr.patch

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-eventlet >= 0.9.15
BuildRequires: python-module-greenlet >= 0.3.1
BuildRequires: python-module-netifaces >= 0.5
BuildRequires: python-module-simplejson >= 2.0.9
BuildRequires: python-module-pyxattr

Requires(pre):    shadow-utils

%description
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.
Objects are written to multiple hardware devices in the data center, with the
OpenStack software responsible for ensuring data replication and integrity
across the cluster. Storage clusters can scale horizontally by adding new nodes,
which are automatically configured. Should a node fail, OpenStack works to
replicate its content from other active nodes. Because OpenStack uses software
logic to ensure data replication and distribution across different devices,
inexpensive commodity hard drives and servers can be used in lieu of more
expensive equipment.

%package account
Summary: Account services for Swift
Group: System/Servers

Requires: %name = %version-%release

%description account
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %name account server.

%package container
Summary: Container services for Swift
Group: System/Servers

Requires: %name = %version-%release

%description container
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %name container server.

%package object
Summary: Object services for Swift
Group: System/Servers

Requires: %name = %version-%release
Requires: rsync >= 3.0

%description object
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %name object server.

%package proxy
Summary: A proxy server for Swift
Group: System/Servers

Requires: %name = %version-%release
Requires: python-module-keystonemiddleware
Requires: python-module-swift-plugin-swift3

%description proxy
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %name proxy server.

%package doc
Summary: Documentation for %name
Group: Documentation

%description doc
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains documentation files for %name.

%prep
%setup

%patch0001 -p1

# Remove bundled egg-info
rm -rf swift.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

# Remove dependency on pbr and set version as per rpm
sed -i 's/RPMVERSION/%{version}/; s/RPMRELEASE/%{release}/' swift/__init__.py

%build
%python_build
# Fails unless we create the build directory
mkdir -p doc/build
# Build docs
%__python setup.py build_sphinx

# Fix hidden-file-or-dir warning
#rm doc/build/html/.buildinfo

%install
%python_install
# systemd units
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/%name-account.service
install -p -D -m 644 %SOURCE21 %buildroot%_unitdir/%name-account@.service
install -p -D -m 644 %SOURCE23 %buildroot%_unitdir/%name-account-replicator.service
install -p -D -m 644 %SOURCE24 %buildroot%_unitdir/%name-account-replicator@.service
install -p -D -m 644 %SOURCE25 %buildroot%_unitdir/%name-account-auditor.service
install -p -D -m 644 %SOURCE26 %buildroot%_unitdir/%name-account-auditor@.service
install -p -D -m 644 %SOURCE27 %buildroot%_unitdir/%name-account-reaper.service
install -p -D -m 644 %SOURCE28 %buildroot%_unitdir/%name-account-reaper@.service
install -p -D -m 644 %SOURCE4 %buildroot%_unitdir/%name-container.service
install -p -D -m 644 %SOURCE41 %buildroot%_unitdir/%name-container@.service
install -p -D -m 644 %SOURCE43 %buildroot%_unitdir/%name-container-replicator.service
install -p -D -m 644 %SOURCE44 %buildroot%_unitdir/%name-container-replicator@.service
install -p -D -m 644 %SOURCE45 %buildroot%_unitdir/%name-container-auditor.service
install -p -D -m 644 %SOURCE46 %buildroot%_unitdir/%name-container-auditor@.service
install -p -D -m 644 %SOURCE47 %buildroot%_unitdir/%name-container-updater.service
install -p -D -m 644 %SOURCE48 %buildroot%_unitdir/%name-container-updater@.service
install -p -D -m 644 %SOURCE49 %buildroot%_unitdir/%name-container-reconciler.service
install -p -D -m 644 %SOURCE5 %buildroot%_unitdir/%name-object.service
install -p -D -m 644 %SOURCE51 %buildroot%_unitdir/%name-object@.service
install -p -D -m 644 %SOURCE53 %buildroot%_unitdir/%name-object-replicator.service
install -p -D -m 644 %SOURCE54 %buildroot%_unitdir/%name-object-replicator@.service
install -p -D -m 644 %SOURCE55 %buildroot%_unitdir/%name-object-auditor.service
install -p -D -m 644 %SOURCE56 %buildroot%_unitdir/%name-object-auditor@.service
install -p -D -m 644 %SOURCE57 %buildroot%_unitdir/%name-object-updater.service
install -p -D -m 644 %SOURCE58 %buildroot%_unitdir/%name-object-updater@.service
install -p -D -m 644 %SOURCE59 %buildroot%_unitdir/%name-object-expirer.service
install -p -D -m 644 %SOURCE6 %buildroot%_unitdir/%name-proxy.service

# sysv init scripts
install -p -D -m 755 %SOURCE120 %buildroot%_initdir/%name-account
install -p -D -m 755 %SOURCE123 %buildroot%_initdir/%name-account-replicator
install -p -D -m 755 %SOURCE125 %buildroot%_initdir/%name-account-auditor
install -p -D -m 755 %SOURCE127 %buildroot%_initdir/%name-account-reaper
install -p -D -m 755 %SOURCE140 %buildroot%_initdir/%name-container.service
install -p -D -m 755 %SOURCE143 %buildroot%_initdir/%name-container-replicator
install -p -D -m 755 %SOURCE145 %buildroot%_initdir/%name-container-auditor
install -p -D -m 755 %SOURCE147 %buildroot%_initdir/%name-container-updater
install -p -D -m 755 %SOURCE149 %buildroot%_initdir/%name-container-reconciler
install -p -D -m 755 %SOURCE150 %buildroot%_initdir/%name-object.service
install -p -D -m 755 %SOURCE153 %buildroot%_initdir/%name-object-replicator
install -p -D -m 755 %SOURCE155 %buildroot%_initdir/%name-object-auditor
install -p -D -m 755 %SOURCE157 %buildroot%_initdir/%name-object-updater
install -p -D -m 755 %SOURCE159 %buildroot%_initdir/%name-object-expirer
install -p -D -m 755 %SOURCE160 %buildroot%_initdir/%name-proxy

# Remove tests
rm -fr %buildroot/%python_sitelibdir/test
# Misc other
install -d -m 755 %buildroot%_sysconfdir/swift
install -d -m 755 %buildroot%_sysconfdir/swift/account-server
install -d -m 755 %buildroot%_sysconfdir/swift/container-server
install -d -m 755 %buildroot%_sysconfdir/swift/object-server
install -d -m 755 %buildroot%_sysconfdir/swift/proxy-server
# Config files
install -p -D -m 660 %SOURCE22 %buildroot%_sysconfdir/swift/account-server.conf
install -p -D -m 660 %SOURCE42 %buildroot%_sysconfdir/swift/container-server.conf
install -p -D -m 660 %SOURCE52 %buildroot%_sysconfdir/swift/object-server.conf
install -p -D -m 660 %SOURCE61 %buildroot%_sysconfdir/swift/proxy-server.conf
install -p -D -m 660 %SOURCE62 %buildroot%_sysconfdir/swift/object-expirer.conf
install -p -D -m 660 %SOURCE64 %buildroot%_sysconfdir/swift/container-reconciler.conf
install -p -D -m 660 %SOURCE7 %buildroot%_sysconfdir/swift/swift.conf
# Install pid directory
install -d -m 755 %buildroot%_runtimedir/swift
install -d -m 755 %buildroot%_runtimedir/swift/account-server
install -d -m 755 %buildroot%_runtimedir/swift/container-server
install -d -m 755 %buildroot%_runtimedir/swift/object-server
install -d -m 755 %buildroot%_runtimedir/swift/proxy-server
# syslog
install -d -m 755 %buildroot%_logdir/swift
# Swift run directories
mkdir -p %buildroot%_tmpfilesdir
install -p -m 0644 %SOURCE20 %buildroot%_tmpfilesdir/openstack-swift.conf
# Install recon directory
install -d -m 755 %buildroot%_cachedir/swift
# Install home directory
install -d -m 755 %buildroot%_sharedstatedir/swift
# man pages
install -d -m 755 %buildroot%_man5dir
for m in doc/manpages/*.5; do
  install -p -m 0644 $m %buildroot%_man5dir
done
install -d -m 755 %buildroot%_man1dir
for m in doc/manpages/*.1; do
  install -p -m 0644 $m %buildroot%_man1dir
done

%pre
# 160:160 for keystone (openstack-swift)
%_sbindir/groupadd -r -g 160 -f swift 2>/dev/null ||:
%_sbindir/useradd -r -u 160 -g swift -c 'OpenStack Swift Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/swift swift 2>/dev/null ||:


%post account
%post_service %name-account
%post_service %name-account-replicator
%post_service %name-account-auditor
%post_service %name-account-reaper

%preun account
%preun_service %name-account
%preun_service %name-account-replicator
%preun_service %name-account-auditor
%preun_service %name-account-reaper

%post container
%post_service %name-container
%post_service %name-container-replicator
%post_service %name-container-auditor
%post_service %name-container-updater

%preun container
%preun_service %name-container
%preun_service %name-container-replicator
%preun_service %name-container-auditor
%preun_service %name-container-updater

%post object
%post_service %name-object
%post_service %name-object-replicator
%post_service %name-object-auditor
%post_service %name-object-updater

%preun object
%preun_service %name-object
%preun_service %name-object-replicator
%preun_service %name-object-auditor
%preun_service %name-object-updater

%post proxy
%post_service %name-proxy
%post_service %name-object-expirer
%post_service %name-container-reconciler.service

%preun proxy
%preun_service %name-proxy
%preun_service %name-object-expirer
%preun_service %name-container-reconciler.service

%files
%doc AUTHORS LICENSE README.md
%doc etc/dispersion.conf-sample etc/drive-audit.conf-sample etc/object-expirer.conf-sample
%doc etc/swift.conf-sample
%_man5dir/dispersion.conf.5*
%_man1dir/swift-dispersion-populate.1*
%_man1dir/swift-dispersion-report.1*
%_man1dir/swift-get-nodes.1*
%_man1dir/swift-init.1*
%_man1dir/swift-orphans.1*
%_man1dir/swift-recon.1*
%_man1dir/swift-ring-builder.1*
%_tmpfilesdir/openstack-swift.conf
%dir %_sysconfdir/swift
%config(noreplace) %attr(640, root, swift) %_sysconfdir/swift/swift.conf
%dir %_logdir/swift
%dir %attr(0755, swift, root) %_runtimedir/swift
%dir %attr(0755, swift, root) %_cachedir/swift
%dir %attr(0755, swift, root) %_sharedstatedir/swift
%dir %python_sitelibdir/swift
%_bindir/swift-account-audit
%_bindir/swift-config
%_bindir/swift-drive-audit
%_bindir/swift-get-nodes
%_bindir/swift-init
%_bindir/swift-ring-builder
%_bindir/swift-dispersion-populate
%_bindir/swift-dispersion-report
%_bindir/swift-recon*
%_bindir/swift-oldies
%_bindir/swift-orphans
%_bindir/swift-form-signature
%_bindir/swift-temp-url
%python_sitelibdir/swift/*.py*
%python_sitelibdir/swift/cli
%python_sitelibdir/swift/common
%python_sitelibdir/swift/account
%python_sitelibdir/swift/obj
%python_sitelibdir/swift-%{version}*.egg-info

%files account
%doc etc/account-server.conf-sample
%_man5dir/account-server.conf.5*
%_man1dir/swift-account-auditor.1*
%_man1dir/swift-account-info.1*
%_man1dir/swift-account-reaper.1*
%_man1dir/swift-account-replicator.1*
%_man1dir/swift-account-server.1*
%_unitdir/%name-account*.service
%_initdir/%name-account*
%dir %_sysconfdir/swift/account-server
%config(noreplace) %attr(640, root, swift) %_sysconfdir/swift/account-server.conf
%dir %attr(0755, swift, root) %_runtimedir/swift/account-server
%_bindir/swift-account-auditor
%_bindir/swift-account-info
%_bindir/swift-account-reaper
%_bindir/swift-account-replicator
%_bindir/swift-account-server

%files container
%doc etc/container-server.conf-sample
%_man5dir/container-server.conf.5*
%_man1dir/swift-container-auditor.1*
%_man1dir/swift-container-info.1*
%_man1dir/swift-container-replicator.1*
%_man1dir/swift-container-server.1*
%_man1dir/swift-container-sync.1*
%_man1dir/swift-container-updater.1*
%_unitdir/%name-container*.service
%exclude %_unitdir/%name-container-reconciler.service
%_initdir/%name-container*
%exclude %_initdir/%name-container-reconciler
%dir %_sysconfdir/swift/container-server
%config(noreplace) %attr(640, root, swift) %_sysconfdir/swift/container-server.conf
%dir %attr(0755, swift, root) %_runtimedir/swift/container-server
%_bindir/swift-container-auditor
%_bindir/swift-container-info
%_bindir/swift-container-server
%_bindir/swift-container-replicator
%_bindir/swift-container-updater
%_bindir/swift-container-sync
%python_sitelibdir/swift/container

%files object
%doc etc/object-server.conf-sample etc/rsyncd.conf-sample
%_man5dir/object-server.conf.5*
%_man1dir/swift-object-auditor.1*
%_man1dir/swift-object-info.1*
%_man1dir/swift-object-replicator.1*
%_man1dir/swift-object-server.1*
%_man1dir/swift-object-updater.1*
%_unitdir/%name-object*.service
%exclude %_unitdir/%name-object-expirer.service
%_initdir/%name-object*
%exclude %_initdir/%name-object-expirer
%dir %_sysconfdir/swift/object-server
%config(noreplace) %attr(640, root, swift) %_sysconfdir/swift/object-server.conf
%dir %attr(0755, swift, root) %_runtimedir/swift/object-server
%_bindir/swift-object-auditor
%_bindir/swift-object-info
%_bindir/swift-object-replicator
%_bindir/swift-object-server
%_bindir/swift-object-updater

%files proxy
%doc etc/proxy-server.conf-sample etc/object-expirer.conf-sample
%_man5dir/object-expirer.conf.5*
%_man5dir/proxy-server.conf.5*
%_man1dir/swift-object-expirer.1*
%_man1dir/swift-proxy-server.1*
%_unitdir/%name-container-reconciler.service
%_unitdir/%name-object-expirer.service
%_unitdir/%name-proxy.service
%_initdir/%name-container-reconciler
%_initdir/%name-object-expirer
%_initdir/%name-proxy
%dir %_sysconfdir/swift/proxy-server
%config(noreplace) %attr(640, root, swift) %_sysconfdir/swift/container-reconciler.conf
%config(noreplace) %attr(640, root, swift) %_sysconfdir/swift/proxy-server.conf
%config(noreplace) %attr(640, root, swift) %_sysconfdir/swift/object-expirer.conf
%dir %attr(0755, swift, root) %_runtimedir/swift/proxy-server
%_bindir/swift-container-reconciler
%_bindir/swift-object-expirer
%_bindir/swift-proxy-server
%python_sitelibdir/swift/proxy

%files doc
%doc LICENSE doc/build/html

%changelog
* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.13.1-alt2
- _cachedir packaging fixed

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 1.13.1-alt1
- 1.13.1 (based on Fedora 1.13.1-5.fc21.src)

* Thu Aug 29 2013 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt3
- Cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt2.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt2
- Use post/preun_service scripts in spec

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt1
- Initial release for Sisyphus (based on Fedora)
