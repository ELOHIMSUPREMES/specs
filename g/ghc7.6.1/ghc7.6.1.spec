Name: ghc7.6.1
Version: 7.6.1
Release: alt3

Summary: Glasgow Haskell Compilation system
License: BSD style w/o adv. clause
Group: Development/Haskell
Url: http://haskell.org/ghc/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Patch: ghc-%version-%release.patch

Requires: %name-common

# Automatically added by buildreq on Fri Apr 26 2013
# optimized out: ghc7.6.1-common gnu-config libgmp-devel libgpg-error libtinfo-devel pkg-config python-base time xml-common xml-utils zlib-devel
BuildRequires: binutils-devel docbook-dtds docbook-style-xsl ghc7.6.1 libelf-devel libffi-devel libncurses-devel xsltproc

# Can't build when installed
#BuildRequires: dblatex

%def_without hscolour
%if_with hscolour
BuildRequires: ghc(hscolour)
%endif

%description
Haskell is a standard lazy functional programming language; the
current language version is Haskell 98, agreed in December 1998.

GHC is a state-of-the-art programming suite for Haskell.  Included is
an optimising compiler generating good code for a variety of
platforms, together with an interactive system for convenient, quick
development.  The distribution includes space and time profiling
facilities, a large collection of libraries, and support for various
language extensions, including concurrency, exceptions, and foreign
language interfaces (C, C++, whatever).

A wide variety of Haskell related resources (tutorials, libraries,
specifications, documentation, compilers, interpreters, references,
contact information, links to research groups) are available from the
Haskell home page at <http://www.haskell.org/>.

%package doc
Summary: Documentation for GHC
Group: Development/Haskell
BuildArch: noarch

%description doc
Preformatted documentation for the Glasgow Haskell Compiler
(GHC) and its libraries. Install it if you like to have local
access to the documentation in PostScript and HTML format.
Alternatively, the documentation is available online at
http://haskell.org/ghc/documentation.html

%prep
%setup
%patch -p1

%build
%define _configure_target %nil
#autoreconf -fisv
./boot
%configure
%make_build V=1

%install
%define docdir %_docdir/%name-%version
%makeinstall_std docdir=%docdir
mv %buildroot%docdir/html/* %buildroot%docdir/
rmdir %buildroot%docdir/html
cp -a ANNOUNCE LICENSE README docs/comm %buildroot%docdir/

# generate fake .pkg configs for core packages.
# haskell.prov will convert them to package provides.
for lib in %buildroot%_libdir/ghc-%version/*-[0-9]*; do
	namever=`basename $lib`
	name=${namever%%-*}
	echo -e "name: $name\nversion: ${namever##*-}" >$lib/$name.pkg
done

# generate the file list for lib/ _excluding_ all files needed for profiling
# only
#
# * generating file lists in a BUILD_ROOT spec is a bit tricky: the file list
#   has to contain complete paths, _but_ without the BUILD_ROOT, we also do
#   _not_ want to have directory names in the list; furthermore, we have to make
#   sure that any leading / is removed from %%_libdir, as find has to
#   interpret the argument as a relative path; however, we have to include the
#   leading / again in the final file list (otherwise, rpm complains)
# * isn't there an easier way to do all this?
dir=`pwd`
cd %buildroot
libdir=`echo %_libdir | sed 's|^/||'`
find $libdir ! -type d ! -name 'package.conf*' \
     -print | sed 's|^|/|'\
     >$dir/rpm-files
find $libdir -type d -print | sed 's|^|%%dir /|' >>$dir/rpm-files
cd $dir

# touch our "ghost". ghc-pkg may create him later.
touch %buildroot%_libdir/ghc-%version/package.conf.old
# package-provided *.confs go in this directory:
mkdir -p %buildroot%_libdir/ghc-%version/package.conf.d

mkdir -p %buildroot%_libdir/ghc-%version/lib

# need for multiple ghc versions installed
for s in hp2ps hpc hsc2hs; do
    mv %buildroot%_bindir/$s %buildroot%_bindir/$s-%version
done

mv %buildroot%_man1dir/ghc.1 %buildroot%_man1dir/%name.1

sed -i 's!/html/!/!' %buildroot%_libdir/ghc-%version/package.conf.d/*.conf

%files
%exclude %_bindir/ghc
%exclude %_bindir/ghci
%exclude %_bindir/ghc-pkg
%exclude %_bindir/haddock
%exclude %_bindir/runghc
%exclude %_bindir/runhaskell

%_libdir/ghc-%version
%dir %docdir/
%docdir/[ALR]*
%_bindir/*
%_man1dir/%name.1*
%ghost %_libdir/ghc-%version/package.conf.old
%dir %_libdir/ghc-%version/package.conf.d

%files doc
%docdir/
%exclude %docdir/[AR]*

%changelog
* Fri Apr 26 2013 Dmitry V. Levin <ldv@altlinux.org> 7.6.1-alt3
- Changed ghc defaults to use -fasm instead of -llvm.
- Built ghc using gcc instead of llvm.
- Fixed documentation packaging.
- Built with system libffi.
- Updated build dependencies.

* Fri Nov 30 2012 Denis Smirnov <mithraen@altlinux.ru> 7.6.1-alt2
- rebuild with ghc 7.6.1

* Sun Oct 07 2012 Denis Smirnov <mithraen@altlinux.ru> 7.6.1-alt1
- bootstrap build

