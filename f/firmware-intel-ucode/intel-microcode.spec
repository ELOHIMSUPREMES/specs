%define orig_name intel-microcode
%define orig_timestamp 20170707.1

Name: firmware-intel-ucode
Version: 3
Release: alt0.%orig_timestamp
Epoch: 1

Packager: L.A. Kostis <lakostis@altlinux.org>

Summary: Microcode definitions for Intel processors
License: INTEL SOFTWARE LICENSE AGREEMENT
Group: System/Kernel and hardware
Provides: microcode-data-intel = %version-%release
Obsoletes: microcode-data-intel <= 20130222-alt2

URL: https://anonscm.debian.org/cgit/users/hmh/intel-microcode.git/
Source0: %{orig_name}-%{orig_timestamp}.tar

BuildRequires: iucode_tool

# beware that this probably should be ix86
# but who cares about intel on ARM?
BuildArch: noarch

%description
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%prep
%setup -q -n %orig_name-%{orig_timestamp}

%build
%make_build

%install
mkdir -p %buildroot/lib/firmware/intel-ucode
UCODE=intel-microcode
%ifarch %ix86
# use stripped down version for x86_64 and ia32
UCODE=${UCODE}-64
%endif
mv ${UCODE}.bin %buildroot/lib/firmware/intel-ucode/%{orig_name}.bin

%files
%doc changelog releasenote
%dir /lib/firmware/intel-ucode
/lib/firmware/intel-ucode/*

%changelog
* Mon Sep 04 2017 L.A. Kostis <lakostis@altlinux.ru> 1:3-alt0.20170707.1
- Rebased to Debian package (because Fedora version is outdated):
  * New upstream microcode datafile 20170707
    + New Microcodes:
      sig 0x00050654, pf_mask 0x97, 2017-06-01, rev 0x2000022, size 25600
      sig 0x000806e9, pf_mask 0xc0, 2017-04-27, rev 0x0062, size 97280
      sig 0x000806ea, pf_mask 0xc0, 2017-05-23, rev 0x0066, size 95232
      sig 0x000906e9, pf_mask 0x2a, 2017-04-06, rev 0x005e, size 97280
    + This release fixes the nightmare-level errata SKZ7/SKW144/SKL150/
      SKX150 (Skylake) KBL095/KBW095 (Kaby Lake) for all affected Kaby
      Lake and Skylake processors: Skylake D0/R0 were fixed since the
      previous upstream release (20170511).  This new release adds the
      fixes for Kaby Lake Y0/B0/H0 and Skylake H0 (Skylake-E/X).
    + Fix undisclosed errata in Skylake H0 (0x50654), Kaby Lake Y0
      (0x806ea), Kaby Lake H0 (0x806e9), Kaby Lake B0 (0x906e9)
  * source: remove unneeded intel-ucode/ directory
  * source: remove superseded upstream data file: 20170511

* Thu Dec 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.3
- Updated to 2.1-11 version:
  + Intel CPU microcode 20161104 update.

* Wed Jun 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.2
- Updated to 2.1-8 version:
  + Intel CPU microcode 20151106 update.

* Mon Aug 12 2013 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.1
- 2.1.
- remove amd-ucode (now part of linux-firmware).

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 1:2.0-alt0.2
- Get rid of versioning mess.

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt0.1
- 2.0 release from fedora.
- it's just a helper for seamless in-kernel firmware management.
- combine separate firmware files.

* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 1.17-alt2
- Package only utility. Microcode data will be in separate packages.
- Move utility from %_sbindir to /sbin.
- Use /lib/microcode for microcode data instead of /etc.

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 1.17-alt1
- 1.17

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt2
- Comment ExclusiveArch for now.

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt1
- 1.16

* Mon Nov 13 2006 Denis Smirnov <mithraen@altlinux.ru> 1.14-alt1
- Update to 1.14

* Mon Dec 12 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt2
- Shift service start priority to run after udev is up.
- Remove microcode kernel module after microcode uploading.

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt1
- Initial build.
