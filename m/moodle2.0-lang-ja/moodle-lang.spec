# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ja
%define packagversion 2.0.0
%define packagedate 201305200103
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Japanese
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-ja
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
ln -s -f $(relative %buildroot%_ttffontsdir/sazanami/gothic/sazanami-gothic.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305200103-alt1
- repocop cronbuild 20130524. At your service.
- ja.zip build 2013-05-20 01:03 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305090117-alt1
- repocop cronbuild 20130509. At your service.
- ja.zip build 2013-05-09 01:17 UTC

* Tue Apr 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304090556-alt1
- repocop cronbuild 20130409. At your service.
- ja.zip build 2013-04-09 05:56 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303260003-alt1
- repocop cronbuild 20130327. At your service.
- ja.zip build 2013-03-26 00:03 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303082006-alt1
- repocop cronbuild 20130313. At your service.
- ja.zip build 2013-03-08 20:06 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302072122-alt1
- repocop cronbuild 20130211. At your service.
- ja.zip build 2013-02-07 21:22 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302030525-alt1
- repocop cronbuild 20130204. At your service.
- ja.zip build 2013-02-03 05:25 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301041636-alt1
- repocop cronbuild 20130107. At your service.
- ja.zip build 2013-01-04 16:36 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212090528-alt1
- repocop cronbuild 20121210. At your service.
- ja.zip build 2012-12-09 05:28 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211231905-alt1
- repocop cronbuild 20121126. At your service.
- ja.zip build 2012-11-23 19:05 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211122023-alt1
- repocop cronbuild 20121119. At your service.
- ja.zip build 2012-11-12 20:23 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211061911-alt1
- repocop cronbuild 20121112. At your service.
- ja.zip build 2012-11-06 19:11 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209141356-alt1
- repocop cronbuild 20120917. At your service.
- ja.zip build 2012-09-14 13:56 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209090827-alt1
- repocop cronbuild 20120910. At your service.
- ja.zip build 2012-09-09 08:27 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208311859-alt1
- repocop cronbuild 20120904. At your service.
- ja.zip build 2012-08-31 18:59 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208220409-alt1
- repocop cronbuild 20120828. At your service.
- ja.zip build 2012-08-22 04:09 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208031508-alt1
- repocop cronbuild 20120807. At your service.
- ja.zip build 2012-08-03 15:08 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207191042-alt1
- repocop cronbuild 20120724. At your service.
- ja.zip build 2012-07-19 10:42 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207030108-alt1
- repocop cronbuild 20120710. At your service.
- ja.zip build 2012-07-03 01:08 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206292034-alt1
- repocop cronbuild 20120703. At your service.
- ja.zip build 2012-06-29 20:34 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206251644-alt1
- repocop cronbuild 20120625. At your service.
- ja.zip build 2012-06-25 16:44 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206142054-alt1
- repocop cronbuild 20120618. At your service.
- ja.zip build 2012-06-14 20:54 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206111753-alt1
- repocop cronbuild 20120611. At your service.
- ja.zip build 2012-06-11 17:53 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205271605-alt1
- repocop cronbuild 20120528. At your service.
- ja.zip build 2012-05-27 16:05 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205081813-alt1
- repocop cronbuild 20120514. At your service.
- ja.zip build 2012-05-08 18:13 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205020320-alt1
- repocop cronbuild 20120507. At your service.
- ja.zip build 2012-05-02 03:20 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204171536-alt1
- repocop cronbuild 20120423. At your service.
- ja.zip build 2012-04-17 15:36 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204111524-alt1
- repocop cronbuild 20120416. At your service.
- ja.zip build 2012-04-11 15:24 UTC

* Wed Feb 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202172005-alt1
- repocop cronbuild 20120222. At your service.
- ja.zip build 2012-02-17 20:05 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202131158-alt1
- repocop cronbuild 20120215. At your service.
- ja.zip build 2012-02-13 11:58 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201251804-alt1
- repocop cronbuild 20120125. At your service.
- ja.zip build 2012-01-25 18:04 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201062044-alt1
- repocop cronbuild 20120111. At your service.
- ja.zip build 2012-01-06 20:44 UTC

* Wed Dec 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112260047-alt1
- repocop cronbuild 20111228. At your service.
- ja.zip build 2011-12-26 00:47 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112211927-alt1
- repocop cronbuild 20111221. At your service.
- ja.zip build 2011-12-21 19:27 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112132222-alt1
- repocop cronbuild 20111214. At your service.
- ja.zip build 2011-12-13 22:22 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112011705-alt1
- repocop cronbuild 20111207. At your service.
- ja.zip build 2011-12-01 17:05 UTC

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111301536-alt1
- repocop cronbuild 20111130. At your service.
- ja.zip build 2011-11-30 15:36 UTC

* Mon Nov 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111280210-alt1
- repocop cronbuild 20111128. At your service.
- ja.zip build 2011-11-28 02:10 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111241342-alt1
- repocop cronbuild 20111125. At your service.
- ja.zip build 2011-11-24 13:42 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111151726-alt2
- Fix requires

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151726-alt1
- repocop cronbuild 20111116. At your service.
- ja.zip build 2011-11-15 17:26 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031658-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031658-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031658-alt1
- repocop cronbuild 20111105. At your service.
- ja.zip build 2011-11-03 16:58 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt2
- Update for cronbuild use

* Mon Oct 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt1
- ja.zip build 2011-10-24 16:31 UTC

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110202137-alt1
- ja.zip build 2011-10-20 21:37 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110041726-alt1
- ja.zip build 2011-10-04 17:26 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109272111-alt1
- ja.zip build 2011-09-27 21:11 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109261912-alt1
- ja.zip build 2011-09-26 19:12 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109222056-alt1
- ja.zip build 2011-09-22 20:56 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109212035-alt1
- ja.zip build 2011-09-21 20:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- ja.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109181907-alt1
- ja.zip build 2011-09-18 19:07 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109151910-alt1
- ja.zip build 2011-09-15 19:10 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141837-alt1
- ja.zip build 2011-09-14 18:37 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109131809-alt1
- ja.zip build 2011-09-13 18:09 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109121803-alt1
- ja.zip build 2011-09-12 18:03 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109111621-alt1
- ja.zip build 2011-09-11 16:21 UTC

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109090331-alt1
- ja.zip build 2011-09-09 03:31 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109070502-alt1
- ja.zip build 2011-09-07 05:02 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108231816-alt1
- ja.zip build 2011-08-23 18:16 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108222128-alt1
- ja.zip build 2011-08-22 21:28 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108220123-alt1
- ja.zip build 2011-08-22 01:23 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108191757-alt1
- ja.zip build 2011-08-19 17:57 UTC

* Fri Aug 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108181726-alt1
- ja.zip build 2011-08-18 17:26 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108171909-alt1
- ja.zip build 2011-08-17 19:09 UTC

* Wed Aug 17 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161743-alt1
- ja.zip build 2011-08-16 17:43 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108152131-alt1
- ja.zip build 2011-08-15 21:31 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108121459-alt1
- Rename package to moodle2.0-lang-ja
- ja.zip build 2011-08-12 14:59 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110809-alt1
- ja_utf8.zip build 2011-08-09
- Add %%moodle_langdir/ja_utf8/fonts/default.ttf

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081210
- new build for ALT Linux from cvs
