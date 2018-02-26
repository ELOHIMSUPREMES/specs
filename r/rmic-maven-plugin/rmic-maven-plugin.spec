# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             rmic-maven-plugin
Version:          1.2.0
Release:          alt1_1jpp7
Summary:          Uses the java rmic compiler to generate classes used in remote method invocation
License:          MIT
Group:            Development/Java
URL:              http://mojo.codehaus.org/%{name}

Source0:          http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:        noarch

BuildRequires:    asm2
BuildRequires:    groovy
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-invoker-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-plugin-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-shared-invoker
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    mojo-parent

Requires:         jpackage-utils
Requires:         maven
Requires:         plexus-archiver
Requires:         plexus-compiler
Requires:         plexus-container-default
Requires:         plexus-utils
Source44: import.info

%description
This plugin works with Maven 2 and uses the java rmic compiler to generate
classes used in remote method invocation.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

sed -i -e "s|groupId>plexus|groupId>org.codehaus.plexus|g" pom.xml

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc License.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc License.txt
%{_javadocdir}/%{name}

%changelog
* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp7
- new version

