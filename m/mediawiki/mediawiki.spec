%define webappdir %webserver_webappsdir/mediawiki
%define major 1.20

Summary: A wiki engine, typical installation (with Apache2, MySQL and TeX support) 
Name: mediawiki
Version: %major.4
Release: alt2
License: %gpl2plus
Group: Networking/WWW
Url: http://www.mediawiki.org/

Packager: Aleksey Avdeev <solo@altlinux.ru>

BuildArch: noarch

Source0: http://download.wikimedia.org/mediawiki/%major/%name-%version.tar.gz
Source1: mediawiki-apache2-alt-configs.tar
Source2: README.ALT-ru_RU.UTF-8
Source3: install_php_config.sh
Source4: mediawiki.ini
Source5: README.UPGRADE.ALT-ru_RU.UTF-8
Source6: AdminSettings.sample
Source7: 99-read-user-configs.php

BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-licenses
BuildPreReq: apache2-devel
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: %name-common = %version-%release
Requires: %name-apache2 %name-mysql
Requires: php5-apc ImageMagick

%description
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers

This package supports wiki farms. Configure it through the web
interface. Remember to secure the config dir after completing the
configuration.

This is a typical %name installation (with Apache2, MySQL and
TeX support). Also, optional dependences will be installed:
php5-eaccelerator and ImageMagick.

If you wish pure %name, install only %name-common package.


%package -n %name-common
Summary: Common files for %name
Group: Networking/WWW
PreReq: webserver-common
Requires: php-engine >= 5
Requires: diffutils

Provides: mediawiki-extensions-ParserFunctions
Provides: mediawiki-extensions-ConfirmEdit

Obsoletes: mediawiki-extensions-ParserFunctions
Obsoletes: mediawiki-extensions-ConfirmEdit

Conflicts: mediawiki-extensions-FCKEditor

%description -n %name-common
%summary

%package -n %name-apache2
Summary: Apache2's requires and config files for %name
Group: Networking/WWW
Requires: %name-common = %version-%release
Requires: apache2-common >= 2.2.0
Requires: %_initdir/%apache2_dname
Requires: apache2-httpd-prefork
Requires: apache2-mod_php5 >= 5

%description -n %name-apache2
Install this package, if you wish to run %name under apache2 webserver


%package -n %name-mysql
Summary: Virtual package for mysql requires for %name
Group: Networking/WWW
Requires: %name-common = %version-%release
Requires: php5-mysql mysql-server >= 4.1

%description -n %name-mysql
Install this package, if you wish to run %name with MySQL database


%package -n %name-postgresql
Summary: Virtual package for postgresql requires for %name
Group: Networking/WWW
Requires: %name-common = %version-%release
Requires: php5-pgsql postgresql-server >= 8.1

%description -n %name-postgresql
Install this package, if you wish to run %name with PostgreSQL database

%package -n %name-tex
Summary: Package with TeX support for %name
Group: Networking/WWW
Requires: %name-common = %version-%release
Requires: texvc

%description -n %name-tex
%summary

%package -n %name-hiphop
Summary: Package with hihop support for %name
Group: Networking/WWW
Requires: %name-common = %version-%release

%description -n %name-hiphop
%summary


%prep
%setup

%build

%install
mkdir -p %buildroot%_mediawikidir

# Copy to buildroot all files and directories exclude unneeded
cp -r * %buildroot%_mediawikidir/
# Not needed in the package
rm -rf %buildroot%_mediawikidir/maintenance/dev/
rm -rf %buildroot%_mediawikidir/tests/
rm -rf %buildroot%_mediawikidir/{*.php5,*.phtml}
rm -rf %buildroot%_mediawikidir/{COPYING,CREDITS,FAQ,HISTORY,README,RELEASE-NOTES-*,UPGRADE}

mkdir -p %buildroot%_mediawikidir/config/

sed -i -e "s/__VERSION__/%version/g" %SOURCE2
sed -i -e "s/__VERSION__/%version/g" %SOURCE5
install -m 644 %SOURCE2 ./
install -m 755 %SOURCE3 ./
install -m 644 %SOURCE4 ./
install -m 644 %SOURCE5 ./

# remove undeeded parts
rm -fr %buildroot%_mediawikidir/includes/zhtable
find %buildroot%_mediawikidir/ \
  \( -name .htaccess -or -name \*.cmi \) \
  -print0 \
  | xargs -r0 rm

find %buildroot -name .svnignore -print0 | xargs -r0 rm
find %buildroot -name \*.commoncode -print0 | xargs -r0 rm

# fix permissions
chmod +x %buildroot%_mediawikidir/bin/*
find %buildroot%_mediawikidir -name \*.pl -print0 | xargs -r0 chmod +x


mkdir -p %buildroot%webappdir
cd %buildroot%_mediawikidir
mv cache images %buildroot%webappdir/
ln -sf %webappdir/{cache,images} .
mkdir config/LocalSettings.d/
install -m 644 %SOURCE7 config/LocalSettings.d/
ln -sf %webappdir/config/LocalSettings.php config/

cd %buildroot%webappdir/
mkdir -p config/LocalSettings.d
install -m 600 %SOURCE6 config/
ln -s %_mediawikidir wiki

# Configs for apache2
mkdir -p %buildroot%apache2_confdir
pushd %buildroot%apache2_confdir
tar xvSf %SOURCE1
find -name \*.conf |xargs sed -i "s|WEBAPPDIR|%webappdir|"
popd


# config for -tex package
cat > %buildroot%_mediawiki_settings_dir/10-%name-tex.php << EOF
<?php
\$wgUseTeX = true;
\$wgTexvc  = "%_bindir/texvc";
?>
EOF

# config for enable bundled ParserFunctions
cat > %buildroot%_mediawiki_settings_dir/50-ParserFunctions.php << EOF
<?php

require_once("\$IP/extensions/ParserFunctions/ParserFunctions.php");

?>
EOF


%pre -n %name-common
if [ -L %_mediawikidir/config ]; then 
	rm -f %_mediawikidir/config
fi
if [ -d %_datadir/%name/images -a ! -L %_datadir/%name/images ]; then
	rmdir %_datadir/%name/images 2>/dev/null || {
		mv %_datadir/%name/images %_datadir/%name/images.rpmsave
		echo "%_datadir/%name/images saved as %_datadir/%name/images.rpmsave"
	}
fi
		

%post -n %name-apache2
%_sbindir/a2chkconfig >/dev/null
%post_service %apache2_dname
exit 0

%postun -n %name-apache2
%_sbindir/a2chkconfig >/dev/null
%post_service %apache2_dname
exit 0


%files

%files -n %name-common
%add_findreq_skiplist %_datadir/%name/config/LocalSettings.php
%_mediawikidir/
%exclude %_mediawiki_settings_dir/10-%name-tex.php
%exclude %_datadir/%name/maintenance/hiphop/
%attr(2750,root,%webserver_group) %dir %webappdir/
%attr(2770,root,%webserver_group) %dir %webappdir/config/
%attr(2770,root,%webserver_group) %dir %webappdir/config/LocalSettings.d/
%attr(2775,root,%webserver_group) %dir %webappdir/images/
%attr(2770,root,%webserver_group) %dir %webappdir/cache/
%webappdir/wiki/
%webappdir/images/*
%webappdir/config/AdminSettings.sample

%doc COPYING CREDITS docs FAQ HISTORY README RELEASE-NOTES-%major UPGRADE StartProfiler.sample
%doc README.ALT-ru_RU.UTF-8 README.UPGRADE.ALT-ru_RU.UTF-8 install_php_config.sh mediawiki.ini


%files -n %name-apache2
%config %apache2_mods_start/*.conf
%config %apache2_extra_available/*.conf
%config %apache2_extra_start/*.conf
%config(noreplace) %apache2_sites_available/*.conf

%files -n %name-mysql

%files -n %name-postgresql

%files -n %name-tex
%_mediawiki_settings_dir/10-%name-tex.php

# have no hiphop in the repo
#%files -n %name-hiphop
#%_datadir/%name/maintenance/hiphop/


%changelog
* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.4-alt2
- update README.UPGRADE.ALT
- use macros from rpm-build-mediawiki
- enable ParserFunctions

* Mon Apr 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.4-alt1
- 1.20.4 release

* Tue Feb 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.2-alt1
- 1.20.2 release

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.16.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Michael A. Kangin <prividen@altlinux.org> 1.16.0-alt1
- 1.16.0 release
- Engine to read user's configs from %webappdir/config/LocalSettings.d/

* Mon May 31 2010 Michael A. Kangin <prividen@altlinux.org> 1.16.0-alt0.beta3
- New beta release

* Fri May 21 2010 Michael A. Kangin <prividen@altlinux.org> 1.16.0-alt0.beta2
- Pre-release of new version

* Mon Mar 22 2010 Michael A. Kangin <prividen@altlinux.org> 1.15.2-alt1
- 1.15.2

* Wed Jan 20 2010 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt5
- Fix installation with active mod_rewrite (Closes: #22768)
- Move TeX support into mediawiki-tex package

* Fri Dec 25 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt4
- Fix upgrade from previous version (Closes: #22585)
- New configs layout
- Upgrade notes

* Sun Dec 20 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt3
- Spec cleanup
- Change packages layout

* Sun Jul 19 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt2
- LocalSettings.d/ engine

* Sat Jul 18 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt0
- 1.15.1

* Mon Jun 22 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.0-alt0
- 1.15.0
- redesign package

* Wed Apr 15 2009 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt4
- Fix Requires (Closes: #19506)

* Thu Sep 04 2008 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt3
- Add README.ALT-ru_RU.UTF-8

* Wed Sep 03 2008 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt2
- Removed Requires: tetex-latex, tetex-dvips
- Fix aliases.

* Sat Aug 30 2008 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt1
- Update to 1.13.0.

* Tue Jun 03 2008 Aleksey Avdeev <solo@altlinux.ru> 1.10.4-alt1
- First build for ALT.

