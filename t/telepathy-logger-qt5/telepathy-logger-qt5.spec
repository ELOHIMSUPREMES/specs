
Name: telepathy-logger-qt5
Version: 15.4.0
Release: alt1
%define sover 5
%define libname libtelepathy-logger-qt%sover

Group: Networking/Instant messaging
Summary: Qt Wrapper around TpLogger client library
Url: https://projects.kde.org/telepathy-logger-qt
License: LGPLv2.1+

Source: %name-%version.tar

# Automatically added by buildreq on Mon May 18 2015 (-bi)
# optimized out: cmake cmake-modules elfutils glib2-devel libcloog-isl4 libdbus-devel libdbus-glib libdbus-glib-devel libgio-devel libqt5-core libqt5-dbus libqt5-network libqt5-xml libstdc++-devel libtelepathy-glib libtelepathy-glib-devel libtelepathy-logger libtelepathy-qt5 libtelepathy-qt5-devel libxml2-devel pkg-config python-base python-devel python-modules python-modules-encodings python-modules-xml ruby ruby-stdlibs xml-utils
BuildRequires: doxygen extra-cmake-modules gcc-c++ graphviz libtelepathy-logger-devel libtelepathy-qt5-devel-static
BuildRequires: phonon-devel qt5-base-devel kde-common-devel
BuildRequires: pkgconfig(Qt5GLib-2.0)

%description
Telepathy-logger-qt5 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package devel
Group: Development/KDE and QT
Summary: Qt Wrapper around TpLogger client library
Requires: pkgconfig(Qt5GLib-2.0) libtelepathy-qt5-devel
%description devel
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package -n %libname
Group: System/Libraries
Summary: Qt Wrapper around TpLogger client library

%description -n %libname
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%prep
%setup
#%patch2 -p1
#%patch3 -p1

%build
export QTDIR=%_qt4dir
%Kbuild

%install
%Kinstall

%files -n %libname
%doc AUTHORS ChangeLog HACKING TODO
%_libdir/libtelepathy-logger-qt.so.%sover
%_libdir/libtelepathy-logger-qt.so.*

%files devel
%_libdir/cmake/TelepathyLoggerQt/
%_includedir/TelepathyLoggerQt/
%_libdir/lib*.so

%changelog
* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- initial build
