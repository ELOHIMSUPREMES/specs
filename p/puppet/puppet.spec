%define confdir ext/redhat

Name:    puppet
Version: 5.5.6
Release: alt1

Summary: A network tool for managing many disparate systems
Group:   System/Servers
License: ASL 2.0
URL:     https://puppetlabs.com/

BuildArch: noarch

Source:  %name-%version.tar
Patch:   %name-%version-%release.patch
Source1: client.init
Source2: server.init
Source3: puppet.service
Source4: puppetmaster.service
Source5: puppet-nm-dispatcher

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-em-http-request
BuildRequires: ruby-eventmachine
BuildRequires: ruby-facter
BuildRequires: ruby-hashie
BuildRequires: ruby-heredoc_unindent
BuildRequires: ruby-hiera
BuildRequires: ruby-pathspec
BuildRequires: ruby-plist
BuildRequires: ruby-rgen
BuildRequires: ruby-safe_yaml

Requires: shadow-change
Conflicts: ruby-semantic

%description
Puppet lets you centrally manage every important aspect of your
system using a cross-platform specification language that manages
all the separate elements normally aggregated in different files,
like users, cron jobs, and hosts, along with obviously discrete
elements like packages, services, and files.

%package  server
Summary:  Server for the puppet system management tool
Group:    System/Servers
Requires: %name = %version-%release

%description server
Provides the central puppet server daemon which provides manifests
to clients.  The server can also function as a certificate authority
and file server.

%prep
%setup
%patch -p1
chmod +x ext/regexp_nodes/regexp_nodes.rb
# remove vendor copy of libraries and support non-Linux platforms
#subst 's/require /#require /' \
#       lib/puppet/util/windows.rb
##      lib/puppet/vendor/require_vendored.rb \

#rm -rf \
#       ext/windows \
#       ext/puppet-test \
#       lib/puppet/feature/cfacter.rb \
#       lib/puppet/util/rdoc \
#       lib/puppet/util/windows \
#       lib/puppet/vendor/safe_yaml/spec \
#       lib/puppet/module_tool/skeleton/templates/generator/spec

echo "require 'rdoc'" > lib/puppet/util/rdoc.rb

# Unbundle
rm -r lib/puppet/vendor/*{pathspec,deep_merge}*

%build

%install
%ruby_vendor install.rb \
	     --destdir=%buildroot \
	     --configdir=/etc/puppet \
	     --codedir=/etc/puppet/code \
	     --localedir=%_datadir/puppet/locale \
	     --vardir=%_localstatedir/puppet \
	     --rundir=%_runtimedir/puppet \
	     --logdir=%_logdir/puppet \
	     --no-rdoc \
	     --no-tests

# SysVInit files
install -Dp -m0644 %confdir/client.sysconfig %buildroot%_sysconfdir/sysconfig/puppet
install -Dp -m0755 %SOURCE1 %buildroot%_initrddir/puppet
install -Dp -m0644 %confdir/server.sysconfig %buildroot%_sysconfdir/sysconfig/puppetmaster
install -Dp -m0755 %SOURCE2 %buildroot%_initrddir/puppetmaster
# Systemd files
install -Dp -m0644 %SOURCE3 %buildroot%_unitdir/puppet.service
ln -s %_unitdir/puppet.service %buildroot%_unitdir/puppetagent.service
install -Dp -m0644 %SOURCE4 %buildroot%_unitdir/puppetmaster.service

install -Dp -m0644 %confdir/logrotate %buildroot%_sysconfdir/logrotate.d/puppet
install -Dp -m0644 conf/fileserver.conf %buildroot%_sysconfdir/puppet/fileserver.conf

# Install the ext/ directory to %%_datadir/%%name
install -d %buildroot%_datadir/%name
cp -a ext/ %buildroot%_datadir/%name

# Create other configuration directories
mkdir -p %buildroot%_sysconfdir/puppet/ssl/{public_keys,certificate_requests,certs,ca/requests,ca/private,ca/signed,private,private_keys}
mkdir -p %buildroot%_sysconfdir/puppet/{code,modules,environments/production/manifests}

# Setup tmpfiles.d config
mkdir -p %buildroot%_sysconfdir/tmpfiles.d
echo "D /var/run/%name 0755 _%name %name -" > \
    %buildroot%_sysconfdir/tmpfiles.d/%name.conf

# Create puppet modules directory for puppet module tool
mkdir -p %buildroot%_sysconfdir/%name/modules

# Create service directory
mkdir -p %buildroot{%_localstatedir,%_logdir,%_var/run}/puppet

# Install NetworkManager dispatcher
install -Dpv %SOURCE5 \
    %buildroot%_sysconfdir/NetworkManager/dispatcher.d/98-%{name}

# remove misc packaging artifacts in source not applicable to rpm
rm -rf %buildroot%_datadir/%name/ext/{gentoo,freebsd,solaris,suse,windows,osx,ips,debian}
rm -rf %buildroot%_datadir/%name/ext/{redhat,systemd}
rm -f %buildroot%_datadir/%name/ext/{build_defaults.yaml,project_data.yaml}
# remove obsoleted checks
rm -rf %buildroot%_datadir/%name/ext/nagios

# Add puppetdb example configuration to puppet.conf
cat >> %buildroot%_sysconfdir/puppet/puppet.conf << END.
# Example of puppetdb integration
#[master]
#storeconfigs = true
#storeconfigs_backend = puppetdb
#report = true
#reports = puppetdb
END.

%pre
%_sbindir/groupadd -r -f puppet
%_sbindir/useradd -r -n -g puppet -d %_localstatedir/puppet -s /dev/null -c Puppet _puppet >/dev/null 2>&1 ||:

%post
%post_service puppet

%preun
%preun_service puppet

%post server
%post_service puppetmaster

%preun server
%preun_service puppetmaster

%files
%_initdir/puppet
%_unitdir/puppet.service
%_unitdir/puppetagent.service
%config(noreplace) %_sysconfdir/tmpfiles.d/%name.conf
%dir %_sysconfdir/puppet
%attr(0771,_puppet,puppet) %dir %_sysconfdir/puppet/ssl
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/public_keys
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/certificate_requests
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/certs
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/requests
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/private
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/signed
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/private
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/private_keys
%dir %_sysconfdir/puppet/environments
%dir %_sysconfdir/puppet/environments/production
%dir %_sysconfdir/puppet/environments/production/manifests
%dir %_sysconfdir/puppet/code
%dir %_sysconfdir/puppet/modules
%config(noreplace) %_sysconfdir/puppet/puppet.conf
%config(noreplace) %_sysconfdir/puppet/auth.conf
%config(noreplace) %_sysconfdir/puppet/hiera.yaml
%config(noreplace) %_sysconfdir/sysconfig/puppet
%config(noreplace) %_sysconfdir/logrotate.d/puppet
%_bindir/puppet
%ruby_sitelibdir/*
%_datadir/%name
%_sysconfdir/NetworkManager/dispatcher.d/98-%{name}
%_man8dir/*
%_man5dir/puppet.conf.5*
%attr(1770,_puppet,puppet) %dir %_localstatedir/puppet
%_localstatedir/puppet/
%attr(1770,_puppet,puppet) %dir %_logdir/puppet
%attr(1770,_puppet,puppet) %dir %_var/run/puppet

%files server
%_initdir/puppetmaster
%_unitdir/puppetmaster.service
%config(noreplace) %_sysconfdir/puppet/fileserver.conf
%config(noreplace) %_sysconfdir/sysconfig/puppetmaster

%changelog
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.6-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1
- New version.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt3
- Fix "Cannot determine basic system flavour" (https://tickets.puppetlabs.com/browse/SERVER-14).

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt2
- Create and package all configuration directories.
- Add puppetdb example configuration to puppet.conf.

* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- New version.

* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version.

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.2-alt1
- New version

* Sat Sep 30 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 17 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version

* Wed Jul 19 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version

* Wed Jun 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.4-alt1
- New version

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.3-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.2-alt1
- New version

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.1-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- New version

* Wed Feb 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- new version 4.9.0

* Fri Jan 27 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.2-alt1
- new version 4.8.2

* Wed Jan 18 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.1-alt1
- new version 4.8.1
- aptrpm package provider is default for ALT operating system

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt2
- Fix build without bundled libraries
- Rebuild with fixed ruby autoreq (ALT #32601)

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt1
- new version 4.7.0

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version
- Package missing directories (ALT #30148)

* Sat Apr 25 2015 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version

* Tue Jan 13 2015 Andrey Cherepanov <cas@altlinux.org> 3.7.3-alt1
- New version

* Thu May 15 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version
- Rename services to puppet, puppetmaster
- Add NetworkManager dispatcher script to pickup changes to
  /etc/resolv.conf and such

* Fri Jul 26 2013 Andrey Cherepanov <cas@altlinux.org> 2.7.21-alt2
- Set correct pid file name for services (ALT #29114)
- Set correct user name _puppet in configuration of puppetmasterd


* Fri Jun 07 2013 Andrey Cherepanov <cas@altlinux.org> 2.7.21-alt1
- New version 2.7.21 (ALT #28695)
- Use system group `puppet` instead `_puppet` (ALT #28273)
- New format of puppet.conf (ALT #28517)

* Fri Nov 30 2012 Led <led@altlinux.ru> 2.7.5-alt1.2
- Rebuilt with ruby-1.9.3-alt1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 06 2011 Sergey Alembekov <rt@altlinux.ru> 2.7.5-alt1
- [2.7.5]

* Tue Sep 27 2011 Sergey Alembekov <rt@altlinux.ru> 2.7.3-alt1
- [2.7.3]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.24.8-alt1
- [0.24.8]

* Sat Dec 20 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt3
- Fixed interpackage dependencies

* Sat Dec 20 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt2
- Cleaned up build deps

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt1
- [0.24.6]

* Tue Aug 26 2008 Sir Raorn <raorn@altlinux.ru> 0.24.5-alt1
- Built for Sisyphus

