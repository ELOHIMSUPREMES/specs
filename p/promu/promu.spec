%global import_path github.com/prometheus/promu
%global commit 295a70a7f580b886572861b19545b28accfd4491

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: promu
Version: 0.3.0
Release: alt1
Summary: Prometheus Utility Tool

Group: Development/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

%description
promu is the utility tool for Prometheus projects.

%prep
%setup -q

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install
rm -rf -- %buildroot%_datadir

%files
%_bindir/*

%changelog
* Wed Mar 06 2019 Alexey Shabalin <shaba@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sat Jan 19 2019 Alexey Shabalin <shaba@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Apr 20 2018 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1%ubt
- Initial build for ALT.
