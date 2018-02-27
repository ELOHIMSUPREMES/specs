%define module_name	omnibook
%define module_version  20110911 
%define module_release alt1

%define flavour		ovz-el
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-ovz-el

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Kernel module for some Toshiba and HP laptops
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Patch0: kernel-source-omnibook-0.0-alt.patch

ExclusiveOS: Linux
Url: http://omnibook.sourceforge.net/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
This package is intended to provide Linux kernel support for HP OmniBook,
HP Pavilion, Toshiba Satellite, Tecra, Equium and Compal laptops.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch0 -p1


%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`

%install
install -d %buildroot%module_dir
install -p -m644 omnibook.ko %buildroot%module_dir

install -d %buildroot%_docdir/%name-%version-%release
install -p -m644 doc/{BUGS,CREDITS,ChangeLog,README} \
	%buildroot%_docdir/%name-%version-%release
cp -pr misc %buildroot%_docdir/%name-%version-%release

%files
%defattr(644,root,root,755)
%module_dir
%doc %_docdir/%name-%version-%release

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 20110911-alt1
- build with kernel 3.10 fixed

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 20090714-alt5
- new template

* Tue Nov 15 2011 Anton Protopopov <aspsk@altlinux.org> 20090714-alt4
- Fix build with 3.1.1
- Enable backligiht support

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 20090714-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 20090714-alt2
- technical

* Thu Sep 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20090714-alt1
- updated from git

* Sun Jul 20 2008 Igor Zubkov <icesik@altlinux.org> 0.0-alt1.r274.132633.7
- build for kernel-image-std-def-2.6.25-alt7

* Sat Mar 22 2008 Igor Zubkov <icesik@altlinux.org> 0.0-alt1.r274
- build for Sisyphus

