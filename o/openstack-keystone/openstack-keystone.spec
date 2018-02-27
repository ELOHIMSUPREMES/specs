%def_without python3

Name: openstack-keystone
Version: 2015.1.0
Release: alt1
Summary: OpenStack Identity Service

%add_python_req_skip xmldsig

Group: System/Servers
License: ASL 2.0
URL: http://keystone.openstack.org/
Source0: %name-%version.tar
Source1: %name.logrotate
Source2: %name.service
Source3: %name.sysctl
Source4: %name.tmpfiles
Source5: %name-sample-data
Source20: keystone-dist.conf
Source100: %name.init

BuildArch: noarch

Requires(pre): python-module-keystone = %version-%release
Requires: python-module-keystoneclient >= 1.1.0
Conflicts: python-module-keystoneclient > 1.4.0
Requires: /usr/bin/uuidgen

Requires(pre): shadow-utils

BuildRequires: python-devel
BuildRequires: python-module-sphinx >= 1.0
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-pycadf
BuildRequires: python-module-passlib
BuildRequires: python-module-webtest
BuildRequires: python-module-SQLAlchemy >= 0.9.7
BuildRequires: python-module-migrate >= 0.9.5
BuildRequires: python-module-jsonschema
BuildRequires: python-module-oslo.config >= 1.9.3
BuildRequires: python-module-oslo.messaging >= 1.8.0
BuildRequires: python-module-oslo.db >= 1.7.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.log >= 1.0.0
BuildRequires: python-module-oslo.middleware >= 1.0.0
BuildRequires: python-module-oslo.policy >= 0.3.1
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 1.4.0
BuildRequires: python-module-oslotest >= 1.5.1
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-paste
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-keystoneclient >= 1.1.0
BuildRequires: python-module-dogpile-cache >= 0.5.3
BuildRequires: python-module-ldap
BuildRequires: python-module-oauthlib >= 0.6
BuildRequires: python-module-eventlet >= 0.16.1
BuildRequires: python-module-cryptography >= 0.8

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx >= 1.0
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-pbr
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-pycadf
BuildRequires: python3-module-passlib
BuildRequires: python-module-webtest
BuildRequires: python3-module-SQLAlchemy >= 0.9.7
BuildRequires: python3-module-migrate >= 0.9.5
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-oslo.config >= 1.9.3
BuildRequires: python3-module-oslo.messaging >= 1.8.0
BuildRequires: python3-module-oslo.db >= 1.7.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.log >= 1.0.0
BuildRequires: python3-module-oslo.middleware >= 1.0.0
BuildRequires: python3-module-oslo.policy >= 0.3.1
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 1.4.0
BuildRequires: python3-module-oslotest >= 1.5.1
BuildRequires: python3-module-routes >= 1.12.3
BuildRequires: python3-module-paste
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-keystoneclient >= 1.1.0
BuildRequires: python3-module-dogpile-cache >= 0.5.3
BuildRequires: python3-module-ldap
BuildRequires: python3-module-oauthlib >= 0.6
BuildRequires: python3-module-eventlet >= 0.16.1
%endif


%description
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone daemon.

%package -n python-module-keystone
Summary: Keystone Python libraries
Group: Development/Python
Requires: openssl
Requires: python-module-oslo.config >= 1.9.3
Requires: python-module-oslo.messaging >= 1.8.0
Requires: python-module-oslo.db >= 1.7.0
Requires: python-module-oslo.i18n >= 1.5.0
Requires: python-module-oslo.utils >= 1.4.0
# add not finded requires
Requires: python-module-dogpile-cache
Requires: python-module-PasteDeploy
Requires: python-module-pysaml2

%description -n python-module-keystone
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.

%package -n python3-module-keystone
Summary: Keystone Python libraries
Group: Development/Python3
Requires: openssl
Requires: python3-module-oslo.config >= 1.6.0
Requires: python3-module-oslo.messaging >= 1.6.0
Requires: python3-module-oslo.db
Requires: python3-module-oslo.i18n
Requires: python3-module-oslo.utils

# add not finded requires
Requires: python3-module-dogpile-cache

%description -n python3-module-keystone
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.

%package doc
Summary:	Documentation for OpenStack Identity Service
Group:		Development/Documentation

%description doc
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains documentation for Keystone.

%prep
%setup

find . \( -name .gitignore -o -name .placeholder \) -delete
find keystone -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;
# Remove bundled egg-info
#rm -rf keystone.egg-info

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
cp etc/keystone.conf.sample etc/keystone.conf
# distribution defaults are located in keystone-dist.conf
%python_build
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b man doc/source doc/build/man
sphinx-build -b html doc/source doc/build/html

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/keystone-all %buildroot%_bindir/python3-keystone-all
mv %buildroot%_bindir/keystone-manage %buildroot%_bindir/python3-keystone-manage
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
%if_with python3
rm -fr %buildroot%python3_sitelibdir/*/tests
%endif

install -d -m 755 %buildroot%_sysconfdir/keystone
install -p -D -m 640 etc/keystone.conf %buildroot%_sysconfdir/keystone/keystone.conf
install -p -D -m 644 etc/keystone-paste.ini %buildroot%_datadir/keystone/keystone-dist-paste.ini
# kilo-3 workaround: remove federation from default pipeline
sed -i '/^pipeline/s/federation_extension//' %buildroot%_datadir/keystone/keystone-dist-paste.ini

install -p -D -m 644 %SOURCE20 %buildroot%_datadir/keystone/keystone-dist.conf
install -p -D -m 644 etc/policy.v3cloudsample.json %buildroot%_datadir/keystone/policy.v3cloudsample.json
install -p -D -m 640 etc/logging.conf.sample %buildroot%_sysconfdir/keystone/logging.conf
install -p -D -m 640 etc/default_catalog.templates %buildroot%_sysconfdir/keystone/default_catalog.templates
install -p -D -m 640 etc/policy.json %buildroot%_sysconfdir/keystone/policy.json
install -p -D -m 640 etc/sso_callback_template.html %buildroot%_sysconfdir/keystone/sso_callback_template.html
install -p -D -m 644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/openstack-keystone
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/openstack-keystone.service
install -d -m 755 %buildroot%_sysctldir
install -p -D -m 644 %SOURCE3 %buildroot%_sysctldir/openstack-keystone.conf
install -d -m 755 %buildroot%_tmpfilesdir
install -p -D -m 644 %SOURCE4 %buildroot%_tmpfilesdir/openstack-keystone.conf
install -p -D -m 755 %SOURCE100 %buildroot%_initdir/%name
# Install sample data script.
install -p -D -m 755 tools/sample_data.sh %buildroot%_datadir/keystone/sample_data.sh
install -p -D -m 755 %SOURCE5 %buildroot%_bindir/openstack-keystone-sample-data
# Install sample HTTPD integration files
install -p -D -m 644 httpd/keystone.py  %buildroot%_datadir/keystone/keystone.wsgi
install -p -D -m 644 httpd/wsgi-keystone.conf  %buildroot%_datadir/keystone/

install -d -m 755 %buildroot%_sharedstatedir/keystone
install -d -m 750 %buildroot%_logdir/keystone
install -d -m 755 %buildroot%_runtimedir/keystone

mkdir -p %buildroot%_man1dir
install -p -D -m 644 doc/build/man/*.1 %buildroot%_man1dir/

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

# create keystone ssl dirs
install -d %buildroot%_sysconfdir/keystone/ssl/private
touch %buildroot%_sysconfdir/keystone/ssl/private/signing_key.pem
install -d %buildroot%_sysconfdir/keystone/ssl/certs
touch %buildroot%_sysconfdir/keystone/ssl/certs/signing_cert.pem

%pre
# 163:163 for keystone (openstack-keystone)
%_sbindir/groupadd -r -g 163 -f keystone 2>/dev/null ||:
%_sbindir/useradd -r -u 163 -g keystone -c 'OpenStack Keystone Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/keystone keystone 2>/dev/null ||:


%post
%post_service %name

#Generate ssl certs for pki token support
# su -l -s /bin/sh -c 'exec keystone-manage pki_setup' keystone
/usr/bin/keystone-manage pki_setup --keystone-user keystone --keystone-group keystone
# keystone-manage will create a keystone.log file owned by root; fix that
if [ -f %_logdir/keystone/keystone-manage.log ]; then
    chown keystone:keystone %_logdir/keystone/keystone-manage.log
fi


%preun
%preun_service %name

%files
%doc LICENSE
%doc README.rst
%_bindir/keystone-all
%_bindir/keystone-manage
%_bindir/openstack-keystone-sample-data
%_man1dir/keystone*.1.*
%if_with python3
%_bindir/python3-keystone-all
%_bindir/python3-keystone-manage
%endif
%dir %_datadir/keystone
%attr(0644, root, keystone) %_datadir/keystone/keystone-dist.conf
%attr(0644, root, keystone) %_datadir/keystone/keystone-dist-paste.ini
%attr(0644, root, keystone) %_datadir/keystone/policy.v3cloudsample.json
%attr(0755, root, root) %_datadir/keystone/sample_data.sh
%attr(0644, root, keystone) %_datadir/keystone/keystone.wsgi
%attr(0644, root, keystone) %_datadir/keystone/wsgi-keystone.conf
%_unitdir/%name.service
%_initdir/%name
%_tmpfilesdir/openstack-keystone.conf
%dir %attr(0750, root, keystone) %_sysconfdir/keystone
%dir %attr(0755, root, keystone) %_sysconfdir/keystone/ssl
%dir %attr(0755, root, keystone) %_sysconfdir/keystone/ssl/certs
%ghost %attr(0644, root, keystone) %_sysconfdir/keystone/ssl/certs/signing_cert.pem
%dir %attr(0750, root, keystone) %_sysconfdir/keystone/ssl/private
%ghost %attr(0640, root, keystone) %_sysconfdir/keystone/ssl/private/signing_key.pem
%config(noreplace) %attr(0640, root, keystone) %_sysconfdir/keystone/keystone.conf
%config(noreplace) %attr(0640, root, keystone) %_sysconfdir/keystone/logging.conf
%config(noreplace) %attr(0640, root, keystone) %_sysconfdir/keystone/default_catalog.templates
%config(noreplace) %attr(0640, keystone, keystone) %_sysconfdir/keystone/policy.json
%config(noreplace) %attr(0640, keystone, keystone) %_sysconfdir/keystone/sso_callback_template.html
%config(noreplace) %_sysconfdir/logrotate.d/openstack-keystone
%dir %attr(0755, keystone, keystone) %_sharedstatedir/keystone
%dir %attr(0750, keystone, keystone) %_logdir/keystone
%dir %attr(0755, keystone, keystone) %_runtimedir/keystone
%_sysctldir/openstack-keystone.conf

%files -n python-module-keystone
%python_sitelibdir/keystone
%python_sitelibdir/keystone-*.egg-info

%if_with python3
%files -n python3-module-keystone
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE doc/build/html

%changelog
* Thu May 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- Release Kilo 2015.1.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 2014.2.2-alt1
- 2014.2.2
- backport patches from stable/juno
- add tmpfiles
- update systemd unit
- update init script

* Thu Aug 21 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2.1-alt2
- Fix permission for /etc/keystone to (0700, keystone, keystone):
  * needs for "keystone-manage pki_setup" to generate certs
    in /etc/keystone/ssl, that runs in POSTIN script

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2.1-alt1
- 2014.1.2.1

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- New version - icehouse (based on Fedora)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 2012.2.0.6-alt4
- cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt3.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt3
- Use post/preun_service scripts in spec

* Fri Mar 01 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt2
- Fix python-module-keystone requires

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt1
- Initial release for Sisyphus (based on Fedora)
