Name: galera
Version: 25.3.12
Release: alt1
Summary: Synchronous multi-master wsrep provider (replication engine)
Group: System/Servers
License: GPLv2
Url: http://www.http://galeracluster.com/
Source: %name-%version.tar

Source1: garbd.init
Source2: garbd.service
Source3: garbd.tmpfiles
Source4: garbd.conf

BuildRequires: gcc-c++ scons
BuildRequires: boost-devel boost-program_options-devel
BuildRequires: libcheck-devel libssl-devel

%description
Galera is a fast synchronous multi-master wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see http://launchpad.net/wsrep. For a description of Galera
replication engine see http://www.codership.com.

%prep
%setup

%build
export CPPFLAGS="%optflags"
scons %{?_smp_mflags} strict_build_flags=0

%install
install -D -m 755 %SOURCE1 %buildroot%_initdir/garbd
install -D -m 644 %SOURCE2 %buildroot%_unitdir/garbd.service
mkdir -p %buildroot%_runtimedir/garbd
install -D -m 644 %SOURCE3 %buildroot%_tmpfilesdir/garbd.conf
install -D -m 644 %SOURCE4 %buildroot%_sysconfdir/garbd/garbd.conf
install -D -m 755 garb/garbd %buildroot%_sbindir/garbd
install -D -m 644 libgalera_smm.so %buildroot%_libdir/galera/libgalera_smm.so
install -D -m 644 COPYING %buildroot%_docdir/galera/COPYING
install -D -m 644 chromium/LICENSE %buildroot%_docdir/galera/LICENSE.chromium
install -D -m 644 asio/LICENSE_1_0.txt %buildroot%_docdir/galera/LICENSE.asio
install -D -m 644 www.evanjones.ca/LICENSE %buildroot%_docdir/galera/LICENSE.crc32
install -D -m 644 scripts/packages/README %buildroot%_docdir/galera/README
install -D -m 644 scripts/packages/README-MySQL %buildroot%_docdir/galera/README-MySQL

%post
%post_service garbd

%preun
%preun_service garbd

%files
%dir %_sysconfdir/garbd
%config(noreplace) %_sysconfdir/garbd/garbd.conf
%dir %_docdir/galera
%dir %_libdir/galera
%_sbindir/garbd
%_unitdir/garbd.service
%_initdir/garbd
%_tmpfilesdir/garbd.conf
%_runtimedir/garbd
%_libdir/galera/libgalera_smm.so
%doc %_docdir/galera/COPYING
%doc %_docdir/galera/LICENSE.asio
%doc %_docdir/galera/LICENSE.crc32
%doc %_docdir/galera/LICENSE.chromium
%doc %_docdir/galera/README
%doc %_docdir/galera/README-MySQL

%changelog
* Thu Sep 03 2015 Alexey Shabalin <shaba@altlinux.ru> 25.3.12-alt1
- Initial build
