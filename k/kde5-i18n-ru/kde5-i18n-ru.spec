
%define lng ru
%define lngg Russian

Name: kde5-i18n-%lng
Version: 15.08.1
Release: alt1

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE
License: GPL
Url: http://www.kde.org/

Requires: kf5-filesystem
BuildArch: noarch

Source: kde-l10n-%lng-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libdb4-devel qt5-tools-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel

%description
%lngg language support for KDE.


%prep
%setup -q -n kde-l10n-%lng-%version
rm -rf 4 CMakeLists.txt
mv 5/%lng/* ./
rm -rf 5

find -type f -name CMakeLists.txt | \
while read cm; do
    dirs=`grep add_subdirectory "$cm" | sed 's|.*[(]\(.*\)[)].*|\1|'`
    if [ -n "$dirs" ]; then
	pushd `dirname "$cm"`
	for d in $dirs; do
	    mkdir -p $d
	done
	popd
    fi
done



%build
%K5build


%install
%K5install
%K5install_move data locale doc klettres katepart apps

%files
%dir %_K5doc/%lng/
%lang(%lng) %_K5doc/%lng/*
#
%dir %_K5i18n/%lng/
#%_K5i18n/%lng/entry.desktop
#
%dir %_K5i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K5i18n/%lng/LC_MESSAGES/*.mo
%lang(%lng) %_K5i18n/%lng/LC_MESSAGES/*.qm
#%dir %_K5i18n/%lng/LC_SCRIPTS/
#%lang(%lng) %_K5i18n/%lng/LC_SCRIPTS/*
#
%lang(%lng) %_K5data/apps/kvtml/%lng/
#%lang(%lng) %_K5data/ktuberling/sounds/%lng
#%lang(%lng) %_K5data/ktuberling/sounds/%lng.soundtheme
#%lang(%lng) %_K5data/khangman/%lng.txt
%lang(%lng) %_K5data/klettres/%lng
%lang(%lng) %_K5data/katepart/syntax/logohighlightstyle.%lng.xml
#%lang(%lng) %_K5data/kturtle/data/logokeywords.%lng.xml
#%lang(%lng) %_K5data/kturtle/examples/%lng/
#%lang(%lng) %_K5data/autocorrect/%{lng}_*.xml

%changelog
* Thu Oct 01 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Mon Aug 24 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Tue Jul 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- new version

* Mon Apr 27 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- initial build
