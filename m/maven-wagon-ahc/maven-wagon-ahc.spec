BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		maven-wagon-ahc
Version:	1.2.1
Release:	alt1_2jpp7
Summary:	A wagon provider for HTTP transfers

Group:		Development/Java
License:	EPL
URL:		http://www.sonatype.com

# git clone git://github.com/sonatype/wagon-ahc.git
# git archive --format=tar --prefix=maven-wagon-ahc-1.2.1/ wagon-ahc-1.2.1 | xz > maven-wagon-ahc-1.2.1.tar.xz
Source0:	%{name}-%{version}.tar.xz
Source1:	http://www.eclipse.org/legal/epl-v10.html
Source2:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:	noarch

BuildRequires:	animal-sniffer
BuildRequires:	async-http-client
BuildRequires:	easymock2
BuildRequires:	forge-parent
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	maven
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-surefire-plugin
BuildRequires:	maven-wagon
BuildRequires:	plexus-container-default
BuildRequires:	plexus-utils

Requires:	async-http-client
Requires:	jpackage-utils
Requires:	maven-wagon
Requires:	plexus-utils
Source44: import.info


%description
A wagon provider for HTTP transfers based on the async-http-client.

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -delete
find -name '*.jar' -delete

cp %{SOURCE1} .

%build
# we don't have all test deps, so tests fail
mvn-rpmbuild package javadoc:aggregate -Dmaven.test.skip=true

%install

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/wagon-ahc-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POMs
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%doc epl-v10.html
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2jpp7
- new version

