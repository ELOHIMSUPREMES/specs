
%add_python_req_skip hp3parclient

Name: openstack-cinder
Version: 2015.1.1
Release: alt1
Summary: OpenStack Volume service

Group: System/Servers
License: ASL 2.0
Url: http://www.openstack.org/software/openstack-storage/
Source0: %name-%version.tar
Source1: cinder-dist.conf
Source2: cinder.logrotate
Source3: cinder-tgt.conf
Source4: %name.tmpfiles
Source5: cinder.conf.sample

Source10: openstack-cinder-api.service
Source11: openstack-cinder-scheduler.service
Source12: openstack-cinder-volume.service
Source13: openstack-cinder-backup.service

Source110: openstack-cinder-api.init
Source111: openstack-cinder-scheduler.init
Source112: openstack-cinder-volume.init
Source113: openstack-cinder-backup.init

Source20: cinder-sudoers

Patch101: openstack-cinder-2015.1.1-alt-fix-genconfig.patch

BuildArch: noarch
BuildRequires: crudini
BuildRequires: python-module-d2to1
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-pbr
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-setuptools
BuildRequires: python-module-netaddr

BuildRequires: graphviz
BuildRequires: python-module-eventlet >= 0.16.1
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-SQLAlchemy >= 0.9.7
BuildRequires: python-module-webob
BuildRequires: python-module-migrate >= 0.9.5
BuildRequires: python-module-iso8601
BuildRequires: python-module-PasteDeploy
BuildRequires: python-module-oslo.config >= 1.9.3
BuildRequires: python-module-oslo.concurrency >= 1.8.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.db >= 1.7.0
BuildRequires: python-module-oslo.log >= 1.0.0
BuildRequires: python-module-oslo.messaging >= 1.8.0
BuildRequires: python-module-oslo.middleware >= 1.0.0
BuildRequires: python-module-oslo.rootwrap >= 1.6.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 1.4.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.vmware >= 0.11.1
BuildRequires: python-module-keystonemiddleware >= 1.5.0
BuildRequires: python-module-osprofiler >= 0.3.0
BuildRequires: python-module-glanceclient >= 0.15.0
BuildRequires: python-module-paramiko >= 1.13.0
BuildRequires: python-module-taskflow >= 0.7.1
BuildRequires: python-module-anyjson
BuildRequires: python-module-mox
BuildRequires: python-module-testtools
BuildRequires: python-module-testrepository
BuildRequires: python-module-oslotest
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-barbicanclient >= 3.0.1
BuildRequires: python-module-glanceclient >= 0.15.0
BuildRequires: python-module-novaclient >= 2.22.0

Requires: openstack-utils
Requires: python-module-cinder = %version-%release
Requires: python-module-PasteDeploy

Requires(pre): shadow-utils

Requires: lvm2
# Requires: scsitarget-utils
Requires: targetcli
Requires: python-module-rtslib
Requires: sysfsutils
Requires: sudo
Requires: qemu-img

%description
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

%package -n       python-module-cinder
Summary: OpenStack Volume Python libraries
Group: System/Servers

%description -n   python-module-cinder
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains the cinder Python library.

%package doc
Summary: Documentation for OpenStack Volume
Group: Development/Documentation

%description doc
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains documentation files for cinder.

%prep
%setup
%patch101 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find cinder -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%python_build

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b man doc/source doc/build/man
sphinx-build -b html doc/source doc/build/html
#install -p -D -m 640 %SOURCE5 etc/cinder/cinder.conf.sample
bash tools/config/generate_sample.sh -b . -p cinder -o etc/cinder

%install
%python_install

mkdir -p %buildroot%_man1dir
install -p -D -m 644 doc/build/man/*.1 %buildroot%_man1dir/

# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/cinder
install -d -m 755 %buildroot%_cachedir/cinder
install -d -m 755 %buildroot%_logdir/cinder

# Install config files
install -d -m 755 %buildroot%_sysconfdir/cinder
install -p -D -m 640 etc/cinder/cinder.conf.sample %buildroot%_sysconfdir/cinder/cinder.conf
install -p -D -m 644 etc/cinder/{api-paste.ini,policy.json,rootwrap.conf} %buildroot%_sysconfdir/cinder/
cp -a etc/cinder/rootwrap.d %buildroot%_sysconfdir/cinder/
install -d -m 755 %buildroot%_sysconfdir/cinder/volumes
install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/tgt/conf.d/cinder.conf

# Install initscripts for services
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/openstack-cinder-api.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/openstack-cinder-scheduler.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/openstack-cinder-volume.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/openstack-cinder-backup.service
install -p -D -m 644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf

install -p -D -m 755 %SOURCE110 %buildroot%_initdir/openstack-cinder-api
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/openstack-cinder-scheduler
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/openstack-cinder-volume
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/openstack-cinder-backup

# Install sudoers
install -p -D -m 400 %SOURCE20 %buildroot%_sysconfdir/sudoers.d/cinder

# Install logrotate
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/openstack-cinder

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/cinder

# Remove unneeded in production stuff
rm -f %buildroot%_bindir/cinder-debug
rm -fr %buildroot%python_sitelibdir/cinder/tests
rm -f %buildroot%python_sitelibdir/cinder/openstack/common/test.*
rm -f %buildroot%python_sitelibdir/cinder/test.*
rm -fr %buildroot%python_sitelibdir/run_tests.*
rm -f %buildroot/usr/share/doc/cinder/README*

### set default configuration (mostly applies to package-only setups and quickstart, i.e. not generally crowbar)
%define cinder_conf %buildroot%_sysconfdir/cinder/cinder.conf
crudini --set %cinder_conf DEFAULT log_dir /var/log/cinder
crudini --set %cinder_conf DEFAULT state_path /var/lib/cinder
crudini --set %cinder_conf DEFAULT lock_path /var/run/cinder
crudini --set %cinder_conf DEFAULT volumes_dir /etc/cinder/volumes
crudini --set %cinder_conf DEFAULT iscsi_helper lioadm
crudini --set %cinder_conf DEFAULT sql_connection mysql://cinder:cinder@localhost/cinder
crudini --set %cinder_conf DEFAULT rootwrap_config /etc/cinder/rootwrap.conf
crudini --set %cinder_conf DEFAULT auth_strategy keystone
#NOTE(saschpe): Can't hurt to set the default volume_group, only the LVM driver has a it otherwise:
crudini --set %cinder_conf DEFAULT volume_group cinder-volumes
crudini --set %cinder_conf DEFAULT lvm_type thin
crudini --set %cinder_conf keystone_authtoken signing_dir /var/cache/cinder/keystone-signing
crudini --set %cinder_conf keystone_authtoken admin_tenant_name %%SERVICE_TENANT_NAME%%
crudini --set %cinder_conf keystone_authtoken admin_user %%SERVICE_USER%%
crudini --set %cinder_conf keystone_authtoken admin_password %%SERVICE_PASSWORD%%
crudini --set %cinder_conf keystone_authtoken auth_host 127.0.0.1
crudini --set %cinder_conf keystone_authtoken auth_port 35357
crudini --set %cinder_conf keystone_authtoken auth_protocol http

%pre
# 165:165 for ceilometer (openstack-cinder)
%_sbindir/groupadd -r -g 165 -f cinder 2>/dev/null ||:
%_sbindir/useradd -r -u 165 -g cinder -G cinder,nobody,wheel  -c 'OpenStack Cinder Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/cinder cinder 2>/dev/null ||:


%post
%post_service %name-volume
%post_service %name-api
%post_service %name-scheduler
%post_service %name-backup

%preun
%preun_service %name-volume
%preun_service %name-api
%preun_service %name-scheduler
%preun_service %name-backup

%files
%doc LICENSE
%dir %_sysconfdir/cinder
%config(noreplace) %attr(0640, root, cinder) %_sysconfdir/cinder/cinder.conf
%config %attr(0640, root, cinder) %_sysconfdir/cinder/api-paste.ini
%config %_sysconfdir/cinder/rootwrap.conf
%config %_sysconfdir/cinder/policy.json
%config(noreplace) %_sysconfdir/logrotate.d/openstack-cinder
%config(noreplace) %_sysconfdir/sudoers.d/cinder
%config(noreplace) %_sysconfdir/tgt/conf.d/cinder.conf

%dir %attr(0750, cinder, root) %_logdir/cinder
%dir %attr(0755, cinder, root) %_runtimedir/cinder
%dir %attr(0755, cinder, root) %_sysconfdir/cinder/volumes

%_bindir/cinder-*
%_unitdir/*
%_initdir/*
%_tmpfilesdir/*
%_man1dir/cinder*.1.*

%dir %attr(0755, cinder, cinder) %_sharedstatedir/cinder
%dir %attr(0755, cinder, cinder) %_cachedir/cinder


%files -n python-module-cinder
%python_sitelibdir/*

%files doc
%doc doc/build/html

%changelog
* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1
- drop dist config in datadir

* Tue May 19 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo Release

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- 2014.1.1

* Sat Aug 09 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt3
- sysfsutils added to Requires: warning about systool

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt2
- user cinder added to wheel group, for cinder-rootwrap

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt1
- Initial build for Sisyphus (based on Fedora)
- New version - icehouse

