# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename zh_tw
%define packagversion 2.0.0
%define packagedate 201408170736
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Chinese (Traditional/Big5)
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-zh_tw
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.0
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.0
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Provides: %moodle_name-%packagetype-%packagename = %version-%release
Provides: %moodle_name-%packagetype-%oldpackagename = %version-%release
Conflicts: %moodle_name-%packagetype-%packagename < %version
Conflicts: %moodle_name-%packagetype-%oldpackagename < %version

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-fonts

%description
%summary

%prep
%setup

%build

%install
mkdir -p  %buildroot%moodle_langdir/
cp -rp * %buildroot%moodle_langdir/

# Create symlink for default.ttf
install -d %buildroot%default_ttfdir
ln -s -f $(relative %buildroot%_ttffontsdir/chinese-big5/bkai00mp.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201408170736-alt1
- repocop cronbuild 20140919. At your service.
- zh_tw.zip build 2014-08-17 07:36 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406300221-alt1
- repocop cronbuild 20140705. At your service.
- zh_tw.zip build 2014-06-30 02:21 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406150248-alt1
- repocop cronbuild 20140621. At your service.
- zh_tw.zip build 2014-06-15 02:48 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406031606-alt1
- repocop cronbuild 20140606. At your service.
- zh_tw.zip build 2014-06-03 16:06 UTC

* Sat May 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405011704-alt1
- repocop cronbuild 20140503. At your service.
- zh_tw.zip build 2014-05-01 17:04 UTC

* Sat Apr 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404151136-alt1
- repocop cronbuild 20140419. At your service.
- zh_tw.zip build 2014-04-15 11:36 UTC

* Sat Apr 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404101738-alt1
- repocop cronbuild 20140412. At your service.
- zh_tw.zip build 2014-04-10 17:38 UTC

* Sat Apr 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403310334-alt1
- repocop cronbuild 20140405. At your service.
- zh_tw.zip build 2014-03-31 03:34 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403260538-alt1
- repocop cronbuild 20140329. At your service.
- zh_tw.zip build 2014-03-26 05:38 UTC

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403211204-alt1
- repocop cronbuild 20140322. At your service.
- zh_tw.zip build 2014-03-21 12:04 UTC

* Sat Dec 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312230205-alt1
- repocop cronbuild 20131228. At your service.
- zh_tw.zip build 2013-12-23 02:05 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312201355-alt1
- repocop cronbuild 20131220. At your service.
- zh_tw.zip build 2013-12-20 13:55 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311261620-alt1
- repocop cronbuild 20131129. At your service.
- zh_tw.zip build 2013-11-26 16:20 UTC

* Sat Nov 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311141426-alt1
- repocop cronbuild 20131116. At your service.
- zh_tw.zip build 2013-11-14 14:26 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310171603-alt1
- repocop cronbuild 20131018. At your service.
- zh_tw.zip build 2013-10-17 16:03 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309131817-alt1
- repocop cronbuild 20130920. At your service.
- zh_tw.zip build 2013-09-13 18:17 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211315-alt1
- repocop cronbuild 20130524. At your service.
- zh_tw.zip build 2013-05-21 13:15 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303190756-alt1
- repocop cronbuild 20130319. At your service.
- zh_tw.zip build 2013-03-19 07:56 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- zh_tw.zip build 2013-01-26 15:39 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212220847-alt1
- repocop cronbuild 20121224. At your service.
- zh_tw.zip build 2012-12-22 08:47 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211010223-alt1
- repocop cronbuild 20121105. At your service.
- zh_tw.zip build 2012-11-01 02:23 UTC

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120523. At your service.
- zh_tw.zip build 2012-05-23 15:49 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use %%_ttffontsdir/chinese-big5/bkai00mp.ttf for
  %%moodle_langdir/zh_tw/fonts/default.ttf
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- zh_tw.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- zh_tw.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-zh_tw
- zh_tw.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- zh_tw_utf8.zip build 2010-05-26

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20080926
- new build for ALT Linux from cvs
