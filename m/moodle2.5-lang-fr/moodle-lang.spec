# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename fr
%define packagversion 2.5.0
%define packagedate 201404031150
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname French
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-fr
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.5
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.5
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
* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404031150-alt1
- repocop cronbuild 20140404. At your service.
- fr.zip build 2014-04-03 11:50 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403272038-alt1
- repocop cronbuild 20140328. At your service.
- fr.zip build 2014-03-27 20:38 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403191730-alt1
- repocop cronbuild 20140321. At your service.
- fr.zip build 2014-03-19 17:30 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403111814-alt1
- repocop cronbuild 20140314. At your service.
- fr.zip build 2014-03-11 18:14 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402271836-alt1
- repocop cronbuild 20140228. At your service.
- fr.zip build 2014-02-27 18:36 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402170752-alt1
- repocop cronbuild 20140221. At your service.
- fr.zip build 2014-02-17 07:52 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401301446-alt1
- repocop cronbuild 20140131. At your service.
- fr.zip build 2014-01-30 14:46 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231346-alt1
- repocop cronbuild 20140124. At your service.
- fr.zip build 2014-01-23 13:46 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401162024-alt1
- repocop cronbuild 20140117. At your service.
- fr.zip build 2014-01-16 20:24 UTC

* Fri Jan 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401041042-alt1
- repocop cronbuild 20140110. At your service.
- fr.zip build 2014-01-04 10:42 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312221827-alt1
- repocop cronbuild 20131227. At your service.
- fr.zip build 2013-12-22 18:27 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312181349-alt1
- repocop cronbuild 20131220. At your service.
- fr.zip build 2013-12-18 13:49 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- fr.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312011031-alt1
- repocop cronbuild 20131206. At your service.
- fr.zip build 2013-12-01 10:31 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311252044-alt1
- repocop cronbuild 20131129. At your service.
- fr.zip build 2013-11-25 20:44 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311211153-alt1
- repocop cronbuild 20131122. At your service.
- fr.zip build 2013-11-21 11:53 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311132017-alt1
- repocop cronbuild 20131115. At your service.
- fr.zip build 2013-11-13 20:17 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311062017-alt1
- repocop cronbuild 20131108. At your service.
- fr.zip build 2013-11-06 20:17 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311010643-alt1
- repocop cronbuild 20131101. At your service.
- fr.zip build 2013-11-01 06:43 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310210852-alt1
- repocop cronbuild 20131025. At your service.
- fr.zip build 2013-10-21 08:52 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310141257-alt1
- repocop cronbuild 20131018. At your service.
- fr.zip build 2013-10-14 12:57 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310101301-alt1
- repocop cronbuild 20131011. At your service.
- fr.zip build 2013-10-10 13:01 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309271814-alt1
- repocop cronbuild 20131004. At your service.
- fr.zip build 2013-09-27 18:14 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309261945-alt1
- repocop cronbuild 20130927. At your service.
- fr.zip build 2013-09-26 19:45 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309141808-alt1
- repocop cronbuild 20130920. At your service.
- fr.zip build 2013-09-14 18:08 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309081442-alt1
- repocop cronbuild 20130913. At your service.
- fr.zip build 2013-09-08 14:42 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309051650-alt1
- repocop cronbuild 20130906. At your service.
- fr.zip build 2013-09-05 16:50 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308301839-alt1
- repocop cronbuild 20130831. At your service.
- fr.zip build 2013-08-30 18:39 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308231112-alt1
- repocop cronbuild 20130824. At your service.
- fr.zip build 2013-08-23 11:12 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308151627-alt1
- repocop cronbuild 20130817. At your service.
- fr.zip build 2013-08-15 16:27 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308090935-alt1
- repocop cronbuild 20130810. At your service.
- fr.zip build 2013-08-09 09:35 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307310840-alt1
- repocop cronbuild 20130803. At your service.
- fr.zip build 2013-07-31 08:40 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307201617-alt1
- repocop cronbuild 20130727. At your service.
- fr.zip build 2013-07-20 16:17 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307150855-alt1
- repocop cronbuild 20130720. At your service.
- fr.zip build 2013-07-15 08:55 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307121421-alt1
- repocop cronbuild 20130713. At your service.
- fr.zip build 2013-07-12 14:21 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307051513-alt1
- repocop cronbuild 20130706. At your service.
- fr.zip build 2013-07-05 15:13 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306271051-alt1
- repocop cronbuild 20130629. At your service.
- fr.zip build 2013-06-27 10:51 UTC

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306211951-alt1
- repocop cronbuild 20130622. At your service.
- fr.zip build 2013-06-21 19:51 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306141604-alt1
- repocop cronbuild 20130615. At your service.
- fr.zip build 2013-06-14 16:04 UTC

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306051000-alt1
- repocop cronbuild 20130608. At your service.
- fr.zip build 2013-06-05 10:00 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305300937-alt1
- Rename package to moodle2.5-lang-fr
- fr.zip build 2013-05-30 09:37 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305231013-alt1
- repocop cronbuild 20130524. At your service.
- fr.zip build 2013-05-23 10:13 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305161747-alt1
- repocop cronbuild 20130517. At your service.
- fr.zip build 2013-05-16 17:47 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305081457-alt1
- repocop cronbuild 20130509. At your service.
- fr.zip build 2013-05-08 14:57 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304171806-alt1
- Rename package to moodle2.4-lang-fr
- fr.zip build 2013-04-17 18:06 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304121542-alt1
- repocop cronbuild 20130417. At your service.
- fr.zip build 2013-04-12 15:42 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303311820-alt1
- repocop cronbuild 20130403. At your service.
- fr.zip build 2013-03-31 18:20 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303251657-alt1
- repocop cronbuild 20130327. At your service.
- fr.zip build 2013-03-25 16:57 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303091715-alt1
- repocop cronbuild 20130313. At your service.
- fr.zip build 2013-03-09 17:15 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302271743-alt1
- repocop cronbuild 20130304. At your service.
- fr.zip build 2013-02-27 17:43 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302221221-alt1
- repocop cronbuild 20130225. At your service.
- fr.zip build 2013-02-22 12:21 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302151818-alt1
- repocop cronbuild 20130218. At your service.
- fr.zip build 2013-02-15 18:18 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302032132-alt1
- repocop cronbuild 20130204. At your service.
- fr.zip build 2013-02-03 21:32 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261629-alt1
- repocop cronbuild 20130128. At your service.
- fr.zip build 2013-01-26 16:29 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301201642-alt1
- repocop cronbuild 20130121. At your service.
- fr.zip build 2013-01-20 16:42 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301131659-alt1
- repocop cronbuild 20130114. At your service.
- fr.zip build 2013-01-13 16:59 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301032217-alt1
- repocop cronbuild 20130107. At your service.
- fr.zip build 2013-01-03 22:17 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212292101-alt1
- repocop cronbuild 20121231. At your service.
- fr.zip build 2012-12-29 21:01 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212211307-alt1
- repocop cronbuild 20121224. At your service.
- fr.zip build 2012-12-21 13:07 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212141605-alt1
- repocop cronbuild 20121217. At your service.
- fr.zip build 2012-12-14 16:05 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212062202-alt1
- repocop cronbuild 20121210. At your service.
- fr.zip build 2012-12-06 22:02 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211251437-alt1
- repocop cronbuild 20121126. At your service.
- fr.zip build 2012-11-25 14:37 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211161706-alt1
- repocop cronbuild 20121119. At your service.
- fr.zip build 2012-11-16 17:06 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211101918-alt1
- repocop cronbuild 20121112. At your service.
- fr.zip build 2012-11-10 19:18 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211041143-alt1
- repocop cronbuild 20121105. At your service.
- fr.zip build 2012-11-04 11:43 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210261733-alt1
- repocop cronbuild 20121029. At your service.
- fr.zip build 2012-10-26 17:33 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210190707-alt1
- repocop cronbuild 20121022. At your service.
- fr.zip build 2012-10-19 07:07 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210131448-alt1
- repocop cronbuild 20121015. At your service.
- fr.zip build 2012-10-13 14:48 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210012025-alt1
- repocop cronbuild 20121008. At your service.
- fr.zip build 2012-10-01 20:25 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209251854-alt1
- repocop cronbuild 20121001. At your service.
- fr.zip build 2012-09-25 18:54 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209171957-alt1
- repocop cronbuild 20120918. At your service.
- fr.zip build 2012-09-17 19:57 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209070948-alt1
- repocop cronbuild 20120911. At your service.
- fr.zip build 2012-09-07 09:48 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120904. At your service.
- fr.zip build 2012-08-31 10:30 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208261233-alt1
- repocop cronbuild 20120828. At your service.
- fr.zip build 2012-08-26 12:33 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208161642-alt1
- repocop cronbuild 20120820. At your service.
- fr.zip build 2012-08-16 16:42 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208021945-alt1
- repocop cronbuild 20120807. At your service.
- fr.zip build 2012-08-02 19:45 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207201437-alt1
- repocop cronbuild 20120724. At your service.
- fr.zip build 2012-07-20 14:37 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207161314-alt1
- repocop cronbuild 20120717. At your service.
- fr.zip build 2012-07-16 13:14 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207091604-alt1
- repocop cronbuild 20120710. At your service.
- fr.zip build 2012-07-09 16:04 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207021957-alt1
- repocop cronbuild 20120703. At your service.
- fr.zip build 2012-07-02 19:57 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206201443-alt1
- repocop cronbuild 20120626. At your service.
- fr.zip build 2012-06-20 14:43 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206161419-alt1
- repocop cronbuild 20120619. At your service.
- fr.zip build 2012-06-16 14:19 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206071356-alt1
- repocop cronbuild 20120612. At your service.
- fr.zip build 2012-06-07 13:56 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206031721-alt1
- repocop cronbuild 20120605. At your service.
- fr.zip build 2012-06-03 17:21 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205241640-alt1
- repocop cronbuild 20120529. At your service.
- fr.zip build 2012-05-24 16:40 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205201223-alt1
- repocop cronbuild 20120521. At your service.
- fr.zip build 2012-05-20 12:23 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- fr.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205071515-alt1
- repocop cronbuild 20120508. At your service.
- fr.zip build 2012-05-07 15:15 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- fr.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204231441-alt1
- repocop cronbuild 20120424. At your service.
- fr.zip build 2012-04-23 14:41 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204101256-alt1
- repocop cronbuild 20120417. At your service.
- fr.zip build 2012-04-10 12:56 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204061324-alt1
- repocop cronbuild 20120410. At your service.
- fr.zip build 2012-04-06 13:24 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204010955-alt1
- repocop cronbuild 20120403. At your service.
- fr.zip build 2012-04-01 09:55 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203201952-alt1
- repocop cronbuild 20120327. At your service.
- fr.zip build 2012-03-20 19:52 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203181809-alt1
- Rename package to moodle2.2-lang-fr
- fr.zip build 2012-03-18 18:09 UTC

* Thu Mar 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203061934-alt1
- repocop cronbuild 20120308. At your service.
- fr.zip build 2012-03-06 19:34 UTC

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120301. At your service.
- fr.zip build 2012-03-01 11:00 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202221009-alt1
- repocop cronbuild 20120223. At your service.
- fr.zip build 2012-02-22 10:09 UTC

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202111010-alt1
- repocop cronbuild 20120216. At your service.
- fr.zip build 2012-02-11 10:10 UTC

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202081935-alt1
- repocop cronbuild 20120209. At your service.
- fr.zip build 2012-02-08 19:35 UTC

* Thu Feb 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201302038-alt1
- repocop cronbuild 20120202. At your service.
- fr.zip build 2012-01-30 20:38 UTC

* Thu Jan 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201221740-alt1
- repocop cronbuild 20120126. At your service.
- fr.zip build 2012-01-22 17:40 UTC

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201121858-alt1
- repocop cronbuild 20120112. At your service.
- fr.zip build 2012-01-12 18:58 UTC

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201050916-alt1
- repocop cronbuild 20120105. At your service.
- fr.zip build 2012-01-05 09:16 UTC

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112192151-alt1
- repocop cronbuild 20111222. At your service.
- fr.zip build 2011-12-19 21:51 UTC

* Thu Dec 15 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091829-alt1
- repocop cronbuild 20111215. At your service.
- fr.zip build 2011-12-09 18:29 UTC

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112081249-alt1
- repocop cronbuild 20111208. At your service.
- fr.zip build 2011-12-08 12:49 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111251639-alt1
- repocop cronbuild 20111125. At your service.
- fr.zip build 2011-11-25 16:39 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111232006-alt1
- Rename package to moodle2.1-lang-fr
- fr.zip build 2011-11-23 20:06 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111232006-alt2
- Fix requires

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111232006-alt1
- repocop cronbuild 20111123. At your service.
- fr.zip build 2011-11-23 20:06 UTC

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111202140-alt1
- repocop cronbuild 20111120. At your service.
- fr.zip build 2011-11-20 21:40 UTC

* Sat Nov 19 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111191256-alt1
- repocop cronbuild 20111119. At your service.
- fr.zip build 2011-11-19 12:56 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111181223-alt1
- repocop cronbuild 20111118. At your service.
- fr.zip build 2011-11-18 12:23 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151942-alt1
- repocop cronbuild 20111116. At your service.
- fr.zip build 2011-11-15 19:42 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031917-alt1
- repocop cronbuild 20111105. At your service.
- fr.zip build 2011-11-03 19:17 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt1
- fr.zip build 2011-10-12 18:40 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231534-alt1
- fr.zip build 2011-09-23 15:34 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109230935-alt1
- fr.zip build 2011-09-23 09:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221808-alt1
- fr.zip build 2011-09-22 18:08 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- fr.zip build 2011-09-21 15:30 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109161112-alt1
- fr.zip build 2011-09-16 11:12 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109081534-alt1
- fr.zip build 2011-09-08 15:34 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109041828-alt1
- fr.zip build 2011-09-04 18:28 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241508-alt1
- fr.zip build 2011-08-24 15:08 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108190836-alt1
- fr.zip build 2011-08-19 08:36 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- fr.zip build 2011-08-16 13:07 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108141034-alt1
- fr.zip build 2011-08-14 10:34 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-fr
- fr.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110718-alt1
- fr_utf8.zip build 2011-07-18

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081211
- new build for ALT Linux from cvs
