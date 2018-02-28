Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             weld-parent
Version:          34
Release:          alt1_2jpp8
Summary:          Parent POM for Weld
License:          ASL 2.0
URL:              http://weld.cdi-spec.org
Source0:          https://github.com/weld/parent/archive/%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Source44: import.info

%description
Parent POM for Weld

%prep
%setup -q -n parent-%{version}

%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin ":maven-remote-resources-plugin"
%pom_remove_plugin ":maven-eclipse-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 34-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 31-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 31-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 31-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 26-alt1_1jpp7
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 17-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 17-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 17-alt1_4jpp7
- new version

