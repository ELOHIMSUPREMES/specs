# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename it
%define packagversion 2.1.0
%define packagedate 201210191639
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Italian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-it
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
* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210191639-alt1
- repocop cronbuild 20121022. At your service.
- it.zip build 2012-10-19 16:39 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209281743-alt1
- repocop cronbuild 20121001. At your service.
- it.zip build 2012-09-28 17:43 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209031500-alt1
- repocop cronbuild 20120904. At your service.
- it.zip build 2012-09-03 15:00 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208271704-alt1
- repocop cronbuild 20120828. At your service.
- it.zip build 2012-08-27 17:04 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208031018-alt1
- repocop cronbuild 20120807. At your service.
- it.zip build 2012-08-03 10:18 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207181247-alt1
- repocop cronbuild 20120724. At your service.
- it.zip build 2012-07-18 12:47 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207111821-alt1
- repocop cronbuild 20120717. At your service.
- it.zip build 2012-07-11 18:21 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207060934-alt1
- repocop cronbuild 20120710. At your service.
- it.zip build 2012-07-06 09:34 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206281251-alt1
- repocop cronbuild 20120703. At your service.
- it.zip build 2012-06-28 12:51 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206221655-alt1
- repocop cronbuild 20120626. At your service.
- it.zip build 2012-06-22 16:55 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206121429-alt1
- repocop cronbuild 20120619. At your service.
- it.zip build 2012-06-12 14:29 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206111010-alt1
- repocop cronbuild 20120612. At your service.
- it.zip build 2012-06-11 10:10 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205301541-alt1
- repocop cronbuild 20120605. At your service.
- it.zip build 2012-05-30 15:41 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205281319-alt1
- repocop cronbuild 20120529. At your service.
- it.zip build 2012-05-28 13:19 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205191740-alt1
- repocop cronbuild 20120521. At your service.
- it.zip build 2012-05-19 17:40 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205111121-alt1
- repocop cronbuild 20120515. At your service.
- it.zip build 2012-05-11 11:21 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205020923-alt1
- repocop cronbuild 20120507. At your service.
- it.zip build 2012-05-02 09:23 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- it.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204201050-alt1
- repocop cronbuild 20120424. At your service.
- it.zip build 2012-04-20 10:50 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204130751-alt1
- repocop cronbuild 20120417. At your service.
- it.zip build 2012-04-13 07:51 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204051529-alt1
- repocop cronbuild 20120410. At your service.
- it.zip build 2012-04-05 15:29 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203261748-alt1
- repocop cronbuild 20120327. At your service.
- it.zip build 2012-03-26 17:48 UTC

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
