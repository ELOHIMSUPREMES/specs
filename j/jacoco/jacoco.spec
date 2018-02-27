# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven-local
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global tag 201302030002

Name:      jacoco
Version:   0.6.2
Release:   alt1_1jpp7
Summary:   Java Code Coverage for Eclipse 
Group:     System/Libraries
License:   EPL
URL:       http://www.eclemma.org/jacoco/
Source0:   https://github.com/jacoco/jacoco/archive/v%{version}.tar.gz

Patch0:    removeGroovyScripting.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    eclipse-platform >= 1:4.2.0-0.10
BuildRequires:    eclipse-pde >= 1:4.2.0-0.10
BuildRequires:    tycho
BuildRequires:    maven-shade-plugin >= 1.5
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-dependency-plugin maven-antrun-plugin maven-assembly-plugin maven-clean-plugin maven-compiler-plugin maven-deploy-plugin
BuildRequires:    maven-install-plugin maven-invoker-plugin maven-gpg-plugin maven-jar-plugin maven-javadoc-plugin maven-plugin-plugin
BuildRequires:    maven-release-plugin maven-resources-plugin maven-shade-plugin maven-source-plugin maven-surefire-plugin maven-site-plugin
BuildRequires:    maven-plugin-tools-javadoc
BuildRequires:    dos2unix
BuildRequires:    fest-assert
BuildRequires:    objectweb-asm4
Requires:         ant
Requires:         objectweb-asm4
Source44: import.info

%description
JaCoCo is a free code coverage library for Java, 
which has been created by the EclEmma team based on the lessons learned 
from using and integration existing libraries over the last five years. 


%package    javadoc
Summary:    Java-docs for %{name}
Group:      Development/Java
Requires:   %{name} = %{version}-%{release}
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package    maven-plugin
Summary:    A Jacoco plugin for maven
Group:      System/Libraries
Requires:   maven
Requires:   objectweb-asm4
Requires:   %{name} = %{version}-%{release}

%description maven-plugin
A Jacoco plugin for maven.

%prep
%setup -q 
%patch0

%pom_disable_module ../org.jacoco.examples org.jacoco.build
%pom_disable_module ../org.jacoco.doc org.jacoco.build
%pom_disable_module ../org.jacoco.tests org.jacoco.build
%pom_disable_module ../jacoco org.jacoco.build

#%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin org.jacoco.agent.rt/pom.xml 

# make sure upstream hasn't sneaked in any jars we don't know about
JARS=""
for j in `find -name "*.jar"`; do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
   echo "These jars should be deleted and symlinked to system jars: $JARS"
   exit 1
fi

%build
# Note: Tests must be disabled because they introduce circular dependency
# right now.
OPTIONS="-DrandomNumber=${RANDOM} -DskipTychoVersionCheck package javadoc:aggregate" 

mvn-rpmbuild $OPTIONS

dos2unix org.jacoco.doc/docroot/doc/.resources/doc.css 

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}

for f in    org.jacoco.agent \
            org.jacoco.ant \
            org.jacoco.core \
            org.jacoco.report \
            jacoco-maven-plugin
do
    cp $f/target/$f-%{version}.%{tag}.jar %{buildroot}%{_javadir}/%{name}/$f.jar
done;

cp org.jacoco.agent.rt/target/org.jacoco.agent.rt-%{version}.%{tag}-all.jar %{buildroot}%{_javadir}/%{name}/org.jacoco.agent.rt.jar

# Install maven stuff.
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 org.jacoco.build/pom.xml %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom
for f in    org.jacoco.agent \
            org.jacoco.agent.rt \
            org.jacoco.ant \
            org.jacoco.core \
            org.jacoco.report \
            jacoco-maven-plugin
do
    install -pm 644 $f/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-$f.pom
    %add_maven_depmap JPP.%{name}-$f.pom %{name}/$f.jar
done;

# javadoc 
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rf target/site/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
#agent
%{_javadir}/jacoco/org.jacoco.agent.rt.jar
%{_mavenpomdir}/JPP.%{name}-org.jacoco.agent.rt.pom
#OSGi bundles
%{_javadir}/jacoco/org.jacoco.ant.jar
%{_javadir}/jacoco/org.jacoco.agent.jar
%{_javadir}/jacoco/org.jacoco.core.jar
%{_javadir}/jacoco/org.jacoco.report.jar
%{_mavenpomdir}/JPP.%{name}-org.jacoco.ant.pom
%{_mavenpomdir}/JPP.%{name}-org.jacoco.agent.pom
%{_mavenpomdir}/JPP.%{name}-org.jacoco.core.pom
%{_mavenpomdir}/JPP.%{name}-org.jacoco.report.pom

%doc org.jacoco.doc/docroot/*
%doc org.jacoco.doc/about.html

%files maven-plugin
%{_javadir}/%{name}/jacoco-maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-jacoco-maven-plugin.pom

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1jpp7
- fc update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_3jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_3jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt2_2jpp7
- fixed build

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt1_2jpp7
- new release

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_0.6jpp7
- new version

