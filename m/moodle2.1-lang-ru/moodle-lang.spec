# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ru
%define packagversion 2.1.0
%define packagedate 201304031528
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Russian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-ru
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
* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201304031528-alt1
- repocop cronbuild 20130403. At your service.
- ru.zip build 2013-04-03 15:28 UTC

* Sun Mar 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303172106-alt1
- repocop cronbuild 20130317. At your service.
- ru.zip build 2013-03-17 21:06 UTC

* Wed Mar 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303051413-alt1
- repocop cronbuild 20130306. At your service.
- ru.zip build 2013-03-05 14:13 UTC

* Sat Feb 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302151550-alt1
- repocop cronbuild 20130216. At your service.
- ru.zip build 2013-02-15 15:50 UTC

* Wed Feb 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302131042-alt1
- repocop cronbuild 20130213. At your service.
- ru.zip build 2013-02-13 10:42 UTC

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301280958-alt1
- repocop cronbuild 20130129. At your service.
- ru.zip build 2013-01-28 09:58 UTC

* Sat Jan 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301261559-alt1
- repocop cronbuild 20130126. At your service.
- ru.zip build 2013-01-26 15:59 UTC

* Tue Jan 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301212155-alt1
- repocop cronbuild 20130122. At your service.
- ru.zip build 2013-01-21 21:55 UTC

* Sat Jan 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301121811-alt1
- repocop cronbuild 20130112. At your service.
- ru.zip build 2013-01-12 18:11 UTC

* Fri Jan 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301112113-alt1
- repocop cronbuild 20130111. At your service.
- ru.zip build 2013-01-11 21:13 UTC

* Sat Jan 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301051948-alt1
- repocop cronbuild 20130105. At your service.
- ru.zip build 2013-01-05 19:48 UTC

* Sat Dec 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212221221-alt1
- repocop cronbuild 20121222. At your service.
- ru.zip build 2012-12-22 12:21 UTC

* Wed Dec 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212191047-alt1
- repocop cronbuild 20121219. At your service.
- ru.zip build 2012-12-19 10:47 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211032110-alt1
- repocop cronbuild 20121105. At your service.
- ru.zip build 2012-11-03 21:10 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210011159-alt1
- repocop cronbuild 20121001. At your service.
- ru.zip build 2012-10-01 11:59 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209251230-alt1
- repocop cronbuild 20121001. At your service.
- ru.zip build 2012-09-25 12:30 UTC

* Wed Sep 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209121027-alt1
- repocop cronbuild 20120912. At your service.
- ru.zip build 2012-09-12 10:27 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209111534-alt1
- repocop cronbuild 20120911. At your service.
- ru.zip build 2012-09-11 15:34 UTC

* Thu Sep 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209061450-alt1
- repocop cronbuild 20120906. At your service.
- ru.zip build 2012-09-06 14:50 UTC

* Fri Aug 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208240740-alt1
- repocop cronbuild 20120824. At your service.
- ru.zip build 2012-08-24 07:40 UTC

* Thu Aug 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208161815-alt1
- repocop cronbuild 20120816. At your service.
- ru.zip build 2012-08-16 18:15 UTC

* Sat Aug 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208032056-alt1
- repocop cronbuild 20120804. At your service.
- ru.zip build 2012-08-03 20:56 UTC

* Fri Aug 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208031851-alt1
- repocop cronbuild 20120803. At your service.
- ru.zip build 2012-08-03 18:51 UTC

* Thu Aug 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208022032-alt1
- repocop cronbuild 20120802. At your service.
- ru.zip build 2012-08-02 20:32 UTC

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208012126-alt1
- repocop cronbuild 20120801. At your service.
- ru.zip build 2012-08-01 21:26 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207310756-alt1
- repocop cronbuild 20120731. At your service.
- ru.zip build 2012-07-31 07:56 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207302007-alt1
- repocop cronbuild 20120731. At your service.
- ru.zip build 2012-07-30 20:07 UTC

* Fri Jul 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207200826-alt1
- repocop cronbuild 20120720. At your service.
- ru.zip build 2012-07-20 08:26 UTC

* Thu Jul 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207191051-alt1
- repocop cronbuild 20120719. At your service.
- ru.zip build 2012-07-19 10:51 UTC

* Wed Jul 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207180728-alt1
- repocop cronbuild 20120718. At your service.
- ru.zip build 2012-07-18 07:28 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207151955-alt1
- repocop cronbuild 20120717. At your service.
- ru.zip build 2012-07-15 19:55 UTC

* Sun Jul 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207151637-alt1
- repocop cronbuild 20120715. At your service.
- ru.zip build 2012-07-15 16:37 UTC

* Fri Jul 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207131300-alt1
- repocop cronbuild 20120713. At your service.
- ru.zip build 2012-07-13 13:00 UTC

* Thu Jul 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207120506-alt1
- repocop cronbuild 20120712. At your service.
- ru.zip build 2012-07-12 05:06 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207031030-alt1
- repocop cronbuild 20120703. At your service.
- ru.zip build 2012-07-03 10:30 UTC

* Sat Jun 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206301755-alt1
- repocop cronbuild 20120630. At your service.
- ru.zip build 2012-06-30 17:55 UTC

* Thu Jun 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206140651-alt1
- repocop cronbuild 20120614. At your service.
- ru.zip build 2012-06-14 06:51 UTC

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206130921-alt1
- repocop cronbuild 20120613. At your service.
- ru.zip build 2012-06-13 09:21 UTC

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205231549-alt1
- repocop cronbuild 20120523. At your service.
- ru.zip build 2012-05-23 15:49 UTC

* Fri May 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205041518-alt1
- repocop cronbuild 20120504. At your service.
- ru.zip build 2012-05-04 15:18 UTC

* Wed May 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205021803-alt1
- repocop cronbuild 20120502. At your service.
- ru.zip build 2012-05-02 18:03 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204300527-alt1
- repocop cronbuild 20120501. At your service.
- ru.zip build 2012-04-30 05:27 UTC

* Fri Apr 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204130803-alt1
- repocop cronbuild 20120413. At your service.
- ru.zip build 2012-04-13 08:03 UTC

* Thu Apr 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204122046-alt1
- repocop cronbuild 20120412. At your service.
- ru.zip build 2012-04-12 20:46 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204090808-alt1
- repocop cronbuild 20120410. At your service.
- ru.zip build 2012-04-09 08:08 UTC

* Sun Apr 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204081656-alt1
- repocop cronbuild 20120408. At your service.
- ru.zip build 2012-04-08 16:56 UTC

* Thu Mar 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203221319-alt1
- repocop cronbuild 20120322. At your service.
- ru.zip build 2012-03-22 13:19 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203200757-alt1
- repocop cronbuild 20120320. At your service.
- ru.zip build 2012-03-20 07:57 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203051138-alt1
- repocop cronbuild 20120306. At your service.
- ru.zip build 2012-03-05 11:38 UTC

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120301. At your service.
- ru.zip build 2012-03-01 11:00 UTC

* Sun Feb 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202260940-alt1
- repocop cronbuild 20120226. At your service.
- ru.zip build 2012-02-26 09:40 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202010703-alt1
- repocop cronbuild 20120201. At your service.
- ru.zip build 2012-02-01 07:03 UTC

* Sat Jan 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201280352-alt1
- repocop cronbuild 20120128. At your service.
- ru.zip build 2012-01-28 03:52 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201251829-alt1
- repocop cronbuild 20120125. At your service.
- ru.zip build 2012-01-25 18:29 UTC

* Sat Jan 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201211904-alt1
- repocop cronbuild 20120121. At your service.
- ru.zip build 2012-01-21 19:04 UTC

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201051751-alt1
- repocop cronbuild 20120105. At your service.
- ru.zip build 2012-01-05 17:51 UTC

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112221011-alt1
- repocop cronbuild 20111222. At your service.
- ru.zip build 2011-12-22 10:11 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112211944-alt1
- repocop cronbuild 20111221. At your service.
- ru.zip build 2011-12-21 19:44 UTC

* Thu Dec 15 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112151437-alt1
- repocop cronbuild 20111215. At your service.
- ru.zip build 2011-12-15 14:37 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112141935-alt1
- repocop cronbuild 20111214. At your service.
- ru.zip build 2011-12-14 19:35 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112131517-alt1
- repocop cronbuild 20111213. At your service.
- ru.zip build 2011-12-13 15:17 UTC

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112100727-alt1
- repocop cronbuild 20111210. At your service.
- ru.zip build 2011-12-10 07:27 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- ru.zip build 2011-12-09 16:00 UTC

* Sun Nov 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111271657-alt1
- repocop cronbuild 20111127. At your service.
- ru.zip build 2011-11-27 16:57 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111251919-alt1
- repocop cronbuild 20111125. At your service.
- ru.zip build 2011-11-25 19:19 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111061046-alt1
- Rename package to moodle2.1-lang-ru
- ru.zip build 2011-11-06 10:46 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111061026-alt1
- repocop cronbuild 20111116. At your service.
- ru.zip build 2011-11-06 10:26 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021436-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021436-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111021436-alt1
- repocop cronbuild 20111105. At your service.
- ru.zip build 2011-11-02 14:36 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201902-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201902-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201902-alt1
- ru.zip build 2011-10-20 19:02 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110050641-alt1
- ru.zip build 2011-10-05 06:41 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109272015-alt1
- ru.zip build 2011-09-27 20:15 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109270433-alt1
- ru.zip build 2011-09-27 04:33 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231446-alt1
- ru.zip build 2011-09-23 14:46 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221040-alt1
- ru.zip build 2011-09-22 10:40 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- ru.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109190938-alt1
- ru.zip build 2011-09-19 09:38 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109190636-alt1
- ru.zip build 2011-09-19 06:36 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109160755-alt1
- ru.zip build 2011-09-16 07:55 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141836-alt1
- ru.zip build 2011-09-14 18:36 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109131719-alt1
- ru.zip build 2011-09-13 17:19 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109110824-alt1
- ru.zip build 2011-09-11 08:24 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109071935-alt1
- ru.zip build 2011-09-07 19:35 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241750-alt1
- ru.zip build 2011-08-24 17:50 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108191453-alt1
- ru.zip build 2011-08-19 14:53 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-ru
- ru.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt1
- ru_utf8.zip build 2010-06-17

* Tue Nov 23 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt2.cvs20100617
- inheritance fixed

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100617
- new version

* Tue Oct 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt2.cvs20091014
- rebuild with new Moodle

* Mon Oct 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20091014
- new build from cvs

* Sun Jul 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20090720
- new build from cvs

* Sat Apr 18 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.4-alt1.cvs20090416
- new build from cvs

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081106
- new build from cvs

* Mon Oct 13 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080926
- new build from cvs

* Mon Sep 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080802
- add build requires on rpm-build-webserver-common
- new build from cvs

* Thu Jun 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt2.cvs20080526
- change path moodle location

* Mon Jun 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.cvs20080526
- new build for ALT Linux
