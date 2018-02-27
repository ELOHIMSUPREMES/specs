Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          glassfish-dtd-parser
Version:       1.2
Release:       alt2_0.8.20120120svnjpp7
Summary:       Library for parsing XML DTDs
License:       CDDL 1.1 and GPLv2 with exceptions
Url:           http://java.net/projects/dtd-parser
# svn export https://svn.java.net/svn/dtd-parser~svn/trunk/dtd-parser glassfish-dtd-parser-1.2-SNAPSHOT
# find glassfish-dtd-parser-1.2-SNAPSHOT/ -name '*.jar' -delete
# tar czf glassfish-dtd-parser-1.2-SNAPSHOT-src-svn.tar.gz glassfish-dtd-parser-1.2-SNAPSHOT
Source0:       %{name}-%{version}-SNAPSHOT-src-svn.tar.gz
BuildRequires: bsf
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: sonatype-oss-parent

BuildArch:     noarch
Source44: import.info

%description
Library for parsing XML DTDs.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-SNAPSHOT

%build

%mvn_file :dtd-parser %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.8.20120120svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.6.20120120svnjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.4.20120120svnjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.4.20120120svnjpp7
- new version

