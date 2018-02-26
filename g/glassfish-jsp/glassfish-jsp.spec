AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global artifactId javax.servlet.jsp
%global jspspec 2.2


Name:       glassfish-jsp
Version:    2.2.6
Release:    alt1_2jpp7
Summary:    Glassfish J2EE JSP API implementation

Group:      Development/Java
License:    CDDL and GPLv2 with exceptions
URL:        http://glassfish.org
Source0:    %{artifactId}-%{version}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh

Patch0:     %{name}-build-eclipse-compilers.patch

BuildArch:  noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-release-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  glassfish-jsp-api
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)

Requires:       jpackage-utils
Requires:       mvn(javax.servlet:javax.servlet-api)
Requires:       mvn(javax.el:javax.el-api)
Requires:       mvn(javax.servlet.jsp:javax.servlet.jsp-api)

Provides:   jsp = %{jspspec}
Provides:   jsp%{jspspec}
Source44: import.info

%description
This project provides a container independent implementation of JSP
2.2. The main goals are:
  * Improves current implementation: bug fixes and performance
    improvements
  * Provides API for use by other tools, such as Netbeans
  * Provides a sandbox for new JSP features; provides a reference
    implementation of next JSP spec.


%package javadoc
Summary:    API documentation for %{name}
Group:      Development/Java
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}
%patch0

%build
mvn-rpmbuild install javadoc:javadoc


%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{artifactId}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap -a "javax.servlet:jsp-api"

%files
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_2jpp7
- new release

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_1jpp7
- full version

