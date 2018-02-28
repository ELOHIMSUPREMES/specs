Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global vertag 3f1ee79d50cf

Name:             snakeyaml
Version:          1.13
Release:          alt1_9jpp8
Summary:          YAML parser and emitter for the Java programming language
License:          ASL 2.0
# http://code.google.com/p/snakeyaml
URL:              http://code.google.com/p/%{name}
Source0:          https://snakeyaml.googlecode.com/archive/v%{version}.zip#/%{name}-%{version}.zip

# Upstream has forked gdata-java and base64 and refuses [1] to
# consider replacing them by external dependencies.  Bundled libraries
# need to be removed and their use replaced by system libraries.
# See rhbz#875777 and http://code.google.com/p/snakeyaml/issues/detail?id=175
#
# Remove use of bundled Base64 implementation
Patch0:           0001-Replace-bundled-base64-implementation.patch
# We don't have gdata-java in Fedora any longer, use commons-codec instead
Patch1:           0002-Replace-bundled-gdata-java-client-classes-with-commo.patch
# Fix tests on Java 8 (can be removed if version > 1.13)
Patch2:           java8-use-linked-hashmap.patch

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(biz.source_code:base64coder)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-eclipse-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.springframework:spring-core)
Source44: import.info

%description
SnakeYAML features:
    * a complete YAML 1.1 parser. In particular,
      SnakeYAML can parse all examples from the specification.
    * Unicode support including UTF-8/UTF-16 input/output.
    * high-level API for serializing and deserializing
      native Java objects.
    * support for all types from the YAML types repository.
    * relatively sensible error messages.


%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{vertag}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%mvn_file : %{name}

%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-javadoc-plugin

sed -i "/<artifactId>spring</s/spring/&-core/" pom.xml
rm -f src/test/java/examples/SpringTest.java

# Replacement for bundled gdata-java-client
%pom_add_dep commons-codec:commons-codec

# remove bundled stuff
rm -rf target
rm -rf src/main/java/org/yaml/snakeyaml/external

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_9jpp8
- unbootsrap build

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_7jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_4jpp7
- new version

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_3jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_1jpp7
- new version

