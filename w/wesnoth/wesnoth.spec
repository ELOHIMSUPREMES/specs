%define _unpackaged_files_terminate_build 1
%def_with build_using_scons
%def_with install_using_scons
%def_without install_using_manual
%def_without install_using_cmake
# remnants of configure, drop them later
%def_enable nls
%def_enable rpath
%def_disable debug
%def_disable tests
%def_disable static
%def_enable python
%def_enable optipng
%def_enable game
%def_enable server
%def_enable editor
%def_enable tools
%def_enable display_revision
%def_enable bandwidth_monitor
%def_enable sdltest
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%define _pseudouser_user     _wesnothd
%define _pseudouser_group    _wesnothd
%define _pseudouser_home     %_var/run/wesnothd

Name: wesnoth
Version: 1.10.7
Release: alt1
Group: Games/Strategy
Summary: 2D fantasy turn-based strategy
Summary(ru_RU.UTF-8): двухмерная пошаговая стратегия в стиле фэнтези
License: %gpl2plus
Url: http://www.%name.org
Source0: %name-%version.tar
Source1: %{name}d.init
Source2: %{name}d.service
Source3: %{name}.sysconfig

Requires: %name-data = %version-%release

BuildRequires(pre): rpm-build-licenses

BuildRequires: ImageMagick-tools asciidoc boost-devel desktop-file-utils fribidi gcc-c++ hd2u imake libICE-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel libfreetype-devel libfribidi-devel libpango-devel libpng-devel po4a subversion xorg-cf-files xsltproc liblua5-devel libpng-devel cmake boost-program_options-devel libdbus-devel boost-asio-devel libpixman-devel libXdmcp-devel
%if_with build_using_scons
BuildRequires: scons
%endif

BuildRequires: fonts-ttf-dejavu fonts-ttf-sazanami-gothic fonts-ttf-wqy-zenhei
BuildRequires: python-devel
%{?_enable_tools:BuildRequires: perl(Tie/File.pm)}
%{?_enable_optipng:BuildRequires: optipng}
%{?_enable_display_revision:BuildRequires: subversion}

Requires: python-module-%name = %version-%release

%description
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.

%description -l ru_RU.UTF-8
'Битва за Вэснот' это пошаговая стратегия в стите фэнтези.
Сражайся за контроль над деревнями, используя различные войска,
которые имеют свои преимущества и недостатки на разных типах
территорий и против разных типов атак. Войска получают опыт и повышают
уровни, переносимые на следующий сценарий в кампании.
Создай Героя и возглавь свою армию. Различные расы с различными
способностями, оружием и заклинаниями.


%package data
Group: Games/Strategy
Summary: Data files to Battle for Wesnoth
BuildArch: noarch
Conflicts: %name < 1.6.5-alt1
Conflicts: %name-editor < 1.10.3

%description data
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains data files to Battle for Wesnoth.


%package doc
Group: Documentation
Summary: Manual to Battle for Wesnoth
Provides: %name-manual = %version-%release
BuildArch: noarch

%description doc
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains manual to Battle for Wesnoth.


%if_enabled editor
%package editor
Group: Games/Strategy
Summary: Battle for Wesnoth map editor
BuildArch: noarch
#
%description editor
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains Battle for Wesnoth map editor.
%endif


%if_enabled tools
%package tools
Group: Games/Strategy
Summary: Battle for Wesnoth tools

%description tools
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains Battle for Wesnoth tools.
%endif


%if_enabled server
%package server
Group: Games/Strategy
Summary: %name server for multiplayer games
Summary(ru_RU.UTF-8): %name сервер для многопользовательских игр

%description server
Battle for Wesnoth multiplayer network daemon.

%description server -l ru_RU.UTF-8
Сервер для многопользовательских игр 'Битва за Вэснот'.
%endif

%if_enabled python
%package -n python-module-%name
%py_provides %name
Group: Development/Python
Summary: Python interface to Battle for Wesnoth
BuildArch: noarch

%description -n python-module-%name
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains python interface to Battle for Wesnoth.
%endif

%prep
%setup

%build
%define _optlevel 3
# note for 1.10.5 - outdated.
# evil, evil... configure does not work, cmake does not build translations,
# scons does not build schema_validator
# note for 1.10.7 - upstream really moved to scons.
# scons now works. cmake is outdated and does not build campaignd.
%if_with build_using_scons
scons all prefix=%{_prefix} \
          bindir=%{_bindir} \
          libdir=%{_libdir} \
          python_site_packages_dir=%{python_sitelibdir_noarch}/%{name} \
          extra_flags_release="%optflags" \
          %{?_smp_mflags}

	  # let it be default - translations - for now, for cmake install compatibility
	  #localedirname=locale \
scons schema_generator
#no more built in scons
#scons schema_validator
%else
export PYTHON_PREFIX=/usr
export PYTHON_VERSION=%__python_version
#%%configure \
#    --disable-option-checking \
#    --with-gnu-ld \
#    %{subst_enable nls} \
#    %{subst_enable rpath} \
#    %{subst_enable debug} \
#    %{subst_enable tests} \
#    %{subst_enable static} \
#    %{subst_enable python} \
#    %{subst_enable optipng} \
#    %{subst_enable game} \
#    %{subst_enable server} \
#    %{subst_enable editor} \
#    %{subst_enable tools} \
#    %{subst_enable_to display_revision display-revision} \
#    %{subst_enable sdltest} \

cmake . \
	-DCMAKE_INSTALL_PREFIX=%buildroot%_prefix \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	-DDATAROOTDIR=%_datadir \
	-DBINDIR=%_bindir \
	-DENABLE_TOOLS=ON \
	-DENABLE_NLS=ON \
 	-DGETTEXT_FOUND=ON \
 	-DENABLE_STRICT_COMPILATION=OFF \
	-DCMAKE_INSTALL_PREFIX=%buildroot

%make_build VERBOSE=1
%endif # scons

for s in 96 72 48 36 32 24 22 16; do
    convert -depth 8 -resize ${s}x$s icons/%name-{icon-Mac,$s}.png
    convert -depth 8 -resize ${s}x$s icons/{map-editor-icon-Mac,%{name}_editor-$s}.png
done
bzip2 --keep --best --force changelog

%install

%if_with install_using_cmake
# cmake install
%make_install \
    DESTDIR=%buildroot \
    docdir=%_docdir/%name-%version \
    appentrydir=%_desktopdir \
    install
%else

%if_with install_using_scons
# scons install
scons install install-pytools destdir=$RPM_BUILD_ROOT
rm %buildroot%{_datadir}/icons/wesnoth-icon.png
rm %buildroot%_desktopdir/wesnoth.desktop
rm -rf %buildroot/%python_sitelibdir_noarch/wesnoth
install -m 755 schema_generator %buildroot%_bindir/
%endif

%if_with install_using_manual
# manual install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sbindir
for i in cutter exploder wesnoth; do
        cp -p $i %buildroot%_bindir/
done
cp wesnothd %buildroot%_sbindir/
cp campaignd %buildroot%_sbindir/
mkdir -p %buildroot%{_datadir}/wesnoth
for i in data fonts icons images sounds translations l10n-track; do
        cp -pr $i %buildroot%{_datadir}/wesnoth/
done
%endif

#if with install_using_manual || with install_using_scons
# emulate cmake install
desktop-file-install --dir %buildroot%_desktopdir \
                     --mode="0644" \
                     --remove-key="Version" \
                     icons/%{name}.desktop icons/%{name}_editor.desktop
mkdir -p %buildroot%{_datadir}/pixmaps
cp icons/%{name}-icon.png %buildroot%{_datadir}/pixmaps
cp icons/%{name}_editor-icon.png %buildroot%{_datadir}/pixmaps
mkdir -p %buildroot%_docdir/
cp -a doc/manual %buildroot%_docdir/%name
%endif

install -d -m 0755 %buildroot%_sbindir
[ -e %buildroot%_bindir/%{name}d ] && mv %buildroot{%_bindir,%_sbindir}/%{name}d
[ -e %buildroot%_bindir/campaignd ] && mv %buildroot{%_bindir,%_sbindir}/campaignd

%if_enabled tests
mv %buildroot%_bindir/{,%name-}test
%endif

mkdir -p %buildroot/%python_sitelibdir_noarch
mv %buildroot%_datadir/%name/data/tools/wesnoth %buildroot/%python_sitelibdir_noarch
mv %buildroot%_datadir/%name/data/tools/addon_manager %buildroot/%python_sitelibdir_noarch
mv %buildroot%_datadir/%name/data/tools/unit_tree %buildroot/%python_sitelibdir_noarch

pushd data
pushd tools
for i in wesnoth_addon_manager wml*; do
    cp $i %buildroot/%_bindir/
done
popd
popd

mkdir -p %buildroot%_docdir/%name-%version/manual
mv %buildroot%_docdir/%name/* %buildroot%_docdir/%name-%version/manual/
install -m 0644 README copyright changelog.* %buildroot%_docdir/%name-%version/
install -d -m 0755 %buildroot%_iconsdir/hicolor/64x64/apps
mv %buildroot{%_pixmapsdir/%name-icon,%_iconsdir/hicolor/64x64/apps/%name}.png
mv %buildroot{%_pixmapsdir/%{name}_editor-icon,%_iconsdir/hicolor/64x64/apps/%{name}_editor}.png
install -D -m 0644 {icons/%name-icon-Mac,%buildroot%_iconsdir/hicolor/128x128/apps/%name}.png
install -D -m 0644 {icons/map-editor-icon-Mac,%buildroot%_iconsdir/hicolor/128x128/apps/%{name}_editor}.png
for s in 96 72 48 36 32 24 22 16; do
    install -D -m 0644 {icons/%name-$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name}.png
    install -D -m 0644 {icons/%name-$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%{name}_editor}.png
done
install -D -m 755 %SOURCE1 %buildroot%_initdir/%{name}d
install -D -m 644 %SOURCE2 %buildroot%_unitdir/wesnothd.service
install -D -m 644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/wesnoth


%find_lang --with-man %name
%find_lang --with-man %{name}d

for d in %buildroot%_datadir/%name/translations/*; do
    l=$(basename "$d")
    c=${l:0:2}
    echo "%%lang($c) %%dir %_datadir/%name/translations/$l" >> %name.lang
    echo "%%lang($c) %%dir %_datadir/%name/translations/$l/LC_MESSAGES" >> %name.lang
    [ -f $d/LC_MESSAGES/%name.mo ] && echo "%%lang($c) %_datadir/%name/translations/$l/LC_MESSAGES/%name.mo" >> %name.lang
    for i in anl aoi did dm editor ei httt l lib low multiplayer nr sof sotbe tb test thot trow tsg tutorial units utbs dw help manpages manual; do
	[ -f $d/LC_MESSAGES/%name-$i.mo ] && echo "%%lang($c) %_datadir/%name/translations/$l/LC_MESSAGES/%name-$i.mo" >> %name.lang
    done
done
for f in %buildroot%_datadir/%name/data/languages/*_*.cfg; do
    l=$(basename "$f")
    echo "%%lang(${l:0:2}) %_datadir/%name/data/languages/$l" >> %name.lang
done
#    /usr/share/wesnoth/data/languages/racv.cfg
echo "%%lang(racv) %_datadir/%name/data/languages/racv.cfg" >> %name.lang
#    /usr/share/wesnoth/data/languages/en@shaw.cfg
echo "%%lang(en) %_datadir/%name/data/languages/en@shaw.cfg" >> %name.lang

rm -rf %buildroot%_datadir/%name/icons
rm -f %buildroot%_datadir/%name/fonts/DejaVuSans.ttf
ln -s %_datadir/fonts/ttf/dejavu/DejaVuSans.ttf %buildroot%_datadir/%name/fonts/
# sazanami-fonts-gothic
ln -s %_datadir/fonts/ttf/sazanami/gothic/sazanami-gothic.ttf %buildroot%_datadir/%name/fonts/sazanami-gothic.ttf
# wqy-zenhei-fonts
ln -s %_datadir/fonts/ttf/wqy-zenhei/wqy-zenhei.ttc %buildroot%_datadir/%name/fonts/wqy-zenhei.ttc


sed -i 's/wesnoth-icon/wesnoth/' %buildroot%_desktopdir/%name.desktop
%if_enabled editor
sed -i 's/wesnoth_editor-icon/wesnoth_editor/' %buildroot%_desktopdir/%{name}_editor.desktop
%endif

%if_enabled server
%pre server
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'Wesnoth server' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%preun server
%preun_service %{name}d

%post server
%post_service %{name}d
%endif

%files
%_bindir/%name
%_bindir/wesnoth_addon_manager

%files data -f %name.lang
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/copyright
%doc %_docdir/%name-%version/changelog.* 
%dir %_datadir/%name
%_datadir/%name/fonts
%_datadir/%name/images
%_datadir/%name/sounds
%dir %_datadir/%name/translations
%dir %_datadir/%name/data
%_datadir/%name/data/COPYING.txt
%_datadir/%name/data/ai/
%_datadir/%name/data/campaigns
%_datadir/%name/data/core
%_datadir/%name/data/gui/
%_datadir/%name/data/hardwired
%_datadir/%name/data/multiplayer
%_datadir/%name/data/themes
%_datadir/%name/data/lua
%_datadir/%name/data/test
%_datadir/%name/data/*.cfg
%dir %_datadir/%name/data/languages
%_datadir/%name/l10n-track
%_man6dir/%name.6*

%files doc
%dir %_docdir/%name-%version
%_docdir/%name-%version/manual

%if_enabled editor
%files editor
%_desktopdir/%{name}_editor.desktop
%_iconsdir/hicolor/*/apps/%{name}_editor.png
%endif

%if_enabled tools
%files tools
%_bindir/cutter
%_bindir/exploder
%_bindir/schema_generator
%if_with build_using_scons
%else
%_bindir/schema_validator
%endif
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/tools
%{?_enable_tests:%_bindir/%name-test}
%{?_enable_python:%_bindir/wml*}
%endif

%if_enabled server
%files server -f %{name}d.lang
%_sbindir/%{name}d
%_sbindir/campaignd
%_initdir/%{name}d
%_unitdir/%{name}d.service
%config(noreplace) %_sysconfdir/sysconfig/wesnoth
%_man6dir/%{name}d.6*
%endif

%if_enabled python
%files -n python-module-%name
%python_sitelibdir_noarch/wesnoth
%python_sitelibdir_noarch/addon_manager
%python_sitelibdir_noarch/unit_tree
%endif

%changelog
* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.10.7-alt1
- new version
- use scons for build
- native systemd support
- wesnothd is now run under _wesnothd pseudo user.

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.10.5-alt1
- update to 1.10.5
- linked sazanami fonts
- added missing optional BR: libpixman-devel libXdmcp-devel
- fixed localization packaging (closes: 28689)
- note: #28689 was introduced in 1.10.2-alt1.1 by using cmake.
  tried to fix it using scons, but due to lack of schema_validator,
  used -DGETTEXT_FOUND=ON cmake hack

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1.1
- Rebuilt with Boost 1.52.0

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.2-alt1
- 1.10.2

* Thu Mar 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Jan 30 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Fri Jan 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.4-alt1
- 1.9.4 (1.10-rc1)

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.6-alt2
- rebuild with boost-1.47

* Tue May 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.5-alt3
- build repaired

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.5-alt2
- rebuild with boost-1.45

* Tue Sep 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.5-alt1
- 1.8.5

* Fri Aug 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Fri Jul 09 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Mon Jun 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Fri May 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Sat Apr 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt1
- 1.8.0 (ALT #23272)

* Tue Mar 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt3
- Enable fullscreen by default to hide (ALT #23150)
- Add condstop to wesnothd.init

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt2.1
- Rebuilt with python 2.6

* Thu Oct 08 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt2
- add conflict with old package to data subpackage

* Thu Sep 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Sun Dec 28 2008 Led <led@altlinux.ru> 1.4.7-alt1.2
- add subpackage ais

* Sat Dec 27 2008 Led <led@altlinux.ru> 1.4.7-alt1.1
- cleaned up spec

* Fri Dec 19 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Mon Oct 27 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.0-alt2
- rebuild
- update requires

* Mon Mar 17 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.4.0-alt1
- new stable release

* Thu Feb 28 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.16-alt2
- boost depend added

* Wed Feb 20 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.16-alt1
- new development version

* Fri Nov 30 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.3.11-alt1
- new development version

* Wed Sep 26 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.3.7-alt1
- new version

* Mon Jun 04 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.3.3-alt1
- new version

* Fri Jan 19 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.2.1-alt1
- new version
- 10449 fix

* Fri Dec 15 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.13-alt1
- new version

* Tue Oct 10 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.11-alt1
- new version

* Tue Oct 03 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.10-alt1
- new version
- use fribidi

* Thu Jun 29 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.7-alt1
- new version

* Tue May 23 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.2-alt1
- new version

* Fri Dec 09 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0.2-alt1
- new version

* Wed Oct 26 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0.1-alt1
- new verison

* Mon Oct 10 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0-alt3
- added .spec

* Fri Oct 07 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0-alt2
- temporary removed soundwrapper
- long title fixed

* Tue Oct 04 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0-alt1
- 1.0 release

* Mon Aug 22 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.5-alt1
- new upstream version

* Tue Jul 26 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.4-alt1
- new upstream version

* Tue Jul 12 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.3-alt1
- user interface improvements
- updated translations and documentation
- campaigns and units fixing and balancing
- some new unit and terrains graphics

* Thu Jun 09 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.2-alt1
- lots of improvements in the user interface.
- several bugs in campaigns have already been fixed and
  lots of new death animations.
- the Drakes get reinforcements, with their new level 3 units.
- there are also a great number of changes regarding
  multiplayer balancement and most multiplayer maps have
  been replaced by new ones.

* Wed May 04 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.1-alt1
- New upstream version
- Many bugs have been fixed

* Wed Apr 13 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.0-alt1
- new release
- init script for server

* Tue Mar 01 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.8.11-alt1
- new bugfix release

* Tue Feb 08 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.8.10-alt1
- new release

* Wed Jan 26 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.8.9-alt1
- new version

* Mon Oct 18 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.8-alt2
- menu group fixed

* Tue Jul 06 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.8-alt1
- new version

* Mon May 03 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.7-alt2
- glibc 2.3 build

* Wed Mar 24 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.7-alt1
- Ver 0.7
- New maps, new units, new music. A lot of fixes and improvements

* Fri Jan 30 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.6.1-alt1
- ver 0.6.1.

* Thu Jan 29 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.4.8-alt1
- ALT adaptations.

