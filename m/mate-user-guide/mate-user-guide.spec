Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define fedora 22
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-user-guide
%define version 1.10.1
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.10

# Settings used for build from snapshots.
%{!?rel_build:%global commit 61aec06d978154fea42f1f42d845fdb710c924f7}
%{!?rel_build:%global commit_date 20150618}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:        mate-user-guide
Summary:     User Guide for MATE desktop
Version:     %{branch}.1
%if 0%{?rel_build}
Release:     alt1_1
%else
Release:     alt1_0.1%{?git_rel}
%endif
License:     GPLv2+
URL:         http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-user-guide.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildArch:      noarch

BuildRequires:  mate-common

Requires: yelp
Source44: import.info

%description
Documentations for MATE desktop.

%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%if 0%{?fedora} >= 21
%doc COPYING
%doc AUTHORS NEWS README ChangeLog
%else
%doc AUTHORS COPYING NEWS README ChangeLog
%endif


%changelog
* Wed Oct 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt1_1
- new version

