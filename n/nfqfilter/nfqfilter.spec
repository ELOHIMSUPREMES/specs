Name: nfqfilter
Version: 0.1
Release: alt4
Summary: Filtration system packages based on patterns
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv3
Url: https://github.com/max197616/nfqfilter
Source0: %name-%version.tar

BuildRequires: gcc-c++ libnetfilter_queue-devel libnfnetlink-devel
BuildRequires: libpoco-devel >= 1.6
BuildRequires: libnDPI-devel >= 1.7

%description
Filtration system packages based on patterns

%prep
%setup

%build
%configure

%make_build

%install
%makeinstall

install -m 0644 -D etc/%name.ini %buildroot%_sysconfdir/%name/%name.ini
install -m 0644 -D etc/systemd/%name.service %buildroot%_unitdir/%name.service

install -m 0755 -D nfqfilter.init        %buildroot%_initdir/%name
install -m 0644 -D nfqfilter.sysconfig   %buildroot%_sysconfdir/sysconfig/%name

install -m 0644 -D contrib/domains   %buildroot%_localstatedir/%name/domains
install -m 0644 -D contrib/hosts     %buildroot%_localstatedir/%name/hosts
install -m 0644 -D contrib/protos    %buildroot%_localstatedir/%name/protos
install -m 0644 -D contrib/ssl_host  %buildroot%_localstatedir/%name/ssl_host
install -m 0644 -D contrib/urls      %buildroot%_localstatedir/%name/urls


%files
%doc README COPYING
%_sysconfdir/%name
%_sysconfdir/sysconfig/%name
%_initdir/%name
%_unitdir/*
%_bindir/*
%_localstatedir/%name

%changelog
* Mon Nov 09 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt4
- update to git:c308c8eaff3f320adc3c96d0ef6940d69631ebd3

* Wed Oct 28 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt3
- Added error handler

* Fri Oct 02 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt2
- Correct License LGPL3 -> GPL3

* Wed Sep 30 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt1
- Initial RPM release
