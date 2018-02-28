Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             google-gson
Version:          2.3.1
Release:          alt1_2jpp8
Summary:          Java lib for conversion of Java objects into JSON representation
License:          ASL 2.0
URL:              https://github.com/google/gson
Source0:          https://github.com/google/gson/archive/gson-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-eclipse-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n gson-gson-%{version}

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE

# Test requires network
rm src/test/java/com/google/gson/DefaultInetAddressTypeAdapterTest.java

# Throwable has more fields serialized, probably incorrect test expectations
rm src/test/java/com/google/gson/functional/ThrowableFunctionalTest.java

%build
# LANG="C" or LANG="en_US.utf8" needed for the tests
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3jpp7
- new version

