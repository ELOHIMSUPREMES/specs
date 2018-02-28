%define rname oxygen-icons5

Name: kf5-oxygen-icons
Version: 5.37.0
Release: alt1%ubt
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: Oxygen icons theme
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

BuildArch: noarch

Source: %rname-%version.tar
Patch1: alt-icons-defaults.patch

# Automatically added by buildreq on Fri Dec 11 2015 (-bi)
# optimized out: cmake cmake-modules gtk-update-icon-cache libqt5-core libstdc++-devel perl-Encode perl-XML-LibXML perl-XML-SAX perl-XML-SAX-Base perl-XML-Simple perl-parent python-base python3 python3-base
#BuildRequires: extra-cmake-modules gcc-c++ icon-naming-utils qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: icon-naming-utils

%description
%summary

%package -n icon-theme-oxygen
Summary: Oxygen icons theme
Group: Graphics
Provides: kde4-icon-theme-oxygen = %version-%release
Provides: kde4-icon-theme = %version-%release
Conflicts: kde4base-workspace-core <= 4.11.22-alt4
Conflicts: kde4pim-core <= 4.14.10-alt4
%description -n icon-theme-oxygen
%summary


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install

# 6971
for t in %buildroot/%_iconsdir/* ; do
    [ -d $t ] || continue
    pushd $t
	ls -1d * | \
	while read sz ; do
	    [ -d $sz ] || continue
	    pushd $sz
	    ls -1d * | \
	    while read ctx ; do
		[ -d $ctx ] || continue
		%_libexecdir/icon-name-mapping -c $ctx
	    done
	    popd
	done
    popd
done

# fix broken symlinks
find %buildroot/%_iconsdir -type l | \
while read l ; do
    [ -e $l ] || rm -f $l
done

%files -n icon-theme-oxygen
%_iconsdir/oxygen*/

%changelog
* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt1%ubt
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1%ubt
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.35.0-alt1%ubt
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.34.0-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.33.0-alt1%ubt
- new version

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.32.0-alt1%ubt
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.31.0-alt1%ubt
- new version

* Wed Feb 08 2017 Sergey V Turchin <zerg@altlinux.org> 5.30.0-alt1%ubt
- new version

* Tue Dec 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.29.0-alt1%ubt
- new version

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt0.M80P.1
- build for M80P

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt1
- new version

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt0.M80P.1
- build for M80P

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt2
- don't increase main toolbar icons by default

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt1
- new version

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt1
- new version

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt1
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.22.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.21.0-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- initial build
