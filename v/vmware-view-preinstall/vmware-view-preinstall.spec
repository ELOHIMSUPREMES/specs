Name: vmware-view-preinstall
Version: 4.10.0
Release: alt4

Summary: VMware Horizon Client pre-installation scripts
License: public domain
Group: System/Configuration/Other

Url: http://altlinux.org/vmware-view
ExclusiveArch: %ix86 x86_64

Requires: libXScrnSaver
Requires: libXtst
Requires: libgst-plugins
Requires: libgtk+2
Requires: libgtkmm2
Requires: libpng12
Requires: libudev0
Requires: libusb

BuildArch: noarch

%description
Install this package if you plan to deploy
VMware-Horizon-Client-%version bundle on this system.

%files

%changelog
* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt4
- Make package noarch.

* Thu Mar 14 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt3
- Update requirements from VMware Horizon Client 4.10.0.

* Tue Mar 12 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt2
- Build for i586 and x86_64.

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- New version of VMware-Horizon-Client uses bundled libssl and libcrypto.

* Tue Apr 04 2017 Michael Shigorin <mike@altlinux.org> 3.4.0-alt4
- made "64-bit" package "require" i586-libXScrnSaver
  like skype-preinstall (closes: #33325);
  thanks cas@ for the hint

* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt3
- moved scripts to vmware-view-userinstall so this package
  is a pristine preinstall one

* Tue Sep 22 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- made noarch with runtime getconf(1) instead of build-time %%_lib
- added desktop file and an icon beforehand

* Fri Sep 18 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- initial release

