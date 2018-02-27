Epoch: 0
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat

%global group_id  org.testng

Name:             testng
Version:          6.8.7
Release:          alt1_1jpp7
Summary:          Java-based testing framework
# org/testng/remote/strprotocol/AbstractRemoteTestRunnerClient.java is CPL
License:          ASL 2.0 and CPL
URL:              http://testng.org/
Source0:          https://github.com/cbeust/testng/archive/%{name}-%{version}.tar.gz

BuildArch:        noarch


BuildRequires:    mvn(com.beust:jcommander) >= 1.27
BuildRequires:    mvn(com.google.guava:guava)
BuildRequires:    mvn(com.google.inject:guice)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.ant:ant)
BuildRequires:    mvn(org.beanshell:bsh)
BuildRequires:    mvn(org.sonatype.oss:oss-parent)
BuildRequires:    mvn(org.yaml:snakeyaml)

BuildRequires:    maven-local
BuildRequires:    maven-plugin-bundle
Source44: import.info

%description
TestNG is a testing framework inspired from JUnit and NUnit but introducing
some new functionality, including flexible test configuration, and
distributed test running.  It is designed to cover unit tests as well as
functional, end-to-end, integration, etc.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# build fix for new guice
%pom_add_dep com.google.guava:guava::provided
sed -i "s|com.google.inject.internal|com.google.common.collect|" \
  src/main/java/org/testng/xml/XmlDependencies.java \
  src/main/java/org/testng/xml/XmlGroups.java \
  src/main/java/org/testng/xml/dom/TestNGTagFactory.java \
  src/test/java/test/dependent/InstanceSkipSampleTest.java \
  src/test/java/test/mustache/MustacheTest.java \
  src/test/java/test/thread/B.java

%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
  
# remove bundled stuff
rm -rf spring
rm -rf 3rdparty
rm -rf lib-supplied
rm -rf gigaspaces
rm -f *.jar

# convert to UTF-8
native2ascii -encoding UTF-8 src/main/java/org/testng/internal/Version.java \
  src/main/java/org/testng/internal/Version.java

iconv --from-code=ISO-8859-2 --to-code=UTF-8 ANNOUNCEMENT.txt > ANNOUNCEMENT.txt.utf8
mv -f ANNOUNCEMENT.txt.utf8 ANNOUNCEMENT.txt

%mvn_file : %{name}
# jdk15 classifier is used by some other packages
%mvn_alias : :::jdk15:

%build
%mvn_build -- -Dmaven.local.debug=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt ANNOUNCEMENT.txt CHANGES.txt README

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.8.7-alt1_1jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.8-alt1_1jpp7
- new version

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt3_4jpp7
- fixed deps

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt2_4jpp7
- new release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt2_1jpp7
- added oss-parent pom dependency

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt1_1jpp7
- new version

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt2_2jpp6
- fixed build

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt1_2jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt4_1jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt1_1jpp5
- converted from JPackage by jppimport script

