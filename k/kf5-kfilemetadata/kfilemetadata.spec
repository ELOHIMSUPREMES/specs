%define rname kfilemetadata

%def_enable exiv2

Name: kf5-%rname
Version: 5.3.2
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Workspace 5 extracting text and metadata from different files
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 26 2015 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig libavcodec-devel libavutil-devel libcloog-isl4 libopencore-amrnb0 libopencore-amrwb0 libpoppler1-qt5 libqt5-core libqt5-gui libqt5-xml libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: ebook-tools-devel extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-ki18n-devel libavdevice-devel libavformat-devel libexiv2-devel libpoppler-qt5-devel libpostproc-devel libswscale-devel libtag-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-karchive-devel kf5-ki18n-devel
BuildRequires: ebook-tools-devel libpoppler-qt5-devel libtag-devel
%if_enabled exiv2
BuildRequires: libexiv2-devel
%endif
BuildRequires: libattr-devel
BuildRequires: libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel

%description
KFileMetaData provides a simple library for extracting the text and metadata
from a number of different files. This library is typically used by file
indexers to retreive the metadata.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5filemetadata
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5filemetadata
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING* Readme.md

%files devel
#%_K5inc/kfilemetadata_version.h
%_K5inc/KFileMetaData/
%_K5link/lib*.so
%_K5lib/cmake/KF5FileMetaData
#%_K5archdata/mkspecs/modules/qt_KFileMetaData.pri

%files -n libkf5filemetadata
%_K5lib/libKF5FileMetaData.so.*
%_K5plug/kf5/kfilemetadata/

%changelog
* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
