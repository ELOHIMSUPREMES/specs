# clang 4.0.1 is not supported, only missing clang 3.9
%def_without ClangCodeModel

%add_findreq_skiplist *gdbmacros*
%add_python_req_skip lldb
%add_findreq_skiplist %_datadir/qtcreator/templates/wizards/classes/python/file.py

Name:    qt-creator
Version: 4.4.1
Release: alt1
Summary: Cross-platform IDE for Qt

Group:   Development/Tools
License: LGPLv2 with exceptions or LGPLv3 with exceptions
Url:     http://qt-project.org/wiki/Category:Tools::QtCreator
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
# VCS:   git://code.qt.io/qt-creator/qt-creator.git
Source1: qtcreator.desktop
Source2: qtcreator.appdata.xml

Patch:   %name-%version-%release.patch
Patch1:  qt-creator_ninja-build.patch

Requires: %name-data = %version-%release
Provides: qtcreator = %version-%release

BuildRequires(pre): qt5-base-devel >= 5.5.0
BuildRequires: gcc-c++ 
BuildRequires: qt5-designer >= 5.5.0
BuildRequires: qt5-script-devel >= 5.5.0
BuildRequires: qt5-webkit-devel >= 5.5.0
BuildRequires: qt5-x11extras-devel >= 5.5.0
BuildRequires: qt5-xmlpatterns-devel >= 5.5.0
BuildRequires: qt5-tools-devel >= 5.5.0
BuildRequires: libbotan-devel
%if_with ClangCodeModel
BuildRequires: llvm4.0-devel
BuildRequires: clang4.0-devel
%endif

Requires: qt5-quickcontrols

%description
Qt Creator (previously known as Project Greenhouse) is a new,
lightweight, cross-platform integrated  development environment (IDE)
designed to make development with the Qt application framework
even faster and easier.

%package doc
Summary: %name docs
Group: Documentation
BuildArch: noarch
Requires: %name
Requires: libqt4-sql-sqlite

%description doc
Documentation for %name

%package data
Summary: Data files for %name
Group: Development/Tools
BuildArch: noarch
Requires: %name

%description data
Data files for %name

%prep
%setup
subst 's,tools\/qdoc3,bin,' doc/doc.pri
#subst 's,share\/doc\/qtcreator,share\/qtcreator\/doc,' doc/doc.pri src/plugins/help/helpplugin.cpp
%patch -p1
%patch1 -p1

%build
export QTDIR=%_qt5_prefix
export PATH="%{_qt5_bindir}:$PATH"
%if_with ClangCodeModel
export LLVM_INSTALL_DIR="%_prefix"
%endif
%qmake_qt5 -r IDE_LIBRARY_BASENAME=%_lib USE_SYSTEM_BOTAN=1 CONFIG+=disable_rpath
NPROCS=1
%make_build
%make_build qch_docs

%install
%install_qt5 INSTALL_ROOT=%buildroot/%_prefix

mkdir -p %buildroot%_desktopdir
install %SOURCE1 %buildroot%_desktopdir

mkdir -p %buildroot%_datadir/qtcreator/translations
cp share/qtcreator/translations/*.qm %buildroot%_datadir/qtcreator/translations

for i in 16 24 32 48 64 128 256 512; do
    install -pD -m644 src/plugins/coreplugin/images/logo/${i}/QtProject-qtcreator.png \
                      %buildroot%_iconsdir/hicolor/${i}x${i}/apps/QtProject-qtcreator.png
#    mkdir -p %buildroot%_iconsdir/hicolor/${i}x${i}/apps
#    ln -s %_pixmapsdir/qtcreator_logo_${i}.png \
#          %buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done

install -Dpm0644 %SOURCE2 %buildroot%_datadir/appdata/qtcreator.appdata.xml

%install_qt5 INSTALL_ROOT=%buildroot/%_prefix install_inst_qch_docs

# Remove Windows cdb debugger support to prevent unmet python2.7(cdbext)
rm -f %buildroot%_datadir/qtcreator/debugger/cdbbridge.py

%files
%doc README* LICENSE*
%_bindir/*
%_libdir/qtcreator
%_prefix/libexec/qtcreator
%_iconsdir/hicolor/*/apps/QtProject-qtcreator.png
%_desktopdir/qtcreator.desktop
%_datadir/appdata/qtcreator.appdata.xml

%files doc
%_defaultdocdir/qtcreator

%files data
%dir %_datadir/qtcreator
%_datadir/qtcreator/*

%changelog
* Fri Oct 06 2017 Andrey Cherepanov <cas@altlinux.org> 4.4.1-alt1
- New version
- Add optional build ClangCodeModel plugin (disabled by default)

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1
- New version

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version

* Thu May 25 2017 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version

* Sun Apr 23 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version

* Tue Jan 24 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- new version 4.2.1

* Sat Dec 17 2016 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- new version 4.2.0
- provides qtcreator
- remove Windows cdb debugger support to prevent unmet python2.7(cdbext)

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- new version 4.1.0

* Sun Jun 19 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- new version 4.0.2

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- new version 4.0.1

* Fri May 13 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version

* Tue Mar 29 2016 Sergey V Turchin <zerg@altlinux.org> 3.6.0-alt1.1
- NMU: Rebuild with new Qt5

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version
- Build with Qt5 (closes #31175)

* Fri Feb 07 2014 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.1-alt1
- update to newest version with multiple improvements

* Sun Feb 02 2014 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.1-alt1
- update to new version (closes #29569)

* Thu Apr 11 2013 Anatoly Lyutin <vostok@altlinux.org> 2.7.0-alt1
- new version (closes #28740)

* Tue Dec 18 2012 Anatoly Lyutin <vostok@altlinux.org> 2.6.0-alt2
- true 2.6.0 (closes #28152)

* Mon Nov 26 2012 Anatoly Lyutin <vostok@altlinux.org> 2.6.0-alt1
- new version (closes #27938)

* Fri May 11 2012 Anatoly Lyutin <vostok@altlinux.org> 2.5.0-alt1
- new version

* Mon Jan 09 2012 Anatoly Lyutin <vostok@altlinux.org> 2.4.0-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt1.1
- Rebuild with Python-2.7

* Thu Sep 22 2011 Anatoly Lyutin <vostok@altlinux.org> 2.3.0-alt1
- new version (closes #26219)

* Fri Aug 05 2011 Anatoly Lyutin <vostok@altlinux.org> 2.2.1-alt1
- new version

* Mon Jun 06 2011 Anatoly Lyutin <vostok@altlinux.org> 2.2.0-alt1
- update to 2.2.0

* Fri Mar 04 2011 Anatoly Lyutin <vostok@altlinux.org> 2.1.0-alt1
- update to 2.1.0

* Wed Jul 28 2010 Anatoly Lyutin <vostok@altlinux.org> 2.0.0-alt1
- update to 2.0.0

* Mon Mar 01 2010 Boris Savelev <boris@altlinux.org> 1.3.1-alt1
- new version

* Tue Dec 15 2009 Boris Savelev <boris@altlinux.org> 1.3.0-alt1
- new version (closes: #22547)

* Sun Aug 30 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt3.g26a3a3e
- build from upstream git

* Wed Aug 05 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt2.g0dbe82f
- new version

* Thu Jul 16 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt1.gba2a5a6
- new version

* Tue Jun 30 2009 Boris Savelev <boris@altlinux.org> 1.2.0-alt2.g6315f14
- build from upstream git
- add translations (closes:#20605)

* Fri Jun 26 2009 Boris Savelev <boris@altlinux.org> 1.2.0-alt1.g934ee44
- version up

* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt6.gcf7cd73
- add %_bindir/qtcreator_process_stub (fix #20171)

* Mon May 11 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt5.gcf7cd73
- build from upstream git

* Sun May 03 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt4.ga1dc8f5
- build from upstream git

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt3.git.124.g092d8ca
- build from upstream git

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt2
- build doc (fix #19799)

* Thu Apr 23 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt1
- initial build for Sisyphus from Fedora

* Tue Mar 20 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-4
- fix lib's loading in 64 bit machines

* Tue Mar 18 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-3
- Changed License to LGPLv2 with exceptions and BR to qt4-devel >= 4.5.0

* Tue Mar 17 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-2
- Improved Version to make it more compatible with fedora guidelines

* Sun Mar 15 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-1
- initial RPM release
