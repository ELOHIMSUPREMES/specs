%define oname roundcubemail
Name: roundcube
Version: 1.2.2
Release: alt1

Summary: Browser-based multilingual IMAP client with an application-like user interface

License: GPL2
Group: Networking/Mail
Url: http://roundcube.net/

#Source0: http://prdownloads.sf.net/%oname/%oname-%version.tar
Source0: https://github.com/roundcube/roundcubemail/releases/download/%version/roundcubemail-%version.tar
Source1: %name.apache.conf
Source2: composer.json-dist
BuildArch: noarch

BuildPreReq: rpm-build-apache2
BuildRequires: rpm-macros-webserver-common
BuildRequires: php5

Requires: composer >= 1.1.3

# check it with composer.json or on http://trac.roundcube.net/wiki/Howto_Requirements
Requires: php5 >= 5.3.7
Requires: webserver-common php-engine
Requires: pear-Mail_Mime >= 1.10.0
Requires: pear-Net_SMTP >= 1.7.1
Requires: pear-Net_IDNA2 >= 0.1.1
Requires: pear-Auth_SASL >= 1.0.6
# managesieve plugin
Requires: pear-Net_Sieve >= 1.3.4
# for enigma plugin
#Requires: pear-Crypt_GPG >= 1.4.1
Requires: pear-Net_Socket >= 1.0.12
Requires: pear-Mail_mimeDecode

Requires: php5-dom php5-mcrypt php5-openssl
Requires: php5-pdo_mysql
Requires: php5-mbstring php5-fileinfo php5-mcrypt php5-zip php5-pspell

Provides: roundcube-plugin-acl
Obsoletes: roundcube-plugin-acl

AutoReq: yes,nomingw32,noshell

%add_findreq_skiplist %_datadir/%name/plugins/*
%add_python_req_skip %_datadir/%name/plugins/*
%add_python_compile_exclude %_datadir/%name/plugins/*

%description
RoundCube Webmail is a browser-based multilingual IMAP client with an application-like user interface.
It provides full functionality you expect from an e-mail client, including MIME support, LDAP address book,
folder manipulation, message searching and spell checking.
RoundCube Webmail is written in PHP and requires a MySQL or Postgres database.

%package apache2
Summary: %name's apache config file
Group: System/Servers
Requires: %name = %version-%release
Requires: apache2-httpd
BuildArch: noarch

%description apache2
%name's apache config file

%prep
%setup -n %oname-%version
sed -i 's,php_,php5_,' .htaccess

%install
mkdir -p %buildroot%_datadir/%name/
install -Dpm 0644 index.php %buildroot%_datadir/%name/index.php
install -Dpm 0644 .htaccess %buildroot%_datadir/%name/.htaccess
install -Dpm 0644 robots.txt %buildroot%_datadir/%name/robots.txt
cp -ar SQL bin program installer plugins skins %buildroot%_datadir/%name/

cat > %buildroot%_datadir/%name/installer/.htaccess << EOF
# deny webserver access to this directory
<ifModule mod_authz_core.c>
    Require all denied
</ifModule>
<ifModule !mod_authz_core.c>
    Deny from all
</ifModule>
EOF

mkdir -p %buildroot%_localstatedir/%name/{temp,logs,enigma}/
ln -s %_localstatedir/%name/logs/ %buildroot%_datadir/%name/
ln -s %_localstatedir/%name/temp/ %buildroot%_datadir/%name/
rm -rf %buildroot%_datadir/%name/plugins/enigma/home/
ln -s %_localstatedir/%name/enigma/ %buildroot%_datadir/%name/plugins/enigma/home

cp %buildroot%_datadir/%name/installer/.htaccess %buildroot%_localstatedir/%name/temp/
cp %buildroot%_datadir/%name/installer/.htaccess %buildroot%_localstatedir/%name/logs/
cp %buildroot%_datadir/%name/installer/.htaccess %buildroot%_localstatedir/%name/enigma/

mkdir -p %buildroot%_sysconfdir/%name/
cp -ar config/* %buildroot%_sysconfdir/%name/
ln -s  %_sysconfdir/%name/ %buildroot%_datadir/%name/config

install -Dpm 0644 %SOURCE2 %buildroot%_sysconfdir/%name/composer.json
ln -s  %_sysconfdir/%name/composer.json %buildroot%_datadir/%name/composer.json

ln -s  %_docdir/%name-%version %buildroot%_datadir/%name/doc

install -pD -m0644 %SOURCE1 %buildroot%apache2_extra_available/%name.conf

%post apache2
service httpd2 condreload

%postun apache2
service httpd2 condreload

%files
%_datadir/%name/
%dir %attr(2775,root,%webserver_group) %_localstatedir/%name/
%dir %attr(2775,root,%webserver_group) %_localstatedir/%name/logs/
%dir %attr(2775,root,%webserver_group) %_localstatedir/%name/temp/
%dir %attr(2775,root,%webserver_group) %_localstatedir/%name/enigma/
%_localstatedir/%name/logs/.htaccess
%_localstatedir/%name/temp/.htaccess
%_localstatedir/%name/enigma/.htaccess
%dir %attr(0750,root,%webserver_group) %_sysconfdir/%name/
%config(noreplace) %attr(0640,root,%webserver_group) %_sysconfdir/%name/*
%doc CHANGELOG LICENSE README.md UPGRADING SQL/

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf

%changelog
* Fri Sep 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- cleanup spec, change apache package to apache2
- fix enigma plugin home dir

* Wed Jun 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- new version 1.1.5 (with rpmrb script)

* Fri Feb 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt2
- pack composer.json, add link to doc dir
- improve requirements

* Fri Feb 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- new version 1.1.4 (with rpmrb script)

* Sun Nov 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- new version 1.1.3 (with rpmrb script)
- drop all inrepo tarball changes

* Wed Apr 09 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- release 1.0.0

* Thu Feb 02 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt2
- really 0.7.1 (was 0.5.3 due my script's fault) (ALT bug #26807)

* Wed Jan 11 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)
- fix spec and gear rules

* Fri Aug 12 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Apr 11 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.1-alt1
- 0.5.1

* Mon Oct 11 2010 Timur Batyrshin <erthad@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Sep 30 2010 Timur Batyrshin <erthad@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Sep 08 2010 Timur Batyrshin <erthad@altlinux.org> 0.4-alt1
- 0.4 (closes #24040)
- added README.ALT (closes #22819)
- changed default logging destination to syslog (closes: #24129)

* Thu Apr 22 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.1-alt2
- Fix working with current pear-MDB2_Driver_pgsql (Closes: #23286)
- Add some dependencies on php modules

* Thu Dec 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.3.1-alt1
- 0.3.1
- removed prepackaged PEAR etc. from rpm

* Mon Sep 28 2009 Timur Batyrshin <erthad@altlinux.org> 0.3-alt1
- 0.3 (closes #20693)

* Thu Aug 23 2007 Mikhail Pokidko <pma@altlinux.org> 0.1.rc1.1-alt3
- Added password changing patch

* Wed Aug 22 2007 Mikhail Pokidko <pma@altlinux.org> 0.1.rc1.1-alt2
- Mistypes correction

* Fri Aug 17 2007 Mikhail Pokidko <pma@altlinux.org> 0.1.rc1.1-alt1
- Initial ALT build

