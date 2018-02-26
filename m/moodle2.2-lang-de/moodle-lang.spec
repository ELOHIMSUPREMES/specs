# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename de
%define packagversion 2.2.0
%define packagedate 201211251702
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname German
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-de
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.2
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.2
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
* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211251702-alt1
- repocop cronbuild 20121126. At your service.
- de.zip build 2012-11-25 17:02 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211181000-alt1
- repocop cronbuild 20121119. At your service.
- de.zip build 2012-11-18 10:00 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211111645-alt1
- repocop cronbuild 20121112. At your service.
- de.zip build 2012-11-11 16:45 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211021541-alt1
- repocop cronbuild 20121105. At your service.
- de.zip build 2012-11-02 15:41 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210281116-alt1
- repocop cronbuild 20121029. At your service.
- de.zip build 2012-10-28 11:16 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210211721-alt1
- repocop cronbuild 20121022. At your service.
- de.zip build 2012-10-21 17:21 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210101233-alt1
- repocop cronbuild 20121015. At your service.
- de.zip build 2012-10-10 12:33 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210071633-alt1
- repocop cronbuild 20121008. At your service.
- de.zip build 2012-10-07 16:33 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209280635-alt1
- repocop cronbuild 20121001. At your service.
- de.zip build 2012-09-28 06:35 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209112324-alt1
- repocop cronbuild 20120918. At your service.
- de.zip build 2012-09-11 23:24 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209090651-alt1
- repocop cronbuild 20120911. At your service.
- de.zip build 2012-09-09 06:51 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311647-alt1
- repocop cronbuild 20120904. At your service.
- de.zip build 2012-08-31 16:47 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208211159-alt1
- repocop cronbuild 20120828. At your service.
- de.zip build 2012-08-21 11:59 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208191759-alt1
- repocop cronbuild 20120820. At your service.
- de.zip build 2012-08-19 17:59 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208111045-alt1
- repocop cronbuild 20120814. At your service.
- de.zip build 2012-08-11 10:45 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208060813-alt1
- repocop cronbuild 20120807. At your service.
- de.zip build 2012-08-06 08:13 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207301716-alt1
- repocop cronbuild 20120731. At your service.
- de.zip build 2012-07-30 17:16 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207231150-alt1
- repocop cronbuild 20120724. At your service.
- de.zip build 2012-07-23 11:50 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207121607-alt1
- repocop cronbuild 20120717. At your service.
- de.zip build 2012-07-12 16:07 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207091555-alt1
- repocop cronbuild 20120710. At your service.
- de.zip build 2012-07-09 15:55 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207021842-alt1
- repocop cronbuild 20120703. At your service.
- de.zip build 2012-07-02 18:42 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206241901-alt1
- repocop cronbuild 20120626. At your service.
- de.zip build 2012-06-24 19:01 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206181719-alt1
- repocop cronbuild 20120619. At your service.
- de.zip build 2012-06-18 17:19 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206080854-alt1
- repocop cronbuild 20120612. At your service.
- de.zip build 2012-06-08 08:54 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206041513-alt1
- repocop cronbuild 20120605. At your service.
- de.zip build 2012-06-04 15:13 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205280958-alt1
- repocop cronbuild 20120529. At your service.
- de.zip build 2012-05-28 09:58 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205211742-alt1
- repocop cronbuild 20120521. At your service.
- de.zip build 2012-05-21 17:42 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205120821-alt1
- repocop cronbuild 20120515. At your service.
- de.zip build 2012-05-12 08:21 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205072118-alt1
- repocop cronbuild 20120508. At your service.
- de.zip build 2012-05-07 21:18 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204280914-alt1
- repocop cronbuild 20120501. At your service.
- de.zip build 2012-04-28 09:14 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204161516-alt1
- repocop cronbuild 20120417. At your service.
- de.zip build 2012-04-16 15:16 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204060624-alt1
- repocop cronbuild 20120410. At your service.
- de.zip build 2012-04-06 06:24 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204021424-alt1
- repocop cronbuild 20120403. At your service.
- de.zip build 2012-04-02 14:24 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203230604-alt1
- repocop cronbuild 20120327. At your service.
- de.zip build 2012-03-23 06:04 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203181916-alt1
- Rename package to moodle2.2-lang-de
- de.zip build 2012-03-18 19:16 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203100131-alt1
- repocop cronbuild 20120313. At your service.
- de.zip build 2012-03-10 01:31 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203041741-alt1
- repocop cronbuild 20120309. At your service.
- de.zip build 2012-03-04 17:41 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203012147-alt1
- repocop cronbuild 20120302. At your service.
- de.zip build 2012-03-01 21:47 UTC

* Fri Feb 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202201600-alt1
- repocop cronbuild 20120224. At your service.
- de.zip build 2012-02-20 16:00 UTC

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202171612-alt1
- repocop cronbuild 20120217. At your service.
- de.zip build 2012-02-17 16:12 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202102121-alt1
- repocop cronbuild 20120210. At your service.
- de.zip build 2012-02-10 21:21 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201291051-alt1
- repocop cronbuild 20120203. At your service.
- de.zip build 2012-01-29 10:51 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201271719-alt1
- repocop cronbuild 20120127. At your service.
- de.zip build 2012-01-27 17:19 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201180523-alt1
- repocop cronbuild 20120120. At your service.
- de.zip build 2012-01-18 05:23 UTC

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201101616-alt1
- repocop cronbuild 20120113. At your service.
- de.zip build 2012-01-10 16:16 UTC

* Fri Jan 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201052228-alt1
- repocop cronbuild 20120106. At your service.
- de.zip build 2012-01-05 22:28 UTC

* Fri Dec 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112291253-alt1
- repocop cronbuild 20111230. At your service.
- de.zip build 2011-12-29 12:53 UTC

* Fri Dec 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112232118-alt1
- repocop cronbuild 20111223. At your service.
- de.zip build 2011-12-23 21:18 UTC

* Fri Dec 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112161557-alt1
- repocop cronbuild 20111216. At your service.
- de.zip build 2011-12-16 15:57 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- de.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111252051-alt1
- repocop cronbuild 20111125. At your service.
- de.zip build 2011-11-25 20:51 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-de
- de.zip build 2011-11-02 19:30 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt1
- de.zip build 2011-10-21 05:07 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- de.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109181008-alt1
- de.zip build 2011-09-18 10:08 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109111520-alt1
- de.zip build 2011-09-11 15:20 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108220638-alt2
- Fix requires

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108220638-alt1
- de.zip build 2011-08-22 06:38 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108191519-alt1
- de.zip build 2011-08-19 15:19 UTC

* Fri Aug 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108181355-alt1
- de.zip build 2011-08-18 13:55 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- de.zip build 2011-08-16 13:07

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-de
- de.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110705-alt1
- de_utf8.zip build 2011-07-05

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081028
- new build for ALT Linux from cvs
