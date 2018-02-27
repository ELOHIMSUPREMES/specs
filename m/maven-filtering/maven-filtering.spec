Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             maven-filtering
Version:          1.1
Release:          alt1_2jpp7
Summary:          Shared component providing resource filtering
License:          ASL 2.0
URL:              http://maven.apache.org/shared/%{name}/index.html
Source0:          http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-shared
BuildRequires:    plexus-build-api
BuildRequires:    plexus-containers-component-metadata

Provides:         maven-shared-filtering = 1.0-99
Obsoletes:        maven-shared-filtering < 1.0-99 
Source44: import.info

%description
These Plexus components have been built from the filtering process/code in 
Maven Resources Plugin. The goal is to provide a shared component for all 
plugins that needs to filter resources.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata

%build
# Tests use a package that is no longer present in plexus-build-api (v0.0.7)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_9jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- new release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp7
- full build

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

