%add_python_req_skip guestfs
%define _libexecdir /usr/libexec
%define qemu_user  _libvirt
%define preferred_distros "altlinux,fedora,rhel"
%define kvm_packages ""
%define libvirt_packages "libvirt"
%define askpass_package "openssh-askpass"

Name: virt-manager
Version: 1.2.0
Release: alt2
Summary: Virtual Machine Manager

Group: Emulators
License: GPLv2+
Url: http://virt-manager.org/
BuildArch: noarch

# git://git.fedorahosted.org/virt-manager.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: virt-manager-common = %version-%release
Requires: virt-install = %version-%release
Requires: python-module-pygobject3
Requires: python-module-libxml2
Requires: vte3
Requires: dconf
Requires: dbus-tools-gui
Requires: libosinfo >= 0.2.10
Requires: librsvg

# add requires based on "from gi.repository import foo"
Requires: typelib(GObject)
Requires: typelib(LibvirtGLib)
Requires: typelib(Gtk) = 3.0
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Pango)
Requires: typelib(GLib)
Requires: typelib(Gio)
Requires: typelib(GtkVnc) = 2.0
Requires: typelib(SpiceClientGtk) = 3.0
Requires: typelib(SpiceClientGLib)
Requires: typelib(Vte)
Requires: typelib(Libosinfo)

BuildRequires: python-devel python-module-distribute
BuildRequires: libgio
BuildRequires: intltool
BuildRequires: /usr/bin/pod2man

%add_python_req_skip virtconv
%add_python_req_skip virtinst
%add_python_req_skip virtcli
%add_python_req_skip virtxml

%description
Virtual Machine Manager provides a graphical tool for administering
virtual machines for KVM, Xen, and QEmu. Start, stop, add or remove
virtual devices, connect to a graphical or serial console, and see
resource usage statistics for existing VMs on local or remote machines.
Uses libvirt as the backend management API.

%package common
Summary: Common files used by the different Virtual Machine Manager interfaces
Group: Emulators
Conflicts: %name < %version-%release

%description common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.

%package -n virt-install
Summary: Utilities for installing virtual machines
Group: Emulators

Requires: virt-manager-common = %version-%release

Provides: virt-install
Provides: virt-clone
Provides: virt-convert
Provides: virt-xml
Obsoletes: python-module-virtinst

%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

%prep
%setup
%patch -p1

%build
python setup.py configure \
	--qemu-user=%qemu_user \
	--libvirt-package-names=%libvirt_packages \
	--kvm-package-names=%kvm_packages \
	--preferred-distros=%preferred_distros \
	--askpass-package-names=%askpass_package

#%%python_build

%install
#%%python_install
python setup.py install --root=%buildroot

%find_lang --with-gnome %name

%files
%_bindir/%name
%_datadir/%name/ui/*.ui
%_datadir/%name/virt-manager
%_datadir/%name/virtManager
%_datadir/%name/icons
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/GConf/gsettings/org.virt-manager.virt-manager.convert

%_man1dir/%name.1*
%doc README COPYING NEWS

%files common -f %name.lang
%dir %_datadir/%name
%_datadir/%name/virtcli
%_datadir/%name/virtconv
%_datadir/%name/virtinst

%files -n virt-install
%_bindir/virt-install
%_bindir/virt-clone
%_bindir/virt-convert
%_bindir/virt-xml
%_datadir/%name/virt-install
%_datadir/%name/virt-clone
%_datadir/%name/virt-convert
%_datadir/%name/virt-xml
%_man1dir/virt-install.1*
%_man1dir/virt-clone.1*
%_man1dir/virt-convert.1*
%_man1dir/virt-xml.1*

%changelog
* Wed May 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt2
- backport patches from upstream master:
  + domain: Fix memory stats for shutoff VM (#1215453)
  + sshtunnels: fix exception when the address is not an IP (RH#1218958 ALT#31020)
  + pollhelpers: Fix VM polling on old libvirt (RH#1219443)
  + storage: do not throw exception if the volume or the pool don't exist (RH#219427)
  + interface: read the start mode from the inactive conf XML (RH#1154480)

* Tue May 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0
- update Requires (#30809)

* Thu Sep 11 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed Apr 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1
- updare Requires (#29396, #22760)

* Wed Mar 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1.git.7dfdbb
- upstream snapshot 7dfdbb3f352817a61fa7c06f463500807840348d

* Thu Aug 08 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt2
- add ALT Linux support

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0
- add subpackages virt-install and virt-manager-common

* Wed Apr 10 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Wed Jan 23 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.4-alt1.git0ca8c
- upstream git snapshot 0ca8cf6d4316d1b3f55226c3782a3ac92eb34967

* Tue Jul 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Mon Apr 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt2.git.9d2119
- git snapshot

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Tue Mar 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt3.hg20110224
- snapshot 20110224

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt3.hg20110215
- snapshot 20110215

* Fri Feb 11 2011 Anton Protopopov <aspsk@altlinux.org> 0.8.6-alt2
- Don't always launch consoles for running domains (ALT #25073)

* Tue Jan 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Tue Jan 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1.hg20110107
- snapshot 20110107
- build as noarch

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1.hg20101220
- snapshot 20101220 (with spice support)
- define _libexecdir as /usr/libexec (fix dbus service)

* Tue Dec 07 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt3
- Add perl-Pod-Parser to build requires

* Tue Dec 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt2
- Merge with gears/

* Tue Dec 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Wed Dec 09 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Tue Dec 01 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt2
- Add Packager field

* Thu Oct 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Thu Jul 02 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.0-alt1
- new version
- remove post scripts

* Tue Apr 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt2
- fix #15493, #15494

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt1
- First build for ALTLinux

