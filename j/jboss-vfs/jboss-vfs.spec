Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-vfs
%define version 3.2.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-vfs
Version:          3.2.5
Release:          alt1_3jpp8
Summary:          JBoss Virtual File System
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-vfs/
Source0:          https://github.com/jbossas/jboss-vfs/archive/jboss-vfs-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
#BuildRequires:    mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
Source44: import.info

%description
This package contains the JBoss Virtual File System.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-vfs-jboss-vfs-%{namedversion}

rm -rf src/test/resources/vfs/test/zipeinit.jar
# break build see for e.g. jboss-metadata.spec
%pom_remove_plugin :maven-checkstyle-plugin

%build
# Skipped because jboss-test is not packaged yet
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.5-alt1_3jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_4jpp7
- new version

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_2jpp5
- new version

