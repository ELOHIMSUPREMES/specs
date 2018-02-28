Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           sonar-update-center
Version:        1.12.1
Release:        alt1_4jpp8
Summary:        Sonar Update Center
License:        LGPLv3+
URL:            http://www.sonarqube.org
Source0:        https://github.com/SonarSource/%{name}/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
Source44: import.info

%description
Update center for Sonar - platform for continuous inspection of code quality.

%package -n sonar-packaging-maven-plugin
Group: Development/Java
Summary:        Maven plugin for building Sonar plugins

%description -n sonar-packaging-maven-plugin
Maven plugin for building Sonar plugins.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

find -name '*.jar' -delete

# circular dependency - parent is part of sonar-plugins which needs
# sonar-packaging-maven-plugin to build
%pom_remove_parent

# missing org.freemarker:freemaker and com.github.kevinsawicki:http-request
%pom_disable_module sonar-update-center-mojo

# guava stopped reexporting @Nullable
%pom_add_dep com.google.code.findbugs:jsr305

%mvn_package :sonar-packaging-maven-plugin sonar-packaging-maven-plugin

%build
# missing fest-assert
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files -n sonar-packaging-maven-plugin -f .mfiles-sonar-packaging-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_4jpp8
- unbootsrap build

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

