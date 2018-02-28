%define _unpackaged_files_terminate_build 1
%define oname rabbitmq

Name: rabbitmq-server
Version: 3.5.4
Release: alt2.2
License: MPLv1.1
BuildArch: noarch
Group: System/Servers
Source: %name-%version.tar
Source100: codegen.tar
Source1: rabbitmq-server.init
Source2: rabbitmq-script-wrapper
Source3: rabbitmq-server.logrotate
Source4: rabbitmq-env.conf
Source5: include.mk
Source6: rabbitmq-server.service
Source7: rabbitmq-server.tmpfiles

Patch: rabbitmq-probe-ephemeral-port.patch

URL: http://www.rabbitmq.com/
Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: python-module-simplejson python-modules-xml
BuildRequires: xmlto zip unzip netcat
Requires: erlang

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
mkdir -p codegen
tar -xf %SOURCE100 -C codegen
%patch -p1

%build
sed -i 's|@libexecdir@|%_libexecdir|g' %SOURCE2
sed -i 's|@localstatedir@|%_localstatedir|g' %SOURCE2
sed -i 's|@RABBITMQ_DIR@|%_erllibdir/%name|g' %SOURCE5

export VERSION=%version
%make_build

%install
%make_install TARGET_DIR=%buildroot%_erllibdir/%name \
        SBIN_DIR=%buildroot%_libexecdir/%oname \
        MAN_DIR=%buildroot%_mandir \
        DOC_INSTALL_DIR=%buildroot%_defaultdocdir/%name-%version \
        install

mkdir -p %buildroot%_localstatedir/%oname/mnesia
mkdir -p %buildroot%_logdir/%oname

#Copy all necessary lib files etc.

#Sysvinit support
install -p -D -m 0755 %SOURCE1 %buildroot%_initrddir/%oname

install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/rabbitmqctl
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/%name
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/%oname-plugins
install -p -D -m 0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -p -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/%oname/%{oname}-env.conf
install -p -D -m 0644 %SOURCE5 %buildroot%_datadir/%name/include.mk
install -p -D -m 0644 %SOURCE6 %buildroot%_unitdir/%oname.service
install -p -D -m 0644 %SOURCE7 %buildroot%_tmpfilesdir/%oname.conf
install -d %buildroot%_runtimedir/%oname

mkdir -p %buildroot%_sysconfdir/%oname/conf.d
rm %buildroot%_erllibdir/%name/{LICENSE,LICENSE-MPL-RabbitMQ,INSTALL}

mkdir -p %buildroot/%_erlanglibdir/%name/priv

%pre
%_sbindir/groupadd -r -f rabbitmq &>/dev/null
%_sbindir/useradd -r -g rabbitmq  -d %_localstatedir/rabbitmq -s /dev/null \
   -c 'RabbitMQ messaging server' -M -n rabbitmq &>/dev/null ||:

%post
%post_service %oname

%preun
%preun_service %oname

%files
%_sbindir/*
%_libexecdir/%oname
%_erlanglibdir/%name
%exclude %_erlanglibdir/%name/include
%attr(0750, rabbitmq, rabbitmq) %dir %_localstatedir/%oname
%attr(0750, rabbitmq, rabbitmq) %dir %_logdir/%oname
%attr(0750, rabbitmq, rabbitmq) %dir %_runtimedir/%oname
%config(noreplace) %_logrotatedir/*
%config(noreplace) %_sysconfdir/%oname
%_man1dir/*
%_man5dir/*
%_unitdir/%oname.service
%_tmpfilesdir/%oname.conf
%_initrddir/%oname
%doc LICENSE LICENSE-MPL-RabbitMQ README INSTALL docs/rabbitmq.config.example

%files -n %name-devel
%_erlanglibdir/%name/include
%_datadir/%name

%changelog
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

