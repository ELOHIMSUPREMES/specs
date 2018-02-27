%set_verify_elf_method unresolved=strict

Name: gnustep-steptalk
Version: 0.10.0
Release: alt2.git20131220
Summary: Scripting framework for creating scriptable servers or applications
License: LGPLv2.1+
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/gui/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc

Requires: lib%name = %version-%release

%description
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

%package -n lib%name
Summary: Shared libraries of StepTalk
Group: System/Libraries

%description -n lib%name
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

This package contains shared libraries of StepTalk.

%package -n lib%name-devel
Summary: Development files of StepTalk
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

This package contains development files of StepTalk.

%package doc
Summary: Documentation for StepTalk
Group: Development/Documentation
BuildArch: noarch

%description doc
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

This package contains documentation for StepTalk.

%prep
%setup

%build
buildIt() {
	%make_build \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
		AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
		CONFIG_SYSTEM_LIBS="-lgnustep-base -lobjc2 -lm $1"
}

buildIt
rm -f $(find ./ -name Smalltalk -type f)
buildIt $PWD/Frameworks/StepTalk/StepTalk.framework/libStepTalk.so
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/StepTalk.framework/Versions/0/$i ./
	for j in *.so.*.*; do
		ln -s %_libdir/$j GNUstep/Frameworks/StepTalk.framework/Versions/0/$i
	done
done
rm -f GNUstep/Frameworks/StepTalk.framework/Versions/0/StepTalk
ln -s %_libdir/$j GNUstep/Frameworks/StepTalk.framework/Versions/0/StepTalk
popd

%files
%doc ChangeLog NEWS README TODO WISH
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/StepTalk.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/StepTalk.framework//Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/StepTalk.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/StepTalk.framework//Headers

%files doc
%doc Documentation/*

%changelog
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20131220
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20130630
- New snapshot

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20130302
- New snapshot

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20121202
- Rebuilt with libobjc2 instead of libobjc
- Don't require development packages for runtime packages

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20121202
- Initial build for Sisyphus

