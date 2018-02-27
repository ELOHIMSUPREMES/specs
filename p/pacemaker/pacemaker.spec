Name: pacemaker
Summary: Scalable High-Availability cluster resource manager
Version: 1.1.10
Release: alt4
License: GPLv2+ and LGPLv2+
Url: http://www.clusterlabs.org
Group: System/Servers
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: /proc glib2-devel libxml2-devel libxslt-devel libuuid-devel systemd-devel perl(Pod/Text.pm)
BuildRequires: pkgconfig python-devel gcc-c++ bzlib-devel libpam-devel
BuildRequires: libqb-devel > 0.11.0 libgnutls-devel libltdl-devel libgio-devel
BuildRequires: libncurses-devel libssl-devel libselinux-devel docbook-style-xsl
BuildRequires: bison flex help2man
BuildRequires: libesmtp-devel libsensors3-devel libnet-snmp-devel
#libopenipmi-devel libservicelog-devel
BuildRequires: libcorosync2-devel libcluster-glue-devel
BuildRequires: publican inkscape asciidoc

%define gname haclient
%define uname hacluster

%description
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

It supports "n-node" clusters with significant capabilities for
managing resources and dependencies.

It will run scripts at initialization, when machines go up or down,
when related resources fail and can be configured to periodically check
resource health.

Available rpmbuild rebuild options:
  --with(out) : heartbeat cman corosync doc publican snmp esmtp pre_release

%package cli
License: GPLv2+ and LGPLv2+
Summary: Command line tools for controlling Pacemaker clusters
Group: System/Servers
Requires: perl-DateTime-Format-DateParse

%description cli
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The %name-cli package contains command line tools that can be used
to query and control the cluster from machines that may, or may not,
be part of the cluster.

%package -n lib%name
License: GPLv2+ and LGPLv2+
Summary: Core Pacemaker libraries
Group: System/Servers

%description -n lib%name
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The lib%name package contains shared libraries needed for cluster
nodes and those just running the CLI tools.

%package -n %name-remote
License: GPLv2+ and LGPLv2+
Summary: Pacemaker remote daemon for non-cluster nodes
Group: System/Servers

%description -n %name-remote
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The %name-remote package contains the Pacemaker Remote daemon
which is capable of extending pacemaker functionality to remote
nodes not running the full corosync/cluster stack.

%package -n lib%name-devel
License: GPLv2+ and LGPLv2+
Summary: Pacemaker development package
Group: Development/C
#Requires: %name-cts = %version-%release
Requires: lib%name = %version-%release
Requires: libqb-devel libuuid-devel
Requires: libxml2-devel libxslt-devel bzlib-devel glib2-devel
Requires: libcorosync2-devel

%description -n lib%name-devel
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The lib%name-devel package contains headers and shared libraries
for developing tools for Pacemaker.

%package cts
License: GPLv2+ and LGPLv2+
Summary: Test framework for cluster-related technologies like Pacemaker
Group: System/Servers
Requires: resource-agents

%description cts
Test framework for cluster-related technologies like Pacemaker

%package doc
License: GPLv2+ and LGPLv2+
Summary: Documentation for Pacemaker
Group: System/Servers
BuildArch: noarch

%description doc
Documentation for Pacemaker.

Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

%prep
%setup
%patch -p1

%build
%autoreconf

%configure \
        --with-profiling	\
        --with-gcov		\
        --with-acl		\
        --with-ais		\
        --with-corosync		\
        --with-cs-quorum	\
        --enable-thread-safe	\
        --with-initdir=%_initdir	\
        --localstatedir=%_var		\
        --with-version=%version-%release

subst 's|/usr/bin/help2man|/usr/bin/help2man --no-discard-stderr|g' tools/Makefile

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_var/lib/pacemaker/cores
install -D -m 644 mcp/pacemaker.sysconfig %buildroot%_sysconfdir/sysconfig/pacemaker
install -D -m 755 pacemaker.init %buildroot%_initdir/pacemaker


# Scripts that should be executable
chmod a+x %buildroot%_datadir/pacemaker/tests/cts/CTSlab.py

# These are not actually scripts
find %buildroot -name '*.xml' -type f -print0 | xargs -0 chmod a-x
find %buildroot -name '*.xsl' -type f -print0 | xargs -0 chmod a-x
find %buildroot -name '*.rng' -type f -print0 | xargs -0 chmod a-x
find %buildroot -name '*.dtd' -type f -print0 | xargs -0 chmod a-x

# Dont package static libs
find %buildroot -name '*.a' -type f -print0 | xargs -0 rm -f
find %buildroot -name '*.la' -type f -print0 | xargs -0 rm -f

# Do not package these either
rm -f %buildroot/%_libdir/service_crm.so

GCOV_BASE=%buildroot/%_var/lib/pacemaker/gcov
mkdir -p $GCOV_BASE
find . -name '*.gcno' -type f | while read F ; do
        D=`dirname $F`
        mkdir -p ${GCOV_BASE}/$D
        cp $F ${GCOV_BASE}/$D
done


%pre
groupadd -f -r %gname ||:
getent passwd %uname >/dev/null || useradd -r -g %gname -s /sbin/nologin -c "cluster user" %uname ||:

%post
%post_service %name

%preun
%preun_service %name

%post -n %name-remote
%post_service pacemaker_remote

%preun -n %name-remote
%preun_service pacemaker_remote

%files
%exclude %_datadir/pacemaker/tests
%exclude %_libexecdir/pacemaker/lrmd_test
%exclude %_sbindir/pacemaker_remoted

%config(noreplace) %_sysconfdir/sysconfig/pacemaker
%_sbindir/pacemakerd
%_initdir/pacemaker

%_unitdir/pacemaker.service

%_datadir/pacemaker
%_datadir/snmp/mibs/PCMK-MIB.txt
%_libexecdir/pacemaker/*

#_libdir/heartbeat/*

%_sbindir/crm_attribute
%_sbindir/crm_master
%_sbindir/crm_node
%_sbindir/crm_verify
%_sbindir/attrd_updater
%_sbindir/fence_legacy
%_sbindir/fence_pcmk
%_sbindir/crm_resource
#_bindir/ccs_flatten
#_bindir/disable_rgmanager
%_sbindir/stonith_admin
#_sbindir/crm_uuid

%doc %_mandir/man8/attrd_updater.*
%doc %_mandir/man8/crm_attribute.*
%doc %_mandir/man8/crm_node.*
%doc %_mandir/man8/crm_master.*
%doc %_mandir/man8/fence_pcmk.*
%doc %_mandir/man8/pacemakerd.*
%doc %_mandir/man8/stonith_admin.*

%doc COPYING AUTHORS ChangeLog

%dir %attr (750, %uname, %gname) %_var/lib/pacemaker
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/cib
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/cores
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/pengine
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/blackbox
%ghost %dir %attr (750, %uname, %gname) %_var/run/crm
%dir /usr/lib/ocf
%dir /usr/lib/ocf/resource.d
/usr/lib/ocf/resource.d/pacemaker

#_libexecdir/lcrso/pacemaker.lcrso

%files cli
%_sbindir/cibadmin
#_sbindir/cibsecret
%_sbindir/crm_diff
%_sbindir/crm_error
%_sbindir/crm_failcount
%_sbindir/crm_mon
%_sbindir/crm_standby
%_sbindir/crmadmin
%_sbindir/iso8601
%_sbindir/crm_shadow
%_sbindir/crm_simulate
%_sbindir/crm_report
%_sbindir/crm_ticket
%doc %_mandir/man8/*
%exclude %_mandir/man8/attrd_updater.*
%exclude %_mandir/man8/crm_attribute.*
%exclude %_mandir/man8/crm_node.*
%exclude %_mandir/man8/crm_master.*
%exclude %_mandir/man8/fence_pcmk.*
%exclude %_mandir/man8/pacemakerd.*
%exclude %_mandir/man8/pacemaker_remoted.*
%exclude %_mandir/man8/stonith_admin.*

%doc COPYING AUTHORS ChangeLog

%files -n lib%name
%_libdir/libcib.so.*
%_libdir/liblrmd.so.*
%_libdir/libcrmservice.so.*
%_libdir/libcrmcommon.so.*
%_libdir/libpe_status.so.*
%_libdir/libpe_rules.so.*
%_libdir/libpengine.so.*
%_libdir/libstonithd.so.*
%_libdir/libtransitioner.so.*
%_libdir/libcrmcluster.so.*
%doc COPYING.LIB AUTHORS

%files -n %name-remote
%config(noreplace) %_sysconfdir/sysconfig/pacemaker
%_initdir/pacemaker_remote
%_unitdir/pacemaker_remote.service

%_sbindir/pacemaker_remoted
%_mandir/man8/pacemaker_remoted.*
%doc COPYING.LIB AUTHORS

%files doc
%doc %_docdir/%name

%files cts
%python_sitelibdir/cts
%_datadir/pacemaker/tests/cts
%_libexecdir/pacemaker/lrmd_test
%doc COPYING.LIB AUTHORS

%files -n lib%name-devel
%exclude %_datadir/pacemaker/tests/cts
%_datadir/pacemaker/tests
%_includedir/pacemaker
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%doc COPYING.LIB AUTHORS

%changelog
* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt4
- NMU: added missing Pod dependencies

* Thu Aug 15 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.10-alt3
- Fix initscript

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.10-alt2
- New version

* Mon May 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.10-alt1.rc3
- New RC

* Sat Apr 06 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.9-alt2.git.132019bd
- New version

* Thu Mar 21 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.9-alt1
- Build for ALT
