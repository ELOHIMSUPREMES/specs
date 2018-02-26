BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-modules
%define version 1.1.1
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-modules
Version:          1.1.1
Release:          alt1_6jpp7
Summary:          A Modular Classloading System
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-modules

# git clone git://github.com/jbossas/jboss-modules.git
# cd jboss-modules/ && git archive --format=tar --prefix=jboss-modules-1.1.1.GA/ 1.1.1.GA | xz > jboss-modules-1.1.1.GA.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

# Fixes https://issues.jboss.org/browse/MODULES-128
Patch0:           MODULES-128.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    jboss-parent
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    apiviz
BuildRequires:    junit4

Requires:         jpackage-utils
Source44: import.info

%description
Ths package contains A Modular Classloading System.

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

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# JAVADOC
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp7
- new version

