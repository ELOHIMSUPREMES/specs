Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname jaxb-api
Name:          glassfish-jaxb-api
Version:       2.2.9
Release:       alt1_4jpp7
Summary:       Java Architecture for XML Binding
License:       CDDL or GPLv2 with exception
URL:           http://jaxb.java.net/
# jaxb api and impl have different version
# svn export https://svn.java.net/svn/jaxb~version2/tags/jaxb-2_2_6/tools/lib/redist/jaxb-api-src.zip

Source0:       http://repo1.maven.org/maven2/javax/xml/bind/%{oname}/%{version}/%{oname}-%{version}-sources.jar
Source1:       http://repo1.maven.org/maven2/javax/xml/bind/%{oname}/%{version}/%{oname}-%{version}.pom

BuildRequires: java-javadoc
BuildRequires: jvnet-parent

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-shared-osgi
Requires:      jvnet-parent
BuildArch:     noarch
Source44: import.info

# The Fedora Packaging Committee granted openjdk a bundling exception to carry JAXP and
# JAX-WS (glassfish doesn't need one, since it is the upstream for these files).
# Reference: https://fedorahosted.org/fpc/ticket/292

%description
Glassfish - JAXB (JSR 222) API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{oname}
Requires:      %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
Glassfish - JAXB (JSR 222) API.

This package contains javadoc for %{name}.

%prep
%setup -T -q -c

# fixing incomplete source directory structure
mkdir -p src/main/java

(
  cd src/main/java
  unzip -qq %{SOURCE0}
  rm -rf META-INF
)

cp -p %{SOURCE1} pom.xml

sed -i 's|<location>${basedir}/offline-javadoc</location>|<location>%{_javadocdir}/java</location>|' pom.xml

%build

%mvn_file :%{oname} %{oname}
%mvn_build

%install
%mvn_install

mv %{buildroot}%{_javadocdir}/%{name} \
 %{buildroot}%{_javadocdir}/%{oname}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{oname}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.9-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_1jpp7
- new version

