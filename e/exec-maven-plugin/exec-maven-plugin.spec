Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           exec-maven-plugin
Version:        1.6.0
Release:        alt1_6jpp8
Summary:        Exec Maven Plugin

License:        ASL 2.0
URL:            http://www.mojohaus.org/exec-maven-plugin/
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/%{version}/exec-maven-plugin-%{version}-source-release.zip

Patch1:         exec-maven-plugin-1.6.0-Port-to-Maven-3.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

Obsoletes:      maven-plugin-exec < %{version}-%{release}
Provides:       maven-plugin-exec = %{version}-%{release}
Source44: import.info

%description
A plugin to allow execution of system and Java programs.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n exec-maven-plugin-%{version}

sed -i 's/\r$//' LICENSE.txt
find . -name *.jar -delete

%pom_remove_dep :maven-project
%pom_remove_dep :maven-toolchain
%pom_remove_dep :maven-artifact-manager

%pom_add_dep org.apache.maven:maven-compat
%pom_add_dep junit:junit::test

%pom_remove_plugin :animal-sniffer-maven-plugin

%patch1 -p1

%build
%mvn_build -- -DmavenVersion=3

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_4jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_3jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3jpp7
- new version

