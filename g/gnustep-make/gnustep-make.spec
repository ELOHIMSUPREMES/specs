Name: gnustep-make
Version: 2.6.5
Release: alt1.git20130727
Source: %name-%version-%release.tar
License: GPLv3+
Group: Development/Other
Summary: GNUstep Makefile package
Url: http://www.gnustep.org/

BuildRequires: gcc-objc libgnustep-objc2-devel star
Requires: gnustep-dirs

%description
This package contains the basic scripts, makefiles and directory
layout needed to run and compile any GNUstep software.
This package was configured using flattened mode using the system
GNUstep filesystem layout.

%package devel
Summary: Files needed to develop applications with gnustep-make
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description devel
The makefile package is a simplistic, powerful and extensible way to
write makefiles for a GNUstep-based project. It allows the user to
write a GNUstep-based project without having to deal with the complex
issues associated with the configuration and installation of the core
GNUstep libraries. It also allows the user to easily create
cross-compiled binaries.


%prep
%setup -n %name-%version-%release

%ifarch x86_64
LIB_SUFF=64
%endif
sed -i "s|@64@|$LIB_SUFF|g" FilesystemLayouts/fhs-system-alt

%build
export CC=gcc CXX=g++ CPP='gcc -E'
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-flattened \
	--with-layout=fhs-system-alt \
	--with-objc-lib-flag=-lobjc2

%install
sed -i 's|/usr/sbin/lsattr|lsattr|g' config.guess
%makeinstall_std

if grep -Fle %_target_cpu $(find %buildroot -type f -not -name config.guess -not -name config.sub); then
       echo >&2 %buildroot is dirty
       exit 1
fi

#install -d %buildroot/etc/profile.d

#cat > %buildroot/etc/profile.d/GNUstep.sh << EOF
##!/bin/sh
#. %_datadir/GNUstep/Makefiles/GNUstep.sh
#
#if [ ! -d \$GNUSTEP_USER_ROOT ]; then
#        mkdir \$GNUSTEP_USER_ROOT
#        chmod +rwx \$GNUSTEP_USER_ROOT
#        . %_datadir/GNUstep/Makefiles/GNUstep.sh
#fi
#EOF

#find %buildroot%_datadir/GNUstep/Makefiles/Instance/Documentation \
#        -type f ! -name '*.html' ! -name '*.css' ! -name '*.gz' | xargs gzip -9nf 

gzip ChangeLog

%files
%doc ChangeLog*
%_sysconfdir/GNUstep/
%_bindir/*
#%attr(755,root,root) %_sysconfdir/profile.d/*
%dir %_datadir/GNUstep
%dir %_datadir/GNUstep/Makefiles
%dir %_datadir/GNUstep/Makefiles
%attr(755,root,root) %_datadir/GNUstep/Makefiles/*.csh
%attr(755,root,root) %_datadir/GNUstep/Makefiles/*.sh
#%attr(755,root,root) %_datadir/Tools
%_datadir/GNUstep/Makefiles/tar-exclude-list
%_datadir/GNUstep/Makefiles/config.guess
%_datadir/GNUstep/Makefiles/config.sub
%_datadir/GNUstep/Makefiles/gnustep-make-help
%_man1dir/*
%_man7dir/*

%files devel
%_datadir/GNUstep/Makefiles/*.make
%_datadir/GNUstep/Makefiles/*.template
%_datadir/GNUstep/Makefiles/Instance
%_datadir/GNUstep/Makefiles/Master
%_datadir/GNUstep/Makefiles/TestFramework
%attr(755,root,root) %_datadir/GNUstep/Makefiles/install-sh
%attr(755,root,root) %_datadir/GNUstep/Makefiles/mkinstalldirs

%changelog
* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.5-alt1.git20130727
- Version 2.6.5

* Sun May 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.git20130408
- New snapshot

* Wed Mar 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.git20130316
- New snapshot

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.git20130301
- Version 2.6.4

* Sun Dec 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt12.git20121102
- Rebuilt with linking with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt11.svn20121102
- Applied patch from ldv@ with fix for x86_64

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt10.svn20121102
- Removed -march & -mtune flags

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt9.svn20121102
- Restored replacement i586 -> x86_64 for x86_64

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt8.svn20121102
- Replaced *-alt-linux-gcc by gcc (thnx ldv@)

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt7.svn20121102
- Set CONFIG_SYSTEM_LIBS as variable for add libraries during linking

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt6.svn20121102
- More tuning

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt5.svn20121102
- Fixed for build clients for x86_64

* Mon Dec 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt4.svn20121102
- Set libexecdir to %_libdir

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt3.svn20121102
- Fixed arch type for all installed files

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt2.svn20121102
- Compressed ChangeLog
- Set devel subpackage as noarch
- Built with gnustep-objc2-devel instead of libobjc-devel
- Tuned layout of directories

* Sat Dec 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.svn20121102
- Version 2.6.2

* Mon Jun 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt4.3
- Fixed arch type for x86_64

* Fri Jun 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt4.2
- Set %name-devel as noarch package

* Tue Jun 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt4.1
- Fixed requires on lsattr

* Mon Apr 06 2009 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt4
- fix probable x86_64 problems (thanks to raorn@)

* Mon Mar 30 2009 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt3
- rebuild using filesystem layout fhs-system

* Fri Mar 27 2009 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt2
- rebuild using flattened mode

* Thu Jul 03 2008 Sergey Alembekov <rt@altlinux.ru> 2.0.6-alt1
- build with new upstream version

* Thu Jul 03 2008 Sergey Alembekov <rt@altlinux.ru> 2.0.4-alt1
- build with new version

* Sun Dec 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt0.1
- new version 1.13.0 (with rpmrb script)
- fix duplicate GNUStep dir

* Sat Nov 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.11.1-alt0.1
- initial build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org>
