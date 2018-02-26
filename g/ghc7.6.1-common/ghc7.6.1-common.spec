Name: ghc7.6.1-common
Version: 7.6.1
Release: alt1
BuildArch: noarch

Summary: Glasgow Haskell Compilation system
License: BSD style w/o adv. clause
Group: Development/Haskell
Url: http://haskell.org/ghc/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: haskell-filetrigger
Requires: rpm-build-haskell
Conflicts: ghc <= 7.6.1-alt1
Conflicts: ghc7.4.1-common
Conflicts: ghc7.4.2-common

Source: %name-%version.tar

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

%prep
%setup
%build
%install
# install and fix up the macros file
%define rpmmacrosdir %_sysconfdir/rpm/macros.d
mkdir -p %buildroot%rpmmacrosdir
install ghc.macros %buildroot%rpmmacrosdir/ghc
%__subst 's/@GHC_VERSION@/%version/' %buildroot%rpmmacrosdir/ghc

mkdir -p %buildroot%_bindir

ln -s runghc %buildroot%_bindir/runhaskell
ln -s haddock-ghc-%version %buildroot%_bindir/haddock

for s in runghc hsc2hs hpc ghc ghc-pkg ghci; do
    ln -s $s-%version %buildroot%_bindir/$s
done

%files
%rpmmacrosdir/ghc
%_bindir/*

%changelog
* Fri Nov 30 2012 Denis Smirnov <mithraen@altlinux.ru> 7.6.1-alt1
- first build for Sisyphus
