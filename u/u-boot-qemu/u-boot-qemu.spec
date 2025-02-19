%define allowed_arch armh aarch64 %ix86 x86_64 mips mipsel mips64 mips64el riscv32 riscv64 ppc64

Name: u-boot-qemu
Version: 2019.04
Release: alt2

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: %allowed_arch

Source: %name-%version-%release.tar

BuildRequires: dtc >= 1.4 flex
%ifarch %ix86 x86_64
BuildRequires: python-dev swig
%endif

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package contains U-Boot image for QEMU virt machine.

%ifarch armh
%define qemu qemu_arm
%endif
%ifarch aarch64
%define qemu qemu_arm64
%endif
%ifarch %ix86
%define qemu qemu-x86
%endif
%ifarch x86_64
%define qemu qemu-x86_64
%endif
%ifarch mips
%define qemu qemu_mips
%endif
%ifarch mipsel
%define qemu qemu_mipsel
%endif
%ifarch mips64
%define qemu qemu_mips64
%endif
%ifarch mips64el
%define qemu qemu_mips64el
%endif
%ifarch mips
%define qemu qemu_mips
%endif
%ifarch ppc64
%define qemu qemu-ppce500
%endif
%ifarch riscv32
%define qemu qemu-riscv32
%endif
%ifarch riscv64
%define qemu qemu-riscv64
%endif

%prep
%setup

%build
%make_build %{qemu}_defconfig all

%install
install -pm0644 -D u-boot.bin %buildroot%_datadir/u-boot/%qemu/u-boot.bin

%files
%doc README
%_datadir/u-boot/*

%changelog
* Tue May 07 2019 Anton Midyukov <antohami@altlinux.org> 2019.04-alt2
- Build for allowed Arch

* Tue Apr 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- initial
