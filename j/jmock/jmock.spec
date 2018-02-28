Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jmock
%define version 2.8.1
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}

Name:          jmock
Version:       2.8.1
Release:       alt1_2jpp8
Summary:       Java library for testing code with mock objects
License:       BSD
Url:           http://www.jmock.org/
Source0:       https://github.com/jmock-developers/jmock-library/archive/%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.beanshell:bsh)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.objenesis:objenesis)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Mock objects help you design and test the interactions between the objects in
your programs.
The jMock library:
  * makes it quick and easy to define mock objects, so you don't break the
    rhythm of programming.
  * lets you precisely specify the interactions between your objects, reducing
    the brittleness of your tests.
  * works well with the auto-completion and re-factoring features of your IDE
  * plugs into your favorite test framework
  * is easy to extend.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-library-%{namedversion}

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_plugin :maven-gpg-plugin testjar

%pom_xpath_set "pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib
%pom_xpath_set "pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib %{name}

sed -i "s|%classpath|$(build-classpath objectweb-asm/asm)|" %{name}/pom.xml

%pom_xpath_remove pom:build %{name}-example
%pom_xpath_inject "pom:project" "
<build>
  <sourceDirectory>src/main</sourceDirectory>
</build>" %{name}-example
# package org.jmock.integration.junit{3,4} do not exist
%pom_add_dep org.%{name}:%{name}-junit3:'${project.version}' %{name}-example
%pom_add_dep org.%{name}:%{name}-junit4:'${project.version}' %{name}-example

%mvn_alias org.%{name}:%{name} :%{name}-script
%mvn_package org.%{name}:%{name}::tests:
%mvn_package org.%{name}:%{name}-junit3::tests:

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README*
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt1_2jpp8
- new version

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_2jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_1jpp7
- fc update

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt4_3jpp6
- build with objectweb-asm

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_3jpp6
- new jpp release

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_2jpp5
- fixed build; use cglib21 (with old asm)

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_1jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

