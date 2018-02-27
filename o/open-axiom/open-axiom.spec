%define oname axiom
%define lisp sbcl

%ifarch x86_64
%define arch x86_64
%else
%define arch i586
%endif

Name: open-%oname
Version: 1.5.0
Release: alt2.svn20150403

Summary: OpenAxiom Computer Algebra System
License: BSD-style
Group: Sciences/Mathematics
Url: http://www.open-axiom.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.code.sf.net/p/open-axiom/code/trunk
Source0: %name-%version.tar.bz2
Source3: %oname-16.png
Source4: %oname-32.png
Source5: %oname-48.png
Source6: %oname.desktop
Source7: http://voxel.dl.sourceforge.net/sourceforge/open-axiom/open-axiom-1.3.x-dep.tar.bz2

Requires: %lisp
Conflicts: %oname
Obsoletes: %oname
Conflicts: fricas

BuildRequires: texlive-base-bin texlive-latex-base /proc
BuildRequires: libreadline-devel libncurses-devel binutils-devel
BuildRequires: tcl-devel tk-devel %lisp gcc-c++ clang-devel
BuildRequires: libgmp-devel texinfo libqt4-devel
BuildRequires: sed gawk coreutils diffutils libXt-devel libXext-devel
BuildRequires: libX11-devel libXpm-devel libXpm libXaw-devel
BuildRequires: libXmu-devel libSM-devel libICE-devel libXdmcp-devel
BuildRequires: xorg-xtrans-devel

%description
OpenAxiom is an open source platform for symbolic, algebraic, and
numerical computations. It offers an interactive environment, an
expressive programming language, a compiler, a large set of mathematical
libraries of interest to researchers and practitioners of computational
sciences.

OpenAxiom strives to support ubiquitous, advanced, high quality open
source computer algebra on major operating systems, in particular major
Unix variants, GNU/Linux variants, Windows, and handheld devices. It
aims at being the open source computer algebra system of choice for
research, teaching, engineering, etc.

%package doc
Summary: Documentation for OpenAxiom
Group: Documentation
BuildArch: noarch

%description doc
Documentation for OpenAxiom.

%prep 
%setup
tar -xjf %SOURCE7

sed -i 's|0x|(char)0x|g' \
	src/hyper/ht_icon \
	src/hyper/mouse11.bitmap \
	src/hyper/mouse11.mask \
	src/hyper/initx.c \
	src/hyper/sdown3d.bitmap \
	src/hyper/sdown3dpr.bitmap \
	src/hyper/sup3d.bitmap \
	src/hyper/sup3dpr.bitmap \
	src/graph/include/light11.mask

%build

mv noweb/noweb/* noweb/
TOPDIR=$PWD
NOWEB_DIR=$TOPDIR/noweb.built
export PATH=$NOWEB_DIR:$PATH:$TOPDIR/noweb/src
pushd noweb/src
%make
%make_install DESTDIR=$TOPDIR NOWEB_DIR=$NOWEB_DIR install
popd

export SBCL_HOME=%_libdir/sbcl
export PATH=$PATH:%_qt4dir/bin

%add_optflags -std=gnu++11 -DHAVE_SYS_STAT_H=1 -DHAVE_UNISTD_H=1
%add_optflags %optflags_shared
#autoreconf
./build-setup.sh
%configure \
	--enable-threads \
	--with-lisp=%lisp \
	--with-x
sed -i 's|^\(OBJEXT =\).*|\1 o|' $(find -name Makefile)
%make

%install
%makeinstall_std
ln -s %name %buildroot%_bindir/%oname

install -d %buildroot%_docdir/%name
install -p -m644 src/doc/ps/* %buildroot%_docdir/%name

install -d %buildroot%_libdir/%name/%arch-alt-linux-gnu/src/include
install -d %buildroot%_libdir/%name/%arch-alt-linux-gnu/src/utils
install -p -m644 src/include/* \
	%buildroot%_libdir/%name/%arch-alt-linux-gnu/src/include/
install -p -m644 src/utils/*.H \
	%buildroot%_libdir/%name/%arch-alt-linux-gnu/src/utils/

# icons
install -D -m644 %SOURCE3 %buildroot%_miconsdir/%name.png
install -D -m644 %SOURCE4 %buildroot%_niconsdir/%name.png
install -D -m644 %SOURCE5 %buildroot%_liconsdir/%name.png

# menu items
install -D -m644 %SOURCE6 %buildroot%_desktopdir/%name.desktop

%brp_strip_debug %_bindir/%name

%files
%doc AUTHORS COPYING ChangeLog* MAINTAINERS NEWS README STYLES TODO
%_bindir/*
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_libdir/%name

%files doc
%_docdir/%name

%changelog
* Sat May 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.svn20150403
- New snapshot

* Fri May 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.svn20140502
- New snapshot

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.svn20131215
- New snapshot

* Tue Oct 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.svn20130704
- New snapshot

* Thu Mar 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.svn20121011
- Rebuilt with sbcl 1.1.5

* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20121011
- New snapshot

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20120826
- New snapshot

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20120504
- New snapshot

* Sun Jan 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20120101
- New snapshot

* Tue Aug 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20110816
- New snapshot

* Sun Jul 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20110702
- Version 1.5.0

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20110322
- New snapshot

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20101119.1
- Rebuilt for debuginfo

* Fri Dec 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20101119
- New snapshot
- Fixed build with SBCL

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20100617.1
- Rebuilt for soname set-versions

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20100617
- New snapshot

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20100223
- New snapshot
- Added implicit conflics with fricas

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20091117
- New snapshot
- Fixed for libtool 2.2.6b

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20091001
- New snapshot
- Removed xorg-x11-devel from BuildRequires
- Rebuilt with texlive instead of tetex

* Mon Sep 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090902.2
- Rebuilt with SBCL instead of CLisp

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090902.1
- Avoided conflict with FriCAS
- Fixed program name in desktop file

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090902
- Initial build for Sisyphus
