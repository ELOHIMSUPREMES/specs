%define module_name	virtualbox-addition
%define module_version	4.2.4
%define module_release	alt1

%define kversion	3.6.7
%define krelease	alt2
%define flavour		un-def

%define base_arch %(echo %_target_cpu | sed 's/i.86/i386/;s/athlon/i386/')

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

%define guest_module_name	vboxguest
%define vfs_module_name		vboxsf
%define video_module_name	vboxvideo

Summary: VirtualBox modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.198151.2
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://www.virtualbox.org/
BuildRequires(pre): rpm-build-kernel
BuildPreReq: gcc-c++
BuildRequires: perl
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%guest_module_name = %module_version
BuildRequires: kernel-source-%vfs_module_name = %module_version
BuildRequires: kernel-source-%video_module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Provides: kernel-modules-%guest_module_name-%kversion-%flavour-%krelease = %version-%release
Provides: kernel-modules-%guest_module_name-%flavour = %version-%release

Provides: kernel-modules-%video_module_name-%kversion-%flavour-%krelease = %version-%release
Provides: kernel-modules-%video_module_name-%flavour = %version-%release

Provides: kernel-modules-%vfs_module_name-%kversion-%flavour-%krelease = %version-%release
Provides: kernel-modules-%vfs_module_name-%flavour = %version-%release
Obsoletes: kernel-modules-%vfs_module_name-%flavour

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

# %%if "%flavour" == "ovz-el"
# #Patch1: ovz-el-fix-build.patch
# %%endif

%description
This package contains VirtualBox addition modules (vboxguest, vboxsf, vboxvideo)
that are needed for additonal guests support for VirtualBox.

%prep
%setup -T -c -n kernel-source-%module_name-%module_version
%__tar jxvf %kernel_src/kernel-source-%guest_module_name-%module_version.tar.bz2
%__tar jxvf %kernel_src/kernel-source-%vfs_module_name-%module_version.tar.bz2
%__tar jxvf %kernel_src/kernel-source-%video_module_name-%module_version.tar.bz2

# %%if "%flavour" == "ovz-el"
# %%patch1 -p1
# %%endif

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make -C kernel-source-%guest_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/
cp kernel-source-%guest_module_name-%module_version/Module.symvers \
    kernel-source-%vfs_module_name-%module_version
%make -C kernel-source-%vfs_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/
%make -C kernel-source-%video_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/

%install
%__mkdir_p %buildroot/%module_dir
%__install -pD -m644 kernel-source-%guest_module_name-%module_version/vboxguest.ko \
    %buildroot%module_dir/
%__install -pD -m644 kernel-source-%vfs_module_name-%module_version/vboxsf.ko \
    %buildroot%module_dir/
%__install -pD -m644 kernel-source-%video_module_name-%module_version/vboxvideo.ko \
    %buildroot%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Fri Nov 23 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.4-alt1.198151.2
- Build for kernel-image-un-def-3.6.7-alt2.

* Thu Nov 22 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.4-alt1
- Update to new release

* Wed Aug 29 2012 Anton Protopopov <aspsk@altlinux.org> 4.1.20-alt2
- technical

* Wed Aug 22 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.20-alt1
- Update to new release

* Sun Jul 29 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.18-alt2
- Remove old patch for el-smp

* Sat Jul 28 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.18-alt1
- Update to new release

* Sun Jun 24 2012 Anton Protopopov <aspsk@altlinux.org> 4.1.12-alt3
- Fix build on el-smp

* Fri Apr 06 2012 Anton Protopopov <aspsk@altlinux.org> 4.1.12-alt2
- Technical

* Wed Apr 04 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt1
- Update to new release

* Sun Apr 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.10-alt1
- Update to new release with 3.2 kernel support

* Sat Jan 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.6-alt3
- fix to build with 3.2 kernel

* Mon Dec 12 2011 Anton Protopopov <aspsk@altlinux.org> 4.1.6-alt2
- Fix build with latest el-smp

* Fri Dec 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.6-alt1
- Update to new release

* Tue Nov 01 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.4-alt1
- Update to new release

* Wed Sep 21 2011 Anton Protopopov <aspsk@altlinux.org> 4.0.12-alt2
- Technical

* Mon Jul 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.12-alt1
- 4.0.12

* Sun Feb 20 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt1
- Update to new release

* Thu Jan 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.12-alt1
- Update to new release

* Thu Jun 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt1
- Update to new release

* Tue May 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.8-alt1
- Update to new release

* Sun Apr 04 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.6-alt1
- Update to new release

* Thu Mar 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.4-alt1
- Update to new release

* Tue Nov 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Update to new release

* Wed Oct 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.8-alt1
- Update to new release

* Sun Sep 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.6-alt1
- Update to new release

* Tue Aug 11 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.4-alt1
- Update to new release

* Thu Jul 23 2009 Anton Protopopov <aspsk@altlinux.org> 3.0.2-alt2
- Merge with sin@ to enforce inheritance

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.2-alt1
- Update to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt2
- Merge vboxvfs module into common virtualbox-addition
- Built new video module

* Wed Jul 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt1
- Update to new release

* Sun Jun 14 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.4-alt1
- Update to new release

* Tue May 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.2-alt1
- Update to new release

* Wed Feb 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt1
- Update to new release

* Fri Dec 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt1
- Update to new release

* Sat Nov 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.4-alt1
- Update to new release

* Thu Sep 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Update to last release

* Sun Aug 31 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.4-alt1
- Update to last release

* Sun Jun 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.2-alt1
- Update to last release

* Fri Mar 28 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt1
- Initial virtualbox addition modules build

