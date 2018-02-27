%def_disable embrane
%def_disable plumgrid
%def_disable linuxbridge
%def_disable brocade
%def_disable cisco
%def_disable openvswitch
%def_disable mellanox
%def_disable ofagent

Name: openstack-neutron
Version: 2015.1.0
Release: alt0.b2.0
Provides: openstack-quantum = %version-%release
Obsoletes: openstack-quantum < 2013.2-0.4.b3
Summary: OpenStack Networking Service

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/neutron/

Source0: %name-%version.tar
Source1: neutron.logrotate
Source2: neutron-sudoers
Source3: %name.tmpfiles

Source10: neutron-server.service
Source11: neutron-linuxbridge-agent.service
Source12: neutron-openvswitch-agent.service
Source14: neutron-nec-agent.service
Source15: neutron-dhcp-agent.service
Source16: neutron-l3-agent.service
Source17: neutron-metadata-agent.service
Source18: neutron-ovs-cleanup.service
Source20: neutron-mlnx-agent.service
Source22: neutron-metering-agent.service
Source23: neutron-sriov-nic-agent.service
Source24: neutron-cisco-cfg-agent.service
Source25: neutron-netns-cleanup.service

Source110: neutron-server.init
Source111: neutron-linuxbridge-agent.init
Source112: neutron-openvswitch-agent.init
Source114: neutron-nec-agent.init
Source115: neutron-dhcp-agent.init
Source116: neutron-l3-agent.init
Source117: neutron-metadata-agent.init
Source118: neutron-ovs-cleanup.init
Source120: neutron-mlnx-agent.init
Source122: neutron-metering-agent.init
Source123: neutron-sriov-nic-agent.init
Source124: neutron-cisco-cfg-agent.init
Source125: neutron-netns-cleanup.init

Source40: neutron-dist.conf
#
# patches_base=2014.1.2
#
Patch0001: 0001-remove-runtime-dependency-on-pbr.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1

Requires: python-module-neutron = %version-%release
Requires: python-module-oslo.rootwrap
Requires: openstack-utils

# dnsmasq is not a hard requirement, but is currently the only option
# when neutron-dhcp-agent is deployed.
Requires: dnsmasq
Requires: dnsmasq-utils

Requires(pre): shadow-utils

%description
Neutron is a virtual network service for Openstack. Just like
OpenStack Nova provides an API to dynamically request and configure
virtual servers, Neutron provides an API to dynamically request and
configure virtual networks. These networks connect "interfaces" from
other OpenStack services (e.g., virtual NICs from Nova VMs). The
Neutron API supports extensions to provide advanced network
capabilities (e.g., QoS, ACLs, network monitoring, etc.)

%package -n python-module-neutron
Summary: Neutron Python libraries
Group: Development/Python

Provides: python-module-quantum = %version-%release
Obsoletes: python-module-quantum < 2013.2-0.4.b3

Requires: python-module-keystoneclient >= 1.0.0
Requires: python-module-keystonemiddleware >= 1.0.0
Requires: python-module-oslo.config >= 1.2.0
Requires: python-module-neutronclient >= 2.3.6
Requires: python-module-novaclient >= 2.18.0
Requires: sudo

%description -n python-module-neutron
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron Python library.

%package bigswitch
Summary: Neutron Big Switch plugin
Group: Development/Python

Provides: openstack-quantum-bigswitch = %version-%release
Obsoletes: openstack-quantum-bigswitch < 2013.2-0.4.b3

Requires: %name = %version-%release

%description bigswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the FloodLight Openflow Controller or the Big Switch
Networks Controller.

%package brocade
Summary: Neutron Brocade plugin
Group: Development/Python

Provides: openstack-quantum-brocade = %version-%release
Obsoletes: openstack-quantum-brocade < 2013.2-0.4.b3

Requires: %name = %version-%release
Requires: python-module-ncclient

%description brocade
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Brocade VCS switches running NOS.

%package cisco
Summary: Neutron Cisco plugin
Group: Development/Python
Provides: openstack-quantum-cisco = %version-%release
Obsoletes: openstack-quantum-cisco < 2013.2-0.4.b3

Requires: %name = %version-%release
Requires: python-module-ncclient

%description cisco
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Cisco UCS and Nexus.

%package embrane
Summary: Neutron Embrane plugin
Group: Development/Python

Requires: %name = %version-%release

%description embrane
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
L3-L7 network services using Embrane's heleos platform.

%package hyperv
Summary: Neutron Hyper-V plugin
Group: Development/Python
Provides: openstack-quantum-hyperv = %version-%release
Obsoletes: openstack-quantum-hyperv < 2013.2-0.4.b3

Requires: %name = %version-%release

%description hyperv
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Microsoft Hyper-V.

%package ibm
Summary: Neutron IBM plugin
Group: Development/Python

Requires: %name = %version-%release

%description ibm
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks from IBM.

%package linuxbridge
Summary: Neutron linuxbridge plugin
Group: Development/Python

Provides: openstack-quantum-linuxbridge = %version-%release
Obsoletes: openstack-quantum-linuxbridge < 2013.2-0.4.b3

Requires: bridge-utils
Requires: %name = %version-%release

%description linuxbridge
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks as VLANs using Linux bridging.

%package mellanox
Summary: Neutron Mellanox plugin
Group: Development/Python

Provides: openstack-quantum-mellanox = %version-%release
Obsoletes: openstack-quantum-mellanox < 2013.2-0.4.b3

Requires: %name = %version-%release

%description mellanox
This plugin implements Neutron v2 APIs with support for Mellanox embedded
switch functionality as part of the VPI (Ethernet/InfiniBand) HCA.

%package metaplugin
Summary: Neutron meta plugin
Group: Development/Python

Provides: openstack-quantum-metaplugin = %version-%release
Obsoletes: openstack-quantum-metaplugin < 2013.2-0.4.b3

Requires: %name = %version-%release

%description metaplugin
Neutron provides an API to dynamically request and configure virtual
networks.

%package midonet
Summary: Neutron MidoNet plugin
Group: Development/Python

Provides: openstack-quantum-midonet = %version-%release
Obsoletes: openstack-quantum-midonet < 2013.2-0.4.b3

Requires: %name = %version-%release

%description midonet
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using MidoNet from Midokura.

%package ml2
Summary: Neutron ML2 plugin
Group: Development/Python

Provides: openstack-quantum-ml2 = %version-%release
Obsoletes: openstack-quantum-ml2 < 2013.2-0.4.b3

Requires: %name = %version-%release

%description ml2
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains a neutron plugin that allows the use of drivers
to support separately extensible sets of network types and the mechanisms
for accessing those types.

%package nec
Summary: Neutron NEC plugin
Group: Development/Python

Provides: openstack-quantum-nec = %version-%release
Obsoletes: openstack-quantum-nec < 2013.2-0.4.b3

Requires: %name = %version-%release

%description nec
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using the NEC OpenFlow controller.

%package nuage
Summary: Neutron Nuage plugin
Group: Development/Python

Requires: %name = %version-%release

%description nuage
This plugin implements Neutron v2 APIs with support for Nuage Networks
Virtual Service Platform (VSP).

%package ofagent
Summary: Neutron ofagent plugin from ryu project
Group: Development/Python

Requires: %name = %version-%release

%description ofagent
This plugin implements Neutron v2 APIs with support for the ryu ofagent
plugin.

%package oneconvergence-nvsd
Summary: Neutron One Convergence NVSD plugin
Group: Development/Python

Requires: %name = %version-%release

%description oneconvergence-nvsd
Neutron provides an API to dynamnically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using One Convergence NVSD

%package opencontrail
Summary: Neutron OpenContrail plugin
Group: Development/Python

Requires: %name = %version-%release

%description opencontrail
This plugin implements Neutron v2 APIs with support for the OpenContrail
plugin.

%package openvswitch
Summary: Neutron openvswitch plugin
Group: Development/Python

Requires: %name = %version-%release
Requires: openvswitch

%description openvswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Open vSwitch.

%package plumgrid
Summary: Neutron PLUMgrid plugin
Group: Development/Python

Provides: openstack-quantum-plumgrid = %version-%release
Obsoletes: openstack-quantum-plumgrid < 2013.2-0.4.b3

Requires: %name = %version-%release

%description plumgrid
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the PLUMgrid platform.

%package vmware
Summary: Neutron Nicira plugin
Group: Development/Python

Provides: openstack-quantum-nicira = %version-%release
Obsoletes: openstack-quantum-nicira < 2013.2-0.4.b3
Provides: %name-nicira = %version-%release
Obsoletes: %name-nicira < 2014.1-0.5.b2

Requires: %name = %version-%release

%description vmware
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using VMware NSX.


%package metering-agent
Summary: Neutron bandwidth metering agent
Group: Development/Python

Requires: %name = %version-%release

%description metering-agent
Neutron provides an API to measure bandwidth utilization

This package contains the neutron agent responsible for generating bandwidth
utilization notifications.

%package sriov-nic-agent
Summary: Neutron SR-IOV NIC agent
Group: Development/Python

Requires: %name = %version-%release

%description sriov-nic-agent
Neutron allows to run virtual instances using SR-IOV NIC hardware

This package contains the Neutron agent to support advanced features of
SR-IOV network cards.

%prep
%setup

%patch0001 -p1

find neutron -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i 's/RPMVERSION/%{version}/; s/RPMRELEASE/%{release}/' neutron/version.py

# Ensure SOURCES.txt ends in a newline and if any patches have added files, append them to SOURCES.txt
[ -n "$(tail -c 1 < neutron.egg-info/SOURCES.txt)" ] && echo >> neutron.egg-info/SOURCES.txt
if ls %_sourcedir/*.patch >/dev/null 2>&1; then
  awk '/^new file/ {split(a,files," ");print substr(files[3],3)} {a = $0}' %_sourcedir/*.patch >> neutron.egg-info/SOURCES.txt
fi

chmod 644 neutron/plugins/cisco/README

# Let's handle dependencies ourseleves
rm -f requirements.txt

%build
%python_build

# Loop through values in neutron-dist.conf and make sure that the values
# are substituted into the neutron.conf as comments. Some of these values
# will have been uncommented as a way of upstream setting defaults outside
# of the code. For service_provider and notification-driver, there are
# commented examples above uncommented settings, so this specifically
# skips those comments and instead comments out the actual settings and
# substitutes the correct default values.
while read name eq value; do
  test "$name" && test "$value" || continue
  if [ "$name" = "service_provider" -o "$name" = "notification_driver" ]; then
    sed -ri "0,/^$name *=/{s!^$name *=.*!# $name = $value!}" etc/neutron.conf
  else
    sed -ri "0,/^(#)? *$name *=/{s!^(#)? *$name *=.*!# $name = $value!}" etc/neutron.conf
  fi
done < %SOURCE40

%install
%python_install

# Remove unused files
rm -rf %buildroot%python_sitelibdir/bin
rm -rf %buildroot%python_sitelibdir/doc
rm -rf %buildroot%python_sitelibdir/tools
rm -rf %buildroot%python_sitelibdir/neutron/tests
rm -rf %buildroot%python_sitelibdir/neutron/plugins/*/tests
rm -f %buildroot%python_sitelibdir/neutron/plugins/*/run_tests.*
rm %buildroot/usr/etc/init.d/neutron-server

# Move rootwrap files to proper location
install -d -m 755 %buildroot%_datadir/neutron/rootwrap
mv %buildroot/usr/etc/neutron/rootwrap.d/*.filters %buildroot%_datadir/neutron/rootwrap

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/neutron
mv %buildroot/usr/etc/neutron/* %buildroot%_sysconfdir/neutron
mv %buildroot%_sysconfdir/neutron/api-paste.ini %buildroot%_datadir/neutron/api-paste.ini
chmod 640  %buildroot%_sysconfdir/neutron/plugins/*/*.ini

# Install logrotate
install -p -D -m 644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name

# Install sudoers
install -p -D -m 400 %SOURCE2 %buildroot%_sysconfdir/sudoers.d/neutron

# Install tmpfiles
install -p -D -m 644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf

# Install systemd units
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/neutron-server.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/neutron-linuxbridge-agent.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/neutron-openvswitch-agent.service
install -p -D -m 644 %SOURCE14 %buildroot%_unitdir/neutron-nec-agent.service
install -p -D -m 644 %SOURCE15 %buildroot%_unitdir/neutron-dhcp-agent.service
install -p -D -m 644 %SOURCE16 %buildroot%_unitdir/neutron-l3-agent.service
install -p -D -m 644 %SOURCE17 %buildroot%_unitdir/neutron-metadata-agent.service
install -p -D -m 644 %SOURCE18 %buildroot%_unitdir/neutron-ovs-cleanup.service
install -p -D -m 644 %SOURCE20 %buildroot%_unitdir/neutron-mlnx-agent.service
install -p -D -m 644 %SOURCE22 %buildroot%_unitdir/neutron-metering-agent.service
install -p -D -m 644 %SOURCE23 %buildroot%_unitdir/neutron-sriov-nic-agent.service
install -p -D -m 644 %SOURCE24 %buildroot%_unitdir/neutron-cisco-cfg-agent.service
install -p -D -m 644 %SOURCE25 %buildroot%_unitdir/neutron-netns-cleanup.service

# Install sysV init scripts
install -p -D -m 755 %SOURCE110 %buildroot%_initdir/neutron-server
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/neutron-linuxbridge-agent
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/neutron-openvswitch-agent
install -p -D -m 755 %SOURCE114 %buildroot%_initdir/neutron-nec-agent
install -p -D -m 755 %SOURCE115 %buildroot%_initdir/neutron-dhcp-agent
install -p -D -m 755 %SOURCE116 %buildroot%_initdir/neutron-l3-agent
install -p -D -m 755 %SOURCE117 %buildroot%_initdir/neutron-metadata-agent
install -p -D -m 755 %SOURCE118 %buildroot%_initdir/neutron-ovs-cleanup
install -p -D -m 755 %SOURCE120 %buildroot%_initdir/neutron-mlnx-agent
install -p -D -m 755 %SOURCE122 %buildroot%_initdir/neutron-metering-agent
install -p -D -m 755 %SOURCE123 %buildroot%_initdir/neutron-sriov-nic-agent
install -p -D -m 755 %SOURCE124 %buildroot%_initdir/neutron-cisco-cfg-agent
install -p -D -m 755 %SOURCE125 %buildroot%_initdir/neutron-netns-cleanup

# Setup directories
install -d -m 755 %buildroot%_datadir/neutron
install -d -m 755 %buildroot%_sharedstatedir/neutron
install -d -m 755 %buildroot%_logdir/neutron
install -d -m 755 %buildroot%_runtimedir/neutron

# Install dist conf
install -p -D -m 640 %SOURCE40 %buildroot%_datadir/neutron/neutron-dist.conf

# Install version info file
cat > %buildroot%_sysconfdir/neutron/release <<EOF
[Neutron]
vendor = ALTLinux
product = OpenStack Neutron
package = %release
EOF

%pre
%_sbindir/groupadd -r -f neutron 2>/dev/null ||:
%_sbindir/useradd -r -g neutron -G neutron,wheel -c 'OpenStack Neutron Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/neutron neutron 2>/dev/null ||:


%post
%post_service neutron-dhcp-agent
%post_service neutron-l3-agent
%post_service neutron-metadata-agent
%post_service neutron-server

%preun
%preun_service neutron-dhcp-agent
%preun_service neutron-l3-agent
%preun_service neutron-metadata-agent
%preun_service neutron-server

%post cisco
%post_service neutron-cisco-cfg-agent
%preun cisco
%preun_service neutron-cisco-cfg-agent

%post linuxbridge
%post_service neutron-linuxbridge-agent
%preun linuxbridge
%preun_service neutron-linuxbridge-agent

%post mellanox
%post_service neutron-mlnx-agent
%preun mellanox
%preun_service neutron-mlnx-agent

%post nec
%post_service neutron-nec-agent
%preun nec
%preun_service neutron-nec-agent

%post openvswitch
%post_service neutron-openvswitch-agent
%preun openvswitch
%preun_service neutron-openvswitch-agent

%post metering-agent
%post_service neutron-metering-agent
%preun metering-agent
%preun_service neutron-metering-agent

%post sriov-nic-agent
%post_service neutron-sriov-nic-agent
%preun sriov-nic-agent
%preun_service neutron-sriov-nic-agent

%files
%doc LICENSE
%doc README.rst

%_bindir/neutron-db-manage
%_bindir/neutron-debug
%_bindir/neutron-dhcp-agent
%_bindir/neutron-l3-agent
%_bindir/neutron-metadata-agent
%_bindir/neutron-netns-cleanup
%_bindir/neutron-ns-metadata-proxy
%_bindir/neutron-rootwrap
#%_bindir/neutron-rootwrap-xen-dom0
%_bindir/neutron-sanity-check
%_bindir/neutron-server
%_bindir/neutron-usage-audit

%_unitdir/neutron-dhcp-agent.service
%_unitdir/neutron-l3-agent.service
%_unitdir/neutron-metadata-agent.service
%_unitdir/neutron-server.service
%_unitdir/neutron-netns-cleanup.service
%_initdir/neutron-dhcp-agent
%_initdir/neutron-l3-agent
%_initdir/neutron-metadata-agent
%_initdir/neutron-server
%_initdir/neutron-netns-cleanup

%dir %_sysconfdir/neutron
%_sysconfdir/neutron/release
%attr(-, root, neutron) %_datadir/neutron/neutron-dist.conf
%attr(-, root, neutron) %_datadir/neutron/api-paste.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/dhcp_agent.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/l3_agent.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/metadata_agent.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/policy.json
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/neutron.conf
%config(noreplace) %_sysconfdir/neutron/rootwrap.conf
%dir %_sysconfdir/neutron/plugins
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/sudoers.d/neutron
%dir %attr(0755, neutron, neutron) %_sharedstatedir/neutron
%dir %attr(0755, neutron, neutron) %_logdir/neutron
%dir %attr(0755, neutron, neutron) %_runtimedir/neutron
%_tmpfilesdir/%name.conf
%dir %_datadir/neutron
%dir %_datadir/neutron/rootwrap
%_datadir/neutron/rootwrap/debug.filters
%_datadir/neutron/rootwrap/dhcp.filters
%_datadir/neutron/rootwrap/ipset-firewall.filters
%_datadir/neutron/rootwrap/iptables-firewall.filters
%_datadir/neutron/rootwrap/l3.filters

%files -n python-module-neutron
%doc LICENSE
%doc README.rst
%python_sitelibdir/neutron
%python_sitelibdir/neutron/plugins/__init__.*
%exclude %python_sitelibdir/neutron/plugins/*
%python_sitelibdir/*.egg-info

%files bigswitch
%doc LICENSE
%doc neutron/plugins/bigswitch/README
%_bindir/neutron-restproxy-agent
%python_sitelibdir/neutron/plugins/bigswitch
%dir %_sysconfdir/neutron/plugins/bigswitch
%_sysconfdir/neutron/plugins/bigswitch/ssl
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/bigswitch/*.ini

%if_enabled brocade
%files brocade
%doc LICENSE
%doc neutron/plugins/brocade/README.md
%python_sitelibdir/neutron/plugins/brocade
%dir %_sysconfdir/neutron/plugins/brocade
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/brocade/*.ini
%endif

%if_enabled cisco
%files cisco
%doc LICENSE
%doc neutron/plugins/cisco/README
%_bindir/neutron-cisco-cfg-agent
%_unitdir/neutron-cisco-cfg-agent.service
%_initdir/neutron-cisco-cfg-agent
%python_sitelibdir/neutron/plugins/cisco
%dir %_sysconfdir/neutron/plugins/cisco
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/cisco/*.ini
%endif

%if_enabled embrane
%files embrane
%doc LICENSE
%doc neutron/plugins/embrane/README
%python_sitelibdir/neutron/plugins/embrane
%dir %_sysconfdir/neutron/plugins/embrane
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/embrane/*.ini
%endif

%files hyperv
%doc LICENSE
#%%doc neutron/plugins/hyperv/README
%_bindir/neutron-hyperv-agent
%python_sitelibdir/neutron/plugins/hyperv
%dir %_sysconfdir/neutron/plugins/hyperv
# %%exclude %python_sitelibdir/neutron/plugins/hyperv/agent
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/hyperv/*.ini

%files ibm
%doc LICENSE
%_bindir/neutron-ibm-agent
%doc neutron/plugins/ibm/README
%python_sitelibdir/neutron/plugins/ibm
%dir %_sysconfdir/neutron/plugins/ibm
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/ibm/*.ini

%if_enabled linuxbridge
%files linuxbridge
%doc LICENSE
%doc neutron/plugins/linuxbridge/README
%_bindir/neutron-linuxbridge-agent
%_unitdir/neutron-linuxbridge-agent.service
%_initdir/neutron-linuxbridge-agent
%python_sitelibdir/neutron/plugins/linuxbridge
%_datadir/neutron/rootwrap/linuxbridge-plugin.filters
%dir %_sysconfdir/neutron/plugins/linuxbridge
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/linuxbridge/*.ini
%endif

%if_enabled mellanox
%files mellanox
%doc LICENSE
%doc neutron/plugins/mlnx/README
%_bindir/neutron-mlnx-agent
%_unitdir/neutron-mlnx-agent.service
%_initdir/neutron-mlnx-agent
%python_sitelibdir/neutron/plugins/mlnx
%dir %_sysconfdir/neutron/plugins/mlnx
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/mlnx/*.ini
%endif

%files metaplugin
%doc LICENSE
%doc neutron/plugins/metaplugin/README
%python_sitelibdir/neutron/plugins/metaplugin
%dir %_sysconfdir/neutron/plugins/metaplugin
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/metaplugin/*.ini

%files midonet
%doc LICENSE
#%%doc neutron/plugins/midonet/README
%python_sitelibdir/neutron/plugins/midonet
%dir %_sysconfdir/neutron/plugins/midonet
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/midonet/*.ini

%files ml2
%doc LICENSE
%doc neutron/plugins/ml2/README
%python_sitelibdir/neutron/plugins/ml2
%dir %_sysconfdir/neutron/plugins/ml2
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/ml2/*.ini

%files nec
%doc LICENSE
%doc neutron/plugins/nec/README
%_bindir/neutron-nec-agent
%_unitdir/neutron-nec-agent.service
%_initdir/neutron-nec-agent
%python_sitelibdir/neutron/plugins/nec
%_datadir/neutron/rootwrap/nec-plugin.filters
%dir %_sysconfdir/neutron/plugins/nec
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/nec/*.ini

%files nuage
%doc LICENSE
%python_sitelibdir/neutron/plugins/nuage
%dir %_sysconfdir/neutron/plugins/nuage
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/nuage/*.ini

%if_enabled ofagent
%files ofagent
%doc LICENSE
%doc neutron/plugins/ofagent/README
%_bindir/neutron-ofagent-agent
%python_sitelibdir/neutron/plugins/ofagent
%_datadir/neutron/rootwrap/ofagent.filters
%endif

%files oneconvergence-nvsd
%doc LICENSE
%doc neutron/plugins/oneconvergence/README
%_bindir/neutron-nvsd-agent
%python_sitelibdir/neutron/plugins/oneconvergence
%dir %_sysconfdir/neutron/plugins/oneconvergence
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/oneconvergence/nvsdplugin.ini

%files opencontrail
%doc LICENSE
#%doc neutron/plugins/opencontrail/README
%python_sitelibdir/neutron/plugins/opencontrail
%dir %_sysconfdir/neutron/plugins/opencontrail
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/opencontrail/*.ini

%if_enabled openvswitch
%files openvswitch
%doc LICENSE
%doc neutron/plugins/openvswitch/README
%_bindir/neutron-openvswitch-agent
%_bindir/neutron-ovs-cleanup
%_unitdir/neutron-openvswitch-agent.service
%_initdir/neutron-openvswitch-agent
%_unitdir/neutron-ovs-cleanup.service
%_initdir/neutron-ovs-cleanup
%python_sitelibdir/neutron/plugins/openvswitch
%exclude %python_sitelibdir/neutron/plugins/openvswitch/agent/xenapi
%_datadir/neutron/rootwrap/openvswitch-plugin.filters
%dir %_sysconfdir/neutron/plugins/openvswitch
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/openvswitch/*.ini
%endif

%if_enabled plumgrid
%files plumgrid
%doc LICENSE
%doc neutron/plugins/plumgrid/README
%python_sitelibdir/neutron/plugins/plumgrid
%dir %_sysconfdir/neutron/plugins/plumgrid
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/plumgrid/*.ini
%endif

%files vmware
%doc LICENSE
%_bindir/neutron-check-nsx-config
%_bindir/neutron-nsx-manage
%python_sitelibdir/neutron/plugins/vmware
%dir %_sysconfdir/neutron/plugins/vmware
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/vmware/*.ini

%files metering-agent
%doc LICENSE
%_unitdir/neutron-metering-agent.service
%_initdir/neutron-metering-agent
%_bindir/neutron-metering-agent
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/metering_agent.ini

%files sriov-nic-agent
%doc LICENSE
%_bindir/neutron-sriov-nic-agent
%_unitdir/neutron-sriov-nic-agent.service
%_initdir/neutron-sriov-nic-agent
%python_sitelibdir/neutron/plugins/sriovnicagent

%changelog
* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt2
- openvswitch-agent takes plugins.ml2 directly

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt1
- 2014.1.2

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt3
- openvswitch-agent takes plugins.ml2 by default: most usable configuration

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- user neutron added to wheel group, for neutron-rootwrap

* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- First build for ALT (based on Fedora 2014.1.1-5.fc21.src)
- Add "AutoReq: yes, nopython" to subpackages:
  * brocade, midonet, ofagent, plumgrid

