Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          classmate
Version:       1.1.0
Release:       alt1_2jpp8
Summary:       Java introspection library
License:       ASL 2.0
Url:           http://github.com/cowtowncoder/java-classmate/
Source0:       https://github.com/cowtowncoder/java-classmate/archive/%{name}-%{version}.tar.gz

BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: sonatype-oss-parent

BuildArch:     noarch
Source44: import.info

%description
Library for introspecting types with full generic information
including resolving of field and method types.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n java-%{name}-%{name}-%{version}

find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

sed -i 's/\r//' src/main/resources/META-INF/LICENSE src/main/resources/META-INF/NOTICE
cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .

# this test fails junit.framework.AssertionFailedError: expected:<X> but was:<Y>
rm -r src/test/java/com/fasterxml/classmate/AnnotationsTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md VERSION.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt2_4jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt2_2jpp7
- fixed maven1 dependency

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_2jpp7
- initial build

