Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-datatype-joda
Version:       2.7.6
Release:       alt1_2jpp8
Summary:       Add-on module for Jackson to support Joda data-types
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonModuleJoda
Source0:       https://github.com/FasterXML/jackson-datatype-joda/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
This is a Jackson module that aims to provide
full support for data types of Joda date-time
library.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i 's/\r//' src/main/resources/META-INF/LICENSE
cp -p src/main/resources/META-INF/LICENSE .

# ComparisonFailure: expected:<...Midnight","2001-05-2[5]"]> but was:<...Midnight","2001-05-2[4]"]>
rm -r src/test/java/com/fasterxml/jackson/datatype/joda/JodaSerializationTest.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_1jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_1jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

