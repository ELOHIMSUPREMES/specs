# build ids are not currently generated:
# https://code.google.com/p/go/issues/detail?id=5238
#
# also, debuginfo extraction currently fails with
# "Failed to write file: invalid section alignment"
%global __find_debuginfo_files %nil

# we are shipping the full contents of src in the data subpackage, which
# contains binary-like things (ELF data for tests, etc)
%global _unpackaged_files_terminate_build 1

%global go_arches %ix86 x86_64 %arm

%ifarch x86_64
%global gohostarch  amd64
%endif
%ifarch %{ix86}
%global gohostarch  386
%endif
%ifarch %{arm}
%global gohostarch  arm
%endif

%def_disable check

Name:		golang
Version:	1.4.2
Release:	alt1
Summary:	The Go Programming Language
Group:		Development/Other
License:	BSD
URL:		http://golang.org/

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	golang-%version.tar
Patch0:		golang-1.2-verbose-build.patch
Patch2:		golang-1.4.2-alt-certs-path.patch

ExclusiveArch:	%go_arches

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_libdir/golang
%brp_strip_none %_libdir/golang/bin/*

AutoReq: nocpp

# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc}}

%description
Go is expressive, concise, clean, and efficient. Its concurrency mechanisms
make it easy to write programs that get the most out of multicore and
networked machines, while its novel type system enables flexible and
modular program construction.


%package gdb
Summary: The Go Runtime support for GDB
Group: Development/Other
Requires:    %name = %version-%release
BuildArch: noarch

%description gdb
The Go Runtime support for GDB.


%package godoc
Summary: The Go documentation tool
Group: Documentation
Requires:    %name = %version-%release
Requires:    %name-docs = %version-%release

%description godoc
The Go documentation tool.


%package docs
Summary: Go sources and documentation
Group: Documentation
BuildArch:  noarch

%description docs
Go sources and documentation.


%prep
%setup -q

# increase verbosity of build
%patch0 -p1
%patch2 -p2


%build
export PATH="$GOROOT/bin:$PATH"
export GOROOT_FINAL=%_libdir/%name

# TODO use the system linker to get the system link flags and build-id
# when https://code.google.com/p/go/issues/detail?id=5221 is solved
#export GO_LDFLAGS="-linkmode external -extldflags $RPM_LD_FLAGS"

export GOHOSTOS=linux
export GOHOSTARCH=%gohostarch

# use our gcc options for this build, but store gcc as default for compiler
export CC="gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS"
export CC_FOR_TARGET="gcc"

# build
cd src
./make.bash --no-clean

%check
%if_enabled check
export GOROOT=$PWD
export PATH="$GOROOT/bin:$PATH"
export CGO_ENABLED=0

cd src
./run.bash --no-rebuild
%endif

%install
# create the top level directories
mkdir -p -- \
	%buildroot/%_bindir \
	%buildroot/%_libdir/%name \
	%buildroot/%_datadir/%name

# install binaries and runtime files into libdir
cp -av bin pkg src \
	%buildroot/%_libdir/%name

# install sources and other data in datadir
cp -av api doc include lib favicon.ico robots.txt \
	%buildroot/%_datadir/%name

# remove the unnecessary zoneinfo file (Go will always use the system one first)
rm -rfv -- \
	%buildroot/%_datadir/%name/lib/time

find %buildroot/%_libdir/%name/src -maxdepth 1 -type f -print0 |
	xargs -0 rm -fv --

# remove plan9 files
#rm -fv -- %buildroot/%_datadir/%name/include/plan9/mklibc.rc
rm -rfv -- %buildroot/%_datadir/%name/include/plan9

# remove testdata, tests, and non-go files: this is all we need for godoc
find \
	%buildroot/%_libdir/%name/src \
	%buildroot/%_datadir/%name/doc \
	\( \
		\( -type d -name 'testdata'  \) -o \
		\( -type f -name 'Makefile'  \) -o \
		\( -type f -name '*_test.go' \) -o \
		\( -type f -name 'test_*'    \) -o \
		\( -type f -name 'test.'     \) \
	\) \
		-print0 |
	xargs -0 rm -rfv --

# add symlinks for things in datadir
for z in %buildroot/%_datadir/%name/*; do
	n="${z##*/}"
	path="$(relative "$z" "%buildroot/%_libdir/%name/$n")"
	ln -sv -- "$path" %buildroot/%_libdir/%name/$n
done

# add symlinks for binaries.
for z in %buildroot%_libdir/%name/bin/*; do
	n="${z##*/}"
	path="$(relative "$z" "%buildroot/%_bindir/$n")"
	ln -sv -- "$path" %buildroot/%_bindir/$n
done

# restore the gdb debugging script, needed at runtime by gdb
mkdir -p -- %buildroot/%_datadir/%name/gdb
mv -fv  \
	%buildroot/%_libdir/%name/src/runtime/runtime-gdb.py \
	%buildroot/%_datadir/%name/gdb

%files
# binaries
%dir %_libdir/%name
%dir %_libdir/%name/bin
%_libdir/%name/bin/go
%_libdir/%name/bin/gofmt
%_libdir/%name/pkg
%_libdir/%name/src

# data
%dir %_datadir/%name
%_datadir/%name/api
%_datadir/%name/include

# symlinks (lib -> share)
%_bindir/go
%_bindir/gofmt
%_libdir/%name/api
%_libdir/%name/include


%files gdb
# GDB script
%_datadir/%name/gdb


%files godoc
%_libdir/%name/doc
%_libdir/%name/favicon.ico
%_libdir/%name/lib
%_libdir/%name/robots.txt


%files docs
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS VERSION

# data
%dir %_datadir/%name
%_datadir/%name/doc
%_datadir/%name/favicon.ico
%_datadir/%name/robots.txt
%_datadir/%name/lib


%changelog
* Sun May 03 2015 Alexey Gladkov <legion@altlinux.ru> 1.4.2-alt1
- New version (1.4.2).
- Disable tests.

* Fri Dec 12 2014 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- New version (1.4).
- Drop vim subpackage.

* Mon Jun 23 2014 Alexey Gladkov <legion@altlinux.ru> 1.3-alt1
- New version (1.3).

* Tue Dec 10 2013 Alexey Gladkov <legion@altlinux.ru> 1.2-alt1
- New version (1.2).

* Mon Oct 28 2013 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt2
- Add gdb and vim plugins.
- Fix rebuild command (ALT#29508).

* Thu Oct 10 2013 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt1
- New version (1.1.2).
- Fix ssl certs search path (ALT#29449).

* Fri Jun 14 2013 Alexey Gladkov <legion@altlinux.ru> 1.1-alt1
- First build for ALTLinux.

* Sat May 25 2013 Dan Horák <dan[at]danny.cz> - 1.1-3
- set ExclusiveArch

* Fri May 24 2013 Adam Goode <adam@spicenitz.org> - 1.1-2
- Fix noarch package discrepancies

* Fri May 24 2013 Adam Goode <adam@spicenitz.org> - 1.1-1
- Initial Fedora release.
- Update to 1.1

* Thu May  9 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.3.rc3
- Update to rc3

* Thu Apr 11 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.2.beta2
- Update to beta2

* Tue Apr  9 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.1.beta1
- Initial packaging.
