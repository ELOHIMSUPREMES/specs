Name: ubridge
Version: 0.9.4
Release: alt1

Summary: Bridge for UDP tunnels, Ethernet, TAP and VMnet interfaces
License: GPLv3
Group: Networking/Other
Url: https://github.com/GNS3/ubridge

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc libpcap-devel

%description
uBridge is a simple application to create user-land bridges between various
technologies. Currently bridging between UDP tunnels, Ethernet and TAP
interfaces is supported. Packet capture is also supported.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_bindir
cp %name %buildroot%_bindir

%post
chmod 4755 %_bindir/%name

%files
%doc LICENSE README.rst
%_bindir/%name

%changelog
* Mon Aug 08 2016 Anton Midyukov <antohami@altlinux.org> 0.9.4-alt1
- Initial build for ALT Linux Sisyphus.
