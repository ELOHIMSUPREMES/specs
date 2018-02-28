# TODO:fix build Python bindings
%def_disable python
%define  git_rev a1c7f64

Name: 	 gnucash
Version: 2.6.12
Release: alt1

Summary: GnuCash is an application to keep track of your finances
Summary(ru_RU.UTF8): Программа учёта финансов GnuCash

License: GPLv2+
Group:   Office
Url: 	 http://www.gnucash.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
Source5: %name-README.RU
Source7: conv_gnucash2.sh

AutoReq: yes, noperl

BuildRequires: doxygen graphviz guile18-devel intltool libglade-devel libgnomeoffice-devel libgnomeui-devel libgtkhtml3-devel libofx-devel libreadline-devel slib-guile
BuildRequires: libGConf-devel
BuildRequires: libdbi-devel
BuildRequires: libdbi-drivers-devel
BuildRequires: libdbi-drivers-dbd-sqlite
BuildRequires: libdbi-drivers-dbd-mysql
BuildRequires: libdbi-drivers-dbd-pgsql
#if_disabled goffice_internal
BuildPreReq: libgnomeoffice-devel
#endif
BuildRequires: swig
BuildRequires: zlib-devel
BuildRequires: libxslt-devel
BuildRequires: aqbanking-devel
BuildRequires: libwebkitgtk2-devel
%if_enabled python
BuildRequires: python-devel
%endif

Requires: lib%name = %version-%release
Requires: slib-guile
Requires: dconf

%description
GnuCash is a personal finance manager. A check-book like
register GUI allows you to enter and track bank accounts,
stocks, income and even currency trades. The interface is
designed to be simple and easy to use, but is backed with
double-entry accounting principles to ensure balanced books.

%description -l ru_RU.UTF8
GnuCash -- это личный финансовый менеджер. Книга учёта
в виде журнала на экране позволит вам вводить и отслеживать
состояние банковских счетов, ценных бумаг, приход денег и
даже курсы валют. Интерфейс программы разработан простым и
лёгким в использовании, но в то же время применяется
принцип двойной записи для обеспечения сведения баланса.

%package -n lib%name-devel
Group: Development/C
Summary: Libraries needed to develop for gnucash
Summary(ru_RU.UTF8): Библиотеки, требуемые для разработки с gnucash
Requires: lib%name = %version
Obsoletes: %name-devel

%description -n lib%name-devel
Libraries needed to develop for gnucash.
%description -n lib%name-devel -l ru_RU.UTF8
Библиотеки, требуемые для разработки с gnucash.

%package -n lib%name
Summary: Libraries for gnucash (sql backends too).
Group: System/Libraries

%add_findprov_lib_path %_libdir/%name

%description -n lib%name
This package provides libraries to use gnucash.


%description -n lib%name -l ru_RU.UTF8
Пакет предоставляет библиотеки, используемые gnucash.

%package quotes
Summary: Allow GnuCash to fetch quotes
Group: Office
Requires: %name
Requires: perl-Date-Manip perl-Finance-Quote

%description quotes
Virtula package that install needed perl modules for quote's online
fetch and update.

%prep
%setup -q

%build
%autoreconf
%add_optflags -Wno-error=deprecated-declarations

%if_enabled python
sed -i 's|get_python_lib(0|get_python_lib(1|g' configure
export PYTHON=/usr/bin/python
%endif

# Print fake revision to build from VCS
echo -e '#!/bin/sh\ntest $1 = "-r" && echo "%git_rev"\ntest $1 = "-t" && echo "git"\nexit 0' > util/gnc-vcs-info

%configure \
	   --enable-ofx \
	   --enable-aqbanking \
	   --with-html-engine=webkit \
	   --enable-locale-specific-tax \
	   --enable-dbi \
%if_enabled python
	   --enable-python \
%endif
	   --disable-static

%make_build
#ifdef python
#  PYTHON_CPPFLAGS="$(pkg-config python --cflags)"
#endif

%install
%makeinstall_std

rm -rf %buildroot%_bindir/gnucash-valgrind \
       %buildroot%_libexecdir/%name/src/

%find_lang %name --with-gnome

install -m755 %SOURCE7 %buildroot%_bindir/conv_gnucash2.sh

tar cfj ChangeLog.tar.bz2 ChangeLog*

rm -f %buildroot%_datadir/gnucash/gnome \
      %buildroot%_bindir/gnc-test-env \
      %buildroot%_bindir/gnc-fq-update

%files -n lib%name-devel
%doc ChangeLog.*
%_includedir/%name/

%files -n lib%name
%_libdir/lib*.so.*
%dir %_libdir/%name/
%_libdir/%name/lib*so*.0
%_libdir/%name/*.la
%_libdir/*.so
%_libdir/%name/*.so

# hbci отдельно
#%exclude %_libdir/%name/libgncmod-hbci*

%files -f %name.lang
%doc AUTHORS ChangeLog.tar.bz2 HACKING NEWS README*
%doc doc/README.* doc/guile-hackers.txt
%doc %_defaultdocdir/%name/
%_bindir/*
%config %_sysconfdir/%name
%_desktopdir/%name.desktop
%_libexecdir/%name/overrides/
%_datadir/%name/
%doc %_man1dir/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/appdata/%name.appdata.xml
%_datadir/glib-2.0/schemas/org.%name.*.xml

#hbci отдельно
#%exclude %_datadir/%name/glade/hbci*

%files quotes

%changelog
* Tue Apr 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.12-alt1
- New version

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.11-alt1
- New version

* Sat Jan 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.10-alt1
- New version

* Mon Oct 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.9-alt1
- New version

* Wed Sep 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.8-alt1
- New version

* Fri Jul 03 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.7-alt1
- New version

* Thu Apr 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- New version

* Mon Jan 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version
- Fix License

* Sat Oct 04 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version

* Fri Apr 11 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.3-alt1
- New version

* Mon Mar 24 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version
- Fix check for build python bindings

* Thu Jan 30 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version
- Replace GConf2 bt dconf

* Thu Jan 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version
- Use aqbanking
- Remove redundant binaries and registration of GConf schemas

* Sun Nov 24 2013 Andrey Cherepanov <cas@altlinux.org> 2.4.13-alt1
- New version
- Build with libofx-0.9.9

* Sun Apr 08 2012 Alexey Morsov <swi@altlinux.ru> 2.4.10-alt1
- new version

* Fri Jan 13 2012 Andrey Cherepanov <cas@altlinux.org> 2.4.8-alt2
- Remove libgsf-gnome support (no more gnome-vfs/bonobo support in libgsf)

* Mon Nov 07 2011 Alexey Morsov <swi@altlinux.ru> 2.4.8-alt1
- new version
- fix postgresql9 devel package name

* Mon Sep 12 2011 Alexey Morsov <swi@altlinux.ru> 2.4.7-alt1
- new version

* Sun Mar 20 2011 Alexey Morsov <swi@altlinux.ru> 2.4.4-alt1
- new version
- add zlib-devel

* Sat Mar 12 2011 Alexey Morsov <swi@altlinux.ru> 2.4.3-alt1
- new version

* Fri Feb 11 2011 Alexey Morsov <swi@altlinux.ru> 2.4.2-alt1
- new version

* Tue Jan 11 2011 Alexey Morsov <swi@altlinux.ru> 2.4.0-alt2.1
- clean spec
- build with sql backends

* Tue Jan 11 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt2
- add virtual package for quotes fetching
- fix perl module name (thanks Alexey Morsov)

* Fri Jan 07 2011 Alexey Morsov <swi@altlinux.ru> 2.4.0-alt1
- new version
- spec clean up
- remove unneeded patches

* Thu Apr 22 2010 Andrey Cherepanov <cas@altlinux.org> 2.2.9-alt4
- fix requirements for build in Sisyphus

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt3
- restore post/postun for gconf (fix bug #21627)

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt2
- build with guile18
- fix build with goffice

* Thu May 21 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt1
- new version 2.2.9 (with rpmrb script)

* Thu Dec 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt2
- rebuild with new libofx 0.9.0
- remove post/postun sections
- fix files listed twice

* Sat Oct 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt1
- new version 2.2.7 (with rpmrb script)
- update buildreqs

* Tue Sep 09 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.6-alt1
- new version 2.2.6 (with rpmrb script)

* Thu Jul 31 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.5-alt2
- rebuild with libgnomeoffice 0.7
- add install/uninstall_info

* Thu May 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.5-alt1
- new version 2.2.5 (with rpmrb script)

* Thu Apr 03 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt2
- really fix filenames handling (bug #14694)

* Sat Mar 08 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- new version 2.2.4 (with rpmrb script)
- fix gconf schemas installing (thanks to Yury Aliaev)

* Thu Feb 28 2008 Yury Aliaev <mutabor@altlinux.ru> 2.2.3-alt2
- fixed filenames handling in non-utf8 locales

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)
- use new icons from tarball

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- build release 2.2.2
- rebuild with libgnomeoffice 0.6

* Tue Dec 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt0.1svn
- build from svn r16633
- rebuild with libgnomeoffice 0.5
- cleanup spec

* Fri Sep 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sat Jun 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)
- rebuild with new libgnomeoffice 0.4

* Sun Apr 29 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)
- bzip Changelogs

* Thu Apr 19 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)

* Fri Dec 29 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt0.2
- build with external qof

* Sat Dec 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt0.1
- new version 2.0.3 (with rpmrb script)

* Sat Dec 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1.1
- rebuild with internal libgnomeoffice

* Wed Oct 18 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- update buildreq

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt0.1
- new version 2.0.2 (with rpmrb script)

* Sun Jul 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new stable release 2.0.0 (fix bug #9823))
- add missed libdir/gnucash

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060521
- new build from SVN (r14146)

* Fri May 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060512
- new build from SVN (r14029)

* Fri Apr 14 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060414
- new build from SVN (r13773)
- double make for build error workaround

* Mon Jan 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060123
- new build from SVN (r12926), russian translation updated
- NOTE: convert your old gnucash files with conv_gnucash2.sh script

* Wed Dec 01 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1cvs20041201
- first build with GNOME2 (for developing purposes ONLY)
- use a macro for ldconfig

* Sun May 23 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt2
- build with rebuilt gnome1 libraries
- remove python requiring

* Wed Apr 28 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt1
- new version
- applied full diff patch from debian unstable (due dlopen problem)

* Wed Jan 14 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt3
- update ru.po
- move .so files from -devel to libgnucash for dynamic linking purposes
- change require python to universal way (without version)
- remove COPYING from doc

* Sat Jan 03 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt2
- build without *.la files
- build with gcc3.3
- disable guppi support

* Thu Dec 04 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt1
- new version
- build with Guppi
- add autostart gconfd-1 before gnucash in start script

* Mon Oct 06 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- new version
- disable autoreq for perl and set it manually

* Sun Jun 22 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version

* Mon Mar 24 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version
- postgres backend enabled
- update russian translation

* Sun Jan 26 2003 Vitaly Lipatov <lav@altlinux.ru> 1.7.8-alt1
- new version

* Mon Jan 06 2003 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version
- Warning: Be careful with RUB currency (use RUR instead) in your file.
- update russian translation
- postgres disabled via build problems
- add needed binaries in file section
- add README_koi8-r.txt
- cleanup spec

* Sat Dec 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- gnucash-devel rename to libgnucash-devel
- spec cleanup
- add Postgres support package (untested)
- new version
- update ru.po

* Mon Nov 04 2002 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt2
- remove dependences on libtermcap
- update russian translation

* Fri Nov 01 2002 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version
- spec updated

* Mon Feb 18 2002 AEN <aen@logic.ru> 1.6.5-alt3
- ru.po updates from Vitaly Lipatov

* Tue Jan 22 2002 AEN <aen@logic.ru> 1.6.5-alt2
- rebuilt with new Guppi

* Mon Jan 14 2002 AEN <aen@logic.ru> 1.6.5-alt1
- new version

* Wed Dec 05 2001 AEN <aen@logic.ru> 1.6.4-alt5
- rebuilt with gtkhtml-1.0.0

* Wed Nov 21 2001 AEN <aen@logic.ru> 1.6.4-alt4
- rebuild with libguppi-0.40.2

* Fri Nov 09 2001 AEN <aen@logicru> 1.6.4-alt3
- rebuilt with new gal

* Thu Nov 1 2001 AEN <aen@logic.ru> 1.6.4-alt2
- rebuild in new environment

* Fri Oct 12 2001 AEN <aen@logic.ru> 1.6.4-alt1
- new version

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Tue Oct 24 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.8-1mdk
- new version 1.4.8
- added buildconflicts with libxml2-devel

* Mon Oct  9 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.7-2mdk
- added /usr/lib/gnucash/perl/* library files
- added la files in devel
- added man pages
- added requirement in devel
- gnucash.so is needed in the *normal* package because of swig
- moved libgncengine.so from devel to normal, just in case...

* Mon Oct  2 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.7-1mdk
- new version

* Tue Sep 12 2000  <rchaillat@bi.mandrakesoft.com> 1.4.6-1mdk
- new version

* Thu Aug 31 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.5-2mdk
- added comment about g-wrap
- added menu file

* Wed Aug 30 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.5-1mdk
- went back to stable releases
- macroszification
- corrected icons
- added some more BuildRequires (xpm, guile-devel)
- specfile clean-up
- split application and devel packages

* Fri Jul 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.5.0-1mdk
- Updated version

* Tue Jul 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.4.2-3mdk
- Repaired missing libs

* Mon Jul 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.4.2-1mdk
- Updated version / release 2 hours ago.

* Sat Jul 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.4.1-1mdk
- Updated version

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.1-5mdk
- Give full path when using convert.
- BuildPrereq: /usr/bin/convert.
- Regenerate libtoolize everywhere there is a configure.
- BuildRequires: eperl swig.

* Mon Apr 10 2000 Francis Galiegue <fg@mandrakesoft.com> 1.3.1-4mdk

- Patched to compile with perl 5.6.0

* Wed Mar 22 2000 Francis Galiegue <fg@mandrakesoft.com> 1.3.1-3mdk

- Icon for menu entry
- Rebuilt on kenobi

* Mon Mar 13 2000 Francis Galiegue <francis@mandrakesoft.com> 1.3.1-2mdk

- Menu'ized, changed group to Office (was: Applications/Finance)

* Mon Mar 13 2000 Francis Galiegue <francis@mandrakesoft.com>

- First RPM for Mandrake

* Mon Feb 29 2000 Christian Schaller <Uraues@linuxrising.org>
- Updated for use with TurboLinux and some minor SPEC changes
