%define module_name	ipset
%define module_version	6.19
%define module_release	alt1

%define flavour		un-def
BuildRequires(pre): kernel-headers-modules-un-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: ipset kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Patch0: kernel-source-ipset-6.19-alt-build.patch

ExclusiveOS: Linux
URL: http://ipset.netfilter.org/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch 

%description
ipset kernel modules.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch -p1

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`/net/netfilter IP_NF_SET_MAX=256 IP_NF_SET_HASHSIZE=1024

%install
install -d %buildroot%module_dir
install -p -m644 net/netfilter/ipset/*.ko %buildroot%module_dir
install -p -m644 net/netfilter/*.ko %buildroot%module_dir


%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Fri Jun 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.19-alt1
- new version

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- new version 

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 4.1-alt1
- fisrt build for Sisyphus, specfile from Igor Zubkov
