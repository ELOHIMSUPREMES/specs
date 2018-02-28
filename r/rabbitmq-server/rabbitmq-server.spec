%define _unpackaged_files_terminate_build 1
%define oname rabbitmq

%add_findreq_skiplist */ocf/resource.d/rabbitmq/*

# workaround for not find Provides in plugins/*.ez files
%add_erlang_req_modules_skiplist app_utils credit_flow gen_server2 mirrored_supervisor pmon priority_queue ranch rand_compat supervisor2 time_compat
%add_erlang_req_modules_skiplist rabbit_amqqueue rabbit_auth_backend_dummy rabbit_auth_backend_internal rabbit_backing_queue rabbit_basic
%add_erlang_req_modules_skiplist rabbit_channel rabbit_control_misc rabbit_event rabbit_exchange_decorator rabbit_health_check rabbit_net
%add_erlang_req_modules_skiplist rabbit_networking rabbit_nodes rabbit_queue_decorator rabbit_reader



Name: rabbitmq-server
Version: 3.6.8
Release: alt2
License: MPLv1.1
BuildArch: noarch
Group: System/Servers
Source: %name-%version.tar
Source1: rabbitmq-server.init
Source2: rabbitmq-script-wrapper
Source3: rabbitmq-server.logrotate
Source4: rabbitmq-env.conf
Source5: include.mk
Source6: rabbitmq-server.service
Source7: rabbitmq-server.tmpfiles

Patch1: rabbitmq-server-0001-Remove-excessive-sd_notify-code.patch
Patch2: rabbitmq-server-0002-Add-systemd-notification-support.patch
Patch3: rabbitmq-server-0003-Revert-Distinct-exit-codes-for-CLI-utilities.patch
Patch4: rabbitmq-server-0004-Allow-guest-login-from-non-loopback-connections.patch
Patch5: rabbitmq-server-0005-rabbit_prelaunch-must-use-RABBITMQ_SERVER_ERL_ARGS.patch
Patch101: rabbitmq-common-0001-Use-proto_dist-from-command-line.patch

URL: http://www.rabbitmq.com/
Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: python-module-simplejson python-modules-xml
BuildRequires: xmlto zip unzip netcat rsync
Requires: erlang

# workaround for not find Provides in plugins/*.ez files
Provides: erlang_app(rabbit_common) = %version
Provides: erlang_app(ranch) = %version

Provides: erlang_mod(ec_semver) = %version
Provides: erlang_mod(rabbit_cert_info) = %version
Provides: erlang_mod(rabbit_core_metrics) = %version
Provides: erlang_mod(rabbit_data_coercion) = %version
Provides: erlang_mod(rabbit_pbe) = %version

# second workaround for not requires tsung
Provides: erlang_mod(rabbit_binary_parser)  = %version
Provides: erlang_mod(rabbit_command_assembler) = %version
Provides: erlang_mod(rabbit_misc) = %version


Summary: The RabbitMQ server

%description
RabbitMQ is an implementation of AMQP, the emerging standard for high
performance enterprise messaging. The RabbitMQ server is a robust and
scalable implementation of an AMQP broker.

%package -n %name-devel
Summary: %name header files
License: MPLv1.1
Group: Development/Erlang

%description -n %name-devel
Erlang header files for %name

%prep
%setup -q
cd deps/rabbit
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
cd ../..

cd deps/rabbit_common
%patch101 -p1
cd ../..

# We have to remove it until common_test subpackage lands RHOS
rm -f \
    deps/amqp_client/src/rabbit_ct_client_helpers.erl \
    deps/rabbit_common/src/rabbit_ct_broker_helpers.erl \
    deps/rabbit_common/src/rabbit_ct_helpers.erl

%build
sed -i 's|@libexecdir@|%_libexecdir|g' %SOURCE2
sed -i 's|@localstatedir@|%_localstatedir|g' %SOURCE2
#sed -i 's|@RABBITMQ_DIR@|%_erlanglibdir/rabbitmq_server-%version|g' %SOURCE5

export VERSION=%version
%make_build

%install
%makeinstall_std \
        VERSION="%version" \
        PREFIX=%_prefix \
        install-bin install-man


mkdir -p %buildroot%_localstatedir/%oname/mnesia
mkdir -p %buildroot%_logdir/%oname

#Copy all necessary lib files etc.

#Sysvinit support
install -p -D -m 0755 %SOURCE1 %buildroot%_initrddir/%oname

install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/rabbitmqctl
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/%{oname}-server
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/%{oname}-plugins
install -p -D -m 0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -p -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/%oname/%{oname}-env.conf
install -p -D -m 0644 deps/rabbit/docs/rabbitmq.config.example %buildroot%_sysconfdir/%oname/rabbitmq.config
#install -p -D -m 0644 %SOURCE5 %buildroot%_datadir/%name/include.mk
install -p -D -m 0644 %SOURCE6 %buildroot%_unitdir/%oname.service
install -p -D -m 0644 %SOURCE7 %buildroot%_tmpfilesdir/%oname.conf
install -d %buildroot%_runtimedir/%oname

# Make necessary symlinks
mkdir -p %buildroot%_libexecdir/%oname
for app in rabbitmq-defaults rabbitmq-env rabbitmq-plugins rabbitmq-server rabbitmqctl ; do
    ln -r -s %buildroot%_erlanglibdir/rabbitmq_server-%version/sbin/${app} %buildroot%_libexecdir/%oname/${app}
done

install -p -D -m 0755 scripts/rabbitmq-server.ocf %buildroot%_libexecdir/ocf/resource.d/rabbitmq/rabbitmq-server
install -p -D -m 0755 scripts/rabbitmq-server-ha.ocf %buildroot%_libexecdir/ocf/resource.d/rabbitmq/rabbitmq-server-ha

mkdir -p %buildroot%_sysconfdir/%oname/conf.d
rm -f %buildroot%_erlanglibdir/rabbitmq_server-%version/{LICENSE,LICENSE-*,INSTALL}

%pre
%_sbindir/groupadd -r -f rabbitmq &>/dev/null
%_sbindir/useradd -r -g rabbitmq  -d %_localstatedir/rabbitmq -s /dev/null \
   -c 'RabbitMQ messaging server' -M -n rabbitmq &>/dev/null ||:

%post
%post_service %oname

%preun
%preun_service %oname

%files
%doc LICENSE LICENSE-* deps/rabbit/docs/rabbitmq.config.example
%_sbindir/*
%_libexecdir/%oname
%_erlanglibdir/rabbitmq_server-%version
%_erldir/bin/*
%exclude %_erlanglibdir/rabbitmq_server-%version/include
%attr(0750, rabbitmq, rabbitmq) %dir %_localstatedir/%oname
%attr(0750, rabbitmq, rabbitmq) %dir %_localstatedir/%oname/mnesia
%attr(0750, rabbitmq, rabbitmq) %dir %_logdir/%oname
%attr(0750, rabbitmq, rabbitmq) %dir %_runtimedir/%oname
%config(noreplace) %_logrotatedir/*
%config(noreplace) %_sysconfdir/%oname
%_man1dir/*
%_man5dir/*
%_unitdir/%oname.service
%_tmpfilesdir/%oname.conf
%_initrddir/%oname
%_libexecdir/ocf/resource.d/rabbitmq

%files -n %name-devel
%_erlanglibdir/rabbitmq_server-%version/include
#%_datadir/%name

%changelog
* Tue Mar 28 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.8-alt2
- fix logrotate config

* Fri Mar 17 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.8-alt1
- 3.6.8
- fixed CVE-2016-9877

* Wed Sep 28 2016 Alexey Shabalin <shaba@altlinux.ru> 3.6.5-alt1
- 3.6.5

* Fri Jun 10 2016 Denis Medvedev <nbr@altlinux.org> 3.5.4-alt2.2
- Recompile with OTP-18.3.3

* Sun Apr 10 2016 Denis Medvedev <nbr@altlinux.org> 3.5.4-alt2.1
- Recompile with OTP-18.3

* Thu Sep 17 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5.4-alt2
- Fix version

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5.4-alt1
- 3.5.4

* Sun Dec 29 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.2.2-alt1
- New version (ALT #27190)

* Wed Aug 21 2013 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt4
- Fix spacing in the sysvinit script

* Fri Aug 16 2013 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt3
- Fix sysvinit script

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt2
- Change configuration file name
- Return sysvinit support

* Thu Oct 04 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt1
- New version 2.8.7

* Sat Oct 31 2009 Maxim Ivanov <redbaron at altlinux.org> 1.7.0-alt1
- New version
- New plugin architecture introduced

* Sun Sep 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt3
- New conf.d dir for plugable addons configs
- fix condreload arg support in init script

* Mon Jul 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt2
- Header files packed separately now
- Fix added condstop to init script

* Sun Jul 19 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt1
- Initial build for ALTLinux

