# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename it
%define packagversion 2.4.0
%define packagedate 201309161441
%define moodlebranch 2.4
%define moodlepackagename %moodle_name%moodlebranch
%define langname Italian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.4-lang-it
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.4
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.4
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
* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309161441-alt1
- repocop cronbuild 20130920. At your service.
- it.zip build 2013-09-16 14:41 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309051323-alt1
- repocop cronbuild 20130906. At your service.
- it.zip build 2013-09-05 13:23 UTC

* Fri Aug 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308191323-alt1
- repocop cronbuild 20130823. At your service.
- it.zip build 2013-08-19 13:23 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308010808-alt1
- repocop cronbuild 20130802. At your service.
- it.zip build 2013-08-01 08:08 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307181352-alt1
- repocop cronbuild 20130719. At your service.
- it.zip build 2013-07-18 13:52 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307091025-alt1
- repocop cronbuild 20130712. At your service.
- it.zip build 2013-07-09 10:25 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306261309-alt1
- repocop cronbuild 20130628. At your service.
- it.zip build 2013-06-26 13:09 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306200820-alt1
- repocop cronbuild 20130621. At your service.
- it.zip build 2013-06-20 08:20 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306131019-alt1
- repocop cronbuild 20130614. At your service.
- it.zip build 2013-06-13 10:19 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306060654-alt1
- repocop cronbuild 20130607. At your service.
- it.zip build 2013-06-06 06:54 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305301307-alt1
- repocop cronbuild 20130531. At your service.
- it.zip build 2013-05-30 13:07 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221013-alt1
- repocop cronbuild 20130524. At your service.
- it.zip build 2013-05-22 10:13 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305160843-alt1
- repocop cronbuild 20130517. At your service.
- it.zip build 2013-05-16 08:43 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305021315-alt1
- repocop cronbuild 20130509. At your service.
- it.zip build 2013-05-02 13:15 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304101622-alt1
- Rename package to moodle2.4-lang-it
- it.zip build 2013-04-10 16:22 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304051026-alt1
- repocop cronbuild 20130410. At your service.
- it.zip build 2013-04-05 10:26 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303291309-alt1
- repocop cronbuild 20130403. At your service.
- it.zip build 2013-03-29 13:09 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303251222-alt1
- repocop cronbuild 20130327. At your service.
- it.zip build 2013-03-25 12:22 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303151252-alt1
- repocop cronbuild 20130320. At your service.
- it.zip build 2013-03-15 12:52 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303111859-alt1
- repocop cronbuild 20130313. At your service.
- it.zip build 2013-03-11 18:59 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303011426-alt1
- repocop cronbuild 20130304. At your service.
- it.zip build 2013-03-01 14:26 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302211359-alt1
- repocop cronbuild 20130225. At your service.
- it.zip build 2013-02-21 13:59 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302151335-alt1
- repocop cronbuild 20130218. At your service.
- it.zip build 2013-02-15 13:35 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302081433-alt1
- repocop cronbuild 20130211. At your service.
- it.zip build 2013-02-08 14:33 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302011046-alt1
- repocop cronbuild 20130204. At your service.
- it.zip build 2013-02-01 10:46 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301231613-alt1
- repocop cronbuild 20130128. At your service.
- it.zip build 2013-01-23 16:13 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301181315-alt1
- repocop cronbuild 20130121. At your service.
- it.zip build 2013-01-18 13:15 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212311346-alt1
- repocop cronbuild 20130107. At your service.
- it.zip build 2012-12-31 13:46 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212190813-alt1
- repocop cronbuild 20121224. At your service.
- it.zip build 2012-12-19 08:13 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212071927-alt1
- repocop cronbuild 20121210. At your service.
- it.zip build 2012-12-07 19:27 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211060906-alt1
- repocop cronbuild 20121112. At your service.
- it.zip build 2012-11-06 09:06 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211021123-alt1
- repocop cronbuild 20121105. At your service.
- it.zip build 2012-11-02 11:23 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210261809-alt1
- repocop cronbuild 20121029. At your service.
- it.zip build 2012-10-26 18:09 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210191639-alt1
- repocop cronbuild 20121022. At your service.
- it.zip build 2012-10-19 16:39 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210110758-alt1
- repocop cronbuild 20121015. At your service.
- it.zip build 2012-10-11 07:58 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209281743-alt1
- repocop cronbuild 20121001. At your service.
- it.zip build 2012-09-28 17:43 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209071509-alt1
- repocop cronbuild 20120911. At your service.
- it.zip build 2012-09-07 15:09 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209031500-alt1
- repocop cronbuild 20120904. At your service.
- it.zip build 2012-09-03 15:00 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208271939-alt1
- repocop cronbuild 20120828. At your service.
- it.zip build 2012-08-27 19:39 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208031044-alt1
- repocop cronbuild 20120807. At your service.
- it.zip build 2012-08-03 10:44 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207181247-alt1
- repocop cronbuild 20120724. At your service.
- it.zip build 2012-07-18 12:47 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207111821-alt1
- repocop cronbuild 20120717. At your service.
- it.zip build 2012-07-11 18:21 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207060935-alt1
- repocop cronbuild 20120710. At your service.
- it.zip build 2012-07-06 09:35 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207031105-alt1
- repocop cronbuild 20120703. At your service.
- it.zip build 2012-07-03 11:05 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206221655-alt1
- repocop cronbuild 20120626. At your service.
- it.zip build 2012-06-22 16:55 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191525-alt1
- repocop cronbuild 20120619. At your service.
- it.zip build 2012-06-19 15:25 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121428-alt1
- repocop cronbuild 20120612. At your service.
- it.zip build 2012-06-12 14:28 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205301541-alt1
- repocop cronbuild 20120605. At your service.
- it.zip build 2012-05-30 15:41 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205290808-alt1
- repocop cronbuild 20120529. At your service.
- it.zip build 2012-05-29 08:08 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205191740-alt1
- repocop cronbuild 20120522. At your service.
- it.zip build 2012-05-19 17:40 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111113-alt1
- repocop cronbuild 20120515. At your service.
- it.zip build 2012-05-11 11:13 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205020921-alt1
- repocop cronbuild 20120508. At your service.
- it.zip build 2012-05-02 09:21 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- it.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204241332-alt1
- repocop cronbuild 20120424. At your service.
- it.zip build 2012-04-24 13:32 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204130750-alt1
- repocop cronbuild 20120417. At your service.
- it.zip build 2012-04-13 07:50 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204051529-alt1
- repocop cronbuild 20120410. At your service.
- it.zip build 2012-04-05 15:29 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203261748-alt1
- repocop cronbuild 20120327. At your service.
- it.zip build 2012-03-26 17:48 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203151213-alt1
- Rename package to moodle2.2-lang-it
- it.zip build 2012-03-15 12:13 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203151213-alt1
- repocop cronbuild 20120320. At your service.
- it.zip build 2012-03-15 12:13 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203071224-alt1
- repocop cronbuild 20120309. At your service.
- it.zip build 2012-03-07 12:24 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203021637-alt1
- repocop cronbuild 20120302. At your service.
- it.zip build 2012-03-02 16:37 UTC

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202171607-alt1
- repocop cronbuild 20120217. At your service.
- it.zip build 2012-02-17 16:07 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202091352-alt1
- repocop cronbuild 20120210. At your service.
- it.zip build 2012-02-09 13:52 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201301101-alt1
- repocop cronbuild 20120203. At your service.
- it.zip build 2012-01-30 11:01 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201271320-alt1
- repocop cronbuild 20120127. At your service.
- it.zip build 2012-01-27 13:20 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201201425-alt1
- repocop cronbuild 20120120. At your service.
- it.zip build 2012-01-20 14:25 UTC

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201131805-alt1
- repocop cronbuild 20120113. At your service.
- it.zip build 2012-01-13 18:05 UTC

* Fri Dec 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112281450-alt1
- repocop cronbuild 20111230. At your service.
- it.zip build 2011-12-28 14:50 UTC

* Fri Dec 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112231732-alt1
- repocop cronbuild 20111223. At your service.
- it.zip build 2011-12-23 17:32 UTC

* Fri Dec 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112151055-alt1
- repocop cronbuild 20111216. At your service.
- it.zip build 2011-12-15 10:55 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- it.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111231825-alt1
- Rename package to moodle2.1-lang-it
- it.zip build 2011-11-23 18:25

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111211610-alt2
- Fix requires

* Mon Nov 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111211610-alt1
- repocop cronbuild 20111121. At your service.
- it.zip build 2011-11-21 16:10 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111171327-alt1
- repocop cronbuild 20111118. At your service.
- it.zip build 2011-11-17 13:27 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151304-alt1
- repocop cronbuild 20111116. At your service.
- it.zip build 2011-11-15 13:04 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111041554-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111041554-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111041554-alt1
- repocop cronbuild 20111105. At your service.
- it.zip build 2011-11-04 15:54 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201547-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201547-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201547-alt1
- it.zip build 2011-10-20 15:47 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110051735-alt1
- it.zip build 2011-10-05 17:35 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231416-alt1
- it.zip build 2011-09-23 14:16 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- it.zip build 2011-09-21 15:30 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141727-alt1
- it.zip build 2011-09-14 17:27 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109131401-alt1
- it.zip build 2011-09-13 14:01 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109121617-alt1
- it.zip build 2011-09-12 16:17 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109071500-alt1
- it.zip build 2011-09-07 15:00 UTC

* Wed Aug 17 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- it.zip build 2011-08-16 13:07 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-it
- it.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110319-alt1
- it_utf8.zip build 2011-03-19

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081204
- new build for ALT Linux from cvs
