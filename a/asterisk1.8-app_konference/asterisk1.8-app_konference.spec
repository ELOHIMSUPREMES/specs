%define ast_version 1.8.32.2

Name: asterisk1.8-app_konference
Summary: Conference module for Asterisk
Version: 1.5
Release: alt37
License: GPL
Group: System/Servers
Url: http://sourceforge.net/projects/appkonference

%define modules_dir %_libdir/asterisk/%ast_version/modules

Source: %name-%version.tar

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: asterisk1.8 = %ast_version

BuildRequires(pre): asterisk1.8-devel

# Automatically added by buildreq on Sat Dec 26 2009 (-bb)
BuildRequires: asterisk1.8-devel

%description
%summary

%prep
%setup
sed -i "s!/usr/lib/asterisk/modules!%modules_dir!g" konference/Makefile

%build
pushd konference
export ASTERISK_INCLUDE_DIR=/usr/include/asterisk-%ast_version
%make_build

%install
pushd konference
export DESTDIR=%buildroot
export MODULE_DIR=%modules_dir
export ASTDATADIR=%buildroot/var/lib/asterisk
mkdir -p "${ASTDATADIR}/documentation"
mkdir -p %buildroot%modules_dir

%make_install INSTALL_MODULES_DIR=%buildroot%modules_dir install

%files
%doc asterikast konference/*.txt konference/README
%attr(0440,root,_asterisk) %modules_dir/app_konference.so

%changelog
* Wed Mar 18 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt37
- Asterisk update

* Wed Mar 18 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt36
- Asterisk update

* Mon Apr 28 2014 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt35
- Asterisk update

* Tue Mar 11 2014 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt34
- Asterisk update

* Wed Jan 15 2014 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt33
- Asterisk update

* Sun Sep 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt32
- Asterisk update

* Thu Aug 29 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt31
- fix repocop warning about incorrect TMP use

* Thu Aug 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt30
- Asterisk update

* Sun May 19 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt29
- Asterisk update

* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt28
- Asterisk update

* Sat Jan 26 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt27
- Asterisk update

* Mon Jan 21 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt26
- Asterisk update

* Sat Jan 05 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt25
- Asterisk update

* Sat Jan 05 2013 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt24
- Asterisk update

* Tue Dec 11 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt23
- Asterisk update

* Sun Nov 11 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt22
- Asterisk update

* Fri Nov 02 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt21
- Asterisk update

* Mon Sep 24 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt20
- Asterisk update

* Sun Sep 16 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt19
- Asterisk update

* Wed Aug 08 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt18
- Asterisk update

* Tue Jul 31 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt17
- Asterisk update

* Sat May 05 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt16
- Asterisk update

* Thu Feb 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt15
- Asterisk update

* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt14
- Asterisk update

* Sat Dec 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt13
- Asterisk update

* Wed Oct 26 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt12
- Asterisk update

* Wed Oct 05 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt11
- Asterisk update

* Fri Sep 02 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt10
- Asterisk update

* Fri Jul 22 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt9
- Asterisk update

* Sun Feb 27 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt8
- Asterisk update

* Thu Feb 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt7
- Asterisk update

* Wed Feb 09 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt6
- Asterisk update

* Fri Jan 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt5
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt4
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt3
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt2
- Asterisk update

* Thu Dec 23 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt1
- first build for Sisyphus

