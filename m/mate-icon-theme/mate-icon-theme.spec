Group: Graphical desktop/Other
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-icon-theme
%define version 1.10.1
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.10

# Settings used for build from snapshots.
%{!?rel_build:%global commit cdb0d70862035cd1b65c4deb495ea1016ea2d206}
%{!?rel_build:%global commit_date 20150530}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-icon-theme
Version:        %{branch}.1
%if 0%{?rel_build}
Release:        alt1_2
%else
Release:        alt1_2
%endif
Summary:        Icon theme for MATE Desktop
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-icon-theme.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildArch:      noarch

BuildRequires:  mate-common
BuildRequires:  icon-naming-utils
Source44: import.info


%description
Icon theme for MATE Desktop

%package devel
Group: Graphical desktop/Other
Summary: Development files for mate-icon-theme

%description devel
Development files for mate-icon-theme

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
%configure  --enable-icon-mapping

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

%files
%doc AUTHORS COPYING README
%{_datadir}/icons/mate
%{_datadir}/icons/menta

%files devel
%{_datadir}/pkgconfig/mate-icon-theme.pc


%changelog
* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt1_2
- new fc release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

