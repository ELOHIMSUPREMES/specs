# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename es
%define packagversion 2.1.0
%define packagedate 201309261151
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Spanish
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-es
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

%description
%summary

%prep
%setup

%build

%install
mkdir -p  %buildroot%moodle_langdir/
cp -rp * %buildroot%moodle_langdir/

%files
%moodle_langdir/*

%changelog
* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309261151-alt1
- repocop cronbuild 20130927. At your service.
- es.zip build 2013-09-26 11:51 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309151651-alt1
- repocop cronbuild 20130920. At your service.
- es.zip build 2013-09-15 16:51 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307271811-alt1
- repocop cronbuild 20130802. At your service.
- es.zip build 2013-07-27 18:11 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307101128-alt1
- repocop cronbuild 20130712. At your service.
- es.zip build 2013-07-10 11:28 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306221635-alt1
- repocop cronbuild 20130628. At your service.
- es.zip build 2013-06-22 16:35 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306161332-alt1
- repocop cronbuild 20130621. At your service.
- es.zip build 2013-06-16 13:32 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306041808-alt1
- repocop cronbuild 20130607. At your service.
- es.zip build 2013-06-04 18:08 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305290546-alt1
- repocop cronbuild 20130531. At your service.
- es.zip build 2013-05-29 05:46 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305221223-alt1
- repocop cronbuild 20130524. At your service.
- es.zip build 2013-05-22 12:23 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305131121-alt1
- repocop cronbuild 20130517. At your service.
- es.zip build 2013-05-13 11:21 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305060958-alt1
- repocop cronbuild 20130509. At your service.
- es.zip build 2013-05-06 09:58 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201304121225-alt1
- repocop cronbuild 20130417. At your service.
- es.zip build 2013-04-12 12:25 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303191450-alt1
- repocop cronbuild 20130319. At your service.
- es.zip build 2013-03-19 14:50 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303121803-alt1
- repocop cronbuild 20130313. At your service.
- es.zip build 2013-03-12 18:03 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302270957-alt1
- repocop cronbuild 20130304. At your service.
- es.zip build 2013-02-27 09:57 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302200954-alt1
- repocop cronbuild 20130225. At your service.
- es.zip build 2013-02-20 09:54 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301262010-alt1
- repocop cronbuild 20130128. At your service.
- es.zip build 2013-01-26 20:10 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301151654-alt1
- repocop cronbuild 20130121. At your service.
- es.zip build 2013-01-15 16:54 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301090906-alt1
- repocop cronbuild 20130114. At your service.
- es.zip build 2013-01-09 09:06 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212301014-alt1
- repocop cronbuild 20121231. At your service.
- es.zip build 2012-12-30 10:14 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212170959-alt1
- repocop cronbuild 20121224. At your service.
- es.zip build 2012-12-17 09:59 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212141305-alt1
- repocop cronbuild 20121217. At your service.
- es.zip build 2012-12-14 13:05 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212051126-alt1
- repocop cronbuild 20121210. At your service.
- es.zip build 2012-12-05 11:26 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211300843-alt1
- repocop cronbuild 20121203. At your service.
- es.zip build 2012-11-30 08:43 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211171308-alt1
- repocop cronbuild 20121119. At your service.
- es.zip build 2012-11-17 13:08 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211091427-alt1
- repocop cronbuild 20121112. At your service.
- es.zip build 2012-11-09 14:27 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211031423-alt1
- repocop cronbuild 20121105. At your service.
- es.zip build 2012-11-03 14:23 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210181259-alt1
- repocop cronbuild 20121022. At your service.
- es.zip build 2012-10-18 12:59 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210020723-alt1
- repocop cronbuild 20121008. At your service.
- es.zip build 2012-10-02 07:23 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209212056-alt1
- repocop cronbuild 20121001. At your service.
- es.zip build 2012-09-21 20:56 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209151106-alt1
- repocop cronbuild 20120918. At your service.
- es.zip build 2012-09-15 11:06 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209081850-alt1
- repocop cronbuild 20120911. At your service.
- es.zip build 2012-09-08 18:50 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206032043-alt1
- repocop cronbuild 20120605. At your service.
- es.zip build 2012-06-03 20:43 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- es.zip build 2012-05-23 15:49 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120430. At your service.
- es.zip build 2012-04-27 11:30 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204011048-alt1
- repocop cronbuild 20120403. At your service.
- es.zip build 2012-04-01 10:48 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203190925-alt1
- repocop cronbuild 20120320. At your service.
- es.zip build 2012-03-19 09:25 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120306. At your service.
- es.zip build 2012-03-01 11:00 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112201840-alt1
- repocop cronbuild 20111220. At your service.
- es.zip build 2011-12-20 18:40 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112101156-alt1
- repocop cronbuild 20111213. At your service.
- es.zip build 2011-12-10 11:56 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112061030-alt1
- repocop cronbuild 20111206. At your service.
- es.zip build 2011-12-06 10:30 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-es
- es.zip build 2011-11-02 19:30 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111011736-alt4
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111011736-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111011736-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111011736-alt1
- repocop cronbuild 20111105. At your service.
- es.zip build 2011-11-01 17:36 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191503-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191503-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191503-alt1
- es.zip build 2011-10-19 15:03 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109212053-alt1
- es.zip build 2011-09-21 20:53 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- es.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108281454-alt1
- es.zip build 2011-08-28 14:54 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241221-alt1
- es.zip build 2011-08-24 12:21 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108221159-alt1
- es.zip build 2011-08-22 11:59 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- es.zip build 2011-08-16 13:07 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-es
- es.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20101112-alt1
- es_utf8.zip build 2010-11-12

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101112
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081208
- new build for ALT Linux from cvs
