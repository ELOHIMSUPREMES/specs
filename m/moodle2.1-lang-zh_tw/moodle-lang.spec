# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename zh_tw
%define packagversion 2.1.0
%define packagedate 201404101738
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Chinese (Traditional/Big5)
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-zh_tw
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.1
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.1
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
* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404101738-alt1
- repocop cronbuild 20140411. At your service.
- zh_tw.zip build 2014-04-10 17:38 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403310334-alt1
- repocop cronbuild 20140404. At your service.
- zh_tw.zip build 2014-03-31 03:34 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403260538-alt1
- repocop cronbuild 20140328. At your service.
- zh_tw.zip build 2014-03-26 05:38 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403191726-alt1
- repocop cronbuild 20140321. At your service.
- zh_tw.zip build 2014-03-19 17:26 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403082359-alt1
- repocop cronbuild 20140314. At your service.
- zh_tw.zip build 2014-03-08 23:59 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402221510-alt1
- repocop cronbuild 20140228. At your service.
- zh_tw.zip build 2014-02-22 15:10 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402041243-alt1
- repocop cronbuild 20140207. At your service.
- zh_tw.zip build 2014-02-04 12:43 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401231731-alt1
- repocop cronbuild 20140124. At your service.
- zh_tw.zip build 2014-01-23 17:31 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401111531-alt1
- repocop cronbuild 20140117. At your service.
- zh_tw.zip build 2014-01-11 15:31 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312291709-alt1
- repocop cronbuild 20140103. At your service.
- zh_tw.zip build 2013-12-29 17:09 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312241635-alt1
- repocop cronbuild 20131227. At your service.
- zh_tw.zip build 2013-12-24 16:35 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312191656-alt1
- repocop cronbuild 20131220. At your service.
- zh_tw.zip build 2013-12-19 16:56 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311261619-alt1
- repocop cronbuild 20131129. At your service.
- zh_tw.zip build 2013-11-26 16:19 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311141426-alt1
- repocop cronbuild 20131115. At your service.
- zh_tw.zip build 2013-11-14 14:26 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310171603-alt1
- repocop cronbuild 20131018. At your service.
- zh_tw.zip build 2013-10-17 16:03 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309271321-alt1
- repocop cronbuild 20131004. At your service.
- zh_tw.zip build 2013-09-27 13:21 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309131817-alt1
- repocop cronbuild 20130920. At your service.
- zh_tw.zip build 2013-09-13 18:17 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305211315-alt1
- repocop cronbuild 20130524. At your service.
- zh_tw.zip build 2013-05-21 13:15 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303190756-alt1
- repocop cronbuild 20130320. At your service.
- zh_tw.zip build 2013-03-19 07:56 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- zh_tw.zip build 2013-01-26 15:39 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212220847-alt1
- repocop cronbuild 20121224. At your service.
- zh_tw.zip build 2012-12-22 08:47 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211050340-alt1
- repocop cronbuild 20121112. At your service.
- zh_tw.zip build 2012-11-05 03:40 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211010917-alt1
- repocop cronbuild 20121105. At your service.
- zh_tw.zip build 2012-11-01 09:17 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210260917-alt1
- repocop cronbuild 20121029. At your service.
- zh_tw.zip build 2012-10-26 09:17 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210190918-alt1
- repocop cronbuild 20121022. At your service.
- zh_tw.zip build 2012-10-19 09:18 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- zh_tw.zip build 2012-05-23 15:49 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201291011-alt1
- repocop cronbuild 20120203. At your service.
- zh_tw.zip build 2012-01-29 10:11 UTC

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111210. At your service.
- zh_tw.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-zh_tw
- zh_tw.zip build 2011-11-02 19:30 UTC

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
