Name: rust
Version: 1.9.0
Release: alt1
Summary: The Rust Programming Language

Group: Development/Other
License: Apache 2.0, MIT
URL: http://www.rust-lang.org/

# Cloned from https://github.com/rust-lang/rust
Source: %name-%version.tar
# Cloned from https://github.com/rust-lang/llvm
Source1: llvm.tar
# Cloned from https://github.com/rust-lang/jemalloc
Source2: jemalloc.tar
# Cloned from https://github.com/rust-lang/compiler-rt
Source3: compiler-rt.tar
# Cloned from https://github.com/rust-lang/hoedown
Source4: hoedown.tar
# Cloned from https://github.com/rust-lang/rust-installer
Source5: rust-installer.tar
# Cloned from https://github.com/rust-lang-nursery/libc
Source6: liblibc.tar

# Prebuilt rust, downloaded from http://static.rust-lang.org/stage0-snapshots/
%ifarch x86_64 
Source7: rust-stage0-2016-03-18-235d774-linux-x86_64-1273b6b6aed421c9e40c59f366d0df6092ec0397.tar.bz2
%endif

%ifarch %ix86
Source7: rust-stage0-2016-03-18-235d774-linux-i386-0e0e4448b80d0a12b75485795244bb3857a0a7ef.tar.bz2
%endif

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildPreReq: /proc
BuildRequires: curl gcc-c++ python-devel

%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%package gdb
Group: Development/Other
Summary: run rust compiler under gdb
Requires: %name = %version-%release

%description gdb
%summary

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6
mv llvm jemalloc compiler-rt rust-installer liblibc src
mv hoedown src/rt

mkdir dl
cp %SOURCE7 dl

%build
./configure --disable-manage-submodules \
    --release-channel=stable \
    --disable-docs \
    --enable-dist-host-only \
    --prefix=%prefix \
    --libdir=%_libdir

%ifarch x86_64
%make_build RUSTFLAGS_STAGE0="-L x86_64-unknown-linux-gnu/stage0/lib/rustlib/x86_64-unknown-linux-gnu/lib"
%endif

%ifarch %ix86
%make_build RUSTFLAGS_STAGE0="-L i686-unknown-linux-gnu/stage0/lib/rustlib/i686-unknown-linux-gnu/lib"
%endif

%install
%makeinstall_std

%files
%doc COPYRIGHT LICENSE-APACHE LICENSE-MIT README.md
%_bindir/rustc
%_bindir/rustdoc
%_libdir/lib*
%dir %_libdir/rustlib
%_libdir/rustlib/*
%exclude %_libdir/rustlib/etc/*
%exclude %_libdir/rustlib/install.log
%exclude %_libdir/rustlib/manifest-*
%exclude %_libdir/rustlib/rust-installer-version
%exclude %_libdir/rustlib/uninstall.sh
%exclude %_libdir/rustlib/components
%_man1dir/rustc.*
%_man1dir/rustdoc.*

%files gdb
%_bindir/rust-gdb
%_libdir/rustlib/etc/*

%changelog
* Mon May 30 2016 Vladimir Lettiev <crux@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Apr 22 2016 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Fri Mar 04 2016 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Fri Jan 22 2016 Vladimir Lettiev <crux@altlinux.ru> 1.6.0-alt1
- 1.6.0
- separated rust-gdb package

* Fri Jan 15 2016 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- initial build

