%define rname oxygen-icons5

Name: kf5-oxygen-icons
Version: 5.23.0
Release: alt1
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
BuildRequires(pre): rpm-build-kf5
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
