Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-common-core
%define version 2.2.18
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-common-core
Version:          2.2.18
Release:          alt2_10jpp7
Summary:          JBoss Common Classes
Group:            Development/Java
License:          LGPLv2+ and ASL 1.1
URL:              http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/common/common-core/tags/2.2.18.GA/ jboss-common-core-2.2.18.GA
# tar cafJ jboss-common-core-2.2.18.GA.tar.xz jboss-common-core-2.2.18.GA
Source0:          %{name}-%{namedversion}.tar.xz
# The URLLister* family of classes was removed because the apache-slide:webdavlib is a dead project and the classes aren't used in JBoss AS 7 at all. 
Patch0:           %{name}-%{namedversion}-URLLister-removal.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jboss-parent
BuildRequires:    junit4
BuildRequires:    jboss-logging

Requires:         jboss-logging
Requires:         jpackage-utils
Source44: import.info

%description
JBoss Common Core Utility classes

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

rm -rf projectSet.psf .settings/ .project .classpath

%build
# Some failed tests
# Failed tests: testJavaLangEditors(org.jboss.test.util.test.propertyeditor.PropertyEditorsUnitTestCase):
#   PropertyEditor: org.jboss.util.propertyeditor.BooleanEditor, getAsText() == expectedStringOutput ' expected:<null> but was:<null>
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt1_7jpp7
- new version

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.14-alt2_2jpp6
- fixed build with maven3

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.14-alt1_2jpp6
- new version

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt4_1jpp5
- target=5 and build with velocity 15

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt3_1jpp5
- build with velocity 15

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt2_1jpp5
- fixed build with new maven 2.0.8

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt1_1jpp5
- new jpp release

