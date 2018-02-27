Summary: Tool to manage your infrastructure
Name: salt
Version: 2015.5.1
Release: alt3
Url: http://saltstack.org
Source0: %name-%version.tar
License: apache-2.0
Group: System/Configuration/Other

Packager: Valentin Rosavitskiy <valintinr@altlinux.org>

BuildRequires: python-module-setuptools perl-podlators python-module-nose libzeromq-devel python-module-zmq-devel python-module-Crypto python-module-msgpack python-module-yaml

BuildArch: noarch

%add_python_req_skip win32api win32event win32service win32serviceutil winerror pythoncom

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in the
world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds, or even thousands of individual
servers. It handles them quickly and through a simple yet manageable interface.

%package -n python-module-salt
Summary: Management component for salt, a parallel remote execution system
Group: Development/Python
Requires: python-module-yaml python-module-msgpack python-module-json

%description  -n python-module-salt
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in the
world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds, or even thousands of individual
servers. It handles them quickly and through a simple yet manageable interface.

%package -n python-module-salt-tests
Summary: Test files for management component for salt, a parallel remote execution system
Group: Development/Python
Requires: python-module-yaml python-module-msgpack python-module-json

%description  -n python-module-salt-tests
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in the
world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds, or even thousands of individual
servers. It handles them quickly and through a simple yet manageable interface.

%package master
Summary: Management component for salt, a parallel remote execution system
Group: System/Configuration/Other
Requires: python-module-salt = %version-%release

%description master
The Salt master is the central server to which all minions connect.

%package minion
Summary: Client component for salt, a parallel remote execution system
Group: System/Configuration/Other
Requires: python-module-salt = %version-%release

%description minion
Salt minion is queried and controlled from the master.

%package api
Summary: API for salt
Group: System/Configuration/Other
Requires: python-module-salt = %version-%release

%description api
salt-api is a modular interface on top of Salt that can provide
a variety of entry points into a running Salt system. It can start
and manage multiple interfaces allowing a REST API to coexist
with XMLRPC or even a Websocket API.

%prep
%setup

%build
%python_build

%install
%python_build_install --prefix=/usr

install -D -m 755 pkg/altlinux/salt-master.init %buildroot%_initdir/salt-master
install -D -m 755 pkg/altlinux/salt-syndic.init %buildroot%_initdir/salt-syndic
install -D -m 755 pkg/altlinux/salt-minion.init %buildroot%_initdir/salt-minion
install -D -m 755 pkg/altlinux/salt-api.init %buildroot%_initdir/salt-api

mkdir -p %buildroot%_unitdir
install -p -m 0644 pkg/salt-master.service %buildroot%_unitdir/
install -p -m 0644 pkg/salt-syndic.service %buildroot%_unitdir/
install -p -m 0644 pkg/salt-minion.service %buildroot%_unitdir/
install -p -m 0644 pkg/salt-api.service %buildroot%_unitdir/

mkdir -p %buildroot%_sysconfdir/salt/
install -p -m 0640 conf/minion %buildroot%_sysconfdir/salt/minion
install -p -m 0640 conf/master %buildroot%_sysconfdir/salt/master

mkdir -p %buildroot%_sysconfdir/sysconfig
echo "ARG=''" >  %buildroot%_sysconfdir/sysconfig/salt-master
echo "ARG=''" >  %buildroot%_sysconfdir/sysconfig/salt-syndic
echo "ARG=''" >  %buildroot%_sysconfdir/sysconfig/salt-minion

install -D -m 0644 pkg/salt.bash %buildroot%_sysconfdir/bash_completion.d/salt

install -D -m 0644 pkg/altlinux/master.logrotate %buildroot%_sysconfdir/logrotate.d/salt-master
install -D -m 0644 pkg/altlinux/minion.logrotate %buildroot%_sysconfdir/logrotate.d/salt-minion

#TODO: temp fix
rm -rf %python_sitelibdir/salt/cloud/deploy
rm -rf %buildroot%python_sitelibdir/salt/cloud/deploy

#create symlink for opennode
cd %buildroot%python_sitelibdir/salt/modules
ln -s ../../opennode/cli/actions onode

#check
#__python setup.py test --runtests-opts=-u

%post master
%post_service salt-master
%post_service salt-syndic

%preun master
%preun_service salt-master
%preun_service salt-syndic

%post minion
%post_service salt-minion

%preun minion
%preun_service salt-minion


%files -n python-module-salt
%doc AUTHORS README* LICENSE HACKING.rst
%exclude %python_sitelibdir/salt/daemons/test
%python_sitelibdir/*
%_man7dir/salt.7.*

%files -n python-module-salt-tests
%dir %python_sitelibdir/salt/daemons/test
%python_sitelibdir/salt/daemons/test/*


%files master
%config(noreplace) %dir %_sysconfdir/salt
%config(noreplace) %_sysconfdir/salt/master
%config %_sysconfdir/bash_completion.d/*
%config(noreplace) %dir %_sysconfdir/bash_completion.d
%config(noreplace) %_sysconfdir/logrotate.d/salt-master

%config(noreplace) %_sysconfdir/sysconfig/salt-master
%config(noreplace) %_sysconfdir/sysconfig/salt-syndic

%_initdir/salt-master
%_initdir/salt-syndic

%_unitdir/salt-master.service
%_unitdir/salt-syndic.service

%_bindir/salt
%_bindir/salt-master
%_bindir/salt-syndic
%_bindir/salt-cp
%_bindir/salt-key
%_bindir/salt-run
%_bindir/salt-ssh
%_bindir/salt-cloud
%_bindir/salt-unity

%_man1dir/salt-master.1.*
%_man1dir/salt-cp.1.*
%_man1dir/salt-key.1.*
%_man1dir/salt-run.1.*
%_man1dir/salt-syndic.1.*
%_man1dir/salt-ssh.1.*
%_man1dir/salt-cloud.1.*
%_man1dir/salt-unity.1.*

%files api
%_bindir/salt-api
%_initdir/salt-api
%_unitdir/salt-api.service
%_man1dir/salt-api.1.*

%files minion
%config(noreplace) %dir %_sysconfdir/salt
%config(noreplace) %_sysconfdir/salt/minion
%config(noreplace) %_sysconfdir/logrotate.d/salt-minion

%config(noreplace) %_sysconfdir/sysconfig/salt-minion

%_initdir/salt-minion
%_unitdir/salt-minion.service

%_bindir/salt-minion
%_bindir/salt-call

%_man1dir/salt-call.1.*
%_man1dir/salt-minion.1.*

%changelog
* Fri May 29 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 2015.5.1-alt3
- New version

* Sat Apr 18 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 2015.2-alt3
- Removed code from previous tag (ALT 30929)

* Thu Feb 12 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 2015.2-alt2
- Add subpackage python-module-salt-tests

* Mon Feb 02 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 2015.2-alt1
- New version

* Wed Dec 10 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 2014.7-alt3
- Add subpackage salt-api

* Mon Nov 03 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 2014.7-alt2
- Fix repocop info symlink-extra-slash

* Tue Oct 28 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 2014.7-alt1
- New version

* Tue May 13 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.17.5-alt1
- New version

* Fri Jan 10 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.17.4-alt1
- New version

* Sun Nov 24 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.17.2-alt1
- New version

* Sat Sep 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.17.0-alt1
- New version

* Wed Jan 02 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11.1-alt3
- Update spec
- Fix init scripts

* Mon Dec 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11.1-alt2
- New version

* Thu Dec 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.10.5-alt1
- Build for ALT
