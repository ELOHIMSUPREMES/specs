%global import_path github.com/influxdata/telegraf
%global commit 7bbd3daa98d5931c6e9025a98105092b0722de0d

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name:		telegraf
Version:	1.3.5
Release:	alt1%ubt
Summary:	The plugin-driven server agent for collecting and reporting metrics

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/telegraf

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar

Source101: telegraf.logrotate
Source102: telegraf.init
Source103: telegraf.service
Source104: telegraf.tmpfiles

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang rpm-build-ubt

%description
Telegraf is an agent written in Go for collecting, processing, aggregating, and writing metrics.

Design goals are to have a minimal memory footprint with a plugin system so that developers
in the community can easily add support for collecting metrics from well known services
(like Hadoop, Postgres, or Redis) and third party APIs (like Mailchimp, AWS CloudWatch,
or Google Analytics).

%prep
%setup -q

%build
# Important!!!
# The %builddir/.gopath created by the hands. It contains the dependencies required for your project.
# This is necessary because the gdm cannot work with the vendor directory and always tries to update
# all dependencies from the external servers. So, we can't use Makefile to compile.
#
# $ export GOPATH="$PWD/.gopath"
# $ git rm -rf -- "$GOPATH"
# $ make
# $ find $GOPATH -type d -name .git |xargs rm -rf --
# $ git add "$GOPATH"

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...


%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot/%_datadir

# Install config files
install -p -D -m 640 etc/telegraf.conf %buildroot%_sysconfdir/%name/%name.conf
install -d -m 750 %buildroot%_sysconfdir/%name/%name.d
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 750 %buildroot%_sharedstatedir/%name
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install logrotate
install -p -D -m 644 %SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'Telegraf Agent Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:
%post
%post_service %name

%preun
%preun_service %name

%files
%doc docs/*
%_bindir/%name
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%dir %attr(0750, root, %name) %_sysconfdir/%name/%name.d
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.conf
%config(noreplace) %_logrotatedir/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name

%changelog
* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1%ubt
- rebuild with Universal Branch Tag
- fix run with sysv init script

* Thu Jul 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- 1.3.5
- upadte init script
- add user home dir to files

* Mon Jul 24 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt2
- add sysv init, systemd unit, logrotate config, tmpfiles

* Sun Jul 23 2017 Alexey Gladkov <legion@altlinux.ru> 1.3.4-alt1
- First build for ALTLinux.
