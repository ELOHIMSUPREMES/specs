BuildRequires: maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-distribution-remote-resources
Version:        1.1
Release:        alt2_4jpp7
Summary:        Jetty toolchain artifact for distribution remote resources

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  jetty-toolchain

Requires:       jpackage-utils
Requires:       maven
Requires:       maven-remote-resources-plugin
Requires:       jetty-toolchain
Source44: import.info

%description
Jetty toolchain artifact for distribution remote distribution resources

%prep
%setup -q

%build
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  install javadoc:aggregate

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dp -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc src/main/resources/LICENSE*
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}


%changelog
* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new version

