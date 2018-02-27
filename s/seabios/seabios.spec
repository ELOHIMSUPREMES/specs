%define debug_level 1

Name: seabios
Version: 1.8.1
Release: alt1
Summary: Open-source legacy BIOS implementation

Group: Emulators
BuildArch: noarch
License: LGPLv3
Url: http://www.seabios.org

# git://git.seabios.org/seabios.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Source10: config.vga.cirrus
Source11: config.vga.isavga
Source12: config.vga.qxl
Source13: config.vga.stdvga
Source14: config.vga.vmware
Source15: config.csm
Source16: config.coreboot
Source17: config.seabios-128k
Source18: config.seabios-256k

BuildRequires: python-base python-modules iasl
BuildRequires: binutils-x86_64-linux-gnu gcc-x86_64-linux-gnu
Conflicts: qemu-common < 1.6.0-alt1

%description
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.

%package -n seavgabios
Summary: Seavgabios for x86
Group: Emulators
BuildArch: noarch

%description -n seavgabios
SeaVGABIOS is an open-source VGABIOS implementation.

%set_verify_elf_skiplist %_datadir/%name/bios*.bin

%prep
%setup -q
%patch -p1

echo %version > .version
sed -i '/VERSION="${VERSION}-.*"$/d' scripts/buildversion.sh

%build
export CFLAGS="$RPM_OPT_FLAGS"
mkdir -p binaries


build_bios() {
	make clean distclean
	cp $1 .config
	echo "CONFIG_DEBUG_LEVEL=%{debug_level}" >> .config
	make oldnoconfig V=1
	make V=1 \
		HOSTCC=gcc \
		CC=x86_64-linux-gnu-gcc \
		AS=x86_64-linux-gnu-as \
		LD=x86_64-linux-gnu-ld \
		OBJCOPY=x86_64-linux-gnu-objcopy \
		OBJDUMP=x86_64-linux-gnu-objdump \
		STRIP=x86_64-linux-gnu-strip $4

	cp out/$2 binaries/$3
}

# seabios
build_bios %SOURCE15 Csm16.bin bios-csm.bin
build_bios %SOURCE16 bios.bin.elf bios-coreboot.bin
build_bios %SOURCE17 bios.bin bios.bin
build_bios %SOURCE18 bios.bin bios-256k.bin
cp out/src/fw/*dsdt*.aml binaries

# seavgabios
for config in %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14; do
	name=${config#*config.vga.}
	build_bios ${config} vgabios.bin vgabios-${name}.bin out/vgabios.bin
done

%install
mkdir -p %buildroot%_datadir/%name
install -m 0644 binaries/bios.bin %buildroot%_datadir/%name/bios.bin
install -m 0644 binaries/bios-256k.bin %buildroot%_datadir/%name/bios-256k.bin
install -m 0644 binaries/bios-csm.bin %buildroot%_datadir/%name/bios-csm.bin
install -m 0644 binaries/bios-coreboot.bin %buildroot%_datadir/%name/bios-coreboot.bin
install -m 0644 binaries/*.aml %buildroot%_datadir/%name/

mkdir -p %buildroot%_datadir/seavgabios
install -m 0644 binaries/vgabios*.bin %buildroot%_datadir/seavgabios
ln -r -s %buildroot%_datadir/seavgabios/vgabios-isavga.bin %buildroot%_datadir/seavgabios/vgabios.bin

%files
%doc COPYING COPYING.LESSER README
%dir %_datadir/%name
%_datadir/%name/bios*.bin
%_datadir/%name/*.aml

%files -n seavgabios
%dir %_datadir/seavgabios
%_datadir/seavgabios/vgabios*.bin

%changelog
* Tue Mar 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Tue Nov 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.5.1-alt1
- 1.7.5.1

* Tue Aug 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.5-alt2
- Fix PCI-e hotplug

* Mon Jun 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.5-alt1
- 1.7.5

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt2
- upstream snapshot 0784d04cb6f6e5c893aaf368091f20326fb847fe
- build 256k bios images for qemu 2.0

* Wed Jan 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Wed Oct 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3.2-alt1
- 1.7.3.2

* Fri Aug 16 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3.1-alt1
- 1.7.3.1

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3-alt2
- move seabios binary to _datadir

* Thu Aug 08 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2.2-alt1
- 1.7.2.2

* Tue May 07 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2.1-alt1
- 1.7.2.1

* Tue Feb 19 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt2
- add seavgabios package

* Tue Feb 19 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Fri Sep 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.3.2-alt1
- 1.6.3.2

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.3.1-alt1
- 1.6.3.1

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1.git8e3014
- upstream git snapshot 8e301472e324b6d6496d8b4ffc66863e99d7a505

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.3-alt1
- 0.6.1.3

* Fri Dec 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.2-alt1
- initial build for ALT Linux Sisyphus
