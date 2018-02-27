%define ver_major 1.1
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable gtk_doc

Name: iio-sensor-proxy
Version: %ver_major
Release: alt1

Summary: IIO sensors to input device proxy
Group: System/Kernel and hardware
License: GPLv2+
Url: https://github.com/hadess/%name

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gnome-common intltool gtk-doc
BuildRequires: libgio-devel systemd-devel
BuildRequires: libudev-devel libgudev-devel
# for check
BuildRequires: /proc dbus-tools-gui

%description
%name is a framework for accessing the various environmental sensors
(e.g., accelerometer, magnetometer, proximity, or ambient-light sensors)
built in to recent laptops. The proxy is a daemon that listens to the
Industrial I/O (IIO) subsystem and provides access to the sensor readings
over D-Bus.

As of right now, support for ambient-light sensors and accelerometers is
working; other sensor types are in development. The current API is based
on those used by Android and iOS, but may be expanded in the future. "For
future versions, we'll want to export the raw accelerometer readings, so
that applications, including games, can make use of them, which might
bring up security issues. SDL, Firefox, WebKit could all do with being
adapted, in the near future."


%package devel-doc
Summary: Developer documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Developer documentation for %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_sbindir/%name
%_bindir/monitor-sensor
%_unitdir/%name.service
%_udevrulesdir/40-%name.rules
%_sysconfdir/dbus-1/system.d/net.hadess.SensorProxy.conf
%doc README.md NEWS

%files devel-doc
%_datadir/gtk-doc/html/%name/


%changelog
* Mon Jul 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Sat May 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus

