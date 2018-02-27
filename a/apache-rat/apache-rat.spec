# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           apache-rat
Version:        0.10
Release:        alt1_1jpp7
Summary:        Apache Release Audit Tool (RAT)

Group:          Development/Java
License:        ASL 2.0
URL:            http://creadur.apache.org/rat/
Source0:        http://www.apache.org/dist/creadur/%{name}-%{version}/%{name}-%{version}-src.tar.bz2
Patch2:         apache-rat-0.8-test.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-wagon

BuildRequires:  ant-antunit
BuildRequires:  ant-testutil
BuildRequires:  apache-commons-compress

Requires:       jpackage-utils
Source44: import.info

%description
Release Audit Tool (RAT) is a tool to improve accuracy and efficiency when
checking releases. It is heuristic in nature: making guesses about possible
problems. It will produce false positives and cannot find every possible
issue with a release. It's reports require interpretation.

RAT was developed in response to a need felt in the Apache Incubator to be
able to review releases for the most common faults less labor intensively.
It is therefore highly tuned to the Apache style of releases.

This package just contains meta-data, you will want either apache-rat-tasks,
or apache-rat-plugin.


%package core
Summary:        Core functionality for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       apache-commons-cli
Requires:       apache-commons-collections
Requires:       apache-commons-compress
Requires:       apache-commons-lang
Requires:       apache-commons-io
Requires:       junit

%description core
The core functionality of RAT, shared by the Ant tasks, and the Maven plugin.
It also includes a wrapper script "apache-rat" that should be the equivalent
to running upstream's "java -jar apache-rat.jar".


%package plugin
Summary:        Maven plugin for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{version}-%{release}

%description plugin
Maven plugin for running RAT, the Release Audit Tool.


%package tasks
Summary:        Ant tasks for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{version}-%{release}

%description tasks
Ant tasks for running RAT.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}
%patch2 -p1 -b .test


%build
mvn-rpmbuild -DskipTests=true package javadoc:aggregate

%install
#Dirs
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}

#Parent pom
cp -p pom.xml \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom

#Components
for comp in core plugin tasks
do
  jarname=%{name}-${comp}
  jarfile=$jarname/target/${jarname}-%{version}.jar
  cp -p $jarfile $RPM_BUILD_ROOT%{_javadir}/%{name}/${jarname}.jar
  cp -p ${jarname}/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-${jarname}.pom
  %add_maven_depmap JPP.%{name}-${jarname}.pom %{name}/${jarname}.jar -f ${comp}
done

#Wrapper script
%jpackage_script org.apache.rat.Report "" "" %{name}/%{name}-core:commons-cli:commons-io:commons-collections:commons-compress:commons-lang:junit apache-rat true 

#Ant taksks
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "apache-rat/rat-core apache-rat/rat-tasks" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}

#Javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/
cp -rp target/site/apidocs \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/apache-rat.conf`
touch $RPM_BUILD_ROOT/etc/java/apache-rat.conf


%files
%doc LICENSE NOTICE README.txt RELEASE_NOTES.txt
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%dir %{_javadir}/%{name}

%files core
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
%{_mavendepmapfragdir}/%{name}-core
%{_bindir}/%{name}
%{_javadir}/%{name}/%{name}-core.jar
%config(noreplace,missingok) /etc/java/apache-rat.conf

%files plugin
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP.%{name}-%{name}-plugin.pom
%{_mavendepmapfragdir}/%{name}-plugin
%{_javadir}/%{name}/%{name}-plugin.jar

%files tasks
%doc LICENSE NOTICE
%{_sysconfdir}/ant.d/%{name}
%{_mavenpomdir}/JPP.%{name}-%{name}-tasks.pom
%{_mavendepmapfragdir}/%{name}-tasks
%{_javadir}/%{name}/%{name}-tasks.jar

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_10jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_8jpp7
- fixed build

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_6jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_6jpp7
- new version

