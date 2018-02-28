%define service ceilometer
%def_without doc

Name: openstack-ceilometer
Version: 5.0.1
Release: alt1
Epoch: 1
Summary: OpenStack measurement collection service

Group: System/Servers
License: ASL 2.0
Url: https://wiki.openstack.org/wiki/Ceilometer
Source: %name-%version.tar
Source2: %service.logrotate
Source4: ceilometer-rootwrap-sudoers
Source5: openstack-ceilometer-polkit.rules
Source6: ceilometer.conf
Source7: openstack-ceilometer-polling.sysconfig

Source10: %name-api.service
Source11: %name-collector.service
Source12: %name-compute.service
Source13: %name-central.service
Source14: %name-alarm-notifier.service
Source15: %name-alarm-evaluator.service
Source16: %name-notification.service
Source17: %name-ipmi.service
Source18: %name-polling.service
Source20: %name.tmpfiles

Source110: %name-api.init
Source111: %name-collector.init
Source112: %name-compute.init
Source113: %name-central.init
Source114: %name-alarm-notifier.init
Source115: %name-alarm-evaluator.init
Source116: %name-notification.init
Source117: %name-ipmi.init
Source118: %name-polling.init

Provides: %name-common = %version-%release
Obsoletes: %name-common < %version-%release

Requires: python-module-ceilometer = %EVR
Requires: openstack-utils
Requires: python-module-PasteDeploy
Requires(pre):    shadow-utils


BuildArch: noarch
BuildRequires: crudini
BuildRequires: webserver-common rpm-build-webserver-common rpm-macros-apache2
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1
BuildRequires: python-module-d2to1
BuildRequires: python-module-eventlet >= 0.16.1
BuildRequires: python-module-SQLAlchemy >= 0.9.9
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-migrate >= 0.9.6
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-jsonpath-rw >= 1.2.0
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.db >= 2.4.1
BuildRequires: python-module-oslo.concurrency >= 2.3.0
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.log >= 1.0.0
BuildRequires: python-module-oslo.policy >= 0.5.0
BuildRequires: python-module-oslo.rootwrap >= 2.0.0
BuildRequires: python-module-oslo.service >= 0.7.0
BuildRequires: python-module-oslo.messaging >= 1.16.0
BuildRequires: python-module-oslo.middleware >= 2.8.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-oslo.vmware
BuildRequires: python-module-keystonemiddleware >= 2.0.0
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-pecan >= 1.0.0
BuildRequires: python-module-ceilometerclient >= 1.5.0
BuildRequires: python-module-glanceclient >= 0.18.0
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-neutronclient >= 2.6.0
BuildRequires: python-module-novaclient >= 2.28.1
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-tooz >= 1.19.0
BuildRequires: python-module-wsme >= 0.7

%description
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

%package -n       python-module-ceilometer
Summary: OpenStack ceilometer python libraries
Group: Development/Python
Requires: python-module-PasteDeploy
Requires: python-module-ceilometerclient
Requires: python-module-keystoneclient
Requires: python-module-keystonemiddleware

%description -n   python-module-ceilometer
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer python library.

%package compute
Summary: OpenStack ceilometer compute agent
Group: System/Servers
Requires: %name = %EVR

%description compute
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer agent for
running on OpenStack compute nodes.

%package central
Summary: OpenStack ceilometer central agent
Group: System/Servers
Requires: %name = %EVR

%description central
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the central ceilometer agent.

%package collector
Summary: OpenStack ceilometer collector
Group: System/Servers
Requires: %name = %EVR

# For compat with older provisioning tools.
# Remove when all reference the notification package explicitly
Requires: %name-notification
Requires: python-module-pymongo >= 2.5.2

%description collector
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer collector service
which collects metrics from the various agents.

%package notification
Summary: OpenStack ceilometer notification agent
Group: System/Servers
Requires: %name = %EVR

%description notification
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer notification agent
which pushes metrics to the collector service from the
various OpenStack services.

%package api
Summary: OpenStack ceilometer API service
Group: System/Servers
Requires: %name = %EVR

%description api
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer API service.

%package alarm
Summary: OpenStack ceilometer alarm services
Group: System/Servers
Requires: %name = %EVR

%description alarm
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer alarm notification
and evaluation services.

%package ipmi
Summary: OpenStack ceilometer ipmi agent
Group: System/Servers
Requires: %name = %EVR
Requires: ipmitool

%description ipmi
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ipmi agent to be run on OpenStack
nodes from which IPMI sensor data is to be collected directly,
by-passing Ironic's management of baremetal.

%package polling
Summary: OpenStack ceilometer polling agent
Group: System/Servers
Requires: %name = %EVR
Requires: python-module-libvirt

%description polling
Ceilometer aims to deliver a unique point of contact for billing systems to
aquire all counters they need to establish customer billing, across all
current and future OpenStack components. The delivery of counters must
be tracable and auditable, the counters must be easily extensible to support
new projects, and agents doing data collections should be
independent of the overall system.

This package contains the polling service.


%package doc
Summary: Documentation for OpenStack ceilometer
Group: Development/Documentation

%description doc
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains documentation files for ceilometer.

%prep
%setup

find . \( -name .gitignore -o -name .placeholder \) -delete

find ceilometer -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires


%build
%python_build
oslo-config-generator --output-file etc/ceilometer/ceilometer.conf \
    --namespace ceilometer \
    --namespace oslo.concurrency \
    --namespace oslo.db \
    --namespace oslo.log \
    --namespace oslo.messaging \
    --namespace oslo.policy \
    --namespace oslo.service.service \
    --namespace keystonemiddleware.auth_token

%install
%python_install

%if_with doc
# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo

popd
%endif

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/ceilometer
install -d -m 755 %buildroot%_cachedir/ceilometer
install -d -m 755 %buildroot%_logdir/ceilometer

# Install config files
install -d -m 755 %buildroot%_sysconfdir/ceilometer
install -d -m 755 %buildroot%_sysconfdir/ceilometer/rootwrap.d
install -d -m 755 %buildroot%_sysconfdir/sudoers.d
install -p -D -m 644 %SOURCE4 %buildroot%_sysconfdir/sudoers.d/ceilometer
install -p -D -m 644 etc/ceilometer/ceilometer.conf %buildroot%_sysconfdir/ceilometer/ceilometer.conf
install -p -D -m 644 etc/ceilometer/{api_paste.ini,event_definitions.yaml,event_pipeline.yaml,pipeline.yaml,policy.json} %buildroot%_sysconfdir/ceilometer/
install -p -D -m 644 etc/ceilometer/rootwrap.conf %buildroot%_sysconfdir/ceilometer/rootwrap.conf
install -p -D -m 644 etc/ceilometer/rootwrap.d/ipmi.filters %buildroot%_sysconfdir/ceilometer/rootwrap.d/ipmi.filters
install -p -D -m 640 ceilometer/meter/data/meters.yaml %buildroot%_sysconfdir/ceilometer/meters.yaml
install -p -D -m 644 %SOURCE7 %buildroot%_sysconfdir/sysconfig/openstack-ceilometer-polling

# Install initscripts for services
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/%name-api.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/%name-collector.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/%name-compute.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/%name-central.service
install -p -D -m 644 %SOURCE14 %buildroot%_unitdir/%name-alarm-notifier.service
install -p -D -m 644 %SOURCE15 %buildroot%_unitdir/%name-alarm-evaluator.service
install -p -D -m 644 %SOURCE16 %buildroot%_unitdir/%name-notification.service
install -p -D -m 644 %SOURCE17 %buildroot%_unitdir/%name-ipmi.service
install -p -D -m 644 %SOURCE18 %buildroot%_unitdir/%name-polling.service
install -p -D -m 644 %SOURCE20 %buildroot%_tmpfilesdir/%name.conf

install -p -D -m 755 %SOURCE110 %buildroot%_initdir/%name-api
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/%name-collector
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/%name-compute
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/%name-central
install -p -D -m 755 %SOURCE114 %buildroot%_initdir/%name-alarm-notifier
install -p -D -m 755 %SOURCE115 %buildroot%_initdir/%name-alarm-evaluator
install -p -D -m 755 %SOURCE116 %buildroot%_initdir/%name-notification
install -p -D -m 755 %SOURCE117 %buildroot%_initdir/%name-ipmi
install -p -D -m 755 %SOURCE117 %buildroot%_initdir/%name-polling

# Install logrotate
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name
# Install pid directory
install -d -m 755 %buildroot%_runtimedir/ceilometer

install -D -m 644 %SOURCE5 %buildroot%_datadir/polkit-1/rules.d/11-openstack-ceilometer.rules

# Install sample HTTPD integration files
install -p -D -m 644 ceilometer/api/app.wsgi %buildroot%_datadir/ceilometer/ceilometer.wsgi
install -p -D -m 644 etc/apache2/ceilometer %buildroot%_datadir/ceilometer/ceilometer.conf

install -m 0644 -D -p %SOURCE6 %buildroot%apache2_sites_available/openstack-ceilometer.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/openstack-ceilometer.conf
mkdir -p %buildroot%webserver_cgibindir
ln -s %_datadir/ceilometer/ceilometer.wsgi %buildroot%webserver_cgibindir/ceilometer-wsgi


# Remove unneeded in production stuff
rm -f %buildroot%_bindir/ceilometer-debug
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python_sitelibdir/run_tests.*
rm -f %buildroot/usr/share/doc/ceilometer/README*

%define ceilometer_conf %buildroot%_sysconfdir/ceilometer/ceilometer.conf
crudini --set %ceilometer_conf DEFAULT log_dir %_logdir/ceilometer
crudini --set %ceilometer_conf DEFAULT policy_file %_sysconfdir/ceilometer/policy.json
crudini --set %ceilometer_conf DEFAULT lock_path %_runtimedir/ceilometer
crudini --set %ceilometer_conf keystone_authtoken signing_dir %_cachedir/ceilometer/keystone-signing
crudini --set %ceilometer_conf database connection mongodb://localhost:27017/ceilometer


%pre
# 166:166 for ceilometer (openstack-ceilometer)
%_sbindir/groupadd -r -g 166 -f ceilometer 2>/dev/null ||:
%_sbindir/useradd -r -u 166 -g ceilometer -G ceilometer,nobody  -c 'OpenStack Ceilometer Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/ceilometer ceilometer 2>/dev/null ||:


%post compute
%post_service %name-compute

%post collector
%post_service %name-collector

%post notification
%post_service %name-notification

%post api
%post_service %name-api

%post central
%post_service %name-central

%post alarm
%post_service %name-alarm-notifier
%post_service %name-alarm-evaluator

%post ipmi
%post_service %name-ipmi

%post polling
%post_service %name-polling

%preun compute
%preun_service %name-compute

%preun collector
%preun_service %name-collector

%preun notification
%preun_service %name-notification

%preun api
%preun_service %name-api

%preun central
%preun_service %name-central

%preun alarm
%preun_service %name-alarm-notifier
%preun_service %name-alarm-evaluator

%preun ipmi
%preun_service %name-ipmi

%preun polling
%preun_service %name-polling

%files
%doc LICENSE
%dir %_sysconfdir/ceilometer
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/ceilometer.conf
%config(noreplace) %_sysconfdir/ceilometer/pipeline.yaml
%config(noreplace) %_sysconfdir/ceilometer/policy.json
%config(noreplace) %_sysconfdir/ceilometer/api_paste.ini
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(0750, ceilometer, adm) %_logdir/ceilometer
%dir %attr(0755, ceilometer, root) %_runtimedir/ceilometer
%_tmpfilesdir/%name.conf

%_bindir/ceilometer-dbsync
%_bindir/ceilometer-expirer
%_bindir/ceilometer-send-sample
%dir %attr(0755, ceilometer, ceilometer) %_sharedstatedir/ceilometer
%dir %attr(0755, ceilometer, ceilometer) %_cachedir/ceilometer

%files -n python-module-ceilometer
%python_sitelibdir/*

%if_with doc
%files doc
%doc doc/build/html
%endif

%files compute
%_unitdir/%name-compute.service
%_initdir/%name-compute
%_datadir/polkit-1/rules.d/11-openstack-ceilometer.rules

%files collector
%_bindir/ceilometer-collector*
%_unitdir/%name-collector.service
%_initdir/%name-collector

%files notification
%config(noreplace) %_sysconfdir/ceilometer/meters.yaml
%config(noreplace) %_sysconfdir/ceilometer/event_pipeline.yaml
%config(noreplace) %_sysconfdir/ceilometer/event_definitions.yaml
%_bindir/ceilometer-agent-notification
%_unitdir/%name-notification.service
%_initdir/%name-notification

%files api
%_bindir/ceilometer-api
%_unitdir/%name-api.service
%_initdir/%name-api
%dir %_datadir/ceilometer
%_datadir/ceilometer/*
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf
%webserver_cgibindir/*

%files central
%_unitdir/%name-central.service
%_initdir/%name-central

%files alarm
%_bindir/ceilometer-alarm-notifier
%_bindir/ceilometer-alarm-evaluator
%_unitdir/%name-alarm-notifier.service
%_initdir/%name-alarm-notifier
%_unitdir/%name-alarm-evaluator.service
%_initdir/%name-alarm-evaluator

%files ipmi
%config(noreplace) %_sysconfdir/ceilometer/rootwrap.conf
%config(noreplace) %_sysconfdir/ceilometer/rootwrap.d/ipmi.filters
%config(noreplace) %_sysconfdir/sudoers.d/ceilometer
%_bindir/ceilometer-rootwrap
%_unitdir/%name-ipmi.service
%_initdir/%name-ipmi


%files polling
%_bindir/ceilometer-polling
%_unitdir/%name-polling.service
%_initdir/%name-polling
%config(noreplace) %_sysconfdir/sysconfig/openstack-ceilometer-polling

%changelog
* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:5.0.1-alt1
- 5.0.1

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1:5.0.0-alt1
- 5.0.0 Liberty Release
- add apache2 config for ceilometer-api

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Fri Aug 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1
- drop common package
- drop dist config in datadir

* Wed May 20 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo Release

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0.b2

* Fri Aug 22 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- Requires: python-module-pymongo >= 2.5.2

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- First build for ALT (based on Fedora 2014.1.1-3.fc21.src)
